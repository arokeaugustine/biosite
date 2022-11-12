from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import CommentForm

def postlist(request):
    post = Post.objects.filter(status='published')
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    post_obj = paginator.get_page(page_number)
    return render(request, 'post.html', {'post':post_obj})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    # comment_form = CommentForm()
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # when a comment is posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create comment object but dont save it
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
            comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post':post, 'comments': comments, 'new_comment':new_comment, 'comment_form':comment_form })
    