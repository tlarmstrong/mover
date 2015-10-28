Feature: List Students in a Section

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class Number>".
	When the converter is run.
	Then the output should be "<Class List>".

	Examples:
		| Class Number	| Class	List |
		| CS374 		    | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia |
		| CS374.1		    | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia | 
		| cs374.1		    | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia	|
		| cs 374.1		  | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia |
		| cs 374.01		  | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia	|
