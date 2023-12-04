from django.urls import path
from .views import IndexView, BlogDetail, BlogList, BloguerList, BloguerDetail, comment

app_name = 'blog'
urlpatterns = [
    path('comments/', comment.as_view, name='comment'),
    path('',IndexView,name = 'index'),
    path('Blogs/',BlogList.as_view(),name = 'blogs'),
    path('blog/<int:pk>/',BlogDetail.as_view(),name = "Blog_detail"),
    path('Bloguers/',BloguerList.as_view(),name='Bloguers'),
    path('Bloguer/<int:pk>/', BloguerDetail.as_view(), name='bloguer')



]
