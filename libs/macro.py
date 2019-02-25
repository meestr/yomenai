from discord import Color, Embed

class macro:
    @staticmethod
    async def message(desc:str,color:Color=Color.purple(),title:str=None):
        return Embed(
            type="rich",
            description=desc,
            color=color,
            title=title
        )
    @classmethod
    async def img(cls, url:str, desc:str=None, title:str=None):
        message = await cls.message(desc, title=title)
        message.set_image(url=url)
        return message
    @classmethod
    async def error(cls, desc:str=None, title:str=None):
        return await cls.message(desc=desc,
                                 color=Color.red())

msg = macro.message
img = macro.img
error = macro.error
