# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Task Scheduling',
    'version' : '1.1',
    'summary': 'Task Scheduling',
    'sequence': 10,
    'description': """
Task Scheduling
====================
This modules adds task scheduling in Odoo 15 Community Edition.
    """,
    'category': 'Productivity',
    'website': 'https://example.com',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'data/service_cron.xml', 
        'views/task_views.xml', 
    ],
    'demo': [
       
    ],
    'author': 'Wilson Ndirangu',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
