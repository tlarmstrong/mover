#!/usr/bin/env python

#import pymysql
import cgi
import mMain

print "Content-Type: text/html"
print
print """
    <TITLE>CGI script ! Python</TITLE>
    <H1>This is my first CGI script</H1>
    Hello, world!
"""

mMain.main()



