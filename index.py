from flask import Flask,request,render_template
from trainDataProcess import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


conversation = problemOneData()+problemTwoData()+problemThreeData()+problemFourData()+problemFiveData()+problemSixData()
chatbot = ChatBot("Robot")
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/chat")
def chat():
	question = request.args.get("question")
	print(question)
	return chatbot.get_response(question) 

if __name__ == '__main__':
	app.run("0.0.0.0")
