from odoo import fields, models, api
from odoo.exceptions import ValidationError


class FleetVehicleModel(models.Model):
    _inherit = "fleet.vehicle.model"

    model_year_from = fields.Integer(string="Year from")
    model_year_to = fields.Integer(string="Year to")
    model_type = fields.Char(string="Model type")
    ovoko_car_id = fields.Char(string="Ovoko car ID")
    volume = fields.Many2one("fleet.vehicle.volume", string="Volume")

    @api.constrains("model_year_from", "model_year_to")
    def _check_model_years(self):
        for rec in self:
            if (
                rec.model_year_from
                and rec.model_year_to
                and rec.model_year_to < rec.model_year_from
            ):
                raise ValidationError(
                    "Year to must be greater than or equal to Year from."
                )
