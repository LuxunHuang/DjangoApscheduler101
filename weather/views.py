from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseBadRequest

import time

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

class TT:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def update_a(self, Time):
        self.a = str(Time)

@register_job(scheduler, "interval", seconds=1)
def test_job():
    print("task: " + str(time.time()))
    tt.update_a(int(time.time()))

tt = TT(1 ,2)

register_events(scheduler)

scheduler.start()
print("Scheduler started!")

def taskA(request):
    return HttpResponse(str(tt.a) + "</p>" + str(tt.b))
