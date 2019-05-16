"""Platzigramm views."""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello, world: TATA! =D\nOh, hi! Current\
                        server time is {now}'.format(now=str(now)))


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    # Prints in console
    #print(request)
    # Debugger:
    #import pdb; pdb.set_trace()
    #numbers = numbers.split(',')
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    print(type(numbers), numbers)
    data = {
        'status': 'ok',
        'numbers': sorted(numbers),
        'message': 'Integers sorted successfully.'
    }
    jsonNumbers = JsonResponse(data,
        json_dumps_params = {'indent': 4}
    )
    print(type(jsonNumbers), jsonNumbers)
    return HttpResponse(jsonNumbers)


def say_hi(request, name, age):
    """Return a greeting with name and age."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to platzigram'.format(name)

    return HttpResponse(message)
