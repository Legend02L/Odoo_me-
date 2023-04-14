from odoo import fields, models


class Movimientos(models.Model):
    _name = "sa.movimiento"  # sa_movimiento
    _description = "Movimiento"
    _inherit = "mail.thread"

    name = fields.Char(string="Nombre")
    type_move = fields.Selection(selection=[("ingreso", "Ingreso"), ("gasto", "Gasto")], track_visibility="onchange",
                                 string="Tipo", default="ingreso", required=True)
    date = fields.Datetime(string="Fecha", track_visibility="onchange")
    amount = fields.Float("Monto", track_visibility="onchange")
    receipt_image = fields.Binary("Foto del recibo")
    notas = fields.Html("Notas")

    currency_id = fields.Many2one("res.currency")

    user_id = fields.Many2one("res.users", string="Usuario")
    category_id = fields.Many2one("sa.category", "Categoria")

    tag_ids = fields.Many2many("sa.tag", "sa_mov_sa_tag_rel", "move_id", "tag_id")  # sa_movimiento_sa_tag_rel


class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")

    def ver_movimientos(self):
        return {
            "name": "Movimiento de categoria: "+self.name,
            "type": "ir.actions.act_window",
            "res_model": "sa.movimiento",
            "views": [[False, "tree"]],
            "domain": [["category_id", "=", self.id]]
        }


class Tag(models.Model):
    _name = "sa.tag"
    _description = "Tag"

    name = fields.Char("Nombre")


class ResUsers(models.Model):
    _inherit = "res.users"

    movimiento_ids = fields.One2many("sa.movimiento", "user_id")
