from odoo import fields, models, api


class Employee(models.Model):
    _name = 'acs.employee'
    _description = 'Access Control System Employee'

    name = fields.Char(required=True)
    employee_id_number = fields.Char(required=True)
    father_name = fields.Char()
    address = fields.Char()
    date_of_birth = fields.Date()
    image = fields.Binary(attachment=True)
    phone = fields.Char()
    email = fields.Char()