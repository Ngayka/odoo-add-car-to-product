from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleAutoparts(WebsiteSale):

    def _get_search_domain(
            self,
            search,
            category,
            attrib_values,
            search_in_description=True
    ):
        domain = super()._get_search_domain(
            search,
            category,
            attrib_values,
            search_in_description=search_in_description,
        )
        params = request.httprequest.args

        brand_id = params.get("brand_id")
        model_id = params.get("model_id")
        year = params.get("year")
        volume_id = params.get("volume_id")

        if not any([brand_id, model_id, year, volume_id]):
            return domain

        vehicle_domain = []
        if brand_id:
            vehicle_domain.append(("brand_id", "=", int(brand_id)))

        if model_id:
            vehicle_domain.append(("id", "=", int(model_id)))

        if year:
            year = int(year)
            vehicle_domain += [
                ("model_year_from", "<=", year),
                ("model_year_to", ">=", year),
            ]

        if volume_id:
            vehicle_domain.append(("volume", "=", int(volume_id)))

        vehicles = request.env["fleet.vehicle.model"].sudo().search(vehicle_domain)
        if not vehicles:
            return domain + [("id", "=", 0)]

        products = request.env["product.product"].sudo().search([
            ("is_autoparts", "=", True),
            ("compatible_vehicle_ids", "in", vehicles.ids),
        ])

        templates = products.mapped("product_tmpl_id")
        return domain + [("id", "in", templates.ids)]

