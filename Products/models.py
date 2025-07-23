from django.db import models
from polymorphic.models import PolymorphicModel
from Accounts.models import Vendor

class Category(models.Model):
    
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name
    
class Category_product(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name
    
class Product(PolymorphicModel):
    name = models.CharField(max_length=200,null=False,blank=False)
    brand = models.CharField(max_length=100,null=True,blank=True)
    price = models.PositiveIntegerField(null=False,blank=False)
    discount_price = models.PositiveIntegerField(null=False,blank=False)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/',null=True,blank=True)
    image5 = models.ImageField(upload_to='images/',null=True,blank=True)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    warranty = models.CharField(max_length=100,null=True,blank=False)
    return_policy = models.CharField(max_length=100,default='10 Days return',null=True,blank=True)
    delivery_info = models.CharField(max_length=100,default='Free Delivery',null=True,blank=True)
    created_at = models.DateField(auto_now=True)
    sale = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    category = models.ForeignKey(Category_product,on_delete=models.CASCADE)


    def get_discount(self):
        if self.discount_price < self.price:
            return round((self.price-self.discount_price)*100/self.price,2)
        return 0 

    def saving(self):
        return round(self.price-self.discount_price)
    
    def __str__(self):
        return self.name
    
    def get_type(self):
        return self.__class__.__name__
    

class Mobile(Product):
    m_ram = models.CharField(max_length=100)
    m_storage = models.CharField(max_length=100)
    m_battery = models.CharField(max_length=100)
    m_camera = models.CharField(max_length=100)
    m_processor = models.CharField(max_length=100)
    m_screen_size = models.CharField(max_length=100)
    m_operating_system = models.CharField(max_length=100)

class Laptop(Product):
    l_ram = models.CharField(max_length=100)
    l_storage = models.CharField(max_length=100)
    l_graphic_card = models.CharField(max_length=100)
    l_processor = models.CharField(max_length=100)
    l_screen_size = models.CharField(max_length=100)
    l_operating_system = models.CharField(max_length=100)

class Television(Product):
    t_screen_size = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    smart_tv = models.BooleanField(default=False)
    hdmi_ports = models.IntegerField()
    usb_ports = models.IntegerField()

class Camera(Product):
    camera_type = models.CharField(max_length=100)
    megapixels = models.CharField(max_length=100)
    optical_zoom = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=100)

class Smartwatch(Product):
    w_screen_size = models.CharField(max_length=100)
    w_battery_life = models.CharField(max_length=100)
    features = models.TextField()
    water_resistant = models.BooleanField(default=True)

class Refrigerator(Product):
    r_capacity = models.CharField(max_length=100)
    door_type = models.CharField(max_length=100)
    energy_rating = models.CharField(max_length=100)
    defrost_type = models.CharField(max_length=100)

class WashingMachine(Product):
    w_type = models.CharField(max_length=100)
    w_capacity = models.CharField(max_length=100)
    function_type = models.CharField(max_length=100)
    
class Airconditioner(Product):
    tonnage = models.CharField(max_length=100)
    a_type = models.CharField(max_length=100)
    energy_rating = models.CharField(max_length=100)
    cooling_capacity = models.CharField(max_length=100)
    
class Kitchenappliance(Product):
    appliance_type = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    k_material = models.CharField(max_length=100)
    
class Grocery(Product):
    weight = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=100)
    pack_type = models.CharField(max_length=100)
    organic = models.BooleanField(default=True)

class Clothing(Product):
    c_size = models.CharField(max_length=10)
    fabric = models.CharField(max_length=100)
    c_color = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    c_type = models.CharField(max_length=100)
        
class Footwear(Product):
    s_size = models.CharField(max_length=10)
    s_material = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    s_type = models.CharField(max_length=100)

class Furniture(Product):
    f_material = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=100)
    f_color = models.CharField(max_length=100)
    f_type = models.CharField(max_length=100)

class Lighting(Product):
    light_type = models.CharField(max_length=10)
    wattage = models.CharField(max_length=100)
    l_color = models.CharField(max_length=100)
    is_rechareable = models.BooleanField(default=False)

class Book(Product):
    author = models.CharField(max_length=100)
    publiser = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    pages = models.IntegerField()
    publication_date = models.DateField()

class Babycare(Product):
    age_group = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    hypoallergic = models.BooleanField(default=False)

class Earbuds(Product):
    e_battery_life = models.CharField(max_length=100)
    bluetooth_version = models.CharField(max_length=50)
    has_anc = models.BooleanField(default=True)


