from django.shortcuts import render
from .forms import PlayerForm
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import Player
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



class PlayerFormView(CreateView, SuccessMessageMixin):
    model = Player
    form_class = PlayerForm
    template_name = 'player_form.html'
    success_message = "Player was created successfully"



    def render_to_response(self, context, **response_kwargs):
        context['Success'] = 'Success'
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
    