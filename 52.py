class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method not in self.methods:
                return None

            handler = getattr(self, method.lower(), None)
            if handler:
                return handler(func, request, *args, **kwargs)
            return None

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request, *args, **kwargs)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request, *args, **kwargs)}"