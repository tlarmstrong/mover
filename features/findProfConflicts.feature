Feature: Find a conflicts in a professor's schedule

Scenario Outline: User enters a Instructor ID into the program.
	Given a "<Instructor ID, Term, Time>".
	When we make it go.
	Then the output should be "<Professor Conflicts>".

	Examples:
		| Instructor ID, Term, Time		| Professor Conflicts	     |
		| 437247,201610,TR,1200			|['New time: TR 1200 - 1320', 'Conflict: 11086 TR 1200 - 1320']    |
		| 437247,201610,TR,1230			|['New time: TR 1230 - 1350', 'Conflict: 11086 TR 1200 - 1320']    |
		| 437247,201610,MWF,1200		|['Conflict: None']    				 |
		| 38,201610,TR,900			    |['New time: TR 900 - 1020', 'Conflict: 10773 TR 930 - 1050']     |
		| 437247,201610,W,1500			|['New time: W 1500 - 1750', 'Conflict: 11077 W 1500 - 1650']     |
		| 437247,201610,W,1530			|['New time: W 1530 - 1780', 'Conflict: 11077 W 1500 - 1650']     |
		| 437247,201610,M,1500			|['Conflict: None']     				 |
		| 9979,201610,TR,1400			|['Conflict: None']   				 |
		| 9979,201610,MWF,1400			|['New time: MWF 1400 - 1450', 'Conflict: 11081 MWF 1400 - 1450']   |
		| 9979,201610,MWF,1430			|['New time: MWF 1430 - 1480', 'Conflict: 11081 MWF 1400 - 1450']   |
		| 419266,201610,TR,1330			|['New time: TR 1330 - 1450', 'Conflict: 11092 TR 1330 - 1450']    |
		| 419266,201610,TR,1300			|['New time: TR 1300 - 1420', 'Conflict: 11092 TR 1330 - 1450']    |
		| 287,201610,M,1300				|['New time: M 1300 - 1550', 'Conflict: 11241 MWF 1300 - 1350']   |
		| 287,201610,M,1330				|['New time: M 1330 - 1580', 'Conflict: 11241 MWF 1300 - 1350']   |
		| 68002,201610,TR,800			|['New time: TR 800 - 920', 'Conflict: 10170 TR 800 - 920']      |
		| 68002,201610,TR,830			|['New time: TR 830 - 950', 'Conflict: 10170 TR 800 - 920']      |
		| 419270,201610,MWF,900			|['New time: MWF 900 - 950', 'Conflict: 11079 MWF 900 - 950']     |
		| 419270,201610,MWF,1000		|['Conflict: None']     |
		| 437247,201610,MWF,1200		|['Conflict: None']    				 |
		| 1579,201610,W,1000			|['New time: W 1000 - 1250', 'Conflict: 10164 MWF 1000 - 1050']   |
		| 1579,201610,W,1030			|['New time: W 1030 - 1280', 'Conflict: 10164 MWF 1000 - 1050']   |
		| 1321,201610,TR,800			|['New time: TR 800 - 920', 'Conflict: 10059 TR 800 - 920']      |
		| 1321,201610,TR,900			|['New time: TR 900 - 1020', 'Conflict: 10059 TR 800 - 920']      |
		| 47543,201610,M,800			|['New time: M 800 - 1050', 'Conflict: 10161 MWF 800 - 850']     |
		| 47543,201610,M,830			|['New time: M 830 - 1080', 'Conflict: 10161 MWF 800 - 850']     |
