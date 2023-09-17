import telebot
import buttons
import database
# from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot('6448222136:AAEKKHzwHield6HK5LlUQ2UXBIKwgkP3tvw')


@bot.message_handler(commands=['start'])
def start(message):
    #global user
    user = message.from_user.id
    print(message)
    bot.send_message(user, 'Привет, Salom', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(user, 'Выбирайте, Tanlang', reply_markup=buttons.languages())
    if message.text.lower() == 'помощь':
        bot.send_message(user, 'просто нажите на "регистрация", там вы введёте имя и номер телефона')


@bot.callback_query_handler(lambda call: call.data in ['rus', 'uzb'])
def change_lan(call):
    user = call.message.chat.id
    if call.data =='rus':
        bot.register_next_step_handler(call.message, start_reg)
        bot.send_message(user, 'язык выбран русский')
        bot.send_message(user, 'для следующей операции нажмите на команды', reply_markup=buttons.choice())

    elif call.data == 'uzb':
        bot.register_next_step_handler(call.message, start_reg_uzb)
        bot.send_message(user, "o'zbek tili tanlangan")
        bot.send_message(user, 'keyingi boshqaruv uchun comandalarni ishlating', reply_markup=buttons.choice_uzb())


@bot.message_handler(content_types=['text'])
def start_reg(message):
    if message.text == 'Регистрация':
        bot.send_message(message.from_user.id, 'введите ваше имя и фамилию', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'Помощь':
        bot.send_message(message.from_user.id, 'просто жмите на регистрацию чтобы начать')


def get_name(message):
    user = message.from_user.id
    name = message.text
    bot.send_message(user, f'здравствуйте {name}')
    bot.send_message(user, 'отлично, введите ваш номер для регистрации', reply_markup=buttons.get_number())
    bot.register_next_step_handler(message, get_num, name)


def get_num(message, name):
    user = message.from_user.id
    if message.contact and message.contact.phone_number:
        #bot.send_message(user, 'готово!')
        user_num = message.contact.phone_number
        database.user_reg(user, user_num)
        bot.register_next_step_handler(message, chat, name, user_num)
    elif message.text.lower() == 'далее':
        bot.send_message(user, 'возвращаю, нажмите поделиться а потом далее!', reply_markup=buttons.choice())


def chat(message, name, user_num):
    user = message.from_user.id
    bot.send_message(-1001500295547, f'New guy here!!!\n\nGuy name: {name}\n'
                                    f'Number: {user_num}\n')
    bot.send_message(user, "Отлично, вы были внесены в список")
    bot.register_next_step_handler(message, start_reg)




def start_reg_uzb(message):
    if message.text == 'Toldirish':
        bot.send_message(message.from_user.id, 'Ismizni kiriting', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name_uzb)
    elif message.text == 'Yordam':
        bot.send_message(message.from_user.id, 'Toldirishga bosing')


def get_name_uzb(message):
    user = message.from_user.id
    name = message.text
    bot.send_message(user, f'Assalomu alekum {name}')
    bot.send_message(user, 'yahsi nomeringiz kiritildi', reply_markup=buttons.get_number_uzb())
    bot.register_next_step_handler(message, get_num_uzb, name)


def get_num_uzb(message, name):
    user = message.from_user.id
    if message.contact and message.contact.phone_number:
        #bot.send_message(user, 'готово!')
        user_num = message.contact.phone_number
        database.user_reg(user, user_num)
        bot.register_next_step_handler(message, chat_uzb, name, user_num)
    elif message.text.lower() == "orqaga":
        bot.send_message(user, 'orqaga ketyapman, birinchi kiritishga bosing', reply_markup=buttons.choice_uzb())



def chat_uzb(message, name, user_num):
    user = message.from_user.id

    bot.send_message(-1001500295547, f'New guy here!!!\n\nGuy name: {name}\n'
                                     f'Number: {user_num}\n')
    bot.send_message(user, "Yashi, siz ro'yxatga kiritildiz")
    bot.register_next_step_handler(message, start_reg)




bot.infinity_polling()
