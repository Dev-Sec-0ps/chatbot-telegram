# coding=utf-8
import telebot
import const

from telebot import types
from telebot.types import LabeledPrice

bot = telebot.TeleBot(const.TOKEN)

prices1 = [LabeledPrice(label='Практическая характерология (1000руб)', amount=100000)]
prices2 = [LabeledPrice(label='Анализ публикационной активности на основе работы в Elibrary', amount=200000)]

# Добавляем обработчик сообщений, который проверяет команды, в нашем случае это команда /start
@bot.message_handler(commands=['start'])
def startpg(message):
    # Создаем клавиатуру, с единственной кнопкой "Начать"
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Начать')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id, 'Добро пожаловать в PARALLAX!✋🏻 \nЗдесь вы сможете ознакомиться с нашими услугами и сразу же связаться с экспертами!', reply_markup=startmenu)

#Добавляем обработчик сообщений, который проверяет тип сообщения "Текст"
@bot.message_handler(content_types=['text'])
def osnov(message):
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Начать", то у нас будет выполняться это действие"
    if message.text == 'Начать':
        # Мы присваиваем переменной "send" метод "Отправка сообщения"
        send = bot.send_message(message.chat.id, 'Как вас зовут?')
        # Здесь мы делаем следующий шаг, который изначально будет отправлять переменную "send", а потом переходит к следующей функции под названием "next1"
        bot.register_next_step_handler(send, next1)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Бизнес", то у нас будет выполняться это действие"
    elif message.text == 'О нас':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor1 = types.ReplyKeyboardMarkup(True, False)
            vibor1.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, '💥 Параллакс - это эффект, принцип которого мы применили к образованию и развитию личности. Дело в том, что существует разница восприятия способностей человека им самим, его окружением и совершенно не знакомыми людьми. Всё всегда зависит от угла зрения. \n💥 Мы верим в уникальность и гениальность каждого человека, главное посмотреть на него с нужного угла, что и лежит в основе нашей деятельности.', reply_markup=vibor1)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Программирование", то у нас будет выполняться это действие"
    elif message.text == 'Услуги':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor2 = types.ReplyKeyboardMarkup(True, False)
            vibor2.row('Практическая характерология')
            vibor2.row('Анализ публикационной активности на основе работы в Elibrary')
            vibor2.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Список наших услуг', reply_markup=vibor2)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Лайфаки", то у нас будет выполняться это действие"
    elif message.text == 'Эксперты':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor3 = types.ReplyKeyboardMarkup(True, False)
            vibor3.row('Андрей Игошин')
            vibor3.row('Сергей Суслов')
            vibor3.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Свяжитесь с экспертом', reply_markup=vibor3)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Фитнес", то у нас будет выполняться это действие"
    elif message.text == 'Стоимость':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor4 = types.ReplyKeyboardMarkup(True, False)
            vibor4.row('Оплата')
            vibor4.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, '1. Практическая характерология - 1000руб (к примеру)\n2. Анализ публикационной активности на основе работы в Elibrary - 2000руб (к примеру)', reply_markup=vibor4)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Назал", то у нас будет выполняться это действие"
    elif message.text == 'Назад':
        # Так делается, для того, чтобы перейти к фукнции с назаваением "next2"
        next2(message)

    elif message.text == 'Оплата':
        if biznes == 'biznes':
            vibor10 = types.ReplyKeyboardMarkup(True, False)
            vibor10.row('Практическая характерология (1000руб)')
            vibor10.row('Анализ публикационной активности на основе работы в Elibrary (2000руб)')
            vibor10.row('Назад')
            bot.send_message(message.chat.id, 'Какую услугу хотите оплатить?', reply_markup=vibor10)

    elif message.text == 'Практическая характерология (1000руб)':
        bot.send_invoice(message.chat.id, title='Практическая характерология',
                         description='Нажмите на кноку чтобы оплатить',
                         currency='rub',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices1,
                         start_parameter='account',
                         invoice_payload='1krub',
                         provider_token="401643678:TEST:0c5ba66c-eb8b-4f1b-858c-9e663c2ee558")

    elif message.text == 'Анализ публикационной активности на основе работы в Elibrary (2000руб)':
        bot.send_invoice(message.chat.id, title='Анализ публикационной активности на основе работы в Elibrary',
                         description='Нажмите на кноку чтобы оплатить',
                         currency='rub',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices2,
                         start_parameter='account',
                         invoice_payload='2krub',
                         provider_token="401643678:TEST:0c5ba66c-eb8b-4f1b-858c-9e663c2ee558")

    elif message.text == 'Практическая характерология':
        if biznes == 'biznes':
            vibor5 = types.ReplyKeyboardMarkup(True, False)
            vibor5.row('Назад')
            bot.send_message(message.chat.id, 'Существует достаточное количество методик изучающих характер человека, его качества и свойства. Однако, все они так или иначе, основаны на действиях человека, а не его мотивации к этим действиям. В этом главное отличие практической характерологии. Мы анализируем поведенческие тенденции человека. Это даёт нам возможность определить, чем обусловлено то или иное поведение человека, в чем его сильные и слабые стороны, в каких областях его поджидает успех, а в каких он достигнет лишь посредственных результатов. Преимущества методики в том, что комплексный анализ, не рассматривает характеристики отдельно взятых радикалов, а даёт понимание поведенческих тенденции отдельного человека, в зависимости от того «коктейля» который в нем намешан. Главная ценность этой методики заключается в возможности точечно определить какие качества и навыки человеку следует прокачать, чему стоит научиться, что нужно взять под контроль. На сегодняшний день, ни одна из методик кроме этой, не покажет вам таких результатов.', reply_markup=vibor5)

    elif message.text == 'Анализ публикационной активности на основе работы в Elibrary':
        if biznes == 'biznes':
            vibor6 = types.ReplyKeyboardMarkup(True, False)
            vibor6.row('Назад')
            bot.send_message(message.chat.id, 'Регистрация в научной электронной библиотеке Elibrary (пользовательский и авторский профиль) Поиск публикаций и цитирований автора или Поиск научных публикаций по заданным параметрам Библиометрическая оценка журналов (критерии, показатели, рейтинг) Оценка публикационной активности автора (критерии, показатели, рейтинг) Боблиометрическая оценка организаций (критерии, показатели, рейтинг)', reply_markup=vibor6)

    elif message.text == 'Андрей Игошин':
        if biznes == 'biznes':
            vibor7 = types.ReplyKeyboardMarkup(True, False)
            vibor7.row('Назад')
            bot.send_message(message.chat.id, 'ВК: https://vk.com/igoshinan\n901274646 (к примеру)', reply_markup=vibor7)

    elif message.text == 'Сергей Суслов':
        if biznes == 'biznes':
            vibor8 = types.ReplyKeyboardMarkup(True, False)
            vibor8.row('Назад')
            bot.send_message(message.chat.id, 'ВК: https://vk.com/id17453551\n901274646 (к примеру)', reply_markup=vibor8)


# Создаем функцию, для того, чтобы ответить на первое сообщение "Введите ваше имя:"
def next1(message):
    # Мы присваиваем переменной "send" метод "Отправка сообщения"
    send = bot.send_message(message.chat.id, 'Очень приятно {name}, вы уже пользовались нашими услугами?'.format(name=message.text))
    # Здесь мы делаем следующий шаг, который изначально будет отправлять переменную "send", а потом переходит к следующей функции под названием "next2"
    bot.register_next_step_handler(send, next2)

# Создаем функцию, для того, чтобы ответить на сообщение "Очень приятно {name},Введите ваш возвраст:"
def next2(message):
    global biznes
    biznes = 'biznes'
    # Создаем клавиатуру
    vibor = types.ReplyKeyboardMarkup(True, False)
    vibor.row('О нас')
    vibor.row('Услуги')
    vibor.row('Эксперты')
    vibor.row('Стоимость')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id, 'Что вас интресует?', reply_markup=vibor)

bot.polling()
