from django.db import models
  
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length=100)
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    