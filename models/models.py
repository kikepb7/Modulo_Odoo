from random import randint
from odoo import models, fields, api

class Stock(models.Model):
    _name = 'investment.stock'
    name = fields.Char(string = "Nombre de la acción", required = True, help = "Nombre de la acción")
    ticket = fields.Char(string = "Ticket", required = True, help = "Ticket de la acción")
    description = fields.Text()
    stock_icon = fields.Image(string = "Icono", help = "Icono para la acción")
    user_id = fields.Many2one(
        'res.users',
        ondelete = 'set null', string = "Inversor"
    )
    invest_ids = fields.One2many(
        'investment.invest', 'stock_id', string = 'Inversiones'
    )

    codigo = fields.Char(compute = '_compute_name')
    @api.depends('name')
    def _compute_name(self):
        for accion in self:
            accion.codigo = f"{accion.name} "


class RealState(models.Model):
    _name = 'investment.realState'
    address = fields.Char(string = "Dirección", required = True, help = "Dirección de la propiedad")
    price = fields.Float(string = "Precio", required = True, help = "Precio de la propiedad")
    description = fields.Text()
    realState_icon = fields.Image(string = "Imagen", help = "Imagen de la propiedad")

class Crypto(models.Model):
    _name = 'investment.crypto'
    name = fields.Char(string = "Nombre de la criptomoneda", required = True, help = "Nombre de la criptomoneda")
    crypto_ticket = fields.Char(string = "Ticket", required = True, help = "Ticket de la acción")
    description = fields.Text()
    crypto_icon = fields.Image(string = "Icono", help = "Icono de la criptomoneda")


class Invest(models.Model):
    _name = 'investment.invest'
    name = fields.Char(string = "Nombre de la inversión", required = True, help = "Nombre de la inversión")
    description = fields.Text()
    start_date = fields.Date()
    stock_number = fields.Integer(string = "Número de acciones")

    investor_id = fields.Many2one('res.partner', string = "Inversor")
    stock_id = fields.Many2one(
        'investment.stock', ondelete = 'cascade', string = "Acción", required = True)

    attendee_ids = fields.Many2many('res.partner', string = "Attendees")

    taken_stocks = fields.Float(string = "Acciones compradas", compute = '_taken_stocks')

    @api.depends('stock_number', 'attendee_ids')
    def _taken_stocks(self):
        for s in self:
            if not s.stock_number:
                s.taken_stocks = 0.0
            else:
                s.taken_stocks = 100.0 * len(s.attendee_ids) / s.stock_number
