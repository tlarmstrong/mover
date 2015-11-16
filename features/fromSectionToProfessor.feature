Feature: List who is teaching a Section

Scenario Outline: User enters a Class Number into the program.
	Given a "<Class Number>".
	When we press go.
	Then the output should be "<Prof Name>".

	Examples:
		| Class Number				| Prof Name	   |
		| CS374,201610 		        | Reeves, Brent    |
		| 11081,201610	    		| Reeves, Brent    |
		| PSYC120,201610	    	| Beck, Richard    |
		| 10773,201610	    		| Beck, Richard    |
		| CS311,201610	    		| Prather, James   |
		| 11077,201610	    		| Prather, James   |
		| ITC460,201610	    		| Byrd, Robert     |
		| 11092,201610	    		| Byrd, Robert     |
		| MATH377,201610	    	| Riggs, Mark      |
		| 10170,201610	    		| Riggs, Mark      |
		| CS332,201610	    		| Homer, John      |
		| 11079,201610	    		| Homer, John      |
		| MATH227,201610	    	| Hendricks, Thomas|
		| 10164,201610	    		| Hendricks, Thomas|
		| BIBL211,201610    		| Willis, John     |
		| 10059,201610	    		| Willis, John     |
		| MATH186,201610    		| Karabegov, Alexander     |
		| 10161,201610	    		| Karabegov, Alexander     |
