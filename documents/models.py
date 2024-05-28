from django.db import models

class Document(models.Model):
    document_id = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_url = models.URLField()
    # Add more fields as needed to store document details

    def __str__(self):
        return self.file_name
