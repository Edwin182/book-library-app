from django.urls import path
from .views import BookListView, AddBookView, EditBookView, DeleteBookView

urlpatterns = [
    path('inventory/', BookListView.as_view(), name= 'inventory_page'),
    path('add_book/', AddBookView.as_view(), name = 'add_book'),
    path('edit_book/<int:pk>', EditBookView.as_view(), name = 'edit_book'),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
]