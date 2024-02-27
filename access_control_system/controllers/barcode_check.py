from odoo import http
from odoo.http import request
import json
from odoo.exceptions import ValidationError


class BarcodeCheck(http.Controller):
    @http.route('/check-barcodes', auth='user', type='http')
    def open_check_barcode_page(self):
        if not request.env.user.has_group('access_control_system.group_acs_user'):
            raise ValidationError('You are not allowed to visit this page.')
        return request.render('access_control_system.check_barcode_page')
    
    @http.route('/check-barcodes/validate', auth='user', type='http', csrf=False)
    def validate_barcode(self, barcode):
        employee = request.env['acs.employee'].search([('reference', '=', barcode)])
        if employee:
            data = {
                'name': employee.name,
                'reference': employee.reference,
                'employee_id_number': employee.employee_id_number
            }
            return json.dumps({'employee': data})
        return json.dumps({'employee': False})