from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Link


# Create your views here.

class LinkListView(ListView):
    # query for all the links Link.objects.all()
    # context = {'link': links}
    # return render(request, 'link_list.html', context)
    model = Link
    # template called model_list.html -> link_list.html


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # template model_form -> link_form.html


class LinkUpdateView(UpdateView):
    # create a form
    # check if a get request or a put request
    # either render the form or update and save in our db
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')


class LinkDeleteView(DeleteView):
    # take in a id/primary key of an object
    # query to db for that object
    # check if it exists -> delete the object
    # return some template or forward to user to some url
    model = Link
    success_url = reverse_lazy('link-list')
    # form to submit to delete the item
    # expect a template name model_confirm_delete.html
    # link_confirm_delete.html


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }
    return render(request, 'link_plant/profile.html', context)