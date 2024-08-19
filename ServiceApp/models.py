from django.db import models


class Header(models.Model):
    subtitle = models.CharField(max_length=225, verbose_name="زیرعنوان")
    description1 = models.TextField(verbose_name="توضیح 1")
    description2 = models.TextField(verbose_name="توضیح 2")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "هدر "
        verbose_name_plural = "هدر خدمات"


class Service(models.Model):
    image = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="تصویر پیش نمایش")
    title = models.CharField(max_length=225, verbose_name="عنوان")
    short = models.CharField(max_length=225, verbose_name="پیش نمایش")
    fullImage = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="تصویر بزرگ")
    description = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " مطلب"
        verbose_name_plural = "خدمات"


class Item(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='items')
    label = models.CharField(max_length=225, verbose_name="عنوان")
    value = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = " آیتم"
        verbose_name_plural = "آیتم ها"
