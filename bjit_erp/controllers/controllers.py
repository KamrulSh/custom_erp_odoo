# -*- coding: utf-8 -*-
# from odoo import http


# class BjitErp(http.Controller):
#     @http.route('/bjit_erp/bjit_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bjit_erp/bjit_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bjit_erp.listing', {
#             'root': '/bjit_erp/bjit_erp',
#             'objects': http.request.env['bjit_erp.bjit_erp'].search([]),
#         })

#     @http.route('/bjit_erp/bjit_erp/objects/<model("bjit_erp.bjit_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bjit_erp.object', {
#             'object': obj
#         })
