from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post, Tag
from django.http import Http404,HttpResponseRedirect
from django.core.paginator import Paginator
from .form import CommentForm

def Home(requests):
    if not requests.user.is_authenticated:
        return HttpResponseRedirect('/accounts/signin')
    else:
        all_data = Post.objects.all().order_by('-id')
        page = Paginator(all_data, 4)
        page_number = requests.GET.get('p', 1)
        page_obj = page.get_page(page_number)
        return render(requests, 'home.html', {"posts": page_obj})
    
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

def tag(request, id):
    tag = get_object_or_404(Tag, id=id) 
    posts = tag.post_set.all()  
    
    return render(request, 'tag.html', {"tag": tag, "posts": posts})

def search(request):
    query = request.GET.get('query', None)
    posts = Post.objects.filter(post_title__icontains = query)
    print(posts)
    return render(request, 'search.html', {'query': posts})