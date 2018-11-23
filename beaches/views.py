from django.shortcuts import render
from django.http import HttpResponse
from beaches.models import Category
from beaches.models import Page
from beaches.forms import CategoryForm, PageForm


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
        pages = Page.objects.filter(category=category).order_by('-views')
    except Category.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, 'beaches/category.html', context_dict)

def index(request):
   category_list =Category.objects.order_by('-likes')[:]
   context_dict = {'categories': category_list}

   return render(request, 'beaches/index.html', context_dict)
   

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'beaches/add_category.html', {'form': form})



def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat,'category_name_slug': category_name_slug}

    return render(request, 'beaches/add_page.html', context_dict)
