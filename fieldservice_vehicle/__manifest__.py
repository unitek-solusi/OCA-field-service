# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service Vehicles',
    'summary': 'manage your field service vehicles',
    'version': '11.0.0.1.1',
    'category': 'Field Service',
    'author': 'Open Source Integrators, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/field-service',
    'depends': [
        'fieldservice',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/vehicle_security.xml',
        'views/fsm_vehicle.xml',
        'views/fsm_route.xml',
        'views/menu.xml',
    ],
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'wolfhall',
        'max3903',
    ],
}