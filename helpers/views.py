from django.shortcuts import render

def handle_not_found(request, exception):
    return render(request, '404.html', status=404)

def handle_server_error(request):
    return render(request, '500.html', status=500)