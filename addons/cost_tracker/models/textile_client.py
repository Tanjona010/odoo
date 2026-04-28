from odoo import models, fields


class TextileClient(models.Model):
    _name = "textile.client"
    _description = "Client"

    name = fields.Char(required=True)
    email = fields.Char()
