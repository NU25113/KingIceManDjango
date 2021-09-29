from django.db import models
# from appAccounting.models import tb_Ice_bucket_fallow_warehouse

# Create your models here.
# class tb_List(models.Model):
#     ID_List = models.AutoField(primary_key=True)
#     Name_List = models.CharField(max_length=100,unique=True)
#     def __str__(self):
#         return self.Name_List

# class tb_Agency(models.Model):
#     ID_Aj = models.AutoField(primary_key=True)
#     First_name = models.CharField(max_length=100,unique=True)
#     Last_name = models.CharField(max_length=100)
#     Address = models.TextField()
#     Tel = models.CharField(max_length=50,unique=True)
#     def __str__(self):
#         return self.First_name

# class tb_Agency_rental_information(models.Model):
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     First_name = models.ForeignKey(tb_Agency,on_delete=models.CASCADE)
#     Last_name = models.ForeignKey(tb_Agency,on_delete=models.CASCADE)
#     Address = models.ForeignKey(tb_Agency,on_delete=models.CASCADE)
#     Tel = models.ForeignKey(tb_Agency,on_delete=models.CASCADE)
#     Rental_period = models.DateTimeField(auto_now_add=True)
#     Amount = models.IntegerField()
#     Size_s = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_m = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_l = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Date = models.DateTimeField(auto_now_add=True)
  
#     class Meta:
#              verbose_name_plural ='ข้อมูลการเช่าของเอเจนซี่'

#     def __str__(self):
#         return self.First_name

# class tb_Customer_rental_information(models.Model):
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     First_name = models.CharField(max_length=100,default="",editable=False,unique=True)
#     Last_name = models.CharField(max_length=100)
#     Address = models.TextField()
#     Tel = models.CharField(max_length=50,unique=True)
#     Rental_period = models.DateTimeField(auto_now_add=True)
#     Amount = models.IntegerField()
#     Size_s = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_m = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_l = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Date = models.DateTimeField(auto_now_add=True)
  
#     class Meta:
#              verbose_name_plural ='ข้อมูลการเช่าของลูกค้า'

#     def __str__(self):
#         return self.First_name

    
# class tb_Ice_bucket_balance_information(models.Model):
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Amount = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_s = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_m = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_l = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
  
#     class Meta:
#              verbose_name_plural ='ข้อมูลยอดคงเหลือของถังน้ำแข็ง'

#     def __str__(self):
#         return self.ID_bucket
