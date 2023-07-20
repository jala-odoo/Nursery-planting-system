from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
 
class PlantModel(models.Model):
    _name = "plant.model"
    _description = "describe plant properties"
    _log_access = False
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = "price"

    plant_ID = fields.Char(string="Plant ID",required=True)
    name = fields.Char(string="Name",default="Beautiful Plant")
    scientific_name = fields.Char(string="Scientific Name")
    type = fields.Selection([('Flowering','flowering plant'),('Fruiting','fruiting plant'),('Medicinal','medicinal plant'),('Vegetable','vegetable plant')],default="None",string="Type")
    species = fields.Char(string="Species",default="Unknown")
    price = fields.Float(string="Price")
    expected_harvest_date = fields.Datetime(string="Expected harvest date")
    health_status = fields.Selection([('H','healthy'),('D','dry'),('NW','Need Water')],string="Health status")
    date_of_planting = fields.Datetime(string="Date of planting",default = lambda self:fields.Datetime.today()+relativedelta(days=-7))
    ready_for_sold = fields.Boolean(string="Ready for sold")
    shipping_price = fields.Float(string="Shipping Price")
    sequence = fields.Integer(string="sequence")

    total_amount = fields.Float(string="Total amount",compute="_total_amount",readonly=False)

    # relational fields
    watering_date_ids = fields.One2many("watering.schedule" ,"plant_ID",string="upcoming events")
    # health_status_ids = fields.One2many("growth.tracking","health_status")
    buyer_id = fields.Many2one("res.partner",string="buyer")


    _sql_constraints = [('check_price','CHECK (price > 0)','The price must be strictly positive.'),
                        ('check_shipping_price','CHECK (shipping_price > 0)','The shipping price must be strictly positive.')]


    @api.depends("price","shipping_price")
    def _total_amount(self):
        for y in self:
            y.total_amount = y.price + y.shipping_price
          
    def sold_button(self):
        for y in self:
            y.name="sold"
        return True
    
    def cancel_button(self):
        for y in self:
            y.name="cancel"
        return True

