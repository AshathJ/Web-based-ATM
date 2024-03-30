from flask import Flask , render_template  , request , redirect ,url_for , session
import sqlite3

app = Flask(__name__)

app.secret_key = '123456'

@app.route('/')
def Home():
    #alarm_sound()
    return render_template('home.html')

#===================================================================================================================
@app.route('/Deposit',methods=['GET','POST'])
def Deposit():
    alarm_sound()
    return render_template('drecords.html')

@app.route('/Drecords',methods=['POST','GET'])
def Drecords():
    c=''
    for i in a:
        c= c + str(i)
    if request.method == 'POST':
        c500=int(request.form.get('c500'))
        c1000=int(request.form.get('c1000'))
        c2000=int(request.form.get('c2000'))
        Balance= ATM(c500,c1000,c2000)
        con=sqlite3.connect('atmdatabase.db')
        cur=con.cursor()
        cur.execute("update AZAD set balance = (select balance from AZAD where pin = {})+{} where pin = {}".format(c,Balance,c))
        con.commit()
        alarm_sound()
    return redirect(url_for('generate_otp_route'))


def ATM(c500,c1000,c2000):
    return (c500*500)+(c1000*1000)+(c2000*2000)


#================================================================================================================
@app.route('/Withdrawal')
def Withdrawal():
    alarm_sound()
    return render_template('wrecords.html')

@app.route('/Wrecords',methods=['POST','GET'])
def Wrecords():
    c=''
    for i in a:
        c= c + str(i)
    if request.method == 'POST':
        Balance = request.form.get('amount')
        con=sqlite3.connect('atmdatabase.db')
        cur=con.cursor()
        cur.execute("update AZAD set balance = (select balance from AZAD where pin = {})-{} where pin = {}".format(c,Balance,c))
        con.commit()
        alarm_sound()
    return  redirect(url_for('generate_otp_route'))
    

#=================================================================================================================
@app.route('/Balance')
def Balance():
    c=''
    for i in a:
        c= c + str(i)
    con=sqlite3.connect("atmdatabase.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute('select * from AZAD where pin  = {}'.format(c))
    value=cur.fetchall()
    alarm_sound()
    return render_template('Balance.html',value=value)

#============================================================================================================

@app.route('/Go', methods=['GET', 'POST'])
def Go():
    if request.method == 'POST':
        Go = request.form['destination']
        return redirect(url_for(Go))
    return redirect(url_for('Check'))   

@app.route('/Check')
def Check():
    c=''
    for i in a:
        c= c + str(i)
    con=sqlite3.connect("atmdatabase.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute('select name,accountnumber,pin from AZAD where pin  = {}'.format(c))
    value=cur.fetchone()
    if value :
        session['c']=value['pin']
        return render_template('index.html',value=value)
    else:
        #return redirect(url_for('cancel'))
        return render_template('index.html')



a = []

@app.route('/clear')
def clear():
    a.pop() 
    alarm_sound()
    return render_template('home.html',a=a) #return  'Success' #render_template('home.html')

@app.route('/cancel')
def cancel():
    a.clear()
    alarm_sound()
    return render_template('home.html',a=a) #return  'canceled'



@app.route('/url1')
def url1():
    a.append(1)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url2')
def url2():
    a.append(2)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url3')
def url3():
    a.append(3)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url4')
def url4():
    a.append(4)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url5')
def url5():
    a.append(5)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url6')
def url6():
    a.append(6)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url7')
def url7():
    a.append(7)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url8')
def url8():
    a.append(8)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url9')
def url9():
    a.append(9)
    alarm_sound()
    return render_template('home.html',a=a)

@app.route('/url0')
def url0():
    a.append(0)
    alarm_sound()
    return render_template('home.html',a=a)

#====================================================================================================================

import random
@app.route('/generate-otp')
def generate_otp_route():
    otp = generate_otp()
    return render_template('otp_generated.html', otp=otp)

def generate_otp(length=6):
   # """Generate a numeric OTP of specified length."""     ['4', '5', '7', '2', '7', '1']  ''.join use pannalana string ipdi irukkum
    return '-'.join(random.choices('0123456789', k=length))    #  variable k must important 

#=======================================================================
import time
import winsound

def alarm_sound():
    frequency = 2500   #(2000 HZ)
    duration = 100       #(1000 is 1 mns)
    winsound.Beep(frequency , duration)




#==================================================================================================================
if __name__ == '__main__':
    app.run(debug=True)





