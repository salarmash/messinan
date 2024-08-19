from django.db import models


class About(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    text1 = models.TextField(verbose_name="متن اول")
    text2 = models.TextField(verbose_name="متن دوم")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"


class Gallery(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="About", blank=True, null=True, verbose_name="نگاره")

    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "گالری"


class Counter(models.Model):
    label = models.CharField(max_length=255, verbose_name="عنوان")
    value = models.PositiveSmallIntegerField(default=0, verbose_name="مقدار")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "شمارنده"
        verbose_name_plural = "شمارنده ها"


class Award(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="متن ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "جایزه"
        verbose_name_plural = "جایزه ها"


class Item(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255, verbose_name="عنوان")
    year = models.CharField(max_length=5, verbose_name="سال")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    text1 = models.TextField(verbose_name="متن ")
