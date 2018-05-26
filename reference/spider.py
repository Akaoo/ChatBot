from bs4 import BeautifulSoup
import requests
import json
import re

def getHtml(url):
	try:
		response = requests.get(url)
		if response.status_code==200:
			return response.text
		else:
			return None
	except Exception as e:
		print(e)

def getOnePaperDetails(url):
	text = getHtml(url)
	soup = BeautifulSoup(text, 'lxml')
	# dataTable[1]: the Qualifications
	# dataTable[2]: timetable for Semester 1
	# dataTable[3]: timetable for Semester 2
	dataTable = soup.find_all('table',attrs = {"cellpadding":0,"border":0,'cellspacing':'2'})
	qualifications = list(filter(lambda i:i!="\n",dataTable[1].children))[1:]
	try:
		semester1 = dataTable[2]
	except IndexError:
		semester1 = []
	try:
		semester2 = dataTable[3]
	except IndexError:
		semester2=[]
	############################get the qualifications datas####################################
	qualifiDic = dict()
	for i in range(0,len(qualifications),2):
		major = qualifications[i].find_all(name="a",text=re.compile("\w+"))[0].string
		requisiteList = re.findall("[A-Z]\w*-?\w+\d*",qualifications[i+1].get_text())
		try:
			preIndex = requisiteList.index('Prerequisites')
		except ValueError:
			preIndex = -1
		try:
			coIndex = requisiteList.index('Co-requisites')
		except ValueError:
			coIndex = -1
		if preIndex!=-1 and coIndex!=-1:		
			preReq = requisiteList[preIndex+1:coIndex]
			coReq = requisiteList[coIndex+1:]
		elif preIndex==-1 and coIndex!=-1:
			coReq = requisiteList[coIndex+1:]
			preReq=[]
		elif preIndex!=-1 and coIndex==-1:
			preReq = requisiteList[preIndex+1:]
			coReq=[]
		elif preIndex==-1 and coIndex==-1:
			preReq=[]
			coReq=[]
		qualifiDic[major] = {"Prerequisites":preReq,'Co-requisites':coReq}
	for key in qualifiDic:
		print(key+":")
		print(qualifiDic[key])
	##########################get the Starting Time###########################################
	timeDic = dict()
	if len(semester2)!=0:
		timeDic["Semester 2"] = list(map(lambda i:i.get_text().strip(),semester2.find_all(name="td",attrs={"width":85})))
	else:
		timeDic["Semester 2"]=[]
	if len(semester1)!=0:
		timeDic["Semester 1"] = list(map(lambda i:i.get_text().strip(),semester1.find_all(name="td",attrs={"width":85})))
	else:
		timeDic["Semester 1"]=[]

	for key in timeDic:
		print(key+":")
		print(timeDic[key])
	return qualifiDic,timeDic

def getAllPapers(text):
	soup = BeautifulSoup(text, 'lxml')
	levels = list(map(lambda i:i.string,soup.find_all(name='td',text=re.compile("Level \d+"))))
	dataDic = dict().fromkeys(levels)
	baseDir = "https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/"
	levelList = soup.find_all('table',attrs = {"cellpadding":1,"border":0})
	# here is we get an list:[['MATH502', 'Algebra and Discrete Mathematics', '15.00',https:/
	# /arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/Details/PaperDetails.aspx?actiontype=2&id=39082&id2=3765],....]
	for i in range(len(levelList)):
		courseInfoList = []
		courseInfo = levelList[i].select(".BackgroundLight")
		for course in courseInfo:
			tempList = course.get_text().strip().split('\n')
			tempList.append(baseDir+course.a.attrs['href'])
			qualifiDic,timeDic = getOnePaperDetails(tempList[-1])
			tempList.append(qualifiDic)
			tempList.append(timeDic)
			courseInfoList.append(tempList)
		dataDic[levels[i]] = courseInfoList
	return dataDic

def getCourse():
	url = {"Analytics":"https://autdev.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/analytics-major",
			"Computational Intelligence":"https://autdev.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/computational-intelligence-major",
			"Computer Science":"https://autdev.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/computer-science-major",
			"Networks and Security":"https://autdev.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/networks-and-security-major",
			"Software Development":"https://autdev.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/software-development-major",
			"IT Service Science":"https://autdev.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/it-service-science-major"}
	resDic = dict()
	for key in url:
		courAndCareer = []
		soup = BeautifulSoup(getHtml(url[key]),'lxml')
		courAndCareer.append(soup.find(name="div",id=re.compile("tab-\d+-1")).get_text().strip())
		careers = list(map(lambda i:i.get_text(),soup.find(name="div",id=re.compile("tab-\d+-2")).find_all(name="li")))
		courAndCareer.append(careers)
		resDic[key] = courAndCareer
	return resDic


if __name__ == '__main__':
	#dic = getAllPapers(getHtml('https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/PaperTable.aspx?id=3765'))
	# dic = {}
	# with open("./info.json",'r') as f:
	# 	dic = json.load(f)
	# print(getCourse("https://www.aut.ac.nz/study/study-options/engineering-computer-and-mathematical-sciences/courses/bachelor-of-computer-and-information-sciences/software-development-major"))
	with open("./courses.json","w") as fp:
		json.dump(getCourse(), fp)

	# with open("./courses.json","r") as fp:
	# 	print(json.load(fp))