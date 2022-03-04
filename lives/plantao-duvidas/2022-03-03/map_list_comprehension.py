alunos = [
    {
        "nome": "Gabriel",
        "nota": 10,
    },
    {
        "nome": "Bruno",
        "nota": 8,
    }
]


def dobra_nota(nota):
    return nota * 2

notas_dobradas = [aluno["nota"] * 2 for aluno in alunos]  # [20, 16]
notas_dobradas_map = map(dobra_nota, notas_dobradas)


print(notas_dobradas)
print(list(notas_dobradas_map))
