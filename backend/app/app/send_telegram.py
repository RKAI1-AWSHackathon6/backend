# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print("Start send message to: " + str(update.effective_chat.id))
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# if __name__ == '__main__':
#     application = ApplicationBuilder().token('6009167376:AAE8vaNZgVNa3gQ-OtjFxmHXQ2AU6vZdAMc').build()
    
#     start_handler = CommandHandler('start', start)
#     application.add_handler(start_handler)
    
#     application.run_polling()

# from telegram.ext import ContextTypes, Application

# async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=1225808392, text='One message every minute')

# async def call_once(context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=1084622534, text='Hello, how are your')  #1084622534 1225808392

# application = Application.builder().token('6009167376:AAE8vaNZgVNa3gQ-OtjFxmHXQ2AU6vZdAMc').build()
# job_queue = application.job_queue

# job_queue.run_once(call_once, 1)
# job_queue.run_once(call_once, 1)

# application.run_polling()

# from app.core.config import settings
from telegram.ext import ContextTypes, Application
import telegram
import asyncio
from threading import Thread
import threading
import time
from multiprocessing import Process
import multiprocessing as mp

class TelegramMessage:
    def __init__(self, message: str, chat_id: int):
        self.message = message
        self.chat_id = chat_id

class TelegramSender:
    def __init__(self):
        self._bot_id = "6009167376:AAE8vaNZgVNa3gQ-OtjFxmHXQ2AU6vZdAMc"# settings.TELEGRAM_BOT_ID
        # super.__init__("Telegram senders thread")
        self.outof_process_message_queue_ = mp.Queue()
        self.init_process = Process(target=self.run, args=(self.outof_process_message_queue_,))
        self.init_process.start()
    
    def send_message(self, message: str) -> None:
        #This function was call from original process
        self.outof_process_message_queue_.put(message)

    def fetch_message(self) -> str:
        #This function was call from new process
        while not self._stop_fetch_message:
            try:
                message = self.in_process_message_queue.get(block=True, timeout=0.05)
                self.process_message(message)
            except Exception as e:
                pass
        print("Fetching thread is stoped")
            

    def run(self, process_queue) -> None:
        # Create new thread to processing new thread
        self.thread = threading.Thread(target=self.fetch_message)
        self._stop_fetch_message = False
        self.thread.start()

        # Save the queue from parent thread
        self.in_process_message_queue = process_queue

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.application = Application.builder().token(self._bot_id).build()
        self.job_queue = self.application.job_queue
        
        self.application.run_polling()
        print("Pulling thread is stoped")
        self._stop_fetch_message = True

    def process_message(self, message: str) -> None:
        if self.job_queue is not None:
            self.job_queue.run_once(self.call_once, 1, data=message, chat_id=1084622534)

    async def call_once(self, context: ContextTypes.DEFAULT_TYPE):
        user_data = context.job.data
        if user_data is not None and (user_data, TelegramMessage):
            print("Send message: " + user_data.message + " to " + str(user_data.chat_id))
            await context.bot.send_message(chat_id=user_data.chat_id, text=user_data.message, parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
                

if __name__ == "__main__":
    tls = TelegramSender()
    time.sleep(1)
    tlmessage = TelegramMessage("Hello, *bold* how are you", 1084622534)
    tls.send_message(tlmessage)