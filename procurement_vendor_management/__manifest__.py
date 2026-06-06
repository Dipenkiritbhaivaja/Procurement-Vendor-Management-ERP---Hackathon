# -*- coding: utf-8 -*-
{
    'name': "procurement_vendor_management",
    'summary': "Procurement and Vendor Management System",
    'description': """
        Manage vendor profiles, track performance, raise procurement requests,
        and handle purchase orders seamlessly in Odoo 18.
    """,
    'author': "Creyox Technologies",
    'website': "https://www.creyox.com",
    'category': 'Inventory/Purchase',
    'version': '18.0.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
