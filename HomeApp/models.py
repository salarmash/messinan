from django.db import models


class Hero(models.Model):
    bg_img = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="عکس پس زمینه")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="زیرنوشت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="عکس")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "هدر سایت"
        verbose_name_plural = "هدر سایت"


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام شرکت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="لوگو")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "همکار"
        verbose_name_plural = "همکاران"


class Testimonial(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.TextField(verbose_name="زیرنوشت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مشتریان"
        verbose_name_plural = "مشتریان"


class TestItems(models.Model):
    test = models.ForeignKey(Testimonial, on_delete=models.CASCADE, related_name="tetsItems")
    name = models.CharField(max_length=255, verbose_name="نام")
    role = models.CharField(max_length=255, verbose_name="شغل")
    text = models.TextField(verbose_name="زیرنوشت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتمها"


class AboutOne(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="زیرنوشت")
    front_img = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="عکس")
    back_img = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="عکس پس زمینه")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما 1"


class AboutTwo(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="زیرنوشت")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="عکس")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما 2"


class Counter(models.Model):
    about = models.ForeignKey(AboutTwo, on_delete=models.CASCADE, related_name='counter')
    label = models.CharField(max_length=255, verbose_name="لیبل")
    value = models.PositiveSmallIntegerField(default=0 , verbose_name="مقدار")

    class Meta:
        verbose_name = "شمارنده"
        verbose_name_plural = "شمارنده ها"


