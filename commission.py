# This file is part of the commission_zip module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta


__all__ = ['AgentZipCode', 'Agent']


class AgentZipCode(ModelSQL, ModelView):
    'Agent Zip Code'
    __name__ = 'agent.zip.code'

    sequence = fields.Integer('Sequence')
    agent = fields.Many2One('commission.agent', 'Agent', required=True,
        ondelete='CASCADE')
    zip_code = fields.Char('Zip Code')

    @classmethod
    def __setup__(cls):
        super(AgentZipCode, cls).__setup__()
        cls._order.insert(0, ('sequence', 'ASC'))


class Agent:
    __metaclass__ = PoolMeta
    __name__ = 'commission.agent'
    zip_codes = fields.One2Many('agent.zip.code', 'agent', 'Zip Codes')
