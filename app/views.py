from django.shortcuts import render
import datetime
from django.http import HttpResponse
import requests
import asyncio
from time import sleep
import httpx
# Create your views here.

def main(request):
    if request.method == "GET":
        return render(request,'index.html')

# async def current_datetime(request):
#     # now = datetime.datetime.now()
#     # html = '<html><body>It is now %s.</body></html>' % now
#     html = requests.get("https://github.com/")
#     return HttpResponse(html)
# def old(request):
#     html = requests.get("https://github.com/")
#     return HttpResponse(html)


# 异步任务
async def http_call_async(a):
    m = "异步任务"
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
        print(a)
    return m

# 同步任务
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)

async def index(request):
    return HttpResponse("# 异步视图 - 无异步或同步任务")

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async('alg'))
    return HttpResponse("# 异步视图 - 调用异步任务")

def sync_view(request):
    http_call_sync()
    return HttpResponse("# 同步视图 - 调用普通同步任务")