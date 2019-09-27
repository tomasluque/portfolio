from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    pub_date = models.DateTimeField()
    body = models.TextField()
    summary = models.TextField()
    articlePic_l = models.ImageField(upload_to='images/')
    articlePic_s = models.ImageField(upload_to='images/')
    gridPic_l = models.ImageField(upload_to='images/')
    gridPic_s = models.ImageField(upload_to='images/')
    picture_caption = models.TextField()
    conclusion = models.TextField()

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title