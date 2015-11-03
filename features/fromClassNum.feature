Feature: Convert a Class Number to a CRN

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class Number>".
	When the converter is activated.
	Then the output should be "<CRN>".

	Examples:
		| Class Number	| CRN	|
		| CS374 		| 11081 |
		| CS374.1		| 11081	| 
		| cs374.1		| 11081	|
		| cs 374.1		| 11081	|
		| cs 374.01		| 11081	|
		| MATH 227		| 10164	| 
		| ITC460		| 11092	| 
		| CS315		 	| 11089	| 
		| IT225		 	| 11094	| 
		| MATH377		| 10170	| 
		| PSYC120		| 10773	|
		| GER111		| GER111 has 2 sections, please choose one: GER111.1, GER111.L1 | 
		| GER111.L1		| 11320	| 
		| CS311 		| 11077	| 
		| MATH186	 	| 10161	| 
		| BIBL211		| 10059	| 
		| MATH187		| 10163	| 
		| BCOR310		| 10765	| 
		| BCOR310.01	| 10765	|
		| bcor310.1		| 10765	|
		| CS330			| 11086	| 
		| cs330			| 11086	|
		| cs 330		| 11086	|


