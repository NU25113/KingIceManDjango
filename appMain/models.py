from django.contrib.auth.models import User
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import F, Sum
from django.db import models
from django.utils.html import format_html
from appAccounting.models import *
# Create your models here.
class employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,  null=True, blank=True)
    name =models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name_plural ='ผู้ใช้'
    def __str__(self):
        return str(self.name)


class Agency(models.Model):
    ID_Aj = models.AutoField(primary_key=True)
    F_Agency = models.CharField(max_length=100,unique=True)
    L_Agency = models.CharField(max_length=100)
    Address = models.TextField(null=True)
    Tel = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='upload',null=True,blank=True)

    class Meta:
                verbose_name_plural ='ข้อมูลเอเจนซี่'

    def __str__(self):
        return str(self.F_Agency)

    def show_image(self):
        if self.image:
            return format_html('<img src="%s" height="50px">' % self.image.url)
        return ''
    show_image.allow_tags = True
    show_image.short_description = 'Image'


class Customer(models.Model): 
    ID_cd = models.AutoField(primary_key=True)
    F_Customer = models.CharField(max_length=100,unique=True,null=True)
    L_Customer = models.CharField(max_length=100,null=True)
    Address = models.TextField(max_length=50,null=True)
    Tel = models.CharField(max_length=50,unique=True,null=True)


    class Meta:
        verbose_name_plural ='ข้อมูลลูกค้า'

    def __str__(self):
        return str(self.F_Customer)

class List(models.Model):
    ID_List = models.AutoField(primary_key=True)
    Name_List = models.CharField(max_length=100)
    Agency = models.ForeignKey(Agency,on_delete=models.SET_NULL, null=True,blank=True)
    Customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    # employee = models.ForeignKey(employee,on_delete=models.SET_NULL, null=True,blank=True)
    complete = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='ข้อมูลรายการ'

    def __str__(self):
        return str(self.Name_List)

    # @property
    # def total_price(self):
    #     return self.cartitem_set.aggregate(
    #         total_price=Sum(F('quantity') * F('bucket_main__price'))
    #     )['total_price'] or Decimal('0')
    

    # @property
    # def get_list_total(self):
    #     agency_rents = self.agency_rent_set.all()
    #     total = sum([item.get_total for item in agency_rents])
    #     return total 
        
    # @property
    # def get_list_items(self):
    #     agency_rents = self.agency_rent.all()
    #     total = sum([item.quantity for item in agency_rents])
    #     return total 


# !=====================================================      ฝ่ายบัญชีจัดการสต๊อกคลัง      ==========================================================================
class bucket_main(models.Model):
    ID_bk = models.AutoField(primary_key=True)
    sizes = models.CharField(max_length=1, null=True)
    price = models.DecimalField(default=0,max_digits=7, decimal_places=2)
    Note = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True,blank=True) 
    
    class Meta:
        verbose_name_plural ='ข้อมูลคลังถังน้ำแข็งหลัก'
    def __str__(self):
        return str(self.ID_bk)

    @property
    def total_quantity(self):
        total = bucket_main.objects.aggregate(TOTAL = Sum('price'))['TOTAL']
        return total


# class bucket_tracking(models.Model):
#     Name_List = models.OneToOneField(List, on_delete=models.SET_NULL, null=True)
#     ID_bk = models.OneToOneField(bucket_main,on_delete=models.SET_NULL,null=True,blank=True)
#     Agency = models.ForeignKey(Agency,on_delete=models.SET_NULL, null=True,blank=True)
#     Note = models.TextField(null=True, blank=True)
#     Date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#             verbose_name_plural ='ข้อมูลคลังตามถังน้ำแข็ง'
#     def __str__(self):
#         return str(self.Name_List)

