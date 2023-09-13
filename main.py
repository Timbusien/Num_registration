import telebot
import buttons

bot = telebot.TeleBot('6448222136:AAEKKHzwHield6HK5LlUQ2UXBIKwgkP3tvw')


@bot.message_handler(commands=['start'])
def start(message):
    global user
    user = message.from_user.id
    print(message)
    bot.send_message(user, 'Привет, жми на регистрацию!', reply_markup=buttons.choice())
    # if message.text.lower() == 'помощь':
    #     bot.send_message(user, 'просто нажите на "регистрация", там вы введёте имя и номер телефона')


@bot.message_handler(content_types=['text'])
def start_reg(message):
    if message.text == 'Регистрация':
        bot.send_message(user, 'введите ваше имя и фамилию', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'Помощь':
        bot.send_message(user, 'просто жмите на регистрацию чтобы начать')


def get_name(message):
    name = message.text
    bot.send_message(user, f'здравствуйте {name}')
    bot.send_message(user, 'отлично, введите ваш номер для регистрации', reply_markup=buttons.get_number())
    bot.register_next_step_handler(message, get_num, name)


def get_num(message, name):
    if message.contact and message.contact.phone_number:
        #bot.send_message(user, 'готово!')
        user_num = message.contact.phone_number
        bot.register_next_step_handler(message, chat, name, user_num)
    elif message.text.lower() == 'далее':
         bot.send_message(user, 'возвращаю, нажмите поделиться а потом далее!', reply_markup=buttons.choice())


def chat(message, name, user_num):

    bot.send_message(-1001500295547, f'New guy here!!!\n\nGuy name: {name}\n'
                                     f'Number: {user_num}\n')
    bot.send_message(user, 'Готово, вы были внесены в список')
    bot.register_next_step_handler(message, start_reg)



bot.infinity_polling()




