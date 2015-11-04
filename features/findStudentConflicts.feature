Feature: Find a conflicts in student's schedule

Scenario Outline: User enters a Banner ID into the program.
	Given a "<Banner ID, Term, Time>".
	When we make it go.
	Then the output should be "<Student Conflicts>".

	Examples:
		| Banner ID, Term, Time		| Student Conflicts	   |
		| 47289,201610,1500		| ['11077 W 1500 - 1650']  |
		| 47289,201610,1300		| ['11241 MWF 1300 - 1350']|
		| 269277,201610,800		| ['10170 TR 800 - 920']   |
		| 269277,201610,1400		| ['11081 MWF 1400 - 1450']|
		| 269277,201610,1200		| ['11086 TR 1200 - 1320']|
		| 339212,201610,1000		| ['10164 MWF 1000 - 1050']|
		| 339212,201610,800		| ['10170 TR 800 - 920']   |
		| 339212,201610,1400		| ['11081 MWF 1400 - 1450']|
		| 596651,201610,1500		| ['10163 M 1500 - 1650']  |
		| 596651,201610,1400		| ['11081 MWF 1400 - 1450']|
