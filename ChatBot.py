from chatterbot import ChatBot

class Chatbot(object):
	def __init__(self):
		super(Chatbot, self).__init__()
		self.bot = ChatBot(
		    "ChatBot",
		    storage_adapter="chatterbot.storage.SQLStorageAdapter",
		    logic_adapters=[
		        "chatterbot.logic.BestMatch"
		    ],
		    trainer='chatterbot.trainers.ListTrainer',
		    database="../database.db"
		)

	def train(self,conversations):
		self.bot.train(conversations)

	def response(self,question):
		return self.bot.get_response(question)


