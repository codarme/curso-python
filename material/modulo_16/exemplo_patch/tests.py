""""
Esse arquivo é uma breve demonstração sobre o problema de "onde fazer o patch" quando
estamos escrevendo testes para Python.

Para executá-lo, execute "python3 tests.py"

Um dos testes falha propositalmente.

Para mais informações, leia a seção "Where to Patch" da documentação oficial do Python:
https://docs.python.org/3/library/unittest.mock.html#where-to-patch
"""
from unittest import main, TestCase, mock

import modulo_a, modulo_c


class TestModuloA(TestCase):
    @mock.patch("modulo_a.foo_modulo_b", return_value="mockado!")
    def test_mock_modulo_b_corretamente(self, mock_b):
        """
        Observe que estamos executando o modulo_a.foo_modulo_a
        Logo, o patch que temos que fazer é do nome "foo_modulo_b" em "modulo_a",
        e não onde "foo_modulo_b" é definido.
        """
        response = modulo_a.foo_modulo_a()
        self.assertEqual(response, "mockado!")

    @mock.patch("modulo_b.foo_modulo_b", return_value="mockado!")
    def test_mock_modulo_b_errado(self, mock_b):
        """
        Nesse caso, tentamos fazer o patch de "foo_modulo_b" onde ele é definido,
        ou seja, em "modulo_b". Porém, isso não funciona pois o sistema sendo testado
        é o "modulo_a", onde o nome "foo_modulo_b" é encontrado.
        """
        response = modulo_a.foo_modulo_a()
        # Vai falhar! Chamada em modulo_a.py para foo_modulo_b não foi mockada.
        self.assertEqual(response, "mockado!")


class TestModuloC(TestCase):
    @mock.patch("modulo_c.modulo_b")
    def test_mock_modulo_b_corretamente(self, mock_b):
        """
        O "modulo_c" importa o "modulo_b" completamente. Logo, temos que fazer o patch
        de "modulo_b" a partir de "modulo_c", e, além disso, mockar o atributo
        "modulo_b.foo_modulo_b" para retornar o valor desejado.
        """
        mock_b.foo_modulo_b.return_value = "mockado!"
        response = modulo_c.foo_modulo_c()
        self.assertEqual(response, "mockado!")


if __name__ == "__main__":
    main()