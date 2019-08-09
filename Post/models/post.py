from django.db import models


class Post(models.Model):
    user_id = models.ForeignKey('Auth.IstUser', null=False, related_name="posts", on_delete=models.CASCADE)
    image = models.ImageField(null=False) #default='../../media/image.jpg',
    description = models.TextField()
    category1 = models.BooleanField(default=False)
    category2 = models.BooleanField(default=False)
    category3 = models.BooleanField(default=False)
    category4 = models.BooleanField(default=False)
    category5 = models.BooleanField(default=False)
    category6 = models.BooleanField(default=False)
    category7 = models.BooleanField(default=False)
    category8 = models.BooleanField(default=False)
    category9 = models.BooleanField(default=False)
    category10 = models.BooleanField(default=False)

    # def __str__(self):
    #     return str(self.id), self.user_id



