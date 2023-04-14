# -*- coding: utf-8 -*-

from odoo import models, fields, api


class todo_lg_app(models.Model):
    _name = 'todo_lg_app'
    _description = 'todo app'

    name = fields.Char(string="Nombre")
    state = fields.Char(string="Estado")
    description = fields.Char(string="Descripcion")
    title = fields.Char(string="titulo")
    price = fields.Float(string="Precio")
    date = fields.Datetime(string="Fecha", track_visibility="onchange")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
