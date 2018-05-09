# coding=utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class SimpleChat():

    def __init__(self):
        self.chatbot = ChatBot('myBot',
                               storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                               logic_adapters=[
                                   {
                                       'import_path': 'chatterbot.logic.BestMatch'
                                   },
                                   {
                                       'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                                       'threshold': 0.6,
                                       'default_response': 'Learning'
                                   }
                               ],
                               input_adapter="chatterbot.input.VariableInputTypeAdapter",
                               output_adapter="chatterbot.output.TerminalAdapter",
                               database_uri='mongodb://admin:admin@127.0.0.1:27017/admin?authMechanism=MONGODB-CR',
                               database='chatbot'
                               )

        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train("chatterbot.corpus.english")

    def get_response(self, info):
        return str(self.chatbot.get_response(info))

if __name__ == '__main__':
    chat = SimpleChat()
    res = chat.get_response('Hi')
    print(res)

self.chatbot.train("chatterbot.corpus.english")
self.chatbot.train([
    "Can you tell me the pre-request of ENSE701",
    "Yes, the Pre-request of ENSE701 is COMP603 or COMP610",
    "No problem, the Pre-request of ENSE701 is COMP603 or COMP610"
])
