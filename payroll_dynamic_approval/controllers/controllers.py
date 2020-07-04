# -*- coding: utf-8 -*-
from odoo import http

# class PayrollDynamicApproval(http.Controller):
#     @http.route('/payroll_dynamic_approval/payroll_dynamic_approval/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payroll_dynamic_approval/payroll_dynamic_approval/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payroll_dynamic_approval.listing', {
#             'root': '/payroll_dynamic_approval/payroll_dynamic_approval',
#             'objects': http.request.env['payroll_dynamic_approval.payroll_dynamic_approval'].search([]),
#         })

#     @http.route('/payroll_dynamic_approval/payroll_dynamic_approval/objects/<model("payroll_dynamic_approval.payroll_dynamic_approval"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payroll_dynamic_approval.object', {
#             'object': obj
#         })