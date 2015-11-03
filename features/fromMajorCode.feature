Feature: Convert a Major Code to a list of Sections

Scenario Outline: User enters a Class Number into the program.
	Given a "<Major Code>".
	When the converter is activated.
	Then the output should be "<Sections>".

	Examples:
		| Major Code  | Sections 		|
	    | CS          | CS has 5 sections, please choose one: CS374.1, CS330.1, CS332.1, CS311.1, CS315.1 |
	    | cs          | CS has 5 sections, please choose one: CS374.1, CS330.1, CS332.1, CS311.1, CS315.1 | 
	    | MATH        | MATH has 4 sections, please choose one: MATH377.1, MATH227.1, MATH187.L1, MATH186.1  |
	    | math        | MATH has 4 sections, please choose one: MATH377.1, MATH227.1, MATH187.L1, MATH186.1  | 
	    | ITC  		  | 11092 | 
	    | itc  		  | 11092 |
	    | CS          | CS has 5 sections, please choose one: CS374.1, CS330.1, CS332.1, CS311.1, CS315.1 | 
	    | IT          | 11094   | 
	    | MATH        | MATH has 4 sections, please choose one: MATH377.1, MATH227.1, MATH187.L1, MATH186.1| 
	    | PSYC  	  | 10773 | 
	    | psyc  	  | 10773 |
	    | GER         | GER has 2 sections, please choose one: GER111.1, GER111.L1  | 
	    | CS          | CS has 5 sections, please choose one: CS374.1, CS330.1, CS332.1, CS311.1, CS315.1| 
	    | MATH        | MATH has 4 sections, please choose one: MATH377.1, MATH227.1, MATH187.L1, MATH186.1 | 
	    | BIBL 		  | 10059 | 
	    | MATH        | MATH has 4 sections, please choose one: MATH377.1, MATH227.1, MATH187.L1, MATH186.1 | 
	    | BCOR        | 10765 | 
	    | CS  		  | CS has 5 sections, please choose one: CS374.1, CS330.1, CS332.1, CS311.1, CS315.1 | 