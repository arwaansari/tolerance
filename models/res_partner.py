from odoo import models, fields


class CustomerInherit(models.Model):
    _inherit = "res.partner"

    tolerance = fields.Integer(string='Tolerance', store=True)
