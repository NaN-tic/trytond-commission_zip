# This file is part of the commission_zip module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

from sql.operators import Like


__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @fields.depends('party', 'shipment_address')
    def on_change_with_agent(self, name=None):
        if self.shipment_address and self.shipment_address.zip:
            pool = Pool()
            ZipCode = pool.get('agent.zip.code')
            Agent = pool.get('commission.agent')
            cursor = Transaction().cursor

            agent_zip_code = ZipCode.__table__()
            commission_agent = Agent.__table__()
            zip_code = self.shipment_address.zip

            where = (
                (Like(agent_zip_code.zip_code, zip_code))
                )
            while len(zip_code) > 2:
                where |= (Like(agent_zip_code.zip_code, zip_code[:-1]))
                zip_code = zip_code[:-1]
            query = (agent_zip_code
                .join(commission_agent, 'LEFT',
                    condition=(
                        agent_zip_code.agent == commission_agent.id
                        ))
                .select(commission_agent.id,
                    where=where,
                    order_by=agent_zip_code.sequence,
                    ))
            cursor.execute(*query)
            agent_id = cursor.fetchone()
            if agent_id:
                return agent_id[0]
