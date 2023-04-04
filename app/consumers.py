from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        '''
        当有客户端向后端发送websocket连接请求时，自动触发该函数
        :param message:
        :return:
        '''

        print("client内所有内容：",self.scope['client'])
        print("IP地址：",self.scope['client'][0])
        print("端口：", self.scope['client'][1])

        # print("cookies：",self.scope['cookies'])
        print('HTTP头部：',self.scope['headers'])
        # print('请求方法：',self.scope['method'])
        print('请求路径：',self.scope['path'])
        print('当前请求的查询字符串：',self.scope['query_string'])
        # print('请求协议：',self.scope['scheme'])

        '''
        self.scope['client']：一个元组，包含连接者的IP和端口。
        self.scope['cookies']：一个字典，包含所有的cookie。
        self.scope['headers']：一个元组，包含所有的HTTP头部。
        self.scope['method']：当前请求的方法，如GET、POST等。
        self.scope['path']：当前请求的路径。
        self.scope['query_string']：当前请求的查询字符串。
        self.scope['scheme']：当前请求的协议，如http、https等.
        '''

        #添加群组
        async_to_sync(self.channel_layer.group_add)(
            "chat",  # 组名称
            self.channel_name  # 客户端名称
        )

        # 服务器允许客户端创建连接
        self.accept()
        self.send("服务器已经验证！Websocket连接成功！")

    def websocket_receive(self, message):
        '''
        浏览器基于websocket向后端发送数据，自动触发接受消息，并且处理信息
        :param message:
        :return:
        '''
        # 输出消息
        print(message)

        if message['text'] == 'wait':
            self.send("等待！")

        elif message['text'] == 'yibu':
            self.send("任务正在执行")

        else:
            # 服务端向前端回消息
            async_to_sync(self.channel_layer.group_send)(
                "chat",  # 组名称
                {
                    'type': 'chat_message',
                    'message': message['text'] + '哈哈哈！'
                }
            )
            print('已经向前端发送消息')
            # test()
            # self.send('服务器收到了你的消息：%s' % (message['text']))

    def websocket_disconnect(self, message):
        '''
        客户端与服务端断开连接时，自动触发该函数
        :param message:
        :return:
        '''

        async_to_sync(self.channel_layer.group_discard)(
            "chat",  # 组名称
            self.channel_name  # 客户端名称
        )
        print('断开连接')
        raise StopConsumer()

    def chat_message(self, event):
        # message = event['message']
        #
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))

        message = event['message']
        # Send message to WebSocket
        self.send(message)


