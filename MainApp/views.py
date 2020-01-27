rom
django.shortcuts
import render, redirect
from .models import Slider, Add, Recipe, Review, Gallery, Footer, Abouthero, Agallery, Fact, RecipesSection, \
    Recipegallery, Contact, Contactgallery, Write, View
from .forms import CommentForm
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Slider, Add, Recipe, Review, Gallery, Footer, Abouthero, Agallery, Fact, RecipesSection, \
    Recipegallery, Contact, Contactgallery, Write, View


# Create your views here.


def homepage(request):
    sliders = Slider.objects.all()
    add = Add.objects.last()
    recipes = Recipe.objects.all()
    reviews = Review.objects.all()
    gellary = Gallery.objects.last()
    footers = Footer.objects.all()

    context = {
        'sliders': sliders,
        'ad': add,
        'recipes': recipes,
        'reviews': reviews,
        'gellary': gellary,
        'footers': footers,

    }

    return render(request, 'index.html', context=context)

def about(request):
   heros=Abouthero.objects.last()
   agellary = Agallery.objects.last()
   fact = Fact.objects.all()


   context={
       'heros':heros,
       'agellary':agellary,
       'facts':fact,
   }

   return render(request,'about.html',context)


def contact (request):
    contacts = Contact.objects.all()
    contactgallery = Contactgallery.objects.last()
    form = CommentForm()

    context = {
        'contacts': contacts,
        'contactgallery': contactgallery,
        'form': form,
    }
    if request.method == "POST":
        form = CommentForm(request.POST)
        # name=request.POST['name']
        # email=request.POST['email']
        # subject=request.POST['subject']
        # message=request.POST['message']
        # comment=Comment.objects.create(name=name,email=email,subject=subject,messege=message)
        # comment.save()
        if form.is_valid():
            form.save()
            # form=CommentForm()
            # context={
            #     'form':form,
            # }
        return redirect("contact")

    return render(request, 'contact.html', context)

def recipes (request):
    recipesections = RecipesSection.objects.all()
    recipegellary = Recipegallery.objects.last()
    context={
        'recipesections':recipesections,
        'recipegellary':recipegellary,

    }
    return  render(request,'recipes.html',context)

def reviews (request):
    writes=Write.objects.all()
    view=View.objects.last()
    context={
        'writes':writes,
        'view':view,
    }
    return  render(request,'recipe-single.html',context)