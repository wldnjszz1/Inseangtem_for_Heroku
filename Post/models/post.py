from django.db import models


class Post(models.Model):
    user_id = models.ForeignKey('Auth.IstUser', null=False, related_name="posts", on_delete=models.CASCADE)
    image = models.ImageField(null=False) #default='../../media/image.jpg',
    description = models.TextField()
    category1 = models.BooleanField(null=True)
    category2 = models.BooleanField(null=True)
    category3 = models.BooleanField(null=True)
    category4 = models.BooleanField(null=True)
    category5 = models.BooleanField(null=True)
    category6 = models.BooleanField(null=True)
    category7 = models.BooleanField(null=True)
    category8 = models.BooleanField(null=True)
    category9 = models.BooleanField(null=True)
    category10 = models.BooleanField(null=True)

    # def __str__(self):
    #     return str(self.id), self.user_id



