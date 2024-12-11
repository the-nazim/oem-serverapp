from django.db import models

# Create your models here.
class Files(models.Model):
    file_name = models.CharField(max_length=100, blank=False)
    file = models.FileField(upload_to='uploaded_files/')
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def save_name(self, *args, **kwargs):
        if self.file:
            self.file_name = self.file.name
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.file_name