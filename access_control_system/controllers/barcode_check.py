from odoo import http
from odoo.http import request


class BarcodeCheck(http.Controller):
    @http.route('/check-barcodes', auth='user', type='http')
    def open_check_barcode_page(self):
        return request.render('access_control_system.check_barcode_page')