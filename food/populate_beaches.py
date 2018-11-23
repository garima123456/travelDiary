import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travelDiary.settings')

import django
django.setup()

from beaches.models import Category,Page

def populate():
    beaches_cat=add_cat('Beaches',views=100,likes=50)
    add_page(cat=beaches_cat,
        title='Bali',
        url="https://www.tripadvisor.in/Tourism-g294226-Bali-Vacations.html")

    add_page(cat=beaches_cat,
          title='Mauritius',
          url="https://www.tripadvisor.in/Tourism-g293816-Mauritius-Vacations.html")

    add_page(cat=beaches_cat,
          title='Maldives',
          url="https://www.lonelyplanet.com/maldives")

    hillstation_cat = add_cat('Hill_Stations',views=60,likes=40)

    add_page(cat=hillstation_cat,
        title='Switzerland',
        url="https://www.lonelyplanet.com/switzerland")
    add_page(cat=hillstation_cat,
        title='Ireland',
        url="https://www.discoverireland.ie/")
    add_page(cat=hillstation_cat,
        title='Bhutan',
        url="https://www.tripadvisor.in/Tourism-g293844-Bhutan-Vacations.html")

    deserts=add_cat('desert',views=60,likes=40)

    add_page(cat=deserts,
        title='Egypt',
        url="https://www.lonelyplanet.com/egypt")
    add_page(cat=deserts,
        title='Ireland',
        url="https://www.discoverireland.ie/")
    add_page(cat=deserts,
        title='Dubai',
        url="https://www.tripadvisor.in/Tourism-g295424-Dubai_Emirate_of_Dubai-Vacations.html")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Travel Diary population script..."
    populate()










    
