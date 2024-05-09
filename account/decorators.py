from django.shortcuts import redirect


def authenticated(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request, *args, **kwargs)

    return inner
