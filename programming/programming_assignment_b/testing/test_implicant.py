import implicant
import unittest
'''
    Tests assume your Implicant class has the following methods:
        .get_str() --> string representation, e.g. "a'b"
        .get() --> tuple representation, e.g. ("a'","b")
        .get_implicant_bin_repr() --> binary representation, e.g. (0,1)
        .get_hamming_weight() --> hamming weight, e.g. 1  for minterm a'b
        .get_cover() --> tuple containing minterm cover,
                         e.g. (1,) for minterm a'b  
                              (0,1) for term a' that was a result of simplification a'b'(0), a'b(1)
        .simplify(another_implicant) --> is simplification is possible return simplified term with updated minterm cover; otherwise None
'''

class TestImplicantMethods(unittest.TestCase):

    def test_type_error_on_init(self):
        with self.assertRaises(TypeError):
            implicant.Implicant(1001)

    def test_implicant(self):
        imp = implicant.Implicant("ab'c'd")
        self.assertEqual(imp.get(), ("a","b'","c'","d") )

    def test_implicant_str(self):
        imp = implicant.Implicant("ab'c'd")
        self.assertEqual(imp.get_str(), "ab'c'd" )

    def test_implicant_cover(self):
        imp = implicant.Implicant("ab'c'd")
        self.assertEqual(imp.get_cover(), (9,) )

    def test_implicant_binary(self):
        imp = implicant.Implicant("ab'c'd")
        self.assertEqual(imp.get_implicant_bin_repr(), (1,0,0,1) )

    def test_implicant_hamming(self):
        imp = implicant.Implicant("ab'c'd")
        self.assertEqual(imp.get_hamming_weight(), 2)

    def test_simplify(self):
        imp_9 = implicant.Implicant("ab'c'd")
        imp_11 = implicant.Implicant("ab'cd")
        # differ in exaclty one literal, keep ab'd

        result = imp_9.simplify(imp_11)
        self.assertEqual(result.get(), ("a","b'","d") )
        self.assertEqual(result.get_str(), "ab'd" )
        self.assertEqual(result.get_cover(), (9,11) )
        
        ''' expect the same anwer     
        result2 = imp_11.simplify(imp_9)
        self.assertEqual(result.get(), ("a","b'","d") )
        self.assertEqual(result.get_str(), "ab'd" )
        self.assertEqual(result.get_cover(), [9,11] )
        '''
 
    def test_simplify_none_1(self):
        imp_9 = implicant.Implicant("ab'c'd")  
        imp_12 = implicant.Implicant("abc'd'")  
        # M0 and M12 differ in more than one literal --> None

        result = imp_9.simplify(imp_12)
        self.assertEqual(result, None)


    def test_simplify_none_2(self):
        imp_9 = implicant.Implicant("ab'c'd")  
        imp_4 = implicant.Implicant("ab'c'")  
        # not the same length --> None

        result = imp_9.simplify(imp_4)
        self.assertEqual(result, None)
 
    def test_simplify_none_3(self):
        x1 = implicant.Implicant("a'cd'")  
        x2 = implicant.Implicant("a'bd'")  
        # not the same variables--> None

        result = x2.simplify(x2)
        self.assertEqual(result, None)

    def test_simplify_none_4(self):
        x1 = implicant.Implicant("a'cd'")  
        x2 = implicant.Implicant("a'bd'")  
        # not the same variables--> None

        result = x2.simplify(x2)
        self.assertEqual(result, None)
 
    def test_simplify_minterms_function_of_2_vars(self):
        """
            not really a unit tests

            for a function of two variables we have:

              b
          a      0     1
              ┌─────┬─────┐
            0 │ m0  │ m1  │   00  01
              ├─────┼─────┤
            1 │ m2  │ m3  │   10  11
              └─────┴─────┘
            m0,m0: --> None
            m0,m1: simplify a'b'(0), a'b(1) --> a'(0,1)
            m0,m2: simplify a'b'(0), ab'(2) --> b'(0,2)
            m0,m3: simplify a'b'(0), ab(3) --> None, b/c diagonal are not adjacent, does not simplify
            
            m1, m0: was already done
            m1, m1: --> None
            m1,m2: simplify a'b(1), ab'(2) --> None b/c diagonal are not adjacent, does not simplify
            m1,m3: simplify a'b(1), ab(3) --> b(1,3)
            
            m2,m0: was already done
            m2,m1: was already done
            m2,m2: --> None
            m2,m3: simplify ab'(2), ab(3) --> a(2,3)

            # how do we handle case: f(a,b) = a'b' + a'b + ab' + ab
            #  all of the cells are 1 ? --> 1

        """

        imp_0 = implicant.Implicant("a'b'")
        imp_1 = implicant.Implicant("a'b")
        imp_2 = implicant.Implicant("ab'")
        imp_3 = implicant.Implicant("ab")

        #  simplify m0, m0  --> None
        result = imp_0.simplify(imp_0)
        self.assertEqual(result, None)

        #  simplify a'b'(0), a'b(1) --> a'(0,1)
        result = imp_0.simplify(imp_1)
        self.assertEqual(result.get(), ("a'",) )
        self.assertEqual(result.get_str(), "a'" )
        self.assertEqual(result.get_cover(), (0,1) )
 
        #  simplify a'b'(0), ab'(2) --> b'(0,2)
        result = imp_0.simplify(imp_2)
        self.assertEqual(result.get(), ("b'",) )
        self.assertEqual(result.get_str(), "b'" )
        self.assertEqual(result.get_cover(), (0,2) )

        #  simplify a'b'(0), ab(3) --> None
        result = imp_0.simplify(imp_3)
        self.assertEqual(result, None)

        #  simplify m1, m0 was alredy done
        #  simplify m1, m1  --> None
        result = imp_1.simplify(imp_1)
        self.assertEqual(result, None)

        #  simplify a'b(1), ab'(2) --> None b/c diagonal are not adjacent, does not simplify
        result = imp_1.simplify(imp_2)
        self.assertEqual(result, None)
 
        #  simplify a'b(1), ab(3) --> b(1,3)
        result = imp_1.simplify(imp_3)
        self.assertEqual(result.get(), ("b",) )
        self.assertEqual(result.get_str(), "b" )
        self.assertEqual(result.get_cover(), (1,3) )

        #  m2,m0: was already done
        #  m2,m1: was already done
        #  simplify m2, m2  --> None
        result = imp_2.simplify(imp_2)
        self.assertEqual(result, None)

        #  simplify ab'(2), ab(3) --> a(2,3)
        result = imp_2.simplify(imp_3)
        self.assertEqual(result.get(), ("a",) )
        self.assertEqual(result.get_str(), "a" )
        self.assertEqual(result.get_cover(), (2,3) )
 

    def test_simplify_minterms_function_of_2_vars(self):
        """
            not really a unit tests

            for a function of three variables we have:

              bc
          a      00   01    11     10
              ┌─────┬─────┬─────┬─────┐
            0 │ m0  │ m1  │ m3  │ m2  │   000  001  011  010
              ├─────┼─────┼─────┼─────┤
            1 │ m4  │ m5  │ m7  │ m6  │   100  101  111  110
              └─────┴─────┴─────┴─────┘
            
            m0, m0: simplify a'b'c'(0), a'b'c'(0) --> None
            m0, m1: simplify a'b'c'(0), a'b'c(1) --> a'b'(0,1)
            m0, m2: simplify a'b'c'(0), a'bc'(2) --> a'c'(0,2)
            m0, m3: simplify a'b'c'(0), a'bc(3) --> None
            m0, m4: simplify a'b'c'(0), ab'c'(4) --> b'c'(0,4)
            m0, m5: simplify a'b'c'(0), ab'c(5) --> None
            m0, m6: simplify a'b'c'(0), abc'(6) --> None
            m0, m7: simplify a'b'c'(0), abc(7) --> None
         
            # m1,m0 was already done
            m1, m1: simplify a'b'c(1), a'b'c(1) --> None
            m1, m2: simplify a'b'c(1), a'bc'(2) --> None
            m1, m3: simplify a'b'c(1), a'bc(3) --> a'c(1,3)
            m1, m4: simplify a'b'c(1), ab'c'(4) --> None
            m1, m5: simplify a'b'c(1), ab'c(5) --> b'c(1,5)
            m1, m6: simplify a'b'c(1), abc'(6) --> None
            m1, m7: simplify a'b'c(1), abc(7) --> None

            # m2, m0 was already done
            # m2, m1 was already done
            m2, m2: simplify a'bc'(2), a'bc'(2) --> None
            m2, m3: simplify a'bc'(2), a'bc(3) --> a'b(2,3)
            m2, m4: simplify a'bc'(2), ab'c'(4) --> None
            m2, m5: simplify a'bc'(2), ab'c(5) --> None
            m2, m6: simplify a'bc'(2), abc'(6) --> bc'(2,6)
            m2, m7: simplify a'bc'(2), abc(7) --> None
       
            # m3, m0 was already done
            # m3, m1 was already done
            # m3, m2 was already done
            m3, m3: simplify a'bc(3), a'bc(3) --> None
            m3, m4: simplify a'bc(3), ab'c'(4) --> None
            m3, m5: simplify a'bc(3), ab'c(5) --> None
            m3, m6: simplify a'bc(3), abc'(6) --> None
            m3, m7: simplify a'bc(3), abc(7) --> bc(3,7)

            # m4, m0 was already done
            # m4, m1 was already done
            # m4, m2 was already done
            # m4, m3 was already done
            m4, m4: simplify ab'c'(4), ab'c'(4)  --> None
            m4, m5: simplify ab'c'(4), ab'c(5)  --> ab'(4,5)
            m4, m6: simplify ab'c'(4), abc'(6)  --> ac'(4,6)
            m4, m7: simplify ab'c'(4), abc(7)  --> None

            # m5, m0 was already done
            # m5, m1 was already done
            # m5, m2 was already done
            # m5, m3 was already done
            # m5, m4 was already done
            m5, m5: simplify ab'c(5), ab'c(5)  --> None
            m5, m6: simplify ab'c(5), abc'(6)  --> None
            m5, m7: simplify ab'c(5), abc(7)  --> ac(5,7)

            # m6, m0 was already done
            # m6, m1 was already done
            # m6, m2 was already done
            # m6, m3 was already done
            # m6, m4 was already done
            # m6, m5 was already done
            m6, m6: simplify abc'(6), abc'(6)  --> None
            m6, m7: simplify abc'(6), abc(7)  --> ab(6,7)

            row1: m0, m1, m3, m2 --> a'
    
            and so on

            row2: m4, m5, m7, m6 --> a

            col1,col2: m0,m1,m4,m5 --> b'

            col3,col4: m3,m2,m7,m6 --> b

            col2,col3: m1,m5,m3,m7 --> c

            col1,col4: m0,m4,m2,m6 --> c'


        """
        imp_0 = implicant.Implicant("a'b'c'")
        imp_1 = implicant.Implicant("a'b'c")
        imp_2 = implicant.Implicant("a'bc'")
        imp_3 = implicant.Implicant("a'bc")
        imp_4 = implicant.Implicant("ab'c'")
        imp_5 = implicant.Implicant("ab'c")
        imp_6 = implicant.Implicant("abc'")
        imp_7 = implicant.Implicant("abc")

        #
        # m0
        #
        #  m0, m0: simplify a'b'c'(0), a'b'c'(0) --> None
        result = imp_0.simplify(imp_0)
        self.assertEqual(result, None )

        #  m0,m1: simplify a'b'c'(0), a'b'c(1) --> a'b'(0,1)
        result = imp_0.simplify(imp_1)
        self.assertEqual(result.get(), ("a'","b'") )
        self.assertEqual(result.get_str(), "a'b'" )
        self.assertEqual(result.get_cover(), (0,1) )

        #   simplify a'b'c'(0), a'bc'(2) --> a'c'(0,2)
        result = imp_0.simplify(imp_2)
        self.assertEqual(result.get(), ("a'","c'") )
        self.assertEqual(result.get_str(), "a'c'" )
        self.assertEqual(result.get_cover(), (0,2) )

        #    m0, m3: simplify a'b'c'(0), a'bc(3) --> None
        result = imp_0.simplify(imp_3)
        self.assertEqual(result, None )

        #  m0,m4: simplify a'b'c'(0), ab'c'(4) --> b'c'(0,4)
        result = imp_0.simplify(imp_4)
        self.assertEqual(result.get(), ("b'","c'") )
        self.assertEqual(result.get_str(), "b'c'" )
        self.assertEqual(result.get_cover(), (0,4) )

        #  m0, m5: simplify a'b'c'(0), ab'c(5) --> None
        result = imp_0.simplify(imp_5)
        self.assertEqual(result, None )

       #  m0, m6: simplify a'b'c'(0), abc'(6) --> None
        result = imp_0.simplify(imp_6)
        self.assertEqual(result, None )

       #  m0, m7: simplify a'b'c'(0), abc(7) --> None
        result = imp_0.simplify(imp_7)
        self.assertEqual(result, None )

        #
        # m1
        #
        # m1,m0 was already done
        #  m1, m1: simplify a'b'c(1), a'b'c(1) --> None
        result = imp_1.simplify(imp_1)
        self.assertEqual(result, None )

        #  m1, m2: simplify a'b'c(1), a'bc'(2) --> None
        result = imp_1.simplify(imp_2)
        self.assertEqual(result, None )

        #  m1, m3: simplify a'b'c(1), a'bc(3) --> a'c(1,3)
        result = imp_1.simplify(imp_3)
        self.assertEqual(result.get(), ("a'","c") )
        self.assertEqual(result.get_str(), "a'c" )
        self.assertEqual(result.get_cover(), (1,3) )

        #  m1, m4: simplify a'b'c(1), ab'c'(4) --> None
        result = imp_1.simplify(imp_4)
        self.assertEqual(result, None )

        #  m1, m5: simplify a'b'c(1), ab'c(5) --> b'c(1,5)
        result = imp_1.simplify(imp_5)
        self.assertEqual(result.get(), ("b'","c") )
        self.assertEqual(result.get_str(), "b'c" )
        self.assertEqual(result.get_cover(), (1,5) )

        #  m1, m6: simplify a'b'c(1), abc'(6) --> None
        result = imp_1.simplify(imp_6)
        self.assertEqual(result, None )

        #  m1, m7: simplify a'b'c(1), abc(7) --> None
        result = imp_1.simplify(imp_7)
        self.assertEqual(result, None )



        #
        # m2
        #
        # m2, m0 was already done
        # m2, m1 was already done

        #  m2, m2: simplify a'bc'(2), a'bc'(2) --> None
        result = imp_2.simplify(imp_2)
        self.assertEqual(result, None )

        #  m2, m3: simplify a'bc'(2), a'bc(3) --> a'b(2,3)
        result = imp_2.simplify(imp_3)
        self.assertEqual(result.get(), ("a'","b") )
        self.assertEqual(result.get_str(), "a'b" )
        self.assertEqual(result.get_cover(), (2,3) )

        #    m2, m4: simplify a'bc'(2), ab'c'(4) --> None
        result = imp_2.simplify(imp_4)
        self.assertEqual(result, None )


        #    m2, m5: simplify a'bc'(2), ab'c(5) --> None
        result = imp_2.simplify(imp_5)
        self.assertEqual(result, None )


        #    m2, m6: simplify a'bc'(2), abc'(6) --> bc'(2,6)
        result = imp_2.simplify(imp_6)
        self.assertEqual(result.get(), ("b","c'") )
        self.assertEqual(result.get_str(), "bc'" )
        self.assertEqual(result.get_cover(), (2,6) )

        #    m2, m7: simplify a'bc'(2), abc(7) --> None
        result = imp_2.simplify(imp_7)
        self.assertEqual(result, None )

 
        #
        # m3
        #
        # m3, m0 was already done
        # m3, m1 was already done
        # m3, m2 was already done
        
        #  m3, m3: simplify a'bc(3), a'bc(3) --> None
        result = imp_3.simplify(imp_3)
        self.assertEqual(result, None )

        #  m3, m4: simplify a'bc(3), ab'c'(4) --> None
        result = imp_3.simplify(imp_4)
        self.assertEqual(result, None )
       
        #  m3, m5: simplify a'bc(3), ab'c(5) --> None
        result = imp_3.simplify(imp_6)
        self.assertEqual(result, None )

        #  m3, m6: simplify a'bc(3), abc'(6) --> None
        result = imp_3.simplify(imp_6)
        self.assertEqual(result, None )
        
        #  m3, m7: simplify a'bc(3), abc(7) --> bc(3,7)
        result = imp_3.simplify(imp_7)
        self.assertEqual(result.get(), ("b","c") )
        self.assertEqual(result.get_str(), "bc" )
        self.assertEqual(result.get_cover(), (3,7) )


        #
        # m4
        #
        # m4, m0 was already done
        # m4, m1 was already done
        # m4, m2 was already done
        # m4, m3 was already done

        # m4, m4: simplify ab'c'(4), ab'c'(4)  --> None
        result = imp_4.simplify(imp_4)
        self.assertEqual(result, None )
 
        # m4, m5: simplify ab'c'(4), ab'c(5)  --> ab'(4,5)
        result = imp_4.simplify(imp_5)
        self.assertEqual(result.get(), ("a","b'") )
        self.assertEqual(result.get_str(), "ab'" )
        self.assertEqual(result.get_cover(), (4,5) )


        # m4, m6: simplify ab'c'(4), abc'(6)  --> ac'(4,6)
        result = imp_4.simplify(imp_6)
        self.assertEqual(result.get(), ("a","c'") )
        self.assertEqual(result.get_str(), "ac'" )
        self.assertEqual(result.get_cover(), (4,6) )


        # m4, m7: simplify ab'c'(4), abc(7)  --> None
        result = imp_4.simplify(imp_7)
        self.assertEqual(result, None )
 
        #
        # m5
        #
        # m5, m0 was already done
        # m5, m1 was already done
        # m5, m2 was already done
        # m5, m3 was already done
        # m5, m4 was already done

        # m5, m5: simplify ab'c(5), ab'c(5)  --> None
        result = imp_5.simplify(imp_5)
        self.assertEqual(result, None )
 
        # m5, m6: simplify ab'c(5), abc'(6)  --> None
        result = imp_5.simplify(imp_6)
        self.assertEqual(result, None )
 
        # m5, m7: simplify ab'c(5), abc(7)  --> ac(5,7)
        result = imp_5.simplify(imp_7)
        self.assertEqual(result.get(), ("a","c") )
        self.assertEqual(result.get_str(), "ac" )
        self.assertEqual(result.get_cover(), (5,7) )


        #
        # m6
        #
        # m6, m0 was already done
        # m6, m1 was already done
        # m6, m2 was already done
        # m6, m3 was already done
        # m6, m4 was already done
        # m6, m5 was already done
        # m6, m6: simplify abc'(6), abc'(6)  --> None
        result = imp_6.simplify(imp_6)
        self.assertEqual(result, None )
 
        # m6, m7: simplify abc'(6), abc(7)  --> ab(6,7)
        result = imp_6.simplify(imp_7)
        self.assertEqual(result.get(), ("a","b") )
        self.assertEqual(result.get_str(), "ab" )
        self.assertEqual(result.get_cover(), (6,7))

        # Best make use of hamming weight to do less work
        # row1: m0, m1, m3, m2 --> a'
        #    m0  000
        #    m1  001
        #    m3  011
        #    m2  010
        # 
        # hamming 0 with hamming 1
        #      m0 m1 --> a'b'(0,1)
        #      m0 m2 --> a'c'(0,2)
        #
        # hamming 1 with hamming 2
        #      m1 m3 --> a'c(1,3)
        #      m2 m3 --> a'b(2,3)

        # hamming 0 with haming 1
        #  m0m1 m1m3:   a'b'(0,1) a'c(1,3) --> None
        #  m0m1 m2m3:   a'b'(0,1) a'b(2,3) -->  a'(0,1,2,3)
        #  m0m2 m1m3:   a'c'(0,2) a'c(1,3) --> a'(0,2,1,3) same cover as above line if cover is sorted 
        #  m0m2 m2m3:   a'c'(0,2) a'b(2,3) --> None
        #  
        m0m1 = imp_0.simplify(imp_1)  # we already checked the result above
        m0m2 = imp_0.simplify(imp_2)  # we already checked the result above

        m1m3 = imp_1.simplify(imp_3)  # we already checked the result above
        m2m3 = imp_2.simplify(imp_3)  # we already checked the result above

        result = m0m1.simplify(m1m3)
        self.assertEqual(result, None )

        result = m0m1.simplify(m2m3)
        self.assertEqual(result.get(), ("a'",) )
        self.assertEqual(result.get_str(), "a'" )
        self.assertEqual(result.get_cover(), (0,1,2,3) )


        result = m0m2.simplify(m1m3)
        self.assertEqual(result.get(), ("a'",) )
        self.assertEqual(result.get_str(), "a'" )
        self.assertEqual(result.get_cover(), (0,1,2,3) )


        result = m0m2.simplify(m2m3)
        self.assertEqual(result, None )

        # and so on



if __name__ == '__main__':
    unittest.main()

