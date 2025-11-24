from django.shortcuts import render
from django.http import HttpResponse
import math

def triangle_area(request):
    try:
        a = float(request.GET.get('a'))
        b = float(request.GET.get('b'))
        c = float(request.GET.get('c'))

        if a <= 0 or b <= 0 or c <= 0:
            return HttpResponse("Помилка: всі сторони мають бути додатніми числами.")

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return HttpResponse("Помилка: з таких сторін трикутник не існує (порушена нерівність трикутника).")
        s = (a + b + c) / 2

        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        area = round(area, 2)
        response_text = f"Площа трикутника зі сторонами {a}, {b}, {c}: {area}"
        return HttpResponse(response_text)

    except (TypeError, ValueError):
        return HttpResponse("Помилка: передайте параметри a, b, c як числа. Приклад: /triangle-area/?a=3&b=4&c=5")
    except Exception as e:
        return HttpResponse(f"Невідома помилка: {e}")