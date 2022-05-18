# Efficient Janitor
`Easy`
__Tags:__ ``Problem Solving, Algorithms, Interviewer Guidelines``


The janitor of a high school is extremely efficient. By the end of each day, all of the school's waste is in plastic bags weighing between 1.01 pounds and 3.00 pounds. All plastic bags are then taken to the trash bins outside. One trip is described as selecting a number of bags which together do not weigh more than 3.00 pounds, dumping them in the outside trash can and returning to the school. Given the number of plastic bags n, and the weights of each bag, determine the minimum number of trips the janitor has to make.

 

Example

n = 5 

weight = [1.01, 1.99, 2.5, 1.5, 1.01]

 

The janitor can carry all plastic bags out in 3 trips: [1.01 + 1.99 , 2.5, 1.5 + 1.01].

 
### Function Description

Complete the function efficientJanitor in the editor below.

 

efficientJanitor has the following parameter(s):

    float weight[n]:  weights of the bags

 

### Returns

    int:  the minimum number of trips required

 

### Constraints

1 ≤ n ≤ 1000

1.01 ≤ weight[i] ≤ 3.0

 

Input Format For Custom Testing
The first line contains an integer, n, the number of elements in weight.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a floating point number that describes weight[i].

Sample Case 0
Sample Case 1
Interviewer Guidelines
Private
Interviewer guidelines are a set of hints and follow up questions to help you guide and evaluate the candidate.

Hint 1
What is the maximum number of bags that can be carried out together?

 

Answer: There can be no more than 2 numbers in a group because the minimum possible sum of 3 numbers can be 1.01 + 1.01 + 1.01 = 3.03, which exceeds 3.

Hint 2
Which values should you compare to get the most efficient pairing?

 

Sort the array and sum the lowest and highest elements that are not yet grouped. At each grouping, increment the trip counter.
