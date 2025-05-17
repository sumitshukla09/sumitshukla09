*** Settings ***

Documentation	 Todays sessin is about collections


Library		 Collections	


*** Variables ***
${a}	67
${b}	87
${str}	Hello 

@{list1}	Hello	vvdn	tech	manesar		sector 8


&{dict1}	name= vivek	age=23		mobile=7860752096

@{list2}		sector 2	manesar		tech 	vvdn	hello

*** Test Cases ***

TC_001
	  [Documentation]	 this tc will do something
	[Tags]		
	Keyword		Values 
TC_002
	[Docs]		
	[Tags]
	GET_IP		ifonfig

*** keywords ***

Get_IP

	