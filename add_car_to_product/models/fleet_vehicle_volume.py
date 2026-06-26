from odoo import fields, models


class FleetVehicleVolume(models.Model):
    _name = "fleet.vehicle.volume"
    _description = "Vehicle Volume"

    name = fields.Char(
        string="Volume",
        required=True)
