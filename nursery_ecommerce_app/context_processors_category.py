from nursery_ecommerce_app.models.category import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
