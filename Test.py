from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

Flag = 1
while Flag == 1 :
    answer = "Good morning!"
    chatrespone = chatbot.get_response(answer)
    print(chatrespone)
    yn =  input("is the answer correct ? 1 for yes 2 for no")
    if yn == 2 :
        trainanswer = input("What shoule be the right answer")
        chatbot.train(answer, "Bounjour!")
# Get a response to an input statement