from django.shortcuts import render

def studentGrades(request):
    data = {
        'students': [
            {'name': 'Suresh L.', 'percentage': 90},
            {'name': 'Amit P.', 'percentage': 45},
            {'name': 'Radhika E.', 'percentage': 76},
            {'name': 'Nidhi V.', 'percentage': 39},
        ]
    }
    return render(request, 'grades.html', data)
