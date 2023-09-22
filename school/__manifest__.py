# -*- coding: utf-8 -*-
{
    'name': "school",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'sequence' : -100,
    'author': "Sn1zhok",
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/courses_view.xml',
        'views/sessions_view.xml',
        'views/menu.xml',
        'reports/sessions_report.xml'
        'wizard/wizard_view.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}
