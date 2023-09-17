from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def languages():
    buttons = InlineKeyboardMarkup(row_width=2)
    rus = InlineKeyboardButton(text='Русский язык', callback_data='rus')
    uzb = InlineKeyboardButton(text="O'zbek tili", callback_data='uzb')
    buttons.row(rus, uzb)
    return buttons

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



def choice_uzb():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reg = types.KeyboardButton('Toldirish')
    #help_bar = types.KeyboardButton('Помощь')
    buttons.add(reg)
    return buttons

def get_number_uzb():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton('nomerni yuklash', request_contact=True)
    back = types.KeyboardButton('bosqa joyga')
    buttons.add(number, back)
    return buttons






