Feature: List Students in a Section

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class Number>".
	When the converter is run.
	Then the output should be "<Class List>".

	Examples:
		| Class Number	| Class List |
		| CS374,201610 		    | Ward, Nicole;Williams, Leticia;Prince, Leroy;Ford, Thomas;Clanton, Norma;Davis, John; |
		| 11081,201610	    | Ward, Nicole;Williams, Leticia;Prince, Leroy;Ford, Thomas;Clanton, Norma;Davis, John; | 


