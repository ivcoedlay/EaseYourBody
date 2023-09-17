import wget
import time
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from telebot_calendar` import Calendar, CallbackData, RUSSIAN_LANGUAGE
import datetime
import random

bot = telebot.TeleBot('yourtoken')
calendar = Calendar(language=RUSSIAN_LANGUAGE)
calendar_1 = CallbackData('calendar_1', 'action', 'year', 'month', 'day')
now = datetime.datetime.now()
weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
c_spl = []
current_date = ''
current_date_int = []
dictionary = {}

#Случайные неповторяющиеся числа
def rand_num(item_len, result_amount):
    j = list(range(0, item_len))
    random.shuffle(j)
    return j[:result_amount]

#Выдача списка команд
def menu(message):
    bot.send_message(message.chat.id, '📘 /planner — ежедневник с добавлением задач на даты;' +
                     '\n🤷 /stretch_shoulders — разминка для плеч.'+
                     '\n🤸 /stretch_back — разминка для спины.'+
                     '\n👐 /stretch_hands — разминка для рук.'+
                     '\n💆 /stretch_neck — разминка для шеи.'+
                     '\n👀 /eye_break — разминка для глаз.')

#Результат: дата + задача (ежедневник)
def input_date_1(message):
    task = message.text
    task_date = current_date
    if task_date in dictionary:
        dictionary[task_date].append(task)
    else: dictionary[task_date] = [task]
    weekday = weekdays[datetime.datetime(current_date_int[2], current_date_int[1], current_date_int[0], 23, 24, 55, 173504).weekday()]
    bot.send_message(message.chat.id, '✏ Задача: ' + task + ';' + '\n🔢 Дата: ' + task_date+ ', ' + weekday + '.')
    menu(message)


#СКАЧИВАНИЕ ФОТО ДЛЯ СПИНЫ_____________________________________________________________________________________________________________________________________________________________
'''wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20102937-01.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103249-02.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103328-03.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103405-04.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103445-05.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103459-06.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103510-07.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103520-08.jpg")
wget.download("https://cdn.lifehacker.ru/wp-content/uploads/2014/03/20103535-09.jpg")'''


pics = [open("20102937-01.jpg", "rb"),
        open("20103249-02.jpg", "rb"),
        open("20103328-03.jpg", "rb"),
        open("20103405-04.jpg", "rb"),
        open("20103445-05.jpg", "rb"),
        open("20103459-06.jpg", "rb"),
        open("20103510-07.jpg", "rb"),
        open("20103520-08.jpg", "rb"),
        open("20103535-09.jpg", "rb")]

#Гимнастика по Жданову_____________________________________________________________________________________________________________________________________________________________
wget.download("https://cdn-ru.bitrix24.ru/b12380146/landing/5e6/5e61cfdb24cf444fcf2acce460b217c7/uprazhneniya-dlya-glaz-6_2x.jpg")
wget.download("https://cdn-ru.bitrix24.ru/b12380146/landing/748/748759c10f096abf9239db6c22030b4f/aga_2x.jpg")
wget.download("https://cdn-ru.bitrix24.ru/b12380146/landing/7fb/7fb460bd6a642c38821dfbe5c2d63981/metka_2x.png")
wget.download("https://cdn-ru.bitrix24.ru/b12380146/landing/fea/fea88ea742cf8ce7dfbbbd003a5bc57a/scale_2400_2x.webp")
pics_Zhdanov = [open("uprazhneniya-dlya-glaz-6_2x.jpg", "rb"),
                open("aga_2x.jpg", "rb"),
                open("metka_2x.png", "rb"),
                open("scale_2400_2x.webp", "rb")]
text_Zhdanov = ("🟥 «Моргание». В течение 1-2 минут нужно быстро и часто моргать, не напрягая веки. Благодаря такому упражнению происходит усиление кровообращения и ткани насыщаются кислородом." +
"🟧 «Стрелки». Нужно очерчивать глазами полукруг: сначала по часовой стрелке, затем против." +
"🟨 «Диагонали». Для выполнения упражнения хорошо подходит окно: нужно просто переводить взгляд из верхнего угла в противоположный нижний угол и наоборот. Выполняют 10 движений, затем моргают 15 секунд." +
"🟩 «Вертикали». Движения глаз направлены вверх и вниз. Повторяют 10 раз, после чего опять моргают." +
"🟦 «Прямоугольник». Взглядом рисуйте перед собой прямоугольник, сначала по часовой стрелке, затем — против. Это упражнение так же следует повторить примерно 10 раз." +
"🟥 «Зигзаг». Взглядом рисуется ломаная линия. Сначала сверху вниз, затем снизу-вверх." +
"🟧 «Циферблат». Представьте перед собой воображаемый циферблат. Нужно поднять глаза сначала на 12 часов, затем — на 3, 6, 9. Повторить в другую сторону." +
"🟨 «Песочные часы». Упражнение заключается в «рисовании» взглядом песочных часов, сначала в одну, затем — в другую сторону." +
"🟩 «Метка на стекле». Для выполнения упражнения нужно прикрепить к оконному стеклу на уровне глаз какую-либо метку (почтовую марку, кусочек бумаги или просто нарисовать точку маркером). Расстояние от метки до глаз – около 30 см. Затем поочередно фокусироваться на оконном стекле и на любом предмете за окном (дерево, соседний дом и т.п.). Переводить взгляд нужно каждые 10-30 секунд." +
"🟦 Массаж. Благодаря самомассажу ускоряется циркуляция жидкостей в тканях и уменьшается отечность. Руки должны быть чистыми и теплыми, а упражнение лучше выполнять сидя. Аккуратно тремя пальцами рук необходимо слегка нажимать на веки обоих глаз, а само касание должно длиться не больше секунды. Повторить 3-5 раз.")
#Гимнастика Норбекова_____________________________________________________________________________________________________________________________________________________________
wget.download("https://elitplus-clinic.ru/assets/gallery/all_img/tablica-norbekova-10022020.jpg")
pics_Norbekov = open("tablica-norbekova-10022020.jpg", "rb")
text_Norbekov = ("🟥 Голова прямая, глаза как можно выше поднимите вверх, мысленно проведя вертикальную черту через лоб. Задержите взгляд на несколько секунд в высшей точке и опустите его вниз\n" + 
"🟧 Исходное положение то же, но глаза направляем вниз, ищем низшую точку на полу и задерживаем на ней взгляд на несколько секунд. Возвращаемся в исходную позицию. Нужно следить за мимикой, не щуриться, работа проводиться только взглядом;\n"+
"🟨 Держим голову ровно, переводим глаза вправо, ищем наиболее отдаленную точку, задерживаем на ней взгляд и возвращаемся в исходное положение. Те же действия проделываем с левой стороной;\n" +
"🟩 Из прямого положения переводим глаза в крайние точки по следующей траектории: левая нижняя — правая верхняя, затем правая нижняя — левая верхняя. Проще говоря, пытаемся глазами нарисовать бантик. Все движения выполняются плавно, не нужно помогать головой и кивать в такт глазам;\n"+
"🟦 Упражнение «Восьмерка». Аккуратно, со средней скоростью прорисуйте глазами восьмерку. Это занятие укрепляет мышцы и нормализует глазное давление;\n" +
"🟪 Шестое помогает при близорукости. Сфокусируйте взгляд поочередно на кончике носа, переносице и между бровями. Возвращаясь из каждой точки, направляйте взгляд перед собой и немного расфокусируйте его, рассмотрите предметы вокруг себя;\n"+
"⬜ «Пальминг». Закройте глаза плотно ладонями, расслабьтесь и представляйте, что вы четко видите без контактных линз и очков. Продолжительность процедуры составляет пять минут. За это время органы зрения достигают полного расслабления.")

#Гимнастика Аветисова_____________________________________________________________________________________________________________________________________________________________

#Гимнастика Бейтса_____________________________________________________________________________________________________________________________________________________________


#Отправка нескольких фото одним сообщением
media = []
for q in pics: media.append(telebot.types.InputMediaPhoto(q))
    
media_Zhdanov = []
for q in pics_Zhdanov: media_Zhdanov.append(telebot.types.InputMediaPhoto(q))

#ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ_____________________________________________________________________________________________________________________________________________________________
denial = 'Ряд положений, которые помогут Вам более точно понимать, чем мы занимаемся и что относится к нашей зоне ответственности: \n1️⃣. Авторы бота и тренировочных программ не несут ответственность за появление неточной информации, а также за использование вами данных, полученных с помощью бота либо найденных по ссылкам, содержащимися в нем. \n2️⃣. Авторы бота не несут ответственности за любой из видов ущерба (включая, но не ограничиваясь, моральный, материальный, физический), который причинен пользователем самому себе или третьим лицам вследствие неверного толкования, применения или иного законного либо незаконного использования информации, включая последствия, которые возникли или могли возникнуть из-за ошибок, опечаток и неточностей в информации. Любая информация может быть использована пользователями исключительно на свой страх и риск. \n3️⃣. Бот разработан и работает только для совершеннолетних пользователей, которые могут понимать всю степень своей ответственности и знать, что влекут за собой те или иные действия. \n4️⃣. Названия торговых марок используются исключительно с консультативной целью. Все торговые названия принадлежат владельцам этих марок и не используются без их официального разрешения в коммерческих целях. \n\nИспользование информации означает согласие пользователя со всеми приведенными в данном тексте условиями и их безоговорочное принятие. Используя информацию, пользователь отказывается от всех возможных претензий и требований к создателям бота.'

#ИСТОЧНИКИ_____________________________________________________________________________________________________________________________________________________________
sources = ''
        
#ПРИВЕТСТВИЕ_____________________________________________________________________________________________________________________________________________________________
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("👋 Поздороваться")
    keyboard.add(button1)
    bot.send_message(message.from_user.id, '👋 Добро пожаловать, ' + message.from_user.first_name + '.\n       Я Ваш бот-помошник!', reply_markup=keyboard)

@bot.message_handler(commands=['stretch_back'])
def workout_plan(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("🔙 Вернуться в меню")
    button2 = types.KeyboardButton("📒 Подробное описание к упражнениям")
    keyboard.add(button2)
    keyboard.add(button1)

    bot.send_media_group(message.chat.id, media)
    bot.send_message(message.chat.id, "Этот комплекс упражнений поможет Вам держать свою спину здоровой, а делать его можно даже за рабочим столом! 😉", reply_markup=keyboard)
        
#ПРОГРАММА ТРЕНИРОВОК_____________________________________________________________________________________________________________________________________________________________
@bot.message_handler(commands=['eye_break'])
def workout_plan(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("💪 Базовая разминка")
    button2 = types.KeyboardButton("🦾 Разминка для продвинутых")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.from_user.id, 'Упражнения — хороший способ снять мышечное напряжение и избавиться от головной боли, сухости в глазах и других симптомов переутомления.', reply_markup=keyboard)
   
#ЕЖЕДНЕВНИК_____________________________________________________________________________________________________________________________________________________________
@bot.message_handler(commands=['planner'])
def planner(message):
    bot.send_message(message.chat.id, '📆 Выберите дату:', reply_markup=calendar.create_calendar(
            name=calendar_1.prefix,
            year=now.year,
            month=now.month))
            
@bot.message_handler(content_types=['text'])
def call(message):
    if message.text == '👋 Поздороваться':
        menu(message)
    elif message.text ==  "🔙 Вернуться в меню":
        menu(message)
    elif message.text == "🎉 Выполнено!":
        menu(message)
    elif message.text == "📒 Подробное описание к упражнениям": #Спина
        bot.send_message(message.chat.id, "🌑 Пожимания плечами\nЭто упражнение задействует верх спины. Сядьте ровно и поставьте обе ноги на пол. Руки должны висеть вдоль туловища. Поднимите плечи к ушам, держа при этом шею ровной. Задержитесь на мгновение и опустите плечи обратно.\n\n🌒 Сведение лопаток\nСядьте ровно, поставив ноги на пол, а руки протянув вдоль туловища. Сведите лопатки вместе, не поднимая при этом плечи. Задержитесь на секунду и вытяните плечи вперед. Это растянет ваш плечевой пояс в противоположную сторону.\n\n🌓 Вращения плечами\nСядьте ровно, поставив ноги на пол. Положите кисти себе на плечи. Сделайте несколько вращений вперед так, словно Вы плывете.\n\n🌔 Скручивания спины\nСядьте ровно на край стула, поставив обе ноги на пол. Колени должны быть параллельны друг другу. Положите руки себе за голову и поверните туловище вправо, а затем влево.\n\n🌕 Поясничные прогибания\nСядьте ровно на край стула, поставив ноги на пол и положив руки за голову. Прогните спину и посмотрите в потолок. Шея, плечи и голова должны уйти максимально назад, а середина спины — вперед.\n\n🌖 Сгибания вперед сидя\nСядьте прямо, поставив обе ноги на пол. Сведите колени вместе и наклонитесь вперед, положив на них грудь. Избегайте скругления спины. Вы можете немного себе помочь, взявшись руками за голени. Задержитесь в этой позиции максимально долго и вернитесь в исходную.\n\n🌗 Наклоны в стороны\nСядьте на край стула и поставьте обе ноги на пол. Держите колени параллельно друг другу. Положите обе руки за голову и наклоните туловище влево. Вернитесь в исходное положение и наклоните его вправо. Не наклоняйте спину вперед или назад.\n\n🌘 Поза кошки-коровы\nСядьте на край стула и поставьте обе ноги на пол. Колени не должны соприкасаться, руки положите на колени. Вытяните середину спины вперед, стараясь не помогать себе тазом и плечами. Затем, скруглите спину и вытяните ее назад.\n\n🌑 Сгибания в стороны\nСядьте ровно на край стула. Положите руки на колени. Согните спину в левую сторону, затем повторите то же самое в правую сторону. Не помогайте себе плечами и тазом.")
        menu(message)
    elif message.text == "📕 Подробное описание к упражнениям": #Жданов
        bot.send_message(message.chat.id, text_Norbekov)
        menu(message)
    elif message.text == "🔴 Гимнастика для глаз по Жданову":
        keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("📕 Подробное описание к упражнениям") 
        button2 = types.KeyboardButton("🔙 Вернуться в меню")
        keyboard.add(button1)
        keyboard.add(button2)
        bot.send_media_group(message.chat.id, media_Zhdanov)
        bot.send_message(message.chat.id, "По уверениям самого профессора Владимира Жданова, его методика восстановления зрения подходит людям с миопией, пресбиопией, астигматизмом, косоглазием.", reply_markup=keyboard)
            '''
    elif message.text == "🔵 Гимнастика для глаз Норбекова":
    elif message.text == "🟡 Гимнастика для глаз Аветисова":
    elif message.text == "🟢 Гимнастика для глаз Бейтса":'''
            
    elif message.text == "💪 Базовая разминка":
        
    elif message.text == "🦾 Разминка для продвинутых":
        keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("🔴 Гимнастика для глаз по Жданову")
        button2 = types.KeyboardButton("🔵 Гимнастика для глаз Норбекова")
        button3 = types.KeyboardButton("🟡 Гимнастика для глаз Аветисова")
        button4 = types.KeyboardButton("🟢 Гимнастика для глаз Бейтса")
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        bot.send_message(message.from_user.id, '', reply_markup=keyboard)

    elif message.text == "🪧 Отказ от ответственности":
        keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("🫧 Источники тренировочных материалов")
        keyboard.add(button1)
        bot.send_message(message.from_user.id, denial, reply_markup=keyboard)
    elif message.text == "🫧 Источники тренировочных материалов":
        bot.send_message(message.from_user.id, sources)
        menu(message)
    else:
        bot.send_message(message.chat.id, '❓ Не могу Вас понять... Пожалуйста, введите комманду.')
        #print(message)
    


@bot.callback_query_handler(func=lambda call: call.data.startswith(calendar_1.prefix))
def callback_inline(call: types.CallbackQuery):
    name, action, year, month, day = call.data.split(calendar_1.sep)
    date = calendar.calendar_query_handler(bot=bot, call=call, name=name, action=action, year=year, month=month, day=day)

    if action == 'DAY':
        bot.send_message(chat_id=call.from_user.id, text=f'✅ Вы выбрали {date.strftime("%d.%m.%Y")}')
        global current_date, current_date_int
        current_date = date.strftime("%d.%m.%Y")
        c_spl = current_date.split('.')
        current_date_int = [int(c_spl[0].lstrip('0')), int(c_spl[1].lstrip('0')), int(c_spl[2].lstrip('0'))] #Убираем нули из начала дат "01.08" и др.
        
        msg = bot.send_message(call.from_user.id, '📝 Введите задачу для даты:')
        bot.register_next_step_handler(msg, input_date_1)
        
    elif action == 'CANCEL':
        bot.send_message(chat_id=call.from_user.id, text='📘 /planner — ежедневник с добавлением задач на даты;' +
                         '\n📗 /workout_plan — составление программы тренировок.')
 


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        #logger.error(e) или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
