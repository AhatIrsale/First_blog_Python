from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import DetailView,ListView

from blog.models import *



def IndexView(request):
    num_blogs = Blog.objects.all().count()
    num_bloguers = User.objects.all().count()

    num_comments= Comments.objects.all().count()
    context = {
        'num_blogs':num_blogs,
        'num_bloguers':num_bloguers,
        'num_comments':num_comments
    }
    template_name = 'blog/index.html'
    return render(request,template_name,context)

class BlogList(ListView):
    model = Blog
    context_object_name = 'Blog'
    template_name = 'blog/Blogs.html'

class BlogDetail(DetailView):
    model = Blog
    template_name = 'Blog/Blog_Detail.html'
    context_object_name = 'blog'
class BloguerList(ListView):
    model = User
    template_name   = 'Blog/bloguers.html'
    context_object_name   = 'Bloguers'

class BloguerDetail(DetailView):
    model = User
    template_name = 'Blog/Bloguer.html'
    context_object_name = 'Bloguer'
class comment(DetailView):
    model = Comments
    template_name ='comments/comment.html'
    context_object_name = 'comments'
#def get_queryset(self):
    #return User.type.filter(borrower=self.request.user).filter(type__exact='Bloguer').order_by('name')

