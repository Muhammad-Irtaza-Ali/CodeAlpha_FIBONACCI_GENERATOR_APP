from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def fibonacci_view(request):
    sequence=[]
    n=request.GET.get('n')
    if n and n.isdigit():
        n=int(n)
        a,b=0,1
        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b
    return render(request, 'fibonacci/fibonacci.html', {'sequence':sequence})
