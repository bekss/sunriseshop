from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from django.core.files.storage import FileSystemStorage

photo_storage = FileSystemStorage(location='/media/images')


class Category(models.Model):
    name_category = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_category


class Tovar(models.Model):
    name_tovar = models.CharField(max_length=50)
    price_tovar = models.IntegerField(validators=[RegexValidator(r'^\d{1,9}$')])
    image_tovar = models.ImageField(upload_to='images/', )
    amount = models.IntegerField(verbose_name='количество',default=0, validators=[RegexValidator(r'^\d{1,5}$')])
    category_tovar = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name_tovar

    def image(self):
        return self.image_tovar