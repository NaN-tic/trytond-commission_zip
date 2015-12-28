# This file is part of the commission_zip module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .commission import *
from .sale import *


def register():
    Pool.register(
        AgentZipCode,
        Agent,
        Sale,
        module='commission_zip', type_='model')
