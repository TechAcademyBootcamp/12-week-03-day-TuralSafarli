from django.db import models

# Create your models here.

class News(models.Model):


    title=models.CharField('Title', max_length=255)
    description=models.TextField('Description',)
    images=models.ImageField('Images', upload_to='imagesnews/', )
    author_name=models.CharField('Author', max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    

    class Meta:
        verbose_name = 'Xeber'
        verbose_name_plural = 'Xeberler'

    def __str__(self):
        return self.title

    
