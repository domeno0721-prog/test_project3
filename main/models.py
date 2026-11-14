from django.db import models

# Create your models here.
class Wort(models.Model):
    ru_wort = models.CharField('русское слово', max_length=50)
    d_wort = models.CharField('немецкое слово',max_length=50)
    lektion = models.IntegerField("Лекцион", default=111)
    
    def __str__(self):
        return self.d_wort
    
    class Meta:
        verbose_name = "слово"
        verbose_name_plural  = "слова"