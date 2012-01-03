#!/usr/bin/python

import unittest

def roman(num):
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10
    milhar = (num // 1000) % 10

    start = 4
    intervals = [
        (5, "IV", 0), # 4
        (9, "V", num - 5), # 5 a 8
        (10, "IX", 0), # 9
        (40, "X" * dezena, unidade), # 10 a 39
        (50, "XL", unidade), # 40 a 49
        (90, "L", num - 50), # 50 a 89
        (100, "XC", unidade), # 90 a 99
        (400, "C" * centena, (dezena * 10) + unidade), # 100 a 399
        (500, "CD", num - 400), # 400 a 499
        (900, "D", num - 500), # 500 a 899
        (1000, "CM", num - 900), # 900 a 999
        (4000, "M" * milhar, num - milhar * 1000), # 1000 a 3999
    ]
    
    for (end, string, recursion) in intervals:
        if start <= num < end:
            return string + roman(recursion)
        start = end
        
    return "I" * num


class BaseTest(unittest.TestCase):

    def test_babacas(self):
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
            
        

