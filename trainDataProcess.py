import json

def problemOneData():
	question = "What are the pre-requisites and co-requisites for {}?"
	conversations = []
	with open("./info.json","r") as fp:
		infoDict = json.load(fp)
		for level in infoDict:
			courses = infoDict[level]
			for course in courses:
				conversations.append(question.format(course[0]))
				requisites = course[4]
				answer = ""
				for key in requisites:
					answer += "For "+key
					req = requisites[key]
					if req["Prerequisites"]==[]:
						answer += ",No Pre-requisite papers specified."
					else:
						answer += ","+",".join(req["Prerequisites"])
					if req["Co-requisites"]==[]:
						answer += ",No Co-requisites papers specified."
					else:
						answer += ","+",".join(req["Co-requisites"])
				conversations.append(answer)		
				conversations.append(question.format(course[1]))
				conversations.append(answer)
	return conversations


def problemTwoData():
	question = "If I take a {0} what other papers should I take next for {1}?"
	conversations = []
	with open("./info.json","r") as fp:
		infoDict = json.load(fp)
		for level in infoDict:
			courses = infoDict[level]
			for course in courses:
				curCourseName = course[1]
				requisites = course[4]
				for key in requisites:
					answer = ""
					conversations.append(question.format(key,curCourseName))
					req = requisites[key]
					if req["Co-requisites"]==[]:
						answer += "No Co-requisites papers specified."
					else:
						answer += ",".join(req["Co-requisites"])		
					conversations.append(answer)
	return conversations

def problemThreeData():
	question = "What would be a suggested set of papers for a {0}?"
	conversations = []
	with open("./courses.json","r") as fp:
		infoDict = json.load(fp)
		for major in infoDict:
			conversations.append(question.format(major))
			conversations.append(infoDict[major][0])
	return conversations	


def problemFourData():
	question = "What would be a suggested set of papers for a {0}?"
	conversations = []
	with open("./courses.json","r") as fp:
		infoDict = json.load(fp)
		for major in infoDict:
			careers = infoDict[major][1]
			for career in careers:
				conversations.append(question.format(career))
				conversations.append(infoDict[major][0])
	return conversations	


def problemFiveData():
	resDic = dict()
	with open("./info.json","r") as fp:
		data = json.load(fp) 
		courseId = []
		for key in data:
			# get the course in diff Level
			courses = data[key]
			#course like [id,name,point,url,requisites,timetable]
			for course in courses:
				courseId.append(course[0])

		for cour in courseId:
			resDic[cour] = []

		for cour in courseId:
			for key in data:
				# get the course in diff Level
				courses = data[key]
				#course like [id,name,point,url,requisites,timetable]
				for course in courses:
					requisites = course[4]
					for key in requisites:
						req = requisites[key]
						# print(req)
						pre_req = req["Prerequisites"]
						if cour in pre_req:
							if course[0] not in resDic[cour]:
								resDic[cour].append(course[0])
	conversations = []
	question = "If I have failed {0} what papers can I still take?"
	for courId in resDic:
		conversations.append(question.format(courId))
		if resDic[courId]!=[]:
			conversations.append("You can't take "+",".join(resDic[courId])+" .But else you can!")
		else:
			conversations.append("There are no limits")
	return conversations

def problemSixData():
	conversations = []
	question = "What semesters is {0} offered in 2018"
	with open("./info.json","r") as fp:
		data = json.load(fp) 
		courseId = []
		for key in data:
			# get the course in diff Level
			courses = data[key]
			#course like [id,name,point,url,requisites,timetable]
			for course in courses:
				conversations.append(question.format(course[0]))
				answer = ""
				timetable = course[5]
				if timetable["Semester 2"]==[] and timetable["Semester 1"]==[]:
					answer = "This time No that lesson"
				elif timetable["Semester 2"]!=[] and timetable["Semester 1"]==[]:
					answer = "Semester 2"
				elif timetable["Semester 2"]==[] and timetable["Semester 1"]!=[]:
					answer = "Semester 1"
				elif timetable["Semester 2"]!=[] and timetable["Semester 1"]!=[]:
					answer = "Semester 1 and Semester 2"
				conversations.append(answer)
				conversations.append(question.format(course[1]))
				conversations.append(answer)
	return conversations




# con = problemOneData()+problemTwoData()
# from chatterbot import ChatBot
# chatbot = ChatBot("Ron Obvious")
# from chatterbot.trainers import ListTrainer


# chatbot.set_trainer(ListTrainer)
# chatbot.train(con)


# response = chatbot.get_response("If I take a Graduate Diploma in Science what other papers should I take next for Math604?")
# print(response)