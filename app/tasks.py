from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time

@shared_task
def send_message(message):
    print("异步任务已经在你的程序中执行")
    time.sleep(10)
    print('异步任务已经执行完毕')

    print('通过Chanels通道层，将任务执行结果返回前端')
    # 服务端向前端回消息
    channel_layer = get_channel_layer()  # 实例化get_channel_layer()对象，用于向组群发送消息
    async_to_sync(channel_layer.group_send)(
        "chat",
        {
            "type": "chat.message",
            "message": "异步任务执行完成！" + message,
        }
    )
    print('已经向前端发送消息')