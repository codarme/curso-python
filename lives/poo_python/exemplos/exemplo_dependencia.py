from dataclasses import dataclass
from typing import Iterable


@dataclass
class Turma:
    pass

@dataclass
class Aluno:
    pass

@dataclass
class Curso:
    turmas: Iterable[Turma]

    def matricular(self, aluno: Aluno):
        self.turmas.append(aluno)

