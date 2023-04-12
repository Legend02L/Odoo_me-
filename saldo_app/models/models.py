from odoo import fields, models

class Movimientos(models.Model):
    _name = "sa.movimiento" #sa_movimiento
    _description = "Movimiento"

    name = fields.Char("Nombre")
    type_move = fields.Selection(selection=[("ingreso","Ingreso"),("gasto","Gasto")])
    date = fields.Datetime("Fecha")
    amount = fields.Float("Monto")
    receipt_image = fields.Binary("Foto del recibo")

    user_id = fields.Many2one("res.users",string="Usuario")
    category_id = fields.Many2one("sa.category","Categoria")

class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")

class Tag(models.Model):
    _name = "sa.tag"
    _description = "Tag"

    name = fields.Char("Nombre")