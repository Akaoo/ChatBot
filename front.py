from flask import Flask,request,render_template
from ChatBot import Chatbot

chatbot = Chatbot()
conversations = ["What are the pre-requisites and co- requisites for ENSE701?",
"No problem, the Pre-requisites of ENSE701 is COMP603 or COMP610",
"If I take a COMP603 what other papers should I take next for Software Development?",
"You should have COMP600, COMP602, INFS600, INFS601, COMP604",

"What would be a suggested set of papers for Software Development?",
'''Year 1: First semester: COMM501, COMP501, COMP502, COMP500
		Second semester: COMP503, INFS500, ENEL504, MATH502 
Year 2: First semester: COMP603, INFS600, INFS601, Elective Paper
		Second semester: COMP600, COMP604, COMP602, Elective Paper
Year 3: First semester: ENSE701, COMP702, COMP721, Elective Paper
		Second semester: COMP719, COMP703, Elective Paper, Elective Paper''',

"Which papers are suitable for a Web developer?",
"ENEL504 Computer Network Principles, ENEL611 Computer Network Applications, COMP721 Web Development are suitable for Web developer.",


"If I have failed COMP503 what papers can I still take? (or how does this restrict what papers I can take)",
"If you failed COMP610, You can not take COMP603",

"What semesters is ENSE701 offered in 2018?",
"Semester 1 and Semester 2"
]
chatbot.train(conversations)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/response',methods=['POST'])
def response():
	response = chatbot.response(request.form["quesions"])
	return render_template("index.html",**locals())

if __name__ == '__main__':
	app.run("0.0.0.0",port=80,debug=True)