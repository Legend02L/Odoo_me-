# -*- coding: utf-8 -*-
# from odoo import http


# class TodoLgApp(http.Controller):
#     @http.route('/todo_lg_app/todo_lg_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_lg_app/todo_lg_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_lg_app.listing', {
#             'root': '/todo_lg_app/todo_lg_app',
#             'objects': http.request.env['todo_lg_app.todo_lg_app'].search([]),
#         })

#     @http.route('/todo_lg_app/todo_lg_app/objects/<model("todo_lg_app.todo_lg_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_lg_app.object', {
#             'object': obj
#         })
