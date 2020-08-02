from rolepermissions.permissions import register_object_checker

from policlass.roles import Funcionario


@register_object_checker("manage_cadeira")
def gerencia_cadeiras(role, user, cadeira):
    return role == Funcionario
