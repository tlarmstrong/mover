Feature: Find a conflicts in a professor's schedule

Scenario Outline: User enters a Instructor ID into the program.
	Given a "<Instructor ID, Term, Time>".
	When we make it go.
	Then the output should be "<Professor Conflicts>".

	Examples:
		| Instructor ID, Term, Time		| Professor Conflicts	     |
		| 437247,201610,1200			|['11086 TR 1200 - 1320']    |
		| 38,201610,930			        |['10773 TR 930 - 1050']     |
		| 437247,201610,1500			|['11077 W 1500 - 1650']     |
		| 437247,201610,1200			|['11086 TR 1200 - 1320']    |
		| 1321,201610,800			|['10059 TR 800 - 920']      |
		| 47543,201610,800			|['10161 MWF 800 - 850']     |
