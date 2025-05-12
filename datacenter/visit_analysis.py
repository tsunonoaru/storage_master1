from datetime import timedelta
from django.utils import timezone

SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        current_time = timezone.localtime(timezone.now())
        return current_time - visit.entered_at


def is_visit_long(visit):
    duration = get_duration(visit)
    return duration > timedelta(hours=1)


def format_duration(duration):
    total_seconds = duration.total_seconds()

    hours, remainder = divmod(total_seconds, SECONDS_IN_AN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_A_MINUTE)

    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
