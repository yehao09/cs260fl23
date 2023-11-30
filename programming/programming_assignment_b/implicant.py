from icecream import ic
 
class Implicant:
    def __init__(self, implicant: str, covered_minterms=None):

        # check if implicant parameter is str
        if not isinstance(implicant, str):
            raise TypeError("implicant must be str")

        self.implicant_str = implicant

        self.implicant = self.set_implicant()

        self.implicant_bin = self.get_implicant_bin_repr()

        self.cover = self.set_cover(covered_minterms)

    def get_implicant_bin_repr(self):

        result = []
        for element in self.implicant:
            if element[-1] == "'":
                result.append(0)
            else:
                result.append(1)

        return tuple(result)

    def set_cover(self, covered_minterms):
        if not covered_minterms:
            result = 0
            for index in range(len(self.implicant_bin) - 1, -1, -1):
                result += self.implicant_bin[index] * 2 ** (len(self.implicant_bin) - 1 - index)
            return tuple([result])

        return covered_minterms

    def set_implicant(self):
        index = len(self.implicant_str) - 1
        result = []
        while index >= 0:
            if self.implicant_str[index] == "'":
                result.insert(0, self.implicant_str[index - 1] + self.implicant_str[index])
                index -= 1
            else:
                result.insert(0, self.implicant_str[index])
            index -= 1

        return tuple(result)

    def get(self):
        return self.implicant

    def get_cover(self):
        return self.cover

    def get_hamming_weight(self):
        return sum(self.implicant_bin)

    def get_str(self):
        return "".join(self.implicant)


    def simplify(self, another_implicant):
      if not isinstance(another_implicant, Implicant):
        raise TypeError("another_implicant must be of Implicant class")

      count_of_differences = 0
      result = ""
      index = 0

      if len(self.implicant) != len(another_implicant.implicant):
        return None

      while index < len(self.implicant):
        if self.implicant[index] == another_implicant.implicant[index]:
            result = f'{result}{self.implicant[index]}'
        else:
            count_of_differences += 1

        index += 1

      if count_of_differences != 1:
        return None

      return Implicant(result, covered_minterms=self.cover + another_implicant.cover)


if __name__ == "__main__":
      implicant1 = Implicant("a'bc")
      implicant2 = Implicant("abc")
      ic(implicant1.implicant_bin)
      ic(implicant1.cover)
      ic(implicant1.get_implicant())
      ic(implicant2.get_implicant())

      result = implicant1.simplify(implicant2)
      ic(result.get_implicant())
      ic(result.cover)
