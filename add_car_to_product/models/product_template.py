from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_autoparts = fields.Boolean(string="Is autopart")


class ProductProduct(models.Model):
    _inherit = "product.product"

    is_autoparts = fields.Boolean(
        related="product_tmpl_id.is_autoparts",
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

    variant_autopart_name = fields.Char(
        string="Variant name",
        compute="_compute_variant_autopart_name",
    )

    @api.depends(
        "product_tmpl_id.name",
        "compatible_vehicle_ids",
        "compatible_vehicle_ids.brand_id",
        "compatible_vehicle_ids.name",
        "compatible_vehicle_ids.model_type",
        "compatible_vehicle_ids.model_year_from",
        "compatible_vehicle_ids.model_year_to",
    )
    def _compute_variant_autopart_name(self):
        for product in self:
            if product.is_autoparts and product.compatible_vehicle_ids:
                vehicle = product.compatible_vehicle_ids[0]
                years = ""
                if vehicle.model_year_from and vehicle.model_year_to:
                    years = f"{vehicle.model_year_from}-{vehicle.model_year_to}"

                parts = [
                    product.product_tmpl_id.name,
                    vehicle.brand_id.name if vehicle.brand_id else "",
                    vehicle.name or "",
                    vehicle.model_type or "",
                    years,
                ]

                product.variant_autopart_name = " ".join(part for part in parts if part)
            else:
                product.variant_autopart_name = ""
