from django.db import models

class UploadedFile(models.Model):

    # This is a small demo using FileField instead of ImageField, not
    # depending on PIL. You will probably want ImageField in your app.
    file = models.FileField(upload_to="uploads")
    slug = models.SlugField(max_length=50, blank=True)

    def __unicode__(self):
        return self.file

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(UploadedFile, self).save(*args, **kwargs)
