from django.shortcuts import render
from django.views import generic


class ParseIndex(generic.View):
    template_name = "parse/index.html"

    def get(self, request):
        return render(request, self.template_name)