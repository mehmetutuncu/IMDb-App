from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)
    rating = models.FloatField()
    is_top_250 = models.BooleanField(default=False)
    top_250_order = models.IntegerField(default=0)
    is_most_popular = models.BooleanField(default=False)
    most_popular_order = models.IntegerField(default=0)
    name = models.CharField(max_length=512)
    detail_url = models.URLField()
    image = models.URLField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields is not None:
            update_fields.append('modified_date')
        super(BaseModel, self).save(*args, **kwargs)
