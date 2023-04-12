from odoo import fields, models


class Movimientos(models.Model):
    _name = "sa.movimiento"  # sa_movimiento
    _description = "Movimiento"

    name = fields.Char(string="Nombre")
    type_move = fields.Selection(selection=[("ingreso", "Ingreso"), ("gasto", "Gasto")], string="Tipo", default="ingreso", required=True)
    date = fields.Datetime(string="Fecha")
    amount = fields.Float("Monto")
    receipt_image = fields.Binary("Foto del recibo")
    notas = fields.Html("Notas")

    currency_id = fields.Many2one("res.currency")

    user_id = fields.Many2one("res.users", string="Usuario")
    category_id = fields.Many2one("sa.category", "Categoria")

    tag_id = fields.Many2many("sa.tag", "sa_mov_sa_tag_rel", "move_id", "tag_id")  # sa_movimiento_sa_tag_rel


class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")


class Tag(models.Model):
    _name = "sa.tag"
    _description = "Tag"

    name = fields.Char("Nombre")


class ResUsers(models.Model):
    _inherit = "res.users"

    movimiento_ids = fields.One2many("sa.movimiento", "user_id")
