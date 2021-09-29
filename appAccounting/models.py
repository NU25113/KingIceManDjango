from django.db import models
# from appSales.models import tb_List, tb_Agency
# # Create your models here.
# class tb_Ice_bucket_warehouse_information(models.Model):
#     ID_bucket = models.AutoField(primary_key=True)
#     Size_s = models.CharField(max_length=50,default="",editable=False)
#     Size_m = models.CharField(max_length=50,default="",editable=False)
#     Size_l = models.CharField(max_length=50,default="",editable=False)
#     Total_am = models.IntegerField()
#     Note = models.TextField
    

#     class Meta:
#         verbose_name_plural ='ข้อมูลคลังถังน้ำแข็งหลัก'
 
#     def __str__(self):
#         return self.ID_bucket

# class tb_Ice_bucket_fallow_warehouse(models.Model):
#     ID_bucket = models.AutoField(primary_key=True)
#     Size_s = models.CharField(max_length=50,default="",editable=False)
#     Size_m = models.CharField(max_length=50,default="",editable=False)
#     Size_l = models.CharField(max_length=50,default="",editable=False)
#     Total_am = models.IntegerField() 
#     Note = models.TextField(null=True, blank=True)
#     Date = models.DateTimeField(auto_now_add=True)
    

#     class Meta:
#         verbose_name_plural ='ข้อมูลคลังพักถังน้ำแข็ง'
 
#     def __str__(self):
#         return self.ID_bucket

# class tb_Ice_bucket_tracking_information(models.Model):
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Size_s = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_m = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_l = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Total_am = models.IntegerField()
#     Note = models.TextField
#     Date = models.DateTimeField(auto_now_add=True)
    

#     class Meta:
#         verbose_name_plural ='ข้อมูลคลังตามถังน้ำแข็ง'
 
#     def __str__(self):
#         return self.Name_List

# class tb_Ice_bucket_warehouse_lost(models.Model):
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     ID_Aj = models.ForeignKey(tb_Agency,on_delete=models.CASCADE)
#     Tenant_name = models.CharField(max_length=50)
#     Amount = models.IntegerField()
#     Size_s = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_m = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Size_l = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Note = models.TextField
#     Date = models.DateTimeField(auto_now_add=True)
    

#     class Meta:
#         verbose_name_plural ='ข้อมูลคลังถังน้ำแข็งสูญหาย'
 
#     def __str__(self):
#         return self.Name_List

# class tb_Ice_bucket_warehouse_damaged(models.Model):
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     Name_recipient = models.CharField(max_length=50)
#     Name_sender = models.CharField(max_length=50)
#     Cost = models.IntegerField()
#     Date = models.DateTimeField(auto_now_add=True)
#     Note = models.TextField

    

#     class Meta:
#         verbose_name_plural ='ข้อมูลคลังถังน้ำแข็งสูญหาย'
 
#     def __str__(self):
#         return self.ID_bucket

# class tb_Agency_rent_informationd(models.Model):
#     ID_bucket = models.ForeignKey(tb_Ice_bucket_fallow_warehouse,on_delete=models.CASCADE)
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     ID_Aj = models.ForeignKey(tb_Agency,on_delete=models.CASCADE)
#     Amount = models.IntegerField()
#     Date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural ='ข้อมูลค่าเช่าเอเจนซี่'
 
#     def __str__(self):
#         return self.Name_List

# class tb_Income_information(models.Model):
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Am_bucket = models.IntegerField()
#     Am_money = models.IntegerField()
#     Date = models.DateTimeField(auto_now_add=True)


    

#     class Meta:
#         verbose_name_plural ='ข้อมูลรายได้'
 
#     def __str__(self):
#         return self.Name_List

# class tb_Budget_information(models.Model):
#     ID_budget = models.AutoField(primary_key=True)
#     Name_budget = models.CharField(max_length=255)
#     Sign_in = models.CharField(max_length=100)
#     Date = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         verbose_name_plural ='ข้อมูลงบประมาณ'
 
#     def __str__(self):
#         return self.Name_budget

# class tb_Cost_information(models.Model):
#     ID_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Name_List = models.ForeignKey(tb_List,on_delete=models.CASCADE)
#     Am_money = models.IntegerField()
#     Sign_in = models.CharField(max_length=100)
#     Date = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         verbose_name_plural ='ข้อมูลค่าใช้จ่าย'
 
#     def __str__(self):
#         return self.Name_List