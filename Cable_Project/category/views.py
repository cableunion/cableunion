import random
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from common.helper.models_help import choice_table


def category_detail(request, cable_type):
    table = choice_table(cable_type)
    try:
        category_detail = table.objects.get(cable_type=cable_type)
        table_all = table.objects.all()
    except:
        category_detail = dict()
        table_all = list()
    relation_category = random.sample(table_all, 4 if len(table_all) > 4 else len(table_all))
    if table and category_detail:
        if table.__name__ == 'Wire':
            template_name = 'category-detail-Wire.html'
        elif table.__name__ == 'MechanicalEquipment':
            template_name = 'category-detail-MechanicalEquipment.html'
        elif table.__name__ == 'Rubber':
            template_name = 'category-detail-Rubber.html'
        else:
            template_name = 'category-detail-error.html'
    else:
        template_name = 'category-detail-error.html'
    vm = {
        'category_detail': category_detail,
        'relation_category': relation_category
    }
    return render_to_response(template_name, vm, RequestContext(request))