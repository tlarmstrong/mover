Feature: Find a professor's schedule

Scenario Outline: User enters a Instructor ID into the program.
	Given a "<Instructor ID, Term>".
	When we hit the button.
	Then the output should be "<Professor Schedule>".

	Examples:
		| Instructor ID, Term		| Professor Schedule	   |
		| 437247,201610			|['11077 W 1500 - 1650', '11086 TR 1200 - 1320']| 


