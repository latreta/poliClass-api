from rolepermissions.permissions import register_object_checker

from policlass.roles import Funcionario


@register_object_checker("manage_bloco")
def gerencia_bloco(role, user, bloco):
    return role == Funcionario
