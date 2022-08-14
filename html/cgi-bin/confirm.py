#!/usr/bin/env python

import cgi
from datetime import datetime
import pymysql
import smtplib

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


informationIncorrect = '''
<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >
<TR VALIGN=TOP>
<TD>
<pre>
So, The Information Is Incorrect.

       <a href="/cgi-bin/regist.py">Please Registration Again</a>

       <a href="regist.html">Back To Top</a>
</pre>
</TD>
</TR>

</TABLE>
'''

success = '''<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >
<TR VALIGN=TOP>
<TD>
<pre>
Registration Successful

     Thanks
</pre>
</TD>
</TR>

</TABLE>
'''


def getEmailAndSendSMS(msg, name):
    
        db = pymysql.connect(host='127.0.0.1',port=3306,  db='cs531', passwd='1234', user='root')
        cursor = db.cursor()
      
        sql = """SELECT * FROM users where user_name = '%s'""" % (name)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                email = row[2]
            
            # this is the your email app passqord you need to change to use the SMS feature.
            token = ''
            gmail_user = 'example@gmail.com'
            gmail_password = token
            sent_from = gmail_user
            to = [email]
            subject = msg
            body = '%s\n\n- Thank you' % msg
            email_text = \
                """From: %s
                To: %s
                Subject: %s
                %s
                """ % (sent_from, ", ".join(to), subject, body)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.quit()
        
            # Commit your changes in the database
            db.commit()
            print('<h5>Thank you for your registration, a SMS was sent to your email!</h5>')
        except:
            print ("<h1>Error: unable to send thank you SMS message</h1>")
            # Rollback in case there is any error
            db.rollback()

        # disconnect from server
        db.close()
    

def showFormAndSave(confirm, name, email):
    if confirm == 'yes':
       
        db = pymysql.connect(host='127.0.0.1',port=3306,  db='cs531', passwd='1234', user='root')
        cursor = db.cursor()
        time = datetime.now()
        sql = """INSERT INTO users(user_name, user_email, submission_date) VALUES ('%s', '%s', '%s')""" % (name, email, time)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
            print(header + success)
        except:
            print(name, email)
            # Rollback in case there is any error
            db.rollback()

        # disconnect from server
        db.close()

    else:
        print(header + informationIncorrect)
    

def process():
    name =''
    email = ''
    confirm = ''
    form = cgi.FieldStorage()

    if 'name' in form:
        name = form['name'].value
    if 'email' in form:
        email = form['email'].value
    if 'confirm' in form:
        confirm = form['confirm'].value

    showFormAndSave(confirm, name, email)
    getEmailAndSendSMS('Thank you', name)


if __name__ == '__main__':
    process()
