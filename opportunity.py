# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.modules.account_invoice_contact.invoice import ContactMixin

__all__ = ['Opportunity']
__metaclass__ = PoolMeta


class Opportunity(ContactMixin):
    __name__ = 'sale.opportunity'
    _contact_config_name = 'sale.configuration'
