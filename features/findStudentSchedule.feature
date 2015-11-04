Feature: Find a student's schedule

Scenario Outline: User enters a Banner ID into the program.
	Given a "<Banner ID and Term>".
	When we hit the button.
	Then the output should be "<Student Schedule>".

	Examples:
		| Banner ID and Term	    | Student Schedule	   										|
		| 47289,201610		    | ['11077 W 1500 - 1650', '11081 MWF 1400 - 1450', '11092 TR 1330 - 1450', '11241 MWF 1300 - 1350'] |
		| 269277,201610		    | ['10170 TR 800 - 920', '11079 MWF 900 - 950', '11081 MWF 1400 - 1450', '11086 TR 1200 - 1320']    |
		| 3912,201610		    | ['10164 MWF 1000 - 1050', '10170 MWF 800 - 920', '11079 MWF 900 - 950', '11081 MWF 1400 - 1450']  |
		| 814483,201610		    | ['10164 MWF 1000 - 1050', '10179 MWF 900 - 950', '11081 MWF 1400 - 1450', '11092 TR 1330 - 1450'] |
		




