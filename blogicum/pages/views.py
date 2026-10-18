from django.shortcuts import render


def about(request):
    """Показать информацию о проекте."""
    return render(request, 'pages/about.html')


def rules(request):
    """Показать правила сообщества."""
    return render(request, 'pages/rules.html')