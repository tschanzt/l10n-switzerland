from odoo import models, fields


class PaymentslipAd(models.Model):
    _name = 'l10n_ch.payment_slip.advertisement'

    _order = 'sequence'

    sequence = fields.Integer()
    active = fields.Boolean()
    lang_id = fields.Many2one(
        comodel_name='res.lang',
        string='Language'
    )
    product_ids = fields.Many2many(
        comodel_name='product.product',
        string='Product'
    )
    image = fields.Binary('image')
