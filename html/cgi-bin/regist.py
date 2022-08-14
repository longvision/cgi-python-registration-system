#!/usr/bin/env python


header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/process.py'


formhtml = '''<HTML>
<HEAD>
<TITLE>Registration Form</TITLE>
</HEAD>
  Registration Form
  <form action="/cgi-bin/process.py" method=GET>
  Name: <input type=text name=name value="" size=23>
  <br>
  Email: <input type=text name=email value="" size=23>

    <input type=submit >        
    <input type=reset >
  </form>
</BODY>
</HTML>
'''


def showForm():

    print(header + formhtml)


def process():

    showForm()


if __name__ == '__main__':
    process()
