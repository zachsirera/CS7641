Instructions for running code for Zach Sirera's submission to Assignment 1 
CS 7641 - Fall 2020

1.	Clone repository here: https://github.com/zachsirera/CS7641
	There are four folders, "income", "income_2", "wine", and "wine_2"
	"income" and "wine" represent the analyses that don't use cross validation
	"income_2" and "wine_2" use cross validation.
	Each classifier is in its own file within its folder


2. 	run "pip3 install -r requirements.txt" to get all necessary libraries
		

3. 	The data parsing, model training, validation, and testing is handled automatically when running "main.py" in each of the four folders.
	When you run "python main.py", it should take a little while but then it will print its results. 
	For the non-cross-validated methods (ie not the "_2" folders) it will print the training time and the mean access time for each classifier followed by a list of five numbers. 
	The cross-validated methods will print just the list of five numbers. 
	These numbers are the final accuracy scores for each classifier over the test data that are used in the report. 


4.	All graph generation is handled in "analyze.py" within each subfolder. 
	Running analyze.py will generate all of the graphs that are used in the report. 
	The data in the analyze.py folders is self-contained. You do not need to run the main.py folders to get it. It was copied and pasted into analyze.py as needed. 
