from django.shortcuts import render, get_object_or_404
from datacenter.models import Passcard, Visit
from datacenter.visit_analysis import get_duration, is_visit_long, format_duration
from django.utils import timezone

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    formatted_visits = []
    for visit in this_passcard_visits:
        entered_localtime = timezone.localtime(visit.entered_at)
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        is_strange = is_visit_long(visit)

        formatted_visits.append({
            'entered_at': entered_localtime.strftime('%d-%m-%Y %H:%M'),
            'leaved_at': visit.leaved_at.strftime('%d-%m-%Y %H:%M') if visit.leaved_at else 'Не покинул хранилище',
            'duration': formatted_duration,
            'is_strange': is_strange,
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': formatted_visits,
    }

    return render(request, 'passcard_info.html', context)
