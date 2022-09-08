from django.db import models


class Salesrecord(models.Model):
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name mad lowercase.
    item_type = models.TextField(db_column='Item Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_channel = models.TextField(db_column='Sales Channel', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_id = models.IntegerField(db_column='Order ID', blank=True,primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    units_sold = models.IntegerField(db_column='Units Sold', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_price = models.FloatField(db_column='Unit Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_cost = models.FloatField(db_column='Unit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_revenue = models.FloatField(db_column='Total Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_cost = models.FloatField(db_column='Total Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_profit = models.FloatField(db_column='Total Profit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def get_data(self):
        return{
            'region':self.region,
            'country':self.country,
            'item_type':self.item_type,
            'sale_channel':self.sales_channel,
            'order_id':self.order_id,
            'units_sold':self.units_sold,
            'unit_price':self.unit_price ,
            'unit_cost':self.unit_cost ,
            'total_revenue':self.total_revenue ,
            'total_cost':self.total_cost ,
            'total_profit':self.total_profit ,
        }
    
    class Meta:
        managed = False
        db_table = 'salesrecord'