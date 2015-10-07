# -*- coding: utf-8 -*-
from common.models.category import Wire, MechanicalEquipment, Rubber


def choice_table(cable_type):
    cable_type = cable_type[:1]
    table = None
    if cable_type == 'W':
        table = Wire
    elif cable_type == 'E':
        table = MechanicalEquipment
    elif cable_type == 'R':
        table = Rubber
    return table