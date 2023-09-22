from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')

    def __str__(self):
        return f"instagram {self.message}"

    def message_length(self):
        return len(self.message)

