from rolepermissions.permissions import register_object_checker
from policlass.roles import Funcionario


@register_object_checker("manage_aula")
def gerencia_aula(role, user, aula):
    return role == Funcionario

