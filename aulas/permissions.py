from rolepermissions.permissions import register_object_checker
from policlass.roles import Funcionario, Aluno


@register_object_checker()
def access_aula(role, user, aula):
    if role == Funcionario:
        return True

    if role == Aluno:
        return True

    return False
