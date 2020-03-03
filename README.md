# Kiwi.com-Machine-Learning-weekend-solution
This script is a solution of the task for Machine Learning Weekend event which organized by kiwi.com and take place between dates 27th and 29th of October 2017

The code was developed and tested in python  v3.5.3. 

## Short about the method which I have used

After reading raw JSON data from provided API I analyzed collected output(y) values based on given input(x) values from between -100 and 100 and drew a graph.
It was clear from the graph that it's cubic function. So in order to detect function of this graph, we need to detect coefficients of this cubic function. For that Polynomial regression method was chosen. Fortunately, there is a ready library in python. 
After finding the method I have tested with different input and degree and achieved the best result on degree=4 for Polynomial Regression.
