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
		| 9979,201610,1400			|['11081 MWF 1400 - 1450']   |
		| 419266,201610,1330			|['11092 TR 1330 - 1450']    |
		| 287,201610,1300			|['11320 MWF 1300 - 1350']   |
		| 68002,201610,800			|['10170 MWF 800 - 920']     |
		| 419270,201610,900			|['11079 MWF 900 - 950']     |
		| 437247,201610,1200			|['11086 TR 1200 - 1320']    |
		| 1579,201610,1000			|['10164 MWF 1000 - 1050']   |
		| 1321,201610,800			|['10059 TR 800 - 920']      |
		| 47543,201610,800			|['10161 MWF 800 - 850']     |
