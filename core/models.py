from django.db import models
import uuid
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Portfolio(BaseModel):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()

    thumbnail = models.ImageField(upload_to='portfolioapp/thumbnails/', null=True, blank=True)
    demo_video = models.FileField(upload_to='portfolioapp/demo/', storage=RawMediaCloudinaryStorage(), null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)    # Priority based display

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']

class PortfolioFile(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="portfolio_to_files")

    main_file = models.FileField(upload_to='portfolioapp/project_file/', storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.main_file.name

    
    def fileName(self):
        name = self.main_file.name.split("/")
        return name[-1]

    def fileExt(self):
        ext = self.main_file.name.split(".")
        return ext[1]