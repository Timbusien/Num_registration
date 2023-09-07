from telebot import types

def choice():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reg = types.KeyboardButton('Регистрация')
    #help_bar = types.KeyboardButton('Помощь')
    buttons.add(reg)
    return buttons

def get_number():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton('поделиться', request_contact=True)
    back = types.KeyboardButton('далее')
    buttons.add(number, back)
    return buttons




