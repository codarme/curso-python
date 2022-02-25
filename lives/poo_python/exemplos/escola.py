"""
ESCOLA DE PROGRAMAÇÃO
======================

# Cursos e matrícula
* Nossa escola possui diversos Cursos e cada Curso pode ter múltiplas Turmas.
* Usuários podem se matricular em um ou mais Cursos.
    * Essa matrícula gera um Aluno associado ao Usuário e à Turma na qual ele foi matriculado.
    * A Turma 
    * Alunos podem ser removidos de uma Turma.


# Turmas
* Cada Turma tem uma data de início e data de fim.
    * Turmas de um mesmo Curso não podem ocorrer durante as mesmas datas.
* Toda Turma tem um limite máximo de alunos matriculados nela.
* Alunos só podem ser matriculados em um Curso se houverem Turmas "disponíveis" para aquele Curso.
* Uma Turma é considerada disponível se: ainda não foi iniciada e não está cheia (limite de alunos).


# Aulas
* Todo Curso possui uma grade que é expressa através de uma lista ordenada de Aulas.
* Aulas podem estar publicadas ou não. 
* A grade do Curso (lista de aulas) pode ser vazia (sob construção).
* Aulas podem ser adicionadas a um curso apenas se estiverem publicadas.
* Para publicar uma aula é necessário que ela possua pelo menos 1 conteúdo (ConteudoAula).
* A mesma Aula pode estar presente em duas grades.


# Conteúdo
* Um Conteúdo pode ser um Vídeo, Texto ou Áudio.


# Extras
* Administrador: usuários que possuem acesso para editar o curso, matricular e remover alunos.
* Progresso: como saber quais conteúdos um determinado aluno assistiu?
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