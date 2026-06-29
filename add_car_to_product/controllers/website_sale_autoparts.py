from odoo import http
from odoo.http import request


class WebsiteSaleAutoparts(http.Controller):

    @http.route("/shop/autoparts/models", type="json", auth="public", website=True)
    def get_models(self, brand_id):
        models = request.env["fleet.vehicle.model"].sudo().search([
            ("brand_id", "=", int(brand_id))
        ])
        return [{"id": model.id, "name": model.name} for model in models]

    @http.route("/shop/autoparts/search", type="http", auth="public", website=True)
    def autoparts_search(self, brand_id=None, model_id=None, year=None, volume_id=None, **kwargs):
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

        products = request.env["product.product"].sudo().search([
            ("is_autoparts", "=", True),
            ("compatible_vehicle_ids", "in", vehicles.ids),
        ])

        return request.render("website_sale.products", {
            "products": products,
            "search": "",
        })

