from django.db import models


# Create your models here.
class Slider(models.Model):
    title1 = models.CharField(max_length=100, null=False, blank=False)
    title2 = models.CharField(max_length=100, null=False, blank=False)
    title3 = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to="slider/", null=False, blank=False)

    def __str__(self):
        return self.title1


class Add(models.Model):
    image1 = models.ImageField(upload_to="add/", null=False, blank=False)
    image2 = models.ImageField(upload_to="add/", null=False, blank=False)
    image3 = models.ImageField(upload_to="add/", null=False, blank=False)
    text1 = models.CharField(max_length=100, null=False, blank=False)
    text2 = models.CharField(max_length=100, null=False, blank=False)
    text3 = models.CharField(max_length=100, null=False, blank=False)
    text4 = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.text1

class Recipe(models.Model):
    image=models.ImageField(upload_to="recipe/",null=False,blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    rating=models.IntegerField(null=False,blank=False)
    def __str__(self):
        return self.title



class Review (models.Model):
    image=models.ImageField(upload_to="review/",null=False,blank=False)
    date=models.DateField(auto_now=True)
    rating=models.IntegerField(null=False,blank=False)
    title=models.CharField(max_length=100,null=False,blank=False)
    author=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.author

class Gallery(models.Model):
    image1=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image2=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image3=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image4=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image5=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image6=models.ImageField(upload_to="gallery/",null=False,blank=False)
class Footer(models.Model):

    image1 = models.ImageField(upload_to="gallery/", null=False, blank=False)
    date = models.DateField(auto_now=True)
    title2 = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)





#model for about.

class Abouthero(models.Model):
    image=models.ImageField(upload_to="hero/",null=False,blank=False)
class Agallery(models.Model):
    image1=models.ImageField(upload_to="agallery/",null=False,blank=False)
    image2=models.ImageField(upload_to="agallery/",null=False,blank=False)
    image3=models.ImageField(upload_to="agallery/",null=False,blank=False)
    image4=models.ImageField(upload_to="agallery/",null=False,blank=False)
    image5=models.ImageField(upload_to="agallery/",null=False,blank=False)
    image6=models.ImageField(upload_to="agallery/",null=False,blank=False)
class Fact(models.Model):
    image1 = models.ImageField(upload_to="fact/", null=False, blank=False)
    total = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)




#model for recipes

class RecipesSection(models.Model):
    image = models.ImageField(upload_to="recipe/", null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title


class Recipegallery(models.Model):
    image1=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image2=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image3=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image4=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image5=models.ImageField(upload_to="gallery/",null=False,blank=False)
    image6=models.ImageField(upload_to="gallery/",null=False,blank=False)


# about section
class Contact(models.Model):
    address=models.TextField(null=False,blank=False)
    phone = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)


class Contactgallery(models.Model):
    image1 = models.ImageField(upload_to="contact/", null=False, blank=False)
    image2 = models.ImageField(upload_to="contact/", null=False, blank=False)
    image3 = models.ImageField(upload_to="contact/", null=False, blank=False)
    image4 = models.ImageField(upload_to="contact/", null=False, blank=False)
    image5 = models.ImageField(upload_to="contact/", null=False, blank=False)
    image6 = models.ImageField(upload_to="contact/", null=False, blank=False)


# comment
class Comment(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    messege = models.TextField(max_length=600, null=False, blank=False)


# review


class Write(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(null=False, blank=False)
    level = models.CharField(max_length=100, null=False, blank=False)
    list = models.CharField(max_length=100, null=False, blank=False)
    descrip = models.CharField(max_length=100, null=True, blank=False)
class View(models.Model):
    image1 = models.ImageField(upload_to="view/", null=False, blank=False)




