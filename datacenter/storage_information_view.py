from django.shortcuts import render
from datacenter.models import Visit
from datacenter.visit_analysis import get_duration, format_duration
from django.utils import timezone

def storage_information_view(request):
    ongoing_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in ongoing_visits:
        entered_localtime = timezone.localtime(visit.entered_at)
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_localtime.strftime('%d-%m-%Y %H:%M'),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
