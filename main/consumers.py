from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Review,Product
from django.contrib.auth.models import User
class ProductViewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Connected from connect function")
        await self.accept()

    async def receive_json(self, content, **kwargs):
        data = content
        # print(data['roomname'])
        if data['command'] == "open":
            await self.channel_layer.group_add(
                data["roomname"],
                self.channel_name
            )
            print("User added")
        elif data['command'] == "send":
            get_user = await database_sync_to_async(User.objects.get)(username=data["user"])
            get_product = await database_sync_to_async(Product.objects.get)(id=data["product"])
            create_review = Review(user=get_user, product=get_product, review=data["review"])
            await database_sync_to_async(create_review.save)()
            await self.channel_layer.group_send(data["roomname"],{
                'type':'review.message',
                "review":data["review"],
                "user":data["user"]
            })

        elif data["command"] == "like":
            await self.channel_layer.group_send(data["roomname"],{
                'type':'like_product',
                'like':data["like"],
                'user':data["user"],

            })

    async def disconnect(self, code):
        pass

    async def review_message(self,event):
        await self.send_json({
            "user":event["user"],
            "review":event["review"]
        })

    # async def like_product(self,event):
    #     await self.send_json({
    #         "user":event["user"],
    #
    #     })4a
