Feature: List Students in a Section

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class Number>".
	When the converter is run.
	Then the output should be "<Class List>".

	Examples:
		| Class Number	 | Class List |
		| CS374,201610   | Ward, Nicole;Williams, Leticia;Prince, Leroy;Ford, Thomas;Clanton, Norma;Davis, John; |
		| 11081,201610	 | Ward, Nicole;Williams, Leticia;Prince, Leroy;Ford, Thomas;Clanton, Norma;Davis, John; | 
		| MATH377,201610 | Williams, Leticia;Prince, Leroy;Clanton, Norma; | 
		| 10170,201610   | Williams, Leticia;Prince, Leroy;Clanton, Norma; | 
		| CS332,201610   | Williams, Leticia;Prince, Leroy;Ford, Thomas;Davis, John; | 
		| 11089,201610   | Clanton, Norma; | 
