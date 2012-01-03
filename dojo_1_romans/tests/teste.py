#!/usr/bin/python

import unittest

def roman(num):
    dezena = (num // 10) % 10
    centena = (num // 100) % 10
    milhar = (num // 1000) % 10
    
    comeco = 4
    tamanhos = [1, 4, 1, 30]
    constr = [dezena, centena, milhar]
    digitos = ["I", "V", "X", "L", "C", "D", "M"]
    
    if not num < 4:
        for potencia in range(3):
            for indice, tamanho in enumerate(tamanhos):
                fim = comeco + tamanho * 10 ** potencia
                if comeco <= num < fim:
                    subtr = comeco
                    string = digitos[indice / 2 + potencia * 2 + 1]
                    if tamanho == 30:
                        subtr = constr[potencia] * 10 ** (potencia + 1) 
                        string = string * constr[potencia]
                    elif tamanho == 1 : string = digitos[potencia * 2] + string
                    return string + roman(num - subtr)
                comeco = fim

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

