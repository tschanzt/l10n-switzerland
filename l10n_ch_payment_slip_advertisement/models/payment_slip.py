from odoo import models, fields


class PaymentSlip(models.Model):

    _inherit = 'l10n_ch.payment_slip'

    payment_slip_advertisement_id = fields.Many2one(
        comodel_name='l10n_ch.payment_slip.advertisement',
        compute='_compute_advertisement',
        store=False,
        readonly=True
    )

    def _compute_advertisement(self):
        lang = self.invoice_id.partner_id.lang
        lang_obj = self.env['res.lang'].search([('code', '=', lang)])
        prod_ids = self.invoice_id.invoice_line_ids.mapped('product_id').ids
        import pdb; pdb.set_trace()

    def _draw_hook(self, draw, print_settings):
        ad = self.payment_slip_advertisement_id
        import pdb; pdb.set_trace()
