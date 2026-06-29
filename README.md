# Add Car To Product

Custom Odoo 17 module that extends Fleet and Product applications to support vehicle compatibility for autoparts.

## Features

- Extends `fleet.vehicle.model` with additional car data:
  - Year from / Year to
  - Model type
  - Engine volume
  - Ovoko car ID
- Adds autoparts flag to product templates.
- Adds autopart-specific fields to product variants:
  - Compatible vehicles
  - For all models
  - OEM
  - Ovoko part ID
- Adds an **Autoparts** tab for product variants.
- Displays compatible vehicles in a table.
- Adds a custom **Car** security group.
- Extends website shop with autoparts search filters:
  - Manufacturer
  - Model name
  - Year
  - Volume

## Requirements

* Docker
* Docker Compose

## Installation

Clone the repository:

```bash
git clone https://github.com/Ngayka/odoo-add-car-to-product.git
cd odoo-add-car-to-product
```

Start Odoo:

```bash
docker compose up -d
```

Update the module:

```bash
docker exec -it odoo17 odoo \
-d odoo17 \
--db_host=db \
--db_user=odoo \
--db_password=odoo \
-u add_car_to_product \
--stop-after-init
```

Open Odoo:

```
http://localhost:8069
```

## Dependencies

* product
* fleet
* website_sale


## Author

Natalia Semenova
