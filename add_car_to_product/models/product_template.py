from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_autoparts = fields.Boolean(string="Is autopart")


class ProductProduct(models.Model):
    _inherit = "product.product"

    is_autoparts = fields.Boolean(
        related="product.template.is_autopatrs",
        store=True,
        readonly=False
    )
    compatible_vehicle_ids = fields.Many2many(
        "fleet.vehicle.model",
        string="Сумісні моделі"
    )
    for_all_models = fields.Boolean(string="Підходить до всіх авто")
    oem = fields.Char(string="OEM")
    ovoko_part_id = fields.Char(string="Ovoko part ID")
