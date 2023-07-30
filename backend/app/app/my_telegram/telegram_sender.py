from app.core.config import settings
from telegram.ext import ContextTypes, Application
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
        self._bot_id = settings.TELEGRAM_BOT_ID
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
            await context.bot.send_message(chat_id=user_data.chat_id, text=user_data.message)
                
        # print("Send message: " + context.)
        # await context.bot.send_message(chat_id=1084622534, text='Hello, how are your')

if __name__ == "__main__":
    tls = TelegramSender()
    time.sleep(1)
    tlmessage = TelegramMessage("Hello, how are you?", 1084622534)
    tls.send_message(tlmessage)