# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Assurance(models.Model):
    _name = 'clientspech.assurance'
    _description = "assurance client handi lourd"

    label = fields.Char(string="IdAssurance", required=True)
    dateSouscription = fields.Date()
    piece = fields.Binary()    
    client_id = fields.Many2one('res.partner',
        ondelete='cascade', string="Client", required=True)
