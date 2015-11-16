Feature: Find a conflicts in student's schedule

Scenario Outline: User enters a Banner ID into the program.
	Given a "<Banner ID, Term, Time>".
	When we make it go.
	Then the output should be "<Student Conflicts>".

	Examples:
		| Banner ID, Term, Time		| Student Conflicts	   |
		| 47289,201610,TR,930		| ['New time: TR 930 - 1050', 'Conflict: 10773 TR 930 - 1050']  |
		| 47289,201610,TR,900		| ['New time: TR 900 - 1020', 'Conflict: 10773 TR 930 - 1050']  |
		| 47289,201610,MWF,1500		| ['New time: MWF 1500 - 1550', 'Conflict: 11077 W 1500 - 1650']  |
		| 47289,201610,MWF,1530		| ['New time: MWF 1530 - 1580', 'Conflict: 11077 W 1500 - 1650']  |
		| 47289,201610,W,1300		| ['New time: W 1300 - 1550', 'Conflict: 11077 W 1500 - 1650', 'Conflict: 11241 MWF 1300 - 1350']  |
		| 47289,201610,M,1400		| ['New time: M 1400 - 1650', 'Conflict: 11081 MWF 1400 - 1450']|
		| 47289,201610,M,1430		| ['New time: M 1430 - 1680', 'Conflict: 11081 MWF 1400 - 1450']|
		| 47289,201610,MWF,1300		| ['New time: MWF 1300 - 1350', 'Conflict: 11241 MWF 1300 - 1350'] |
		| 47289,201610,TR,1330		| ['New time: TR 1330 - 1450', 'Conflict: 11092 TR 1330 - 1450'] |
		| 47289,201610,TR,1300		| ['New time: TR 1300 - 1420', 'Conflict: 11092 TR 1330 - 1450']|
		| 47289,201610,MWF,1300		| ['New time: MWF 1300 - 1350', 'Conflict: 11241 MWF 1300 - 1350']|
		| 269277,201610,TR,800		| ['New time: TR 800 - 920', 'Conflict: 10170 TR 800 - 920']   |
		| 269277,201610,TR,900		| ['New time: TR 900 - 1020', 'Conflict: 10170 TR 800 - 920']  |
		| 269277,201610,MWF,900		| ['New time: MWF 900 - 950', 'Conflict: 11079 MWF 900 - 950']  |
		| 269277,201610,M,1400		| ['New time: M 1400 - 1650', 'Conflict: 11081 MWF 1400 - 1450']|
		| 269277,201610,TR,1200		| ['New time: TR 1200 - 1320', 'Conflict: 11086 TR 1200 - 1320']|
		| 269277,201610,W,1200		| ['Conflict: None']|
		| 339212,201610,MWF,1000	| ['New time: MWF 1000 - 1050', 'Conflict: 10164 MWF 1000 - 1050']|
		| 339212,201610,TR,800		| ['New time: TR 800 - 920', 'Conflict: 10170 TR 800 - 920']   |
		| 339212,201610,TR,900		| ['New time: TR 900 - 1020', 'Conflict: 10170 TR 800 - 920']  |
		| 339212,201610,MWF,900		| ['New time: MWF 900 - 950', 'Conflict: 11079 MWF 900 - 950']  |
		| 339212,201610,TR,1400		| ['Conflict: None']|
		| 339212,201610,MWF,1400	| ['New time: MWF 1400 - 1450', 'Conflict: 11081 MWF 1400 - 1450']|
		| 596651,201610,TR,800		| ['New time: TR 800 - 920', 'Conflict: 10059 TR 800 - 920']   |
		| 596651,201610,M,800		| ['New time: M 800 - 1050', 'Conflict: 10161 MWF 800 - 850']   |
		| 596651,201610,TR,800		| ['New time: TR 800 - 920', 'Conflict: 10059 TR 800 - 920']  |
		| 596651,201610,W,800		| ['New time: W 800 - 1050', 'Conflict: 10161 MWF 800 - 850']  |
		| 596651,201610,W,1500		| ['Conflict: None']  |
		| 596651,201610,M,1500		| ['New time: M 1500 - 1750', 'Conflict: 10163 M 1500 - 1650']  |
		| 596651,201610,TR,930		| ['New time: TR 930 - 1050', 'Conflict: 10765 TR 930 - 1050']  |
		| 596651,201610,MWF,900		| ['New time: MWF 900 - 950', 'Conflict: 11079 MWF 900 - 950']  |
		| 596651,201610,TR,900		| ['New time: TR 900 - 1020', 'Conflict: 10059 TR 800 - 920', 'Conflict: 10765 TR 930 - 1050']  |
		| 596651,201610,MWF,900		| ['New time: MWF 900 - 950', 'Conflict: 11079 MWF 900 - 950']  |
		| 596651,201610,W,1400		| ['New time: W 1400 - 1650', 'Conflict: 11081 MWF 1400 - 1450']|



