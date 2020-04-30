from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Postvote
from django.contrib import messages
from django.utils import timezone

@login_required(login_url="/accounts/signup")
def creators(request):
    posts = Post.objects
    return render(request, 'posts/creators.html', {'posts':posts})

@login_required(login_url="/accounts/signup")
def createpost(request):
    if request.method == 'POST':
        if request.POST['post_summary'] or request.POST['url'] or request.FILES['Image']:
            post = Post()
            post.post_summary = request.POST['post_summary']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            try:
                post.image = request.FILES['photo']
            except KeyError:
                pass
            post.pub_date = timezone.datetime.now()
            post.user = request.user
            post.save()
            # return redirect('/posts/' + str(post.id))
            return redirect('creators')
        else:
            messages.error(request, 'All fields are required !')
            return render(request, 'posts/createpost.html')
    else:
        return render(request, 'posts/createpost.html')

def detailedpost(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'posts/detailedpost.html', {'post':post})

@login_required(login_url="/accounts/signup")
def upvotepost(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        if post.user.username == request.user.username:
            messages.error(request, "Creator can't upvote their own post !")
            return redirect('creators')
        else:
            try:
                vote = Postvote.objects.get(postID=post_id, userID=request.user)
                messages.error(request, 'You have already voted for this post!')
                return redirect('creators')
            except Postvote.DoesNotExist:
                vote = None
                # find product by id and increment
                post = Post.objects.get(id=post_id)
                vote = Postvote(postID=post, userID=request.user)
                post.votes_total += 1
                vote.save()
                post.save()
                return redirect('creators')
