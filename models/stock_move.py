from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    tolerance = fields.Integer(string='Tolerance',
                               related='sale_line_id.tolerance')
