Feature: List who is teaching a Section

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class Number>".
	When we press go.
	Then the output should be "<Prof Name>".

	Examples:
		| Class Number			| Prof Name	   |
		| CS374,201610 		    | Reeves, Brent |
		| 11081,201610	    	| Reeves, Brent | 


