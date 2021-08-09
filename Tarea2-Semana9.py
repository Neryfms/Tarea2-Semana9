import time

import telebot
from telebot import types

TOKEN = '1713791371:AAFG5-f3mFUyRIGZ_E_Se_jcdLpxpgGCG5g'

knownUsers = [] 
userStep = {} 

commands = {

    'start'             : '▶️\nIniciar bot\n\n',
    
    'help'              : '🆘\nMuestra todos los comandos disponibles\n\n',
    
    'conversiones'      : '💽\nMuestra las conversiones de la unidad de almacenamiento\n\n',

    'definiciones'      : '📖\nMuestra las conversiones de la unidad de almacenamiento\n\n'

}

imageSelect1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
imageSelect1.add ('Petabytes a Terabytes.','Gigabytes a Megabytes.', 'Terabytes a Gigabytes.' , 'Megabytes a Kilobytes.', 'Bytes a bits.' )
hideBoard = types.ReplyKeyboardRemove()  

imageSelect2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
imageSelect2.add('Definicion de Terabytes', 'Definicion de Gigabytes', 'Definicion de Megabytes', 'Definicion de Kilobytes','Definicion de Bytes', 'Definicion de Bits')
hideBoard = types.ReplyKeyboardRemove() 

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("He detectado a un nuevo usuario mas sin envargo no ha usado el comando \"/start\"")
        return 0



def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid,"¡Hola " +mention+"!" ,parse_mode="Markdown")

    if cid not in knownUsers: 
    
        knownUsers.append(cid)  
        userStep[cid] = 0 
       
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Me causa emocion que me hayas escrito.")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAO0YQ8M52iwda6I38qVWILyuvR1PagAAmILAAIWYGFLr_jq9I0EzgYgBA')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero te encuentres muy bien")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Será un gusto ayudarte")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Conmigo puedes gestionar la información referente a las unidades de almacenamiento")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Como ser:")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Sus definiciones y sus formulas")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuación te mostraré la lista de comandos")
        command_helping(m)
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ya usaste el comando /start, usa el comando /help para visualizar más comandos")

@bot.message_handler(commands=['helping'])
def command_helping(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    help_text = "Por favor, elije un comando o escríbelo usando ''/+comando''\n\n\n"
    bot.send_chat_action(cid, 'typing')
    time.sleep(5)
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text) 

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    user_id = m.from_user.id 
    user_name = m.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.send_chat_action(cid, 'typing')
    time.sleep(2)
    bot.send_message(cid,"¡"+mention+"!" ,parse_mode="Markdown")
    bot.send_chat_action(cid, 'typing')
    time.sleep(2)
    help_text = "Los siguientes comandos estan disponibles\n\n\nPor favor, elije un comando o escríbelo usando ''/+comando''\n\n\n"
    bot.send_chat_action(cid, 'typing')
    time.sleep(5)
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text) 



@bot.message_handler(commands=['conversiones'])
def command_image(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Seleccione una opcion para mostrar la conversión", reply_markup=imageSelect1)
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_sticker (cid, 'CAACAgIAAxkBAAIHUWEQdv1ETlqk02PuxIrQdMy0bKz2AAK9AQACFkJrCg6w82V7DpvdIAQ') 
    userStep[cid] = 1 

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text
    if text == 'Petabytes a Terabytes.': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Petabytes a Terabytes.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad")

        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('pt a tb.png', 'rb'))
                       
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /conversiones para consultar otra conversion sobre alguna unidad de almacenamiento")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /definiciones para realizar una consulta sobre las definiciones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    
    elif text == 'Gigabytes a Megabytes.': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Gigabytes a Megabytes.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad")

        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('gb a mb.png', 'rb'))
                       
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /conversiones para consultar otra conversion sobre alguna unidad de almacenamiento")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /definiciones para realizar una consulta sobre las definiciones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Terabytes a Gigabytes.': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Terabytes a Gigabytes.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad")

        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('tb a gb.png', 'rb'))
                       
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /conversiones para consultar otra conversion sobre alguna unidad de almacenamiento")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /definiciones para realizar una consulta sobre las definiciones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Megabytes a Kilobytes.': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Megabytes a Kilobytes.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad")

        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('mb a kb.png', 'rb'))
                      
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /conversiones para consultar otra conversion sobre alguna unidad de almacenamiento")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /definiciones para realizar una consulta sobre las definiciones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Bytes a bits.': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Bytes a bits.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad")

        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Bab.png', 'rb'))
               
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /conversiones para consultar otra conversion sobre alguna unidad de almacenamiento")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /definiciones para realizar una consulta sobre las definiciones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡No!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡No!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡Y no!")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAOVYQtbCrBAdATWpwAB7Y4_kdcRotywAAJpAAPBnGAMTjMSb1IRHIwgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Tienes que usar el teclado predefinido!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Por favor, intentalo de nuevo.")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBOWELZSQEmu4xqPpTgnQv4lxM0Oo1AAK6AANSiZEjLQ0Qg2F3qk0gBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Te estaré vigilando")

