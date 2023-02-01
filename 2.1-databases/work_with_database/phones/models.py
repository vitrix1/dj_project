from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    image = models.CharField(max_length=500)
    release_date = models.CharField(max_length=12)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=70)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

