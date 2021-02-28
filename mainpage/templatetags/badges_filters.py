#!/usr/bin/env python

import os
from django import template

register = template.Library()

@register.filter(name='subset')
def subset(lista, grupo):
    """
    Lista badges de la BD ordenados por el campo `order`.
    Grupo es un número entero (0, 1, 2...). Devolverá todos
    los objetos que tengan el campo `order` entre 0 y 100, 100 y 200, etc.
    Si es un número negativo, devolverá todos.
    """
    if lista is None:
        lista = []
    if grupo < 0:
        res = lista
    else:
        r_ini, r_fin = grupo*100, (grupo+1)*100
        res = [badge for badge in lista
               if badge.order>=r_ini and badge.order<r_fin]
    res.sort(key=lambda badge: badge.order)
    return res


@register.filter(name='basename')
def basename(ruta):
    return os.path.basename(ruta)
