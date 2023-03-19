from odoo import models, fields


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super(StockPickingInherit, self).button_validate()
        for rec in self.move_ids_without_package:
            min_tol = rec.product_uom_qty - rec.tolerance
            max_tol = rec.product_uom_qty + rec.tolerance
            if rec.quantity_done > max_tol or rec.quantity_done < min_tol:
                return{
                        'name': 'Warning',
                        'type': 'ir.actions.act_window',
                        'res_model': 'warning.wizard',
                        'view_mode': 'form',
                        'target': 'new'
                }
        return res
