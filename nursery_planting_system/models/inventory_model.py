from odoo import models,fields

class InventoryModel(models.Model):
    _name="inventory.model"
    _description="Manage the inventory of plants"
    _order="quantity asc"

    plant_ID = fields.Char(string="Plant ID",required=True)
    quantity = fields.Integer(string="Quantity(in stock)")