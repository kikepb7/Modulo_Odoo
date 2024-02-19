from odoo import models, fields, api

class Invest(models.Model):
    _name = 'investment.invest'
    name = fields.Char(string = "Titulo", required = True, help = "Nombre de la inversión")
    description = fields.Text()
    invest_icon = fields.Image(string = "Icono", help = "Icono para la inversión")

# class investment(models.Model):
#     _name = 'investment.investment'
#     _description = 'investment.investment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
