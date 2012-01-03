#!/usr/bin/python

import unittest

def roman(num):
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10
    milhar = (num // 1000) % 10

    
    if num == 4:
        return "IV"
    if 5 <= num < 9:
        return "V" + roman(num - 5)
    if num == 9:
        return "IX"
    if 10 <= num < 40:
        return "X" * dezena + roman(unidade)
    if 40 <= num < 50:
        return "XL" + roman(unidade)
    if 50 <= num < 90:
        return "L" + roman(num - 50)
    if 90 <= num < 100:
        return "XC" + roman(unidade)
    if 100 <= num < 400:
        return "C" * centena + roman((dezena * 10) + unidade)
    if 400 <= num < 500:
        return "CD" + roman(num - 400)
    if 500 <= num < 900:
        return "D" + roman(num - 500)
    if 900 <= num < 1000:
        return "CM" + roman(num - 900)
    if 1000 <= num < 4000:
        return "M" * milhar + roman(num - milhar * 1000)
    
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
            
        

