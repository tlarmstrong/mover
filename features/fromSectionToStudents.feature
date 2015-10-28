Feature: List Students in a Section

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class_Number>".
	When the converter is run.
	Then the output should be "<Class_List>".

	Examples:
		| Class_Number	| Class_List |
		| CS374 		    | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia |
		| CS374.1		    | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia | 
		| cs374.1		    | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia	|
		| cs 374.1		  | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia |
		| cs 374.01		  | Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia	|
