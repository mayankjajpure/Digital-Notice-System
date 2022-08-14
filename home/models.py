from django.db import models

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    url=models.CharField(max_length=50)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateField(auto_now=True,null=True)
    def __str__(self) -> str:
        return self.title

        
class Posts(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    url=models.CharField(max_length=50)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')

    def __str__(self) -> str:
        return self.title
    
class notice(models.Model):
    head=models.CharField((""), max_length=20)
    content=models.TextField()

    def __str__(self) -> str:
        return self.head
class Feedback(models.Model):
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    feed=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
