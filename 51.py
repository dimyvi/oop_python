class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if request.get('method', 'GET') == 'GET':
            return f"GET: {self.func(request)}"
        return None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"



@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)