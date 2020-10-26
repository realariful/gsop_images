# -*- coding: utf-8 -*-
from odoo import http

# class GsopImages(http.Controller):
#     @http.route('/gsop_images/gsop_images/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gsop_images/gsop_images/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gsop_images.listing', {
#             'root': '/gsop_images/gsop_images',
#             'objects': http.request.env['gsop_images.gsop_images'].search([]),
#         })

#     @http.route('/gsop_images/gsop_images/objects/<model("gsop_images.gsop_images"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gsop_images.object', {
#             'object': obj
#         })