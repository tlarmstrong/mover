Feature: Find a conflicts in student's schedule

Scenario Outline: User enters a Banner ID into the program.
	Given a "<Banner ID, Term, Time>".
	When we make it go.
	Then the output should be "<Student Conflicts>".

	Examples:
		| Banner ID, Term, Time		| Student Conflicts	   |
		| 47289,201610,1300		    | ['11241 MWF 1300 - 1350'] |


