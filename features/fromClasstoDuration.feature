Feature: Convert a CRN to a Class Title

Scenario Outline: User enters a Class Number into the program.
	Given a "<CRN>".
	When we scream.
	Then the output should be "<Days, Duration, Hours x #Days>".

	Examples:
	| CRN	  | Days, Duration, Hours x #Days	                        |
        | 11081   | ['Days: MWF, Duration: 50 x 3']     |
        | 10164   | ['Days: MWF, Duration: 50 x 3']     |
        | 11092   | ['Days: TR, Duration: 80 x 2']      |
        | 11089   | ['Days: TR, Duration: 80 x 2']      |
        | 11094   | ['Days: TR, Duration: 80 x 2']      |
        | 10170   | ['Days: TR, Duration: 80 x 2']      |
        | 10773   | ['Days: TR, Duration: 80 x 2']      |
        | 11241   | ['Days: MWF, Duration: 50 x 3']     |
        | 11077   | ['Days: W, Duration: 50 x 1']       |
        | 10161   | ['Days: MWF, Duration: 50 x 3']     |
        | 10059   | ['Days: TR, Duration: 80 x 2']      |
        | 10163   | ['Days: M, Duration: 50 x 1']       |
        | 10765   | ['Days: TR, Duration: 80 x 2']      |
        | 11086   | ['Days: TR, Duration: 80 x 2']      |