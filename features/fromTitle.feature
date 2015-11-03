Feature: Convert a Title to a CRN

Scenario Outline: User enters a Class Number into the program.
	Given a "<Title>".
	When the converter is activated.
	Then the output should be "<CRN>".

	Examples:
		| Title						  | CRN   |
	    | Software Engineering        | 11081 | 
	    | Discrete Mathematics        | 10164 | 
	    | Managing Technical Projects | 11092 | 
	    | Mobile Computing I          | 11089 | 
	    | Web Technologies            | 11094 | 
	    | Statistical Methods I       | 10170 | 
	    | Introduction to Psychology  | 10773 | 
	    | Elementary German I         | 11241 | 
	    | Contest Programming         | 11077 | 
	    | Calculus II                 | 10161 | 
	    | Message of the Old Testament| 10059 | 
	    | Calculus Computer Lab       | 10163 | 
	    | The Search for Meaning      | 10765 | 
	    | Human-Computer Interaction  | 11086 | 
	    | human-computer interaction  | 11086 |