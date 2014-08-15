#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable(display=1, logdir='~')

print 'Content-type: text/html'
print
print '<html>'
print "<head><title>Dick Dastardly's Webpage</title></head>"
print '<body>'

print '<font face="Comic Sans MS">'
print '<h1>WELCOME TO MY WEBPAGE</h1>'
print '<p/><center><img src="head.gif" />'
print '<p/><img src="flames1.gif" />'
print '<p/><img src="flames1.gif" />'
print '<p/><img src="flames1.gif" />'
print '<p/>My calcul8or (lol)'
print '<p/><form class="well" action="mycalc.cgi" method="post">'
print '<p/><label>Password:</label><input type="text" name="expr" size="30" />'
print '<p/><input type="submit" value="Submit" class="btn-primary" />'

form = cgi.FieldStorage()
if 'expr' in form:
    result = eval(form['expr'].value)
    print '<p/> {}'.format(result)

    print '<p/><img src="meanmachine.gif" /><img src="meanmachine.gif" /><img src="meanmachine.gif" />'
    print '</font>'
    print '</body>'
    print '</html>'
