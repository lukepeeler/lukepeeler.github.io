import matplotlib.pyplot as pyplot
 
# show the input data in a bar chart
# input: states is a list of lists. Each element in states is a list [[state1, number1], [state2, number2], ...]
def plotBarChart(states):

	stateNames = []
	values = []
	for entry in states:
		stateNames.append(entry[0])
		values.append(entry[1])

	width = 0.5
	pyplot.bar(range(len(stateNames)), values, color="blue", align="center")
	pyplot.xticks(range(len(stateNames)), stateNames)
	pyplot.show()