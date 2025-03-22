import telebot
from config import TOKEN
from logic_ai import get_class

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["photo"]) # указывает, что следующая функция будет обрабатывать сообщения, содержащие фотографии. Это означает, что когда пользователь отправляет изображение, бот вызовет указанную функцию.

def send_class(message):
    file_info = bot.get_file(message.photo[-1].file_id) # пригодится тебе для получения информации о последнем изображении в сообщении. Это нужно, так как Telegram может отправить несколько фотографий в одном сообщении, и здесь берется только последняя.
    
    file_name = file_info.file_path.split('/')[-1] # а так ты сможешь извлечь имя файла из полного пути к файлу, который возвращает Telegram.

    downloaded_file = bot.download_file(file_info.file_path) #Загружает файл по пути, полученному из file_info.

    with open(file_name, 'wb') as new_file: # Открывает новый файл в бинарном режиме записи ('wb'). Этот блок with автоматически закроет файл после завершения работы.
        new_file.write(downloaded_file) #Записывает загруженные данные в новый файл.

    result = get_class(file_name)

    bot.reply_to(message, result)

bot.infinity_polling()