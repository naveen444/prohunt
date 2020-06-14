from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Postvote, Comment, Commentvote, Commentdvote
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
import json

@login_required(login_url="/accounts/signup")
def creators(request):
    posts = Post.objects
    comments = Comment.objects
    return render(request, 'posts/creators.html', {'posts':posts, 'comments':comments})

@login_required(login_url="/accounts/signup")
def createpost(request):
    if request.method == 'POST':
        if request.POST['post_summary'] or request.POST['url'] or request.FILES['Image']:
            post = Post()
            post.post_summary = request.POST['post_summary']
            if request.POST['url']:
                if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                    post.url = request.POST['url']
                else:
                    post.url = 'http://' + request.POST['url']
            else:
                pass
            try:
                post.image = request.FILES['Image']
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

@login_required(login_url="/accounts/signup")
def postcomment(request,post_id):
    if request.method == 'POST':
        comment_text = request.POST.get('the_comment')
        response_data = {}
        post = Post.objects.get(id=post_id)
        comment = Comment(comment_text= comment_text, comment_pub_date=timezone.datetime.now(), post= post, user=request.user)
        comment.save()

        response_data['result'] = 'Create post successful!'
        response_data['text'] = comment.comment_text
        response_data['created'] = comment.comment_pub_date.strftime('%B %d, %Y %I:%M %p')
        response_data['user'] = comment.user.username
        response_data['likes'] = comment.votes_total
        response_data['dislikes'] = comment.dislikes
        response_data['image'] = comment.user.profile.image.url

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@login_required(login_url="/accounts/signup")
def upvotecomment(request, post_id, comment_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        comment = get_object_or_404(Comment, pk = comment_id)
        response_data = {}
        if comment.user.username == request.user.username:
            messages.error(request, "Commenter can't upvote their own post !")
            return redirect('creators')
        else:
            try:
                vote = Commentvote.objects.get(commentID=comment, postID=post, userID=request.user)
                messages.error(request, 'You have already voted for this comment!')
                return redirect('creators')
            except Commentvote.DoesNotExist:
                vote = None
                # find product by id and increment
                post = Post.objects.get(id=post_id)
                # find comment by id and increment
                comment = Comment.objects.get(id=comment_id)
                vote = Commentvote(commentID=comment, postID=post, userID=request.user)
                comment.votes_total += 1
                vote.save()
                comment.save()

                response_data['result'] = 'upvoted successfully!'

                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({"nothing to see": "this isn't happening"}),
                    content_type="application/json"
                )

@login_required(login_url="/accounts/signup")
def dislikecomment(request, post_id, comment_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        comment = get_object_or_404(Comment, pk = comment_id)
        if comment.user.username == request.user.username:
            messages.error(request, "Commenter can't like or dislike their own post !")
            return redirect('creators')
        else:
            try:
                vote = Commentdvote.objects.get(commentID=comment, postID=post, userID=request.user)
                messages.error(request, 'You have already disliked this comment!')
                return redirect('creators')
            except Commentdvote.DoesNotExist:
                vote = None
                # find product by id and increment
                post = Post.objects.get(id=post_id)
                # find comment by id and increment
                comment = Comment.objects.get(id=comment_id)
                vote = Commentdvote(commentID=comment, postID=post, userID=request.user)
                comment.dislikes += 1
                vote.save()
                comment.save()
                return redirect('creators')
