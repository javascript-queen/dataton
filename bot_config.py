from libraries import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TOKEN = '6552600951:AAGwEcPjo7Z-AwIo5dwARNinrXy6mJ4Bbxk'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Art_Bot:

# -------> Предварительные параметры для запуска
    def __init__(self, token):
        
        # <-------------------------
        self.token = token
        self.bot = TeleBot(self.token)
        
        # <-------------------------
        self.this_directory = os.getcwd() + '\\bot_script'
        
        # <-------------------------
        # data_path = self.this_directory + '\\data'
        
        # if not os.path.exists(data_path):
        #     os.mkdir(storage_path)
        
        # <-------------------------
        self.models = self.this_directory + '\\data\\models'
        # self.model = style.load_model(self.models)
        
        # <-------------------------
        
        storage_path = self.this_directory + '\\data\\photo_storage'
                
        if not os.path.exists(storage_path):
            os.mkdir(storage_path)
    
        self.storage = storage_path
        
        # <------ Создание/введение базовых параметров
        
        self.stages_dict = self.this_directory + '\\stages.json'
        check_stages = os.path.isfile(self.stages_dict)
        
        if not check_stages:
            json_stages = {}
            with open(self.stages_dict, 'w') as outfile:
                json.dump(json_stages, outfile)
                
        else:
            with open(self.stages_dict, 'r') as j:
                json_stages = json.loads(j.read())
            
        self.json_stages = json_stages
        
# -------> Запуск бота для перманентной работы
    def run(self):
        
        # <------ Функция приветствия при команде /start
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            user_id = str(message.from_user.id)
            print(self.json_stages)
            
            self.json_stages[user_id] = {
                                        'state' : 'welcome',
                                        'selfie' : None,
                                        'painting' : None
                                        }
            
            if user_id not in self.json_stages:    
                os.chdir(self.storage)
                os.mkdir(str(user_id))
            
            with open(self.stages_dict, 'w') as outfile:
                json.dump(self.json_stages, outfile)
                
            welcome(self.bot, user_id)

        # <------ Функция принятия команды для готовности скачать изображение
        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            user_id = str(message.from_user.id)
            
            if user_id not in self.json_stages:
                self.bot.send_message(user_id, 'Пожалуйста, нажми /start! Без этого я не смогу начать с тобой диалог!')
                
            else:
                if ((message.text == 'Я хочу сделать селфи в стиле картины!' and self.json_stages[user_id]['state'] == 'welcome') or
                    (message.text == 'Хочу переснять' and self.json_stages[user_id]['state'] == 'sent_painting')):
                    
                    self.json_stages[user_id]['state'] = 'painting'
                    
                    with open(self.stages_dict, 'w') as outfile:
                        json.dump(self.json_stages, outfile)
                        
                    self.bot.send_message(user_id, 'Прекрасно, пришли фото нужной картины!')
                    
                elif ((message.text == 'Да, всё окей' and self.json_stages[user_id]['state'] == 'sent_painting') or
                    (message.text == 'Хочу переснять' and self.json_stages[user_id]['state'] == 'sent_selfie')):
                    
                    self.json_stages[user_id]['state'] = 'selfie'
                    self.json_stages[user_id]['painting'] = 'sent'
                    
                    with open(self.stages_dict, 'w') as outfile:
                        json.dump(self.json_stages, outfile)
                        
                    self.bot.send_message(user_id, 'Прекрасно, пришли своё селфи!')
                    
                elif (message.text == 'Да, всё окей' and self.json_stages[user_id]['state'] == 'sent_selfie'):
                    self.json_stages[user_id]['state'] = 'both_sent'
                    self.json_stages[user_id]['selfie'] = 'sent'
                    
                    with open(self.stages_dict, 'w') as outfile:
                        json.dump(self.json_stages, outfile)

                    self.bot.send_message(user_id, 'Отлично, начинаю обработку!')
                    
        # <------ Функция проверки фото и загрузки
        @self.bot.message_handler(content_types=['photo'])
        def scan_message(message):
            user_id = str(message.from_user.id)

            check_photo(self, user_id, message)
        
        # <------ Вспомогательные функции для отправки сообщений

        def welcome(bot, ident):
            user_markup = types.ReplyKeyboardMarkup(True, True)
            user_markup.row('Я хочу сделать селфи в стиле картины!')

            bot.send_message(ident, 'Привет-привет, ты кто?', reply_markup=user_markup)
        
        def check_photo(self, ident, msg):
            if msg.photo and (self.json_stages[ident]['state'] == 'painting' or self.json_stages[ident]['state'] == 'selfie' or 
                            self.json_stages[ident]['state'] == 'retaking_painting' or self.json_stages[ident]['state'] == 'retaking_selfe'):
                                
                file_info = self.bot.get_file(msg.photo[0].file_id)
                download_file = self.bot.download_file(file_info.file_path)
                
                source_file = self.storage + '\\' + str(ident) + '\\' + str(ident) + '_' + self.json_stages[ident]['state'] + '.' + file_info.file_path.split('.')[-1]
                with open(source_file, 'wb') as new_file:
                    new_file.write(download_file)
                
                new_state = 'sent_' + self.json_stages[ident]['state']
                print(new_state)
                self.json_stages[ident]['state'] = new_state
                
                with open(self.stages_dict, 'w') as outfile:
                    json.dump(self.json_stages, outfile)
                    
                user_markup = types.ReplyKeyboardMarkup(True, True)
                user_markup.row('Да, всё окей')
                user_markup.row('Хочу переснять')

                self.bot.send_message(ident, 'Нормуль получилось или хочешь переснять?', reply_markup=user_markup)

        self.bot.infinity_polling(none_stop=True, interval=0)
        