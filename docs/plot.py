import matplotlib.pyplot as pyplot
 
# show the input data in a bar chart
# input: states is a list of lists. Each element in states is a list [[state1, number1], [state2, number2], ...]
def plotBarChart(states):

	stateNames = []
	values = []
	for entry in states:
		stateNames.append(entry[0])
		values.append(entry[1])

	pyplot.bar(range(len(stateNames)), values, color="blue", align="center")
	pyplot.xticks(range(len(stateNames)), stateNames)
	pyplot.show()



# show the input data in a pie chart
# input: counts is a list of integers [count1, count2, count3]. 
#        count1 is the number of students who take both Python and Java
#        count2 is the number of students who take only Python
#        count3 is the number of students who take only Java
def plotPieChart(counts):
	pieLabels = ["Both Python and Java", "Only Python", "Only Java"]
	pyplot.pie(counts, labels=pieLabels, autopct='%.1f%%')
	pyplot.show()