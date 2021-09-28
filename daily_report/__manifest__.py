# -*- coding: utf-8 -*-
{
    'name': "Daily Report",

    'summary': """
        Daily report for employees""",
    'description': """
        Daily report for employees
    """,
    'author': "Kamrul",
    'website': "kamrulsh.github.io",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/report_views.xml',
        'views/activity_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
