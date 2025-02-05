def before_login_page():                                                               # 1st page
    import time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    print("""
        WELCOME TO NET BANKING
        ======================
        1. Login
        2. Register
        3. Exit""")

    print()
    op1 = int(input('Select from the above options: '))
    print()

    if op1 == 1:
        login()

    if op1 == 2:
        reg()
        before_login_page()

    if op1 == 3:
        exit()    

def reg():
    print('~ LOGIN CREDENTIALS ~\n')
    username = input('Create username: ')
    password = input('Create password: ')

    cur.execute("select *from user_credentials")
    users = dict(cur.fetchall())
    if username in users:
        print('Username already exists! Please login.')
        print()
        before_login_page()
        return
    cur.execute("insert into user_credentials values(%s,%s)",(username,password))

    print('\n~ PROFILE DETAILS ~\n')
    AC_no = input('Enter your bank account number: ')
    phone_no = input('Enter your phone no: ')
    email = input('Enter your email: ')
    aadhar_no = input('Enter your aadhar no: ')
    dob = input('Enter your birth date(YYYY-MM-DD): ')
    address = input('Enter your residential address: ')

    print('\n~ TRANSACTION DETAILS ~\n')
    t_passwd = input('Create transaction password: ')

    cur.execute("insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s)",(AC_no,username,phone_no,email,aadhar_no,dob,address,t_passwd))

    mycon.commit()
    
    print()
    print('Registration successful, account created!')

def login():
    global username
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    cur.execute("select *from user_credentials")
    users = dict(cur.fetchall())
    
    if username in users and users[username]==password:
        print()
        print('Login successful!')
        after_login_page()

    else:
        print()
        print('Invalid username or password!. Please try again.')
        before_login_page()

def after_login_page():                                                                # 2nd page  
    print()
    print('\t      HI',username.upper(),"""WELCOME TO YOUR PTL BANK PORTAL
        =======================================================================
        1. Accounts
        2. View profile
        3. Fund transfer
        4. Go to sign in page
        5. Exit""")
    print()

    op2 = int(input('Select from the above options: '))

    if op2 == 1:                                                                               # 1st option of op2
        accounts()

    elif op2 == 2:                                                                             # 2nd option of op2
        q5 = ('select *from customer_details where username= %(s)s')
        d5 = {'s':username}
        cur.execute(q5,d5)
        b = cur.fetchall()
        print()
        print('Your profile details:')
        print()
        print('AC_no                ',b[0][0])
        print('username             ',b[0][1])
        print('phone                ',b[0][2])
        print('email                ',b[0][3])
        print('aadhar no            ',b[0][4])
        print('DOB                  ',b[0][5])
        print('address              ',b[0][6])
        print()

        c = input('Do you need to go back?(y/n): ')
        if c == 'y':
            after_login_page()
        else:
            pass

    elif op2 == 3:                                                                             # 3rd option of op2
        fund_transfer()

    elif op2 == 4:                                                                             # 4th option of op2
        before_login_page()

    elif op2 == 5:                                                                             # 5th option of op2
        exit()

def accounts():                                                                        # 3rd page
    print('''
        1. Savings account
        2. Loan account
        3. Go back
        ''')
    op3 = int(input('Select an option: '))
    print()
            
    if op3 == 1:                                                                            # first options of op3
        q1 = ("select ac_no from customer_details where username = %(s)s")
        d1 = {'s' : username}
        cur.execute(q1,d1)
        temp1 = cur.fetchall()                                                   # stored as tuple inside a list
        for i in temp1[0]:                                                       # changing temp1 to str format 
            x1 = i

        q2 = ("select *from sav_account where ac_no = %(s)s")
        d2 = {'s' : x1}
        cur.execute(q2,d2)                                                
        a = cur.fetchall()
        print('AC no                ',a[0][5])
        print('Account              ',a[0][0])
        print('account type         ',a[0][1])
        print('credit bal           ',a[0][2])
        print('debit bal            ',a[0][3])
        print('book bal             ',a[0][4])
        print()

        v1 = input('Do you need to go back?(y/n): ')
        if v1 == 'y':
            accounts()
        else:
            pass

    elif op3 == 2:                                                                          # second option of op3
        q3 = ("select ac_no from customer_details where username = %(s)s")
        d3 = {'s' : username}
        cur.execute(q3,d3)
        temp2 = cur.fetchall()                                                   # stored as tuple inside a list
        for i in temp2[0]:                                                       # changing temp1 to str format 
            x2 = i
                
        q4 = ("select *from loan_account where ac_no = %(s)s")
        d4 = {'s' : x2}
        cur.execute(q4,d4)                                                #python type list cannot be converted
        a = cur.fetchall()
        print('AC no                ',a[0][5])
        print('Account              ',a[0][0])
        print('account type         ',a[0][1])
        print('credit bal           ',a[0][2])
        print('debit bal            ',a[0][3])
        print('book bal             ',a[0][4])
        print()

        v2 = input('Do you need to go back?(y/n): ')
        if v2 == 'y':
            accounts()
        else:
            pass

    elif op3 == 3:                                                                          # third option of op3
        after_login_page()

