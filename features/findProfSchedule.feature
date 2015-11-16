Feature: Find a professor's schedule

Scenario Outline: User enters a Instructor ID into the program.
	Given a "<Instructor ID, Term>".
	When we hit the button.
	Then the output should be "<Professor Schedule>".

	Examples:
		| Instructor ID, Term	| Professor Schedule	   						|
		| 437247,201610			|['11077 W 1500 - 1650', '11086 TR 1200 - 1320']| 
		| 38,201610				|['10773 TR 930 - 1050']						|
		| 9979,201610			|['11081 MWF 1400 - 1450']						|
		| 419266,201610			|['11092 TR 1330 - 1450', '11094 TR 930 - 1050']|
		| 287,201610			|['11241 MWF 1300 - 1350']						|
		| 68002,201610			|['10170 TR 800 - 920']							|
		| 419270,201610			|['11079 MWF 900 - 950']						|
		| 1579,201610			|['10164 MWF 1000 - 1050', '10163 M 1500 - 1650']|
		| 1321,201610			|['10059 TR 800 - 920']							|
		| 47543,201610			|['10161 MWF 800 - 850']						|
		| 1418,201610			|['10765 TR 930 - 1050']						|
		| 16027,201610			|['11089 TR 1500 - 1620']						|

