from odoo import fields, models


class FleetVehicleModel(models.model):
    _inherit = "fleet.vehicle.model"

    model_year_from = fields.Integer(string="Year from")
    model_year_to = fields.Integer(string="Year to")
    model_type = fields.Char(string="Model type")
    ovoko_car_id = fields.Char(string="Ovoko car ID")
    volume = (...)