def fund_transfer():                                                                   # 4th page
    print('''
        1. Payee details
        2. Add payee
        3. Delete Payee
        4. Send money
        5. Go back\n''')
    op4 = int(input('Select from the above options: '))
    print()

    if op4 == 1:                                                                       # 1st option of op4
        cur.execute('select *from payee_details')
        d = cur.fetchall()

        print('Payee\t\t\tAddress\t\t\t\t\t\t\tAC type\t\t\t\t   AC no\t\t  IFSC code')
        print()
        for i in d:
            print(i[0],'\t\t',i[1],'\t\t\t\t',i[2],'\t\t\t\t',i[3],'\t\t',i[4])
                ## printing pattern works only for medium values, dont type very big or small values

        print()
        e1 = input('Do you need to go back?(y/n): ')
        print()
        if e1 == 'y':
            fund_transfer()
        else:
            pass

    elif op4 == 2:                                                                     # 2nd option of op4
        p_name = input('Enter payee name: ')
        p_name1 = p_name.lower()
        cur.execute('select p_name from payee_details')
        j = cur.fetchall()
        if p_name1 in j:
            print('Payee already exists!')
            fund_transfer()
        else:
            pass

        p_address = input('Enter address of payee: ')
        AC_type = input('Enter account type: ')
        AC_no = input('Enter account number: ')
        IFSC = input('Enter IFSC code: ')

        cur.execute('insert into payee_details values(%s,%s,%s,%s,%s)',(p_name1,p_address,AC_type,AC_no,IFSC))
        mycon.commit()
        print('Payee added succesfully!')
        print()

        e2 = input('Do you need to go back?(y/n): ')
        if e2 == 'y':
            fund_transfer()
        else:
            pass

    elif op4 == 3:                                                                     # 3rd option of op4
        f = input('Enter the payee name you need to delete: ')
        q6 = ('delete from payee_details where p_name= %(s)s')
        d6 = {'s':f}
        cur.execute(q6,d6)
        mycon.commit()
        print('\nPayee',f,'is deleted!\n')

        g = input('Do you need to go back?(y/n):')
        if g == 'y':
            fund_transfer()
        else:
            pass

    elif op4 == 4:                                                                     # 4th option of op4
        p_name = input('Enter payee name to send: ')
        p_name1 = p_name.lower()

        cur.execute('select p_name from payee_details')
        x3 = cur.fetchall()
        k = []
        for i in x3:
            k += i
        if p_name1 in k:
            pass
        else:
            print('Payee name is incorrect or does\'nt exist! Pls try again.')
            fund_transfer()

        amount = input('Enter the amount to be sent: ')
        t_passwd = input('Enter your transaction password: ')

        q7 = ('select t_passwd from customer_details where username= %(s)s')
        d7 = {'s': username}
        cur.execute(q7,d7)

        x4 = cur.fetchall()
        if t_passwd in x4[0]:
            pass
        else:
            print('Entered transaction password is incorrect!')
            fund_transfer()

        confirm = input('Do you need to confirm payment(y/n)?: ')
        if confirm == 'y':
            condition = True
            print('Transaction succesfull! Money sent to',p_name,'.')
        else:
            condition = False
            print('Transaction cancelled! Money not sent.')

        if condition == True:
            q8 = ('select ac_no from customer_details where username= %(s)s')
            d8 = {'s':username}
            cur.execute(q8,d8)
            l = cur.fetchall()
            ac_no = l[0][0]
            q9 = ('update sav_account set credit_bal= (credit_bal- %(s)s) where ac_no= %(p)s')
            d9 = {'s':amount,'p':ac_no}
            cur.execute(q9,d9)
            q10 = ('update sav_account set debit_bal= %(s)s where ac_no= %(p)s')
            d10 = {'s':amount,'p':ac_no}
            cur.execute(q10,d10)
            q11 = ('update sav_account set book_bal= (book_bal - %(s)s) where ac_no= %(p)s')
            d11 = {'s':amount,'p':ac_no}
            cur.execute(q11,d11)
            mycon.commit()

        else:
            pass

        print()
        h = input('Do you need to go back?(y/n): ')
        if h == 'y':
            fund_transfer()
        else:
            pass

    elif op4 == 5:
        after_login_page()

import mysql.connector as con
mycon = con.connect(host='localhost', user='root', password='#SQL1', database='project1')
cur = mycon.cursor()
"""
cur.execute('create table user_credentials(username varchar(30) primary key,password varchar(30) unique)')
cur.execute('create table customer_details(AC_no bigint(10),username varchar(30),phone bigint(10),email varchar(20),aadhar bigint(12),dob date,address varchar(50),t_passwd varchar(30))')
cur.execute('create table sav_account(AC_no bigint(10),account bigint(10),ac_type varchar(2),credit_bal float,debit_bal float,book_bal float)')
cur.execute('create table loan_account(AC_no bigint(10),account bigint(10),ac_type varchar(2),credit_bal float,debit_bal float,book_bal float)')
cur.execute('create table payee_details(p_name varchar(30),p_address varchar(50),AC_type varchar(3),AC_no bigint(10),IFSC varchar(11))')
"""
before_login_page()                                                                  # Initial function call