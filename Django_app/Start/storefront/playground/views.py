from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Customer, Order, OrderItem, Promotion
from tags.models import TaggedItem, Tag



def say_hello(request):
    # # All products
    # query_set = Product.objects.all()
    # list(query_set)

    # Order Items for products in collection 3 (Joins two tables)
    # query_set = OrderItem.objects.filter(product__collection__id=3)
    # list(query_set)

    # # Products that have been ordered and sort by title
    # select_query_set = OrderItem.objects.values('product__id').distinct()
    # query_set = Product.objects.filter(id__in=select_query_set).order_by('title')
    # list(query_set)

    # Querying a generic type
    # Custom manager present in tags>models.py
    # queryset = TaggedItem.objects.get_tags_for(Product,1)

    # # Creating object
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    
    # Updating an existing record
    # This approach executes a query to read once, however does not update the extra fields already present in the memory
    # collection = collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()
    # If you have serious performance issues and wants to avoid extra reading and also update the specific updates mentioned then
    # Collection.objects.filter(pk=11).update(featured_product=None)

    # # Transaction
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # return render(request, 'hello.html', {'name': 'Chinmay', 'tags': list(queryset)})
    return render(request, 'hello.html', {'name': 'Chinmay'})
