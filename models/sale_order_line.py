from odoo import models, fields, api


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    tolerance = fields.Integer(string='Tolerance')

    @api.onchange('product_template_id')
    def set_tolerance(self):
        for rec in self:
            rec.tolerance = rec.order_id.partner_id.tolerance
