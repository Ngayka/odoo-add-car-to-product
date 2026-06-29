{
    "name": "Add Car To Product",
    "version": "17.0.1.0.0",
    "depends": ["product", "fleet", "website_sale"],
    "author": "Semde",
    "category": "Sales",
    "description": "Add car information to products",
    "data": [
        # security
        "security/security.xml",
        "security/ir.model.access.csv",
        # views
        "views/vehicle_model_view_form.xml",
        "views/vehicle_model_view_list.xml",
        "views/product_template_product_form_view.xml",
        "views/product_product_form_view.xml",
        # data
        "data/website_sale_autoparts_templates.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
