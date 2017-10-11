from django.shortcuts import loader, HttpResponse, HttpResponseRedirect
from general.models import Theatre
from general.utils import auth


def theatre_list(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')

    theatres = Theatre.objects.all()
    template = loader.get_template('theatre/theatre_list.html')
    context = {'theatres': theatres}
    return HttpResponse(template.render(context, request))


def theatre_detail(request, index):
    if not auth(request):
        return HttpResponseRedirect('/denied')

    theatre = Theatre.objects.get(pk=index)
    template = loader.get_template('theatre/theatre_detail.html')
    context = {'theatre': theatre}
    return HttpResponse(template.render(context, request))
