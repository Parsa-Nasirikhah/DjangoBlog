from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post, Tag
from django.http import Http404,HttpResponseRedirect
from django.core.paginator import Paginator
from .form import CommentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def Home(requests):
    if not requests.user.is_authenticated:
        return HttpResponseRedirect('/accounts/signin')
    else:
        all_data = Post.objects.all().order_by('-id')
        page = Paginator(all_data, 4)
        page_number = requests.GET.get('p', 1)
        page_obj = page.get_page(page_number)
        return render(requests, 'home.html', {"posts": page_obj})
    
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 4

def post(request, id):
    post = get_object_or_404(Post, id=id) 
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('post', args=[id])) 
    
    else:
        form = CommentForm()
    
    return render(request, 'post.html', {"post_dict": post, 'form': form,
                                          'comments' : post.comment_set.all()})

class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post_dict'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['form'] = CommentForm
        contex['comments'] = self.object.comment_set.all()
        return contex
    

    def post(self, request, pk):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('post', args=[self.object.id])) 

def tag(request, id):
    tag = get_object_or_404(Tag, id=id) 
    posts = tag.post_set.all()  
    
    return render(request, 'tag.html', {"tag": tag, "posts": posts})

def search(request):
    query = request.GET.get('query', None)
    posts = Post.objects.filter(post_title__icontains = query)
    return render(request, 'search.html', {'query': posts})

class SearchView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'query'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query is not None:
            posts = Post.objects.filter(post_title__icontains = query)
            return posts
        else:
            return posts.objects.none()