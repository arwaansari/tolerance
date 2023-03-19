from odoo import models, fields


class PurchaseOrderLineInherit(models.Model):
    _inherit = 'purchase.order.line'

    tolerance = fields.Integer(string='Tolerance',
                               related='order_id.partner_id.tolerance')
