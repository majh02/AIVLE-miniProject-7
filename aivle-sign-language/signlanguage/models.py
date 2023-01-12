from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class AiModel(models.Model):
    AImodel_CHOICE=(
                        ('CNN model-1', 'CNN model-1'),
                        ('CNN model-2', 'CNN model-2'),
                        ('CNN model-3', 'CNN model-3'),
                        ('CNN model-4', 'CNN model-4'),
                        ('CNN model-5', 'CNN model-5'),
    )
    ai_file = models.FileField(blank=True, unique=True) 
    version = models.CharField(max_length=100) 
    is_selected = models.CharField('AI 모델', max_length=20, choices=AImodel_CHOICE, primary_key=True) 
    pub_date = models.DateTimeField('date published', default=timezone.datetime.now()) 
    accuracy = models.FloatField('Accuracy', default=0.0)
    
    def get_absolute_url(self): 
        return reverse('signlanguage:manage') 

class Result(models.Model): 
    image = models.ImageField(blank=True) 
    answer = models.CharField(max_length=10) 
    result = models.CharField(max_length=10) 
    correct = models.CharField(max_length=10, default='wrong') 
    pub_date = models.DateTimeField('date published') 
    model = models.ForeignKey(AiModel, on_delete=models.CASCADE,null = True)
    
    def __str__(self): 
        return self.image.path 
