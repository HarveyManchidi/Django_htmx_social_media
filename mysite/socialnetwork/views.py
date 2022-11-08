from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from accounts.models import Profile


from .models import Post
from .forms import PostCreateForm, PostUpdateForm, CommentForm


# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        
    }
    return render(request, 'socialnetwork/home.html', context)

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
    else:
        form=CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form':form,
    }
    return render(request, 'socialnetwork/post_detail.html', context)



def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            postform=form.save(commit=False)
            postform.author = request.user
            postform.save()
            return redirect('home')
    else:
        form = PostCreateForm()
                
    context = {
        'form': form,
    }
    return render(request,'socialnetwork/post_create.html',context)

def post_update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            postform=form.save(commit=False)
            postform.author = post.author
            postform.save()
            return redirect('home')
    else:
        form = PostUpdateForm(instance=post)
        
    context = {
        'form': form,
    }
    return render(request, 'socialnetwork/post_update.html',context)

def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context = {
        'post': post,
    }
    
    return render(request,'socialnetwork/post_delete.html',context)

def like_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user not in post.likes.all(): 
        post.likes.add(request.user)
        return redirect('home')
    else:
        post.likes.remove(request.user)
        return redirect('home')
    
def comments(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
    else:
        form=CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, 'socialnetwork/partials/comments.html',context)


def feed_follow(request,pk,post_pk):
    profile = Profile.objects.get(pk=pk)
    posts = Post.objects.all()
    post = get_object_or_404(Post,pk=post_pk)
    if request.user not in profile.followers.all():
        profile.followers.add(request.user)
    else:
        profile.followers.remove(request.user)
    posts = Post.objects.all()
    context ={
        'profile': profile,
        'posts': posts,

        }
    return render(request, 'socialnetwork/home.html',context)

def detail_follow(request,pk,post_pk):
    profile = Profile.objects.get(pk=pk)
    post = get_object_or_404(Post,pk=post_pk)
    if request.user not in profile.followers.all():
        profile.followers.add(request.user)
    else:
        profile.followers.remove(request.user)
    context ={
        'profile': profile,
        'post': post,

        }
    return render(request, 'socialnetwork/post_detail.html',context)




