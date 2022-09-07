from django.db import models


class Stackmodel(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    content = models.TextField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.name


class Operation(models.Model):
    stackmodel = models.ForeignKey(Stackmodel, on_delete=models.CASCADE) 
    body = models.TextField()
    old = models.TextField(null=True, blank=True)
    new = models.TextField(null=True, blank=True)
    action = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
