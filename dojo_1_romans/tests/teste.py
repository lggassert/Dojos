#!/usr/bin/python

import unittest

def roman(num):
    if num >= 4000:
        num = 0
    
    if not num < 4:
        constr = [int(i) for i in str(num)]
        constr.pop()
        constr.reverse()

        sizes = [1, 4, 1, 30]
        digits = ["I", "V", "X", "L", "C", "D", "M"]

        start = 4
        for power in range(3):
            for index, size in enumerate(sizes):
                end = start + size * 10 ** power
                if start <= num < end:
                    subtr = start
                    string = digits[index / 2 + power * 2 + 1]
                    if size == 1 : string = digits[power * 2] + string
                    elif size == 30:
                        subtr = constr[power] * 10 ** (power + 1) 
                        string = string * constr[power]
                    return string + roman(num - subtr)
                start = end

    return "I" * num

class BaseTest(unittest.TestCase):

    def test_babacas(self):
        self.assertEquals(roman(-1), "")
        self.assertEquals(roman(4000), "")
        self.assertEquals(roman(42), "XLII")
        self.assertEquals(roman(54), "LIV")
        self.assertEquals(roman(89), "LXXXIX")
        self.assertEquals(roman(200), "CC")
        self.assertEquals(roman(202), "CCII")
        self.assertEquals(roman(400), "CD")
        self.assertEquals(roman(404), "CDIV")
        self.assertEquals(roman(600), "DC")
        self.assertEquals(roman(800), "DCCC")
        self.assertEquals(roman(923), "CMXXIII")
        self.assertEquals(roman(999), "CMXCIX")
        self.assertEquals(roman(3003), "MMMIII")
        self.assertEquals(roman(3974), "MMMCMLXXIV")
        self.assertEquals(roman(3999), "MMMCMXCIX")

    def test_unidades(self):
        romans = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X" ]
        for i, r in enumerate(romans):
            self.assertEquals(roman(i), r)

    def test_basico(self):
        self.assertEquals(roman(1), "I")
        self.assertEquals(roman(2), "II")
        self.assertEquals(roman(50), "L")
        self.assertEquals(roman(100), "C")
        self.assertEquals(roman(500), "D")
        self.assertEquals(roman(1000), "M")

    def test_multiplos_10(self):
        self.assertEquals(roman(10), "X")
        self.assertEquals(roman(20), "XX")
        self.assertEquals(roman(30), "XXX")
        self.assertEquals(roman(40), "XL")
        self.assertEquals(roman(60), "LX")
        self.assertEquals(roman(70), "LXX")
        self.assertEquals(roman(80), "LXXX")
        self.assertEquals(roman(90), "XC")

