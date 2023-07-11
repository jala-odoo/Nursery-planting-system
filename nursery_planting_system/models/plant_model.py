from odoo import models,fields
from dateutil.relativedelta import relativedelta
 


class PlantModel(models.Model):
    _name = "plant.model"
    _description = "describe plant properties"
    _log_access = False

    plant_ID = fields.Char(string="Plant ID",required=True)
    name = fields.Char(string="Name")
    scientific_name = fields.Char(string="Scientific Name")
    type = fields.Char(string="Type")
    species = fields.Char(string="Species",default="Unknown")
    price = fields.Float(string="Price")
    expected_harvest_date = fields.Datetime(string="Expected harvest date")
    health_status = fields.Selection([('H','healthy'),('D','dry'),('NW','Need Water')],string="Health status")
    date_of_planting = fields.Datetime(string="Date of planting",default = lambda self:fields.Datetime.today()+relativedelta(days=-7))

    # relational fields
    watering_date_ids = fields.One2many("watering.schedule" ,"plant_ID",string="upcoming events")
    health_status_ids = fields.One2many("growth.tracking","health_status")
