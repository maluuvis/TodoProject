from django.db import models #importa modelos da db django

# Create your models here.
class Task(models.Model): #classifica como um modelo de database
    
    content = models.CharField(max_length=100) #conteúdo da task
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) #task completa=false

    class Meta:
        ordering = ['-date']

    def __str__(self):        
        return f'conteudo: "{self.content}"" status: "{self.complete}"'
    #retornará: 'conteudo: "Aprender python" status: "False"'