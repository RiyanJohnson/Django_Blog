from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post #importing the Post class from models.py
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)

#dummy data for posts which we used for checking
'''posts = [
    {
        'author':'Riyan Johnson',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date':'February 19th, 2025'
    },
    {
        'author':'bigussy',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date':'February 20th, 2025'
    }
]'''

def home(request):
    context = {
        'posts' : Post.objects.all() #the query to be used in database
    }
    return render(request, 'blog/home.html', context) #response when coming to the homepage

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post 

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post 
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False