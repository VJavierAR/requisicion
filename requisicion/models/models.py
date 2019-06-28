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
    _inherit = ['mail.thread']
    name = fields.Char()
    area = fields.Selection([('Ventas','Ventas'),('Almacen','Almacen'), ('Mesa de Ayuda','Mesa de Ayuda')])
    fecha_prevista=fields.Datetime()
    justificacion=fields.Text()
    product_rel=fields.One2many('product.rel.requisicion','req_rel')
    state = fields.Selection([('draft','Nuevo'),('open','Preparado'), ('done','Hecho')],'State')

    
    @api.one
    def update_estado(self):
        self.write({'state':'open'})
    @api.one
    def update_estado1(self,vals):
        self.write({'state':'done'})
        id=self.env['purchase.order'].create({'partner_id':1,'name':vals['name']})
        for record in self:
            for p in record.product_rel:
                id2=self.env['purchase.order.line'].create({'order_id':id.id,'product_id':p.product.id,'product_qty':p.cantidad})
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('requisicion')
        result = super(requisicion, self).create(vals)
        return result
