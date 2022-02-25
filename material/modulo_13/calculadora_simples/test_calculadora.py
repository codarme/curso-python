from calculadora import somar, dividir
import unittest


class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        soma = somar(2, 4)
        self.assertEqual(soma, 6)

    def test_soma_de_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        self.assertEqual(dividir(10, 1), 10)

    def test_divide_por_zero_(self):
        self.assertEqual(dividir(10, 0), "Não é um número")


unittest.main()