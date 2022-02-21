"""
Esse é o modelo da nossa escola de programação.
Nossa escola possui diversos Cursos e cada Curso pode ter múltiplas Turmas.
Cada Turma tem uma data de início e data de fim.
Turmas de um mesmo Curso não podem ocorrer entre as mesmas datas.
Usuários podem se matricular em um determinado Curso.
A matrícula de um Usuário em um Curso cria um Aluno associado ao Usuário e à Turma na qual ele foi matriculado.
A Turma é selecionada automaticamente, de acordo com a lógica de matrícula.
Toda Turma tem um limite máximo de alunos matriculados nela.
Alunos podem ser removidos de uma Turma.
Alunos só podem ser matriculados em um Curso se houverem Turmas "disponíveis" para aquele Curso.
Uma Turma é considerada disponível se: ainda não foi iniciada e não está cheia (limite de alunos).

Aulas podem estar publicadas ou não. 
Todo Curso possui uma grade que é expressa através de uma lista de Aulas.
A grade do Curso pode estar sob construção e ser vazia.
Aulas podem ser adicionadas ao Curso depois que este foi criado.
A mesma Aula pode ser parte de cursos diferentes.
"""

class Usuario:
    pass


class Aluno:
    pass


class Curso:
    pass


class Turma:
    pass


class Aula:
    pass


class ConteudoAula:
    pass