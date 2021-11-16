class classroom:
	def __init__(self, code, day, startTime, endTime, link='', comment=''):
		self.code = code
		self.day = day
		self.startTime = startTime
		self.endTime = endTime
		self.link = link
		self.comment = comment

subjectDict = {
	'CPE327': 'SOFTWARE ENGINEERING',
	'CPE326': 'OPERATING SYSTEMS',
	'CPE315': 'SIGNALS AND LINEAR SYSTEMS',
	'LNG251': 'SPEAKING SKILLS IN THAI',
	'CPE332': 'PROFESSIONAL ISSUES IN COMPUTER ENG.',
	'PRE380': 'ENGINEERING ECONOMICS',
	'GEN241': 'BEAUTY OF LIFE'
}

weekdayColor = {
	'sunday': 'tomato',
	'monday': 'lightyellow',
	'tuesday': 'lightpink',
	'wednesday': 'lightgreen',
	'thursday': 'orange',
	'friday': 'lightblue',
	'saturday': 'magenta'
}

# code, day, startTime, endTime, link='', comment=''
classroomList = []
classroomList.append(classroom('CPE327', 'monday', 10.5, 12.5, link='https://www.google.com/search?q=class1'))
classroomList.append(classroom('CPE326', 'monday', 13.5, 15.5, link='https://www.google.com/search?q=class2'))
classroomList.append(classroom('CPE315', 'tuesday', 8.5, 10.5, link='https://www.google.com/search?q=class3'))
classroomList.append(classroom('CPE315', 'tuesday', 10.5, 12.5, link='https://www.google.com/search?q=class4'))
classroomList.append(classroom('LNG251', 'tuesday', 13.5, 16.5, link='https://www.google.com/search?q=class5'))
classroomList.append(classroom('CPE332', 'tuesday', 18.0, 19.0, link='https://www.google.com/search?q=class6'))
classroomList.append(classroom('CPE326', 'wednesday', 8.5, 10.5, link='https://www.google.com/search?q=class7'))
classroomList.append(classroom('CPE327', 'wednesday', 13.5, 15.5, link='https://www.google.com/search?q=class8'))

# sec b
classroomList.append(classroom('CPE326', 'monday', 15.5, 17.5, link='https://www.google.com/search?q=class9', comment='sec B'))
classroomList.append(classroom('CPE315', 'wednesday', 10.5, 12.5, link='https://www.google.com/search?q=class10', comment='sec B'))
classroomList.append(classroom('CPE327', 'wednesday', 15.5, 17.5, link='https://www.google.com/search?q=class11', comment='sec B'))

# specail class
specail_label = "Specail Class"
specail_link = 'https://google.com'