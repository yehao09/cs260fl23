from icecream import ic

class Implicant:
    def __init__(self, implicant:str, covered_minterms = None ):

        # check if implicant parameter is str
        if not isinstance(implicant, str):
        # if type(implicant) != str:
            raise TypeError("implicant must be str")

        self.implicant_str = implicant

        self.implicant = self.set_implicant()

    def set_implicant(self):
        index = len(self.implicant_str) -1
        result = []
        while index >=0:
            if self.implicant_str[index] == "'":
                result.insert(0,self.implicant_str[index-1] + self.implicant_str[index])
                index -=1
            else:
                result.insert(0,self.implicant_str[index])
            index -= 1

        return tuple(result)

    def get_implicant(self):
        return self.implicant

if __name__ == "__main__":
    implicant1 = Implicant("a'bc'")
    ic( implicant1.get_implicant() )
