Feature: Find a conflicts in a professor's schedule

Scenario Outline: User enters a Instructor ID into the program.
	Given a "<Instructor ID, Term, Time>".
	When we make it go.
	Then the output should be "<Professor Conflicts>".

	Examples:
		| Instructor ID, Term, Time			| Professor Conflicts	   |
		| 437247,201610,1200			|['11086 TR 1200 - 1320']| 