class bucket_damaged(models.Model):
    ID_bk = models.OneToOneField(bucket_main,on_delete=models.SET_NULL,null=True,blank=True)
    # Sizes = models.models.CharField(max_length=100, null=True,blank=True)
    Name_recipient = models.CharField(max_length=100, null=True, blank=True)
    Name_sender = models.CharField(max_length=100, null=True, blank=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE,  null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    Note = models.TextField(null=True, blank=True)

    

    class Meta:
        verbose_name_plural ='ข้อมูลคลังถังน้ำแข็งชำรุด'

    def __str__(self):
        return str(self.Name_recipient)


class bucket_lost(models.Model):
    Name_List = models.OneToOneField(List, on_delete=models.SET_NULL, null=True,blank=True)
    ID_bk = models.OneToOneField(bucket_main,on_delete=models.SET_NULL,null=True,blank=True)
    # AjFirst_name = models.ForeignKey(tb_Agency,on_delete=models.SET_NULL,max_length=100, null=True,blank=True)
    Agency = models.OneToOneField(Agency,on_delete=models.SET_NULL, null=True,blank=True)
    Customer = models.OneToOneField(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    # quantity = models.IntegerField(default=0, null=True, blank=True)
    Note = models.TextField(null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural ='ข้อมูลคลังถังน้ำแข็งสูญหาย'

    def __str__(self):
        return str(self.Name_List)

class Agency_rent(models.Model):
    bucket_main = models.OneToOneField(bucket_main, on_delete=models.SET_NULL, null=True, blank=True)
    List = models.OneToOneField(List,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    Rental_period = models.DateTimeField(auto_now=False)
    Date = models.DateTimeField(auto_now_add=True)
    # total = models.DecimalField(default=0,max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural ='ข้อมูลค่าเช่าเอเจนซี่'

    @property
    def get_total(self):
        total = self.bucket_main.price * self.quantity
        return total
    quantity_total = property(get_total)

    @property
    def total_quantity(self):
        total = Agency_rent.objects.aggregate(TOTAL = Sum('quantity'))['TOTAL']
        return total

    # @property
    # def get_price(self):
    #     return self.get_total.aggregate(models.Sum('quantity'))


class Income(models.Model):
    bucket_main = models.OneToOneField(bucket_main,on_delete=models.SET_NULL, null=True)
    Agency_rent = models.OneToOneField(Agency_rent,on_delete=models.SET_NULL, null=True)
    Name_List = models.OneToOneField(List, on_delete=models.SET_NULL, null=True,blank=True)
    total_price = models.IntegerField(default=1, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural ='ข้อมูลรายได้'

    def __str__(self):
        return str(self.id)

    @property
    def total_sale(self):
        total = Income.objects.aggregate(TOTAL = Sum('total_price'))['TOTAL']
        return total

class Budget(models.Model):
    ID_budget = models.AutoField(primary_key=True)
    Name_budget = models.CharField(max_length=255)
    price = models.IntegerField(default=0, null=True, blank=True)
    staff = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name_plural ='ข้อมูลค่าใช้จ่าย'

    def __str__(self):
        return str(self.Name_budget)

    @property
    def sum(self):
        total = Budget.objects.aggregate(TOTAL = Sum('price'))['TOTAL']
        return total

# class Cost(models.Model):
#     Name_budget = models.OneToOneField(Budget, on_delete=models.SET_NULL, null=True,blank=True)
#     price = models.IntegerField(null=True, blank=True)
#     staff = models.CharField(max_length=100)
#     Date = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         verbose_name_plural ='ข้อมูลค่าใช้จ่าย'

#     def __str__(self):
#         return str(self.id)

#     @property
#     def sum(self):
#         total = Cost.objects.aggregate(TOTAL = Sum('price'))['TOTAL']
#         return total
# #! ============================================  ฝ่ายขาย  ==========================================================================================
class Customer_rental(models.Model):
    bucket_main = models.OneToOneField(bucket_main,related_name='Customer_idBK',on_delete=models.SET_NULL,null=True,blank=True)
    # size = models.OneToOneField(bucket_main,on_delete=models.SET_NULL,null=True,blank=True)
    List = models.OneToOneField(List,on_delete=models.SET_NULL,null=True,blank=True)
    Customer = models.OneToOneField(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    Rental_period = models.DateTimeField(auto_now=False)
    Date = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name_plural ='ข้อมูลการเช่าของลูกค้า'

    def __str__(self):
        return str(self.Rental_period)