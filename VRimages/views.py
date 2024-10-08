from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post, Comment, Meeting
from .forms import CommentForm, MeetingForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "VRimages/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.all().count()


    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted'
        )
    comment_form = CommentForm()
    meeting_form =MeetingForm()

    return render(
        request,
        "VRimages/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "meeting_form": meeting_form,
        }
    )

def create_meeting(request,slug):
    if request.method == "POST":
        post = get_object_or_404(queryset, slug=slug)
        meeting_form = MeetingForm(data=request.POST)
        if meeting_form.is_valid():
            meeting = meeting_form.save(commit=False)
            meeting.author = request.user
            meeting.post = post
            meeting.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Meeting submitted'
        )
        return(HttpResponseRedirect(reverse("post_detail",)))



def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))









    