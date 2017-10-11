from django.shortcuts import loader, HttpResponse


def denied(request):
    template = loader.get_template('general/access_denied.html')
    context = {}
    return HttpResponse(template.render(context, request))
