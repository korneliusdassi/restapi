from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICE = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOISE = sorted([(item, item) for item in get_all_styles()])

class Bukus(models.Model):
    judul = models.TextField()
    deskripsi= models.TextField()
    harga= models.IntegerField(25)
    rating= models.IntegerField(25)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     ordering = ['created']
    
