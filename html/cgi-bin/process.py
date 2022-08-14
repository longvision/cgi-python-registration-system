#!/usr/bin/env python


import cgi
import os


header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/confirm.py'

errhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''


def showError(error_str):
    print(header + errhtml % (error_str))


formhtml = '''<HTML>

Registration Form
<form method=POST action=/cgi-bin/confirm.py>

<table align=center datasrc="#xmlRegData" border=2>
<tr>
<td> Name:</td>
<td><input type=text name=name value="%s" size=23></td>
</tr>
<tr>
<td>E-mail:</td>
<td><input type=text name=email value="%s" size=23></td>
</tr>
</table>

Is this information correct ?

<input type=radio name='confirm' value='yes'> YES   
<input type=radio name='confirm' value='no' checked> NO 

<input type=submit value=Submit>     
<input type=reset value=Reset>


</form>
</HTML>
'''


def showForm(name, email):

    print(header + formhtml % (name, email))


def process():
    error = ''
    form = cgi.FieldStorage()
    if 'name' in form:
        name = form['name'].value
    else:
        name = 'NONE'
    if 'email' in form:
        email = form['email'].value
    else:
        email = 'NONE'

    if not error:
        showForm(name, email)

    else:
        showError('Error: Please enter correct information')


if __name__ == '__main__':
    process()
