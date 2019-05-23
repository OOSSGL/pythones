"""Post views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


@login_required
def list_posts(request):
    """List existing posts."""
    posts  = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

    '''
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</p></strong>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
    '''


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request = request,
        template_name = 'posts/new.html',
        context = {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
