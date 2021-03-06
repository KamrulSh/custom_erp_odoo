# -*- coding: utf-8 -*-
{
    'name': "bjit ERP",
    'sequence': 1,
    'summary': """
        Creating BJIT ERP module""",
    'description': """
        Creating BJIT ERP module using Employees, Attendances, Project,
        Contacts, Website.
    """,
    'author': "Kamrul",
    'website': "kamrulsh.github.io",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'hr', 'project'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/employees_view.xml',
        'views/views_project_erp.xml',
        'views/tamplates.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
}