@bot.message_handler(commands=['definiciones'])
def command_image(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "Seleccione una opcion para mostrar la conversión", reply_markup=imageSelect2)
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_sticker (cid, 'CAACAgIAAxkBAAIHUWEQdv1ETlqk02PuxIrQdMy0bKz2AAK9AQACFkJrCg6w82V7DpvdIAQ') 
    userStep[cid] = 2

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 2)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text
    if text == 'Definicion de Terabytes': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Definicion de Terabytes")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Terabyte es una unidad de almacenamiento de datos digitales. Es igual a 1024 gigabytes, megabytes 1048576, 1073741824 kilobytes.")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /definiciones para consultar otra definicion sobre alguna unidad de almacenamiento")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /conversiones para realizar una consulta sobre las conversiones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Definicion de Gigabytes': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Definicion de Gigabytes")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Gigabyte es una unidad de almacenamiento de datos digitales. Es igual a 1024 megabytes, kilobytes 1048576 o 1073741824 bytes")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /definiciones para consultar otra definicion sobre alguna unidad de almacenamiento")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /conversiones para realizar una consulta sobre las conversiones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Definicion de Megabytes': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Definicion de Megabytes")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Megabyte es una unidad de almacenamiento de datos digitales. Es igual a 1024 kilobytes o 1,048,576 bytes.")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /definiciones para consultar otra definicion sobre alguna unidad de almacenamiento")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /conversiones para realizar una consulta sobre las conversiones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Definicion de Kilobytes': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Definicion de Kilobytes")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Kilobyte es una unidad de almacenamiento de datos digitales. Es igual a 1024 bytes.")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /definiciones para consultar otra definicion sobre alguna unidad de almacenamiento")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /conversiones para realizar una consulta sobre las conversiones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Definicion de Bytes': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Definicion de Bytes")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Byte es una unidad de información que se utiliza en ingeniería informática. Se refiere a una unidad de memoria direccionable. Su tamaño puede variar dependiendo de la máquina o el lenguaje de la informática. En la mayoría de contextos, un byte equivale a 8 bits (o un octeto). (En 1956, esta unidad fue nombrada por IBM ingeniero Werner Buchholz.)")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /definiciones para consultar otra definicion sobre alguna unidad de almacenamiento")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /conversiones para realizar una consulta sobre las conversiones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  
    elif text == 'Definicion de Bits': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usted ha elejido la opción:")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Definicion de Bits")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Bit es la unidad básica de almacenamiento de información digital. Es un acrónimo de dígito binario. Cada bit de los registros uno de los dos posibles respuestas a una sola pregunta: 0 o 1, sí o no, dentro o fuera. Cuando una base de datos se representa como binario (base 2) números, cada dígito binario es un poco solo.")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /definiciones para consultar otra definicion sobre alguna unidad de almacenamiento")
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Tambien puedes usar el comando /conversiones para realizar una consulta sobre las conversiones de las unidades de almacenamiento")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Y si necesitas ayuda usa el comando /help") 

        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIHk2EQeoklX5QVy2t4CQgmLjs490OxAALSAQACFkJrCgpo79h_0FWBIAQ')
        
        userStep[cid] = 0  

    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡No!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡No!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡Y no!")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAOVYQtbCrBAdATWpwAB7Y4_kdcRotywAAJpAAPBnGAMTjMSb1IRHIwgBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "¡Tienes que usar el teclado predefinido!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Por favor, intentalo de nuevo.")
        bot.send_sticker (cid, 'CAACAgIAAxkBAAIBOWELZSQEmu4xqPpTgnQv4lxM0Oo1AAK6AANSiZEjLQ0Qg2F3qk0gBA')
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Te estaré vigilando")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡No!")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡No!")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, "¡Y no!")
    bot.send_sticker (m.chat.id, 'CAACAgIAAxkBAAO5YQ8PSGtokwxUBV-qzIUoO2nquboAAp8RAAIIoNBJeY4rQ3fKpYkgBA')
    bot.send_message(m.chat.id, "Yo no entiendo la palabra \"" + m.text + "\"\nUsa /start para usar el bot")
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "¡Qué esto no se vuelva a repetir!")
    bot.send_sticker (m.chat.id,'CAACAgIAAxkBAAPdYQthbfLBJlfwsYFoFgsH6_ykG3UAAoQAA0QNzxdaythEmzlA7iAE')
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "¿Entendido?")

bot.infinity_polling()