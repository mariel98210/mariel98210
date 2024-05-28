import statistics
import scipy.stats as stats
import matplotlib.pyplot as plt

def get_input():
	dataset = []
	if choice1 == 1:
		print("Please input your dataset. It must have scale as the level of measurement.")
		

def centralTendency():



#START HERE
print("""
						-----Welcome to my program-----
	[insert name of program] is here to help you with your common statistical problems!
	It showcases basic descriptive and inferential statistical computations
	and is quite simple to use (if you are unaware of Microsoft Excel ;p)
	Prepare your data and enjoy!
""")

while True:
	# choices = {'A':'Mean', 'B':'Median', 'C':'Mode', 'D':'Standard Deviation', 'E':'Variance', 'F':'Range', 'G':'IQR (Inter-Quartile Range)', }
	try:
		print("Enter your data first.")
		choice1 = input("Do you want to:\n1. Input it it right here, right now; or\n2. Import it from an Excel Sheet?")
		data = get_input(choice1)

	print("""
Please enter an option.
	For Measures of Central Tendency:
		A. Mean
		B. Median
		C. Mode
	For Measures of Variability:
		D. Standard Deviation
		E. Variance
		F. Range
		G. IQR (Inter-Quartile Range)
	For Measures of Error/Difference:
		G. Percentage Error
		H. Percentage Difference
	For Measures of Shape and Skewness:
		I. Skewness
		J. Kurtosis
	For Measure of Relation:
		I. Pearson Correlation
	For Hypotheses-Testing:
		J. Significant Difference
	For Graph Visualization:
		K. Histogram
		L. Pie Chart
		M. Bar Plot
		N. Scatter Plot
""") #{choices['A']}

	try:
		choice2 = input(">>> ")
		if choice2 == A or choice2 == B or choice2 == C:
			centralTendency()