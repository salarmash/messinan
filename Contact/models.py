from django.db import models


class Info(models.Model):
    icon = models.ImageField(upload_to="Contact", blank=True, null=True, verbose_name="آیکون")
    label = models.CharField(max_length=200, verbose_name="لیبل")
    value = models.CharField(max_length=200, verbose_name="مقدار")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات"


class Form(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="پست الکترونیکی")
    message = models.TextField(verbose_name="متن پیام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"
