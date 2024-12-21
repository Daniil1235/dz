from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    # path('product/<int:product_id>/', product_detail, name='product_detail'),
    # path('category/<int:category_id>/', category_product, name='category_detail'),
]
