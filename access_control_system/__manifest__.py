{
    'name': "Access Control System",

    'summary': """
        Access Control System for gate pass.    
    """,

    'description': """
        Access Control System for gate pass to manage users and allow them based on given barcode.
    """,

    'author': "HAmayoon Yousafi",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/acs_employee.xml',
        'views/menuitems.xml'
    ]
}
