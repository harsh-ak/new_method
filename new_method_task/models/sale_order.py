from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
   _inherit='sale.order'

   def call_new_method(self):
        
        so_vals = self.env['sale.order'].new({
            'state': 'draft',
            'partner_id':10
            
        })
        print('-----so_vals',so_vals)
        
        so_vals.onchange_partner_id()
        
        print('-----onchnage',so_vals)
        
        values = so_vals._convert_to_write(so_vals._cache)
        print('-------------',values)
        
        so_rec = self.env['sale.order'].create(values)
        print("_____________msuccessss")
        

        




