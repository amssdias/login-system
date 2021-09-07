from django.shortcuts import render

def handle_bad_request(request, exception):
    return render(request, 'errors/400.html', status=400)

def handle_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)

def handle_server_error(request):
    return render(request, 'errors/500.html', status=500)