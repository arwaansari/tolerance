from odoo import models


class WarningWizard(models.Model):
    _name = 'warning.wizard'

    def action_accept(self):
        print('accept')
        self.env['stock.picking'].\
            browse(self.env.context.get('active_ids')).write({'state': "done"})

    def action_dont_accept(self):
        print('dont accept')
        self.env['stock.picking'].browse(self.env.context.get('active_ids')).\
            write({'state': "assigned"})

