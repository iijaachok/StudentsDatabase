from StudentsDatabase import settings

def context_settings(request):

    return {'debug': settings.DEBUG, }