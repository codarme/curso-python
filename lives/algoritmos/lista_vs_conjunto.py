"""
Executar os comandos abaixo no terminal!

python -m timeit --setup "import random;lista = list(range(1000))" "random.randint(1, 100000) in lista"
python -m timeit --setup "import random;lista = set(range(1000))" "random.randint(1, 100000) in lista"

Depois aumentar o range(1000) => range(1000000) e verificar a diferença.
"""