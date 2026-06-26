from odoo import fields, models


class FleetVehicleVolume(models.model):
    _name = "fleet.vehicle.volume"
    _description = "Vehicle Volume"

    name = fields.Char(
        string="Volume",
        required=True)
