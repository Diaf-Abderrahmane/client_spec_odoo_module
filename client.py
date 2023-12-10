from odoo import models, fields

class client(models.Model):
    _inherit = 'res.partner'
    media_comments = fields.Text()
