from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام نویسنده")
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر پروفایل")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر")
    category = models.ForeignKey(Category, related_name="blog", verbose_name="دسته بندی", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blog", verbose_name="نویسنده")
    date = models.DateTimeField(auto_now_add=True)
    popular = models.BooleanField(default=False)
    content_desc = models.TextField(verbose_name="متن اول")
    content_des2 = models.TextField(verbose_name="متن دوم")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "وبلاگ"
        ordering = ("-date",)


class Gallery(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری"


class Header(models.Model):
    subtitle = models.CharField(max_length=225, verbose_name="زیرعنوان")
    description = models.TextField(verbose_name="توضیح ")

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "هدر "
        verbose_name_plural = "هدر ویلاگ"
