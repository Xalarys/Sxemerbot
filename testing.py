from aiogram import Bot,Dispatcher,types,executor
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot("1926725145:AAEAPrBN7TVBOXN5cz8yPXXpI9Zk_XgHueM") 
dp = Dispatcher(bot)
Price = types.LabeledPrice(label="Наушники TWS",amount=800*100)
Price1 = types.LabeledPrice(label="Hoco BS33",amount=1500*100)
Paytoken = "1744374395:TEST:9a6907d35016cd46fca3"
button_hi = KeyboardButton('Товар1')
button_h2 = KeyboardButton('Товар2')
button_h3 = KeyboardButton('Товар3')
greet_kb = ReplyKeyboardMarkup(resize_keyboard = True)
greet_kb.add(button_hi,button_h2,button_h3)

@dp.message_handler(commands=['start'])
async def buy(message: types.Message):
    await bot.send_message(message.chat.id,"Привет",reply_markup=greet_kb)
    message.text.lower()

@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if Paytoken.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id,"Тестовый платеж")
    await bot.send_invoice(message.chat.id,title='Наушники TWS',
                                           description="Беспроводные",
                                           provider_token=Paytoken,
                                           currency="rub",
                                           photo_url="https://imgur.com/56MOP4V",
                                           photo_width=500,
                                           photo_height=230,
                                           is_flexible = False,
                                           prices = [Price],
                                           start_parameter="one-month-subscription",
                                           payload="test-invoise-payload")                    
@dp.pre_checkout_query_handler(lambda query:True)
async def check(pre_checkout_q:types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id,ok=True)

#Успешно
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def good(message:types.Message):
    await bot.send_message(message.chat.id,"ВВедите свой почтовый индекс")
    message.text.lower()
    await bot.send_message(937477907,message.text)


@dp.message_handler()
async def buy(message: types.Message):

    if message.text == 'Товар1':
            if Paytoken.split(':')[1] == 'TEST':
                await bot.send_message(message.chat.id,"Тестовый платеж")
                await bot.send_invoice(message.chat.id,title='Наушники TWS',
                                           description="Беспроводные",
                                           provider_token=Paytoken,
                                           currency="rub",
                                           photo_url="https://avatars.mds.yandex.net/get-mpic/12363834/2a0000018d6a2aef98f0651e5a0f85e94b1f/600x600",
                                           photo_width=500,
                                           photo_height=230,
                                           is_flexible = False,
                                           prices = [Price],
                                           start_parameter="one-month-subscription",
                                           payload="test-invoise-payload")
    if message.text == 'Товар2':
        await bot.send_message(message.chat.id,"Тестовый платеж")
        await bot.send_invoice(message.chat.id,title='Колонка Hoco BS33',
                                               description="Мощная портативная колонка Hoco BS33 имеет компактные размеры 205х71х71 мм и вес 700 г. Встроенный аккумулятор на 1200 мАч обеспечивает до 6 часов работы, заряжается за 1.5 часа. Колонка поддерживает воспроизведение файлов с microSD, USB, Bluetooth 5.0 и проводное подключение. Два динамика диаметром 52 мм каждый обеспечивают мощность до 10 Вт с диапазоном частот 20-20000 Гц. Корпус из прочного пластика с кожаным ремешком для удобства использования.",
                                               provider_token=Paytoken,
                                               currency="rub",
                                               photo_url="https://avatars.mds.yandex.net/get-mpic/5223143/img_id311058862387516119.jpeg/600x600",
                                               photo_width=500,
                                               photo_height=230,
                                               is_flexible = False,
                                               prices = [Price1],
                                               start_parameter="one-month-subscription",
                                               payload="test-invoise-payload")


if __name__ == '__main__':
    executor.start_polling(dp)