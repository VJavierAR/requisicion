# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_requisicion(models.Model):
    _name = 'product.rel.requisicion'
    _description='Rel requisiocion'
    cantidad=fields.Integer()
    product=fields.Many2one('product.product','id')
    req_rel=fields.Many2one('requisicion.requisicion','id')
    
class requisicion(models.Model):
    _name = 'requisicion.requisicion'
    _description='Requisicion'
    name = fields.Char()
    area = fields.Selection([('Ventas','Ventas'),('Almacen','Almacen'), ('Mesa de Ayuda','Mesa de Ayuda')])
    fecha_prevista=fields.Datetime()
    justificacion=fields.Char()
    product_rel=fields.One2many('product.rel.requisicion','req_rel')
    state = fields.Selection([('draft','New'),('open','Started'), ('done','Closed')],'State')

    
    @api.one
    def update_estado(self):
        self.write({'state':'done'})
    