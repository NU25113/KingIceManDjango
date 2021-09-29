from django.db import models
# from django.utils.html import format_html

# Create your models here.
# class tb_user(models.Model):
#     First_name = models.CharField(max_length=50)
#     Last_name= models.CharField(max_length=50)
#     User_Type= models.CharField(max_length=50)
#     Tel= models.CharField(max_length=20)
#     Address= models.CharField(max_length=200)
#     Username= models.CharField(max_length=50)
#     Password= models.CharField(max_length=20)
#     image = models.ImageField(upload_to='upload',null=True,blank=True)

#     class Meta:
#         verbose_name_plural ='ข้อมูลผู้ใช้'

#     def __str__(self):
#         return self.First_name

#     def show_image(self):
#         if self.image:
#             return format_html('<img src="%s" height="50px">' % self.image.url)
#         return ''
#     show_image.allow_tags = True
#     show_image.short_description = 'Image'

class Job_queue(models.Model):
    title = models.CharField(max_length=50)
    queue = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name_plural ='คิวงาน'

    def __str__(self):
        return self.title

