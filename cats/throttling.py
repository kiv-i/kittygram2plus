import datetime as dt

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        now = dt.datetime.now().hour
        if 3 <= now <= 5:
            return False
        return True
