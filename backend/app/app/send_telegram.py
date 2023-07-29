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
import asyncio
from threading import Thread
import threading
import time

async def call_once(context: ContextTypes.DEFAULT_TYPE):
    print(context.chat_data)
    await context.bot.send_message(chat_id=1084622534, text='Hello, how are your')

class TelegramSender(Thread):
    def __init__(self):
        self._bot_id = "6009167376:AAE8vaNZgVNa3gQ-OtjFxmHXQ2AU6vZdAMc"# settings.TELEGRAM_BOT_ID
        # super.__init__("Telegram senders thread")
        threading.Thread.__init__(self)
    
    def send_message(self, message: str) -> None:
        self.process_message(message)

    def run(self) -> None:
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.application = Application.builder().token(self._bot_id).build()
        self.job_queue = self.application.job_queue
        
        self.application.run_polling()

    def process_message(self, message: str) -> None:
        if self.job_queue is not None:
            self.job_queue.run_once(call_once, 1, data=message, chat_id=1084622534)

if __name__ == "__main__":
    tls = TelegramSender()
    tls.start()
    time.sleep(5)
    # tls.send_message("Hello, how are you?")