from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'acs.employee'
    _description = 'Access Control System Employee'

    name = fields.Char(required=True)
    reference = fields.Char(string="Reference", tracking=True, default='New', readonly=True) # employee technical reference
    employee_id_number = fields.Char('ID Number', required=True) # employee id number given by the organization
    father_name = fields.Char()
    address = fields.Char()
    date_of_birth = fields.Date()
    image = fields.Binary(attachment=True)
    phone = fields.Char()
    email = fields.Char()

    _sql_constraints = [
        ('unique_employee_id_number','unique (employee_id_number)','Employee ID number must be unique. This ID number is already assigned.')
    ]

    @api.model
    def create(self, vals):   
        vals['reference'] = self.env['ir.sequence'].next_by_code('acs.employee.sequence')  
        return super().create(vals)
    
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for employee in self:
            if employee.date_of_birth and employee.date_of_birth >= fields.Date.today():
                raise ValidationError('Date of birth must be a date in the past.')