from rolepermissions.permissions import register_object_checker
from policlass.roles import Funcionario


@register_object_checker()
def create_aula(role, user, aula):
    if role == Funcionario:
        return True
    return False


@register_object_checker()
def update_aula(role, user, aula):
    if role == Funcionario:
        return True
    return False


@register_object_checker()
def destroy_aula(role, user, aula):
    if role == Funcionario:
        return True
    return False

