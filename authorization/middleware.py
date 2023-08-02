from django.shortcuts import redirect

class Redirect404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            return self.get_response(request)
        
        if request.path.startswith('/static'):
            return self.get_response(request)
        
        response = self.get_response(request)

        if response.status_code == 404:
            return redirect('/auth/welcome/')

        return response