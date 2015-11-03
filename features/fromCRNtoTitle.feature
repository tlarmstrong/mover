Feature: Convert a CRN to a Class Title

Scenario Outline: User enters a Class Number into the program.
	Given a "<CRN>".
	When the converter is activated.
	Then the output should be "<Class Title>".

	Examples:
	| CRN	  | Class Title	|
        | 11081   | CS374.1: Software Engineering           |
        | 10164   | MATH227.1: Discrete Mathematics         |
        | 11092   | ITC460.1: Managing Technical Projects   |
        | 11089   | CS315.1: Mobile Computing I             |
        | 11094   | IT225.1: Web Technologies               |
        | 10170   | MATH377.1: Statistical Methods I        |
        | 10773   | PSYC120.1: Introduction to Psychology   |
        | 11241   | GER111.1: Elementary German I           |
        | 11077   | CS311.1: Contest Programming            |
        | 10161   | MATH186.1: Calculus II                  |
        | 10059   | BIBL211.10: Message of the Old Testament |
        | 10163   | MATH187.L1: Calculus Computer Lab        |
        | 10765   | BCOR310.1: The Search for Meaning       |
        | 11086   | CS330.1: Human-Computer Interaction     |