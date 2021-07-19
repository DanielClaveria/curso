# -*- coding: utf-8 -*-

{
    'name': 'Cooperative',
    
    'summary': """Cooperative management software""",
    
    'description': """
        Cooperative management software:
        - Persons
        - Sales
        - Activities
    """,
    
    'author': 'Daniel Clavería',
    
    'website': 'https://espaciofuturo.cl',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/cooperative_menuitem.xml',
    ],
    
    'demo':[
        'demo/data_demo.xml',
        
    ],
}