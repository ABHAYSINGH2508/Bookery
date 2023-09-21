from django.urls import path
from .views import BuyBooks,SellBooks,BuyDetailView,BuyListView,SellCreateView,SellUpdateView,SellDeleteView,searchbooks,bestSeller,addToCart,showAddToCartInfo,showAddToCartSN,CartView,CartBuy
app_name='main'
urlpatterns=[
    path('buy/',BuyListView.as_view(),name='buy'),
    path('sell/',SellCreateView.as_view(),name='sell'),
    path('detail/<int:pk>/',BuyDetailView.as_view(),name='detail'),
    path('detail/<int:pk>/update/',SellUpdateView.as_view(),name='update'),
    path('detail/<int:pk>/delete/',SellDeleteView.as_view(),name='delete'),
    path('search/',searchbooks,name='search'),
    path('bestSeller/',bestSeller,name='bestSeller'),
    path('addToCart/',addToCart,name='addToCart'),
    # path('showAddToCart/',showAddToCartInfo,name='showAddToCart'),
    path('showAddToCart/<int:pk>/',CartView.as_view(),name='showAddToCart'),
    path('showAddToCartSN/',showAddToCartSN,name='showAddToCartSN'),
    path('CartBuy/',CartBuy,name='CartBuy'),

]