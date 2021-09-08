from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.specs import ImageSpec

def articles_image_path(instance, filename):
    return f'user_{instance.instance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank = True, upload_to='images/')
    # image = models.ImageField(blank = True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank = True, upload_to=articles_image_path)
    # image = ProcessedImageField(
    #     upload_to = 'thumbnails/',
    #     processors= [ResizeToFill(100, 50)],
    #     format="JPEG",
    #     options={'quality': 60}
    # )
    image = models.ImageField(blank = True, upload_to='origins/')
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors=[ResizeToFill(100, 50)],
        format = 'JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     

    def __str__(self):
        return self.title
