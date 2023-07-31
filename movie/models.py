from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    year = models.IntegerField()
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    watchAgain = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.text[:50]