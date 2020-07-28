from rolepermissions.roles import AbstractUserRole


class Aluno(AbstractUserRole):
    available_permissions = {
        'ver_aulas': True,
        'ver_discentes': True,
        'ver_salas': True,
        'ver_blocos': True,
        'ver_cadeiras': True
    }


class Funcionario(AbstractUserRole):
    available_permissions = {
        'gerenciar_aulas': True,
        'gerenciar_discentes': True,
        'gerenciar_salas': True,
        'gerenciar_cadeiras': True,
        'gerenciar_blocos': True,
    }
