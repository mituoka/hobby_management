from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Image(models.Model):
    
    category_name= models.CharField(max_length=200)
    title_name = models.CharField(max_length=200)
    image_file = models.ImageField(upload_to='')
    comment = models.TextField(max_length=500)

    big = ImageSpecField(source="image_file",
                         processors=[ResizeToFill(1280, 1024)],
                         format='JPEG'
                         )

    thumbnail = ImageSpecField(source='image_file',
                            processors=[ResizeToFill(250,250)],
                            format="JPEG",
                            options={'quality': 60}
                            )

    middle = ImageSpecField(source='image_file',
                        processors=[ResizeToFill(600, 400)],
                        format="JPEG",
                        options={'quality': 75}
                        )

    small = ImageSpecField(source='image_file',
                            processors=[ResizeToFill(75,75)],
                            format="JPEG",
                            options={'quality': 50}
                            )
    def __ser__(self):
        return self.category_name