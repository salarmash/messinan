from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    image = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر")
    finalImage = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر نهایی")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="project", verbose_name="دسته بندی")
    description0 = models.TextField(verbose_name="متن1")
    description1 = models.TextField(verbose_name="متن1")
    description2 = models.TextField(verbose_name="متن1")
    description3 = models.TextField(verbose_name="متن1")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="Project", blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "گالری"


class Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="items")
    label = models.CharField(max_length=255, verbose_name="لیبل")
    value = models.CharField(max_length=255, verbose_name="مقدار")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتمها"


class Header(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "هدر"
        verbose_name_plural = "هدر ها"
