from django.db import models


class Team(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "تیم"
        verbose_name_plural = "تیمها"


class Item(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر")
    name = models.CharField(max_length=255, verbose_name="نام")
    role = models.CharField(max_length=255, verbose_name="پوزیشن")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"