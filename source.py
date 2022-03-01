from mysql import connector
from time import sleep,monotonic
from os import system,get_terminal_size
from random import randint
from keyboard import press_and_release

press_and_release('f11')
global cols,lines,half,screenState,connection,cursor,fee,months,\
    funcDict,administratorPassword,cases

administratorPassword='3°password@administrator'
screenState='#'
fee={'9':300,'10':400,'11':500,'12':600}
months=(
    'apr','may','jun','jul','aug','sep',
    'oct','nov','dec','jan','feb','mar'
    )
cases=[
        '9 a','9 b','9 c',
        '10 a','10 b','10 c',
        '11 math','11 bio','11 art','11 comm',
        '12 math','12 bio','12 art','12 comm'
        ]

global t
def Print(*a,sep=' ',end='\n'):
    global t
    print(' '*8*t,end='')
    print(*a,sep=sep,end=end)
def printM(tab):
    global t
    t=tab
    return Print
def printT(M):
    h=('SRNo.','NAME','CLASS','SEC','fee status','extra ₹')
    d=('+'+'='*7,'='*15,'='*5,'='*4,'='*10,'='*7)
    printM(2)(*d,sep='=+=',end='=+\n')
    printM(2)(*(eval(("'| '+'{}'.center(6)+','+'{}'.center(15)+','+'{}'.center(5)+','+'{}'.center(4)+','+'{}'.center(10)+','+'{}'.center(7)").format(*h)).split(',')),sep=' | ',end=' |\n')
    printM(2)(*d,sep='=+=',end='=+\n')
    d=('+'+'-'*7,'-'*15,'-'*5,'-'*4,'-'*10,'-'*7)
    for i in M:
        printM(2)(*(eval(("'| '+'{}'.center(6)+','+'{}'.center(15)+','+'{}'.center(5)+','+'{}'.center(4)+','+'{}'.center(10)+','+'{}'.center(7)").format(*i)).split(',')),sep=' | ',end=' |\n')
        printM(2)(*d,sep='-+-',end='-+\n')
def isName(a):
    if a=='':
        return False
    if a.isspace():
        return False
    l=a.split()
    r=True
    for i in l:
        r=r and i.isalpha()
    return r

def clear():
    system('cls')
def extendScreen():
    global cols,lines
    system('mode con:cols={} lines={}'.format(cols,lines*30))
def constrictScreen():
    global cols,lines
    system('mode con:cols={} lines={}'.format(cols,lines))
def loadTerminalSize():
    global cols,lines,half
    temp=get_terminal_size()
    cols=temp.columns
    if cols<122:
        cols=122
    lines=temp.lines
    if lines<33:
        lines=33
    half=(lines//2)




def connect():
    global connection,cursor,screenState
    screenState=0
    clear()
    loadTerminalSize()
    print('\n'*half)
    
    loadTerminalSize()
    clear()
    constrictScreen()

    print('\n'*half)
    print('WELCOME TO NEW R S J PUBLIC SCHOOL'.center(cols))    
    print()
    print('MADE BY Raj Yadav'.center(cols))
    print('\n\n')
    print('ENTER PASSWORD : '.rjust(cols//2),end='')    
    pas=input()
    clear()
    print('\n'*half)
    print('validating user , password and fetching database'.center(cols))    
    print('please wait... '.center(cols))
    sleep(1)  
    
    try:
        connection=connector.connect(user='root',passwd=pas,database='new_rsj')
        cursor=connection.cursor()
        connection.autocommit=True
        return "#"
    except:
        clear()
        print('\n'*half)
        print('something went wrong please check following :'.center(cols),end='\n\n')
        print(('1. password'.ljust(20)).center(cols))
        print(('2. database crash'.ljust(20)).center(cols))
        print('\n\n')
        input('press enter to exit'.center(cols))        
        return ''

def submitFeeScreen():
    global cols,lines,half,screenState,connection,cursor
    if screenState!='1':
        clear()
        extendScreen()
        print('\n\n')
        print('you can return to main menu anytime by entering "#" in any input or ctrl+C'.center(cols))
        screenState='1'
        print()
    else:
        print('\n\n')    
    sr=False
    while (not sr):
        print()
        printM(1)('ENTER ≥ 4 Digit SR. No. : ',end='')
        sr=input()
        try:
            sr=int(sr)
            if len(str(sr))<4:
                1/0
            break
        except:
            print()
            if (sr=='#'):
                print('returning to menu...'.center(cols))
                sleep(1)
                return '#'
            printM(2)('please enter a non zero ≥4 digit integer ')
            printM(3)("or enter '#' to goto main menu")            
            sr=False
    
    #connection.reconnect()
    cursor.execute('select * from students where srno={}'.format(sr))
    a=cursor.fetchall()
    if a==[]:
        print('\n\n')
        printM(4)('there is no such student')
        return '1'
    printT(M=a)
    fullYearLeftFee=(11-months.index(a[0][4]))*fee[a[0][2]]-a[0][5]    
    print()
    printM(2)('fee submitted upto                                  :',a[0][4],'month')
    printM(2)('previosly you have submitted extra                  :',a[0][5],'₹')
    printM(2)('as per your class you fee per month                 :',fee[a[0][2]],'₹')    
    printM(2)('as per you previous extra money you need to submitt :',fullYearLeftFee,'₹',end='  ')
    print('for full year payment')
    if fullYearLeftFee==0:
        print()
        printM(3)('no due left')
        print('X'.center('-'))
        return "1"
    amount=0
    while 1:
        printM(2)('how much ₹ you want to pay          :',end='')
        amount=input()
        try:
            amount=int(amount)+a[0][5]
            if (amount==0 or amount>fullYearLeftFee):
                1/0
            break
        except:
            if (amount=='#'):
                print('returning to menu...'.center(cols))
                sleep(1)
                return '#'
            printM(2)('please enter a non zero amount less than or equal to',fullYearLeftFee)
            printM(3)('or enter # for main menu')
    month=months[months.index(a[0][4])+amount//fee[a[0][2]]]
    extra=amount%fee[a[0][2]]
    query='update students set fee_status="{}" ,extra_rupee={} where srno={} ;'.format(month,extra,sr)
    #connection.reconnect()
    cursor.execute(query)
    connection.commit()
    #connection.close
    print('\n\n')
    print('fee submitted successfully'.center(cols))
    print('now your status is'.center(cols))
    #connection.reconnect()
    cursor.execute('select * from students where srno={}'.format(sr))
    printT(cursor.fetchall())
    print('\n')
    print('fee submitted thank you '.center(cols,'!'))
    print('\n')
    printM(3)('enter "#" for menu or any other\
key for again submitting fee :',end='')
    key=input()
    if key=='#':
        print('returning to menu...'.center(cols))
        sleep(1)
        return '#'
    return '1'

def queryScreen():#get list of students in particular class
    global cols,lines,half,screenState,connection,cursor,cases
    if screenState!='2':
        clear()
        extendScreen()
        print('\n\n')
        print('you can return to main menu anytime by entering "#" in any input or ctrl+C'.center(cols),end='\n\n\n')        
        printM(1)('the possible values of class are :')
        print()
        printM(2)('"',end='');print(*cases[0:3],sep='" , "',end='"\n')
        printM(2)('"',end='');print(*cases[3:6],sep='" , "',end='"\n')
        printM(2)('"',end='');print(*cases[6:10],sep='" , "',end='"\n')
        printM(2)('"',end='');print(*cases[10:14],sep='" , "',end='"\n')
        screenState='2'
        print('\n\n')        
    else :
        print('\n\n')    
    Class=''
    while 1:
        printM(3)('ENTER CLASS :',end='')
        Class=input()
        if Class=='#' :
            print('\n\n')
            print('returning to menu ....'.center(cols))
            sleep(1)
            return '#'
        if Class in cases:
            break
        else :
            print()
            printM(2)('pelase enter only possible values ie. :',end='\n\n\n')
            printM(2)('"',end='');print(*cases[0:3],sep='" , "',end='"\n\n')
            printM(2)('"',end='');print(*cases[3:6],sep='" , "',end='"\n\n')
            printM(2)('"',end='');print(*cases[6:10],sep='" , "',end='"\n\n')
            printM(2)('"',end='');print(*cases[10:14],sep='" , "',end='"\n\n')
    query='select * from students where class="{}" and sec="{}";'.format(*Class.split(' '))
    #connection.reconnect()
    cursor.execute(query)
    M=cursor.fetchall()
    if M==[]:
        print('\n\n')
        printM(2)('there is no studen in class {}'.format(Class).center(cols))
        return '2'
    print('\n\n')
    printT(M)
    return '2'

def admissionScreen():
    global cols,lines,half,screenState,connection,cursor,cases
    if screenState!='3':
        clear()
        extendScreen()
        print('\n\n\n')
        print('you can return to main menu anytime by entering "#" in any input or ctrl+C'.center(cols))
        print('\n\n')
        screenState='3'
    else :
        print('\n\n')
    attributes={'name':'','class/sec':''}
    condition={
        'name':'len(attributes[i])<15 and isName(attributes["name"])',
        'class/sec':'attributes[i] in cases'}
    message={'name':'printM(2)("name must be less than 15 character and only alphabet allowed ")',
'class/sec':'''printM(3)("class/sec can have only following values",end='\\n\\n\\n')
printM(2)('"',end='')\nprint(*cases[0:3],sep='" , "',end='"\\n\\n')
printM(2)('"',end='')\nprint(*cases[3:6],sep='" , "',end='"\\n\\n')
printM(2)('"',end='')\nprint(*cases[6:10],sep='" , "',end='"\\n\\n')
printM(2)('"',end='')\nprint(*cases[10:14],sep='" , "',end='"\\n\\n')'''}
    for i in attributes:
        while 1:
            printM(2)('ENTER '+i+' :',end=' ')
            attributes[i]=input()
            if eval(condition[i]):
                break
            elif attributes[i]=='#':
                print('\n\n')
                print('returning to menu ...'.center(cols))
                sleep(1)
                return '#'
            else:                            
                exec(message[i],globals(),locals())
                print()
    
    #connection.reconnect()
    
    query='select max(srno) from students'
    cursor.execute(query)
    sr=cursor.fetchall()
    if sr[0][0]==None:
        sr=1000
    else:
        sr=sr[0][0]+1
    query='insert into students values({},"{}","{}","{}","apr",0)'.format(sr,attributes['name'],*attributes['class/sec'].split())
    cursor.execute(query)
    connection.commit()
    #connection.close
    printM(3)('{} has been admited in class {} with srno. {}'\
        .format(attributes['name'],attributes['class/sec'],sr),end='\n\n\n')
    #connection.reconnect()
    print()
    cursor.execute('select * from students where srno={}'.format(sr))
    printT(cursor.fetchall())
    #connection.close
    print('X'.center(cols,'-'))
    print('\n')
    printM(2)('ENTER "#" FOR RETURNING TO MENU OR ANY OTHER KEY\
FOR NEW ADDMISION  :',end='')
    key=input()
    if key=='#':
        print('\n\n')
        print('returning to menu .....'.center(cols))
        sleep(1)
        return '#'
    else :
        return '3'

def getListScreen():#get list of all students
    global cols,connection,cursor
    clear()
    extendScreen()
    #connection.reconnect()
    print('\n')
    printM(2)('order by : ')
    printM(3)('1.  class')
    printM(3)('2.  sr no.')
    printM(2)('enter your choice (1/2) : ',end="")
    temp=input()
    if temp=="#":
        print('\n'+'returning to menu...'.center(cols))
        sleep(1)
        return "#"
    if temp=='1':    
        cursor.execute('select * from students order by class,sec')
        M=cursor.fetchall()
        print('\n\n')
        printT(M)
        print('\n')
    else :
        cursor.execute('select * from students order by srno')
        M=cursor.fetchall()
        print('\n\n')
        printT(M)
        print('\n')
    input('\t\tenter any key with enter : ')
    return '#'

def promoteStudentScreen():#for promoting student
    global cols,lines,half,screenState,connection,cursor,cases
    if screenState!='5':
        clear()
        extendScreen()
        print('\n\n')
        print('you can return to main menu anytime by entering "#" in any input or ctrl+C'.center(cols))
        screenState='5'
        print()
    else:
        print('\n\n')    
    sr=False
    while (not sr):
        print()
        printM(1)('ENTER ≥ 4 Digit SR. No. : ',end='')
        sr=input()
        try:
            sr=int(sr)
            if len(str(sr))<4:
                1/0
            break
        except:
            print()
            if (sr=='#'):
                print('returning to menu...'.center(cols))
                sleep(1)
                return '#'
            printM(2)('please enter a non zero ≥4 digit integer ')
            printM(3)("or enter '#' to goto main menu")            
            sr=False
    
    #connection.reconnect()
    cursor.execute('select * from students where srno={}'.format(sr))
    a=cursor.fetchall()
    if a==[]:
        print('\n\n')
        printM(4)('there is no such student')
        print('\n')
        print('new session'.center(cols,'-'))
        return '5'
    printT(M=a)
    print('\n')
    Class=""
    while 1:
        printM(1)('ENTER NEW CLASS/SEC :',end=' ')
        Class=input()
        if Class=="#":
            print()
            print('returning to menu ...'.center(cols))
            sleep(1)
            return "#"
        if Class in cases:
            Class,sec=Class.split(' ')
            break
        else:
            print()      
            printM(2)('pelase enter only possible values ie. :',end='\n\n\n')
            printM(2)('"',end='');print(*cases[0:3],sep='" , "',end='"\n\n')
            printM(2)('"',end='');print(*cases[3:6],sep='" , "',end='"\n\n')
            printM(2)('"',end='');print(*cases[6:10],sep='" , "',end='"\n\n')
            printM(2)('"',end='');print(*cases[10:14],sep='" , "',end='"\n\n')
    
    query='update students set class="{}",sec="{}",fee_status="apr" where srno={}'.format(Class,sec,sr)    
    printM(2)('"y" to proceed or any other to halt :',end=' ')
    temp=input()
    if temp=='#':
        print('\n')
        print('returning to menu...'.center(cols))
        sleep(1)
        return '#'
    if temp=="y":
        cursor.execute(query)
        printM(1)('promotion successfull!!')
        printM(1)('updated info.: ')
        cursor.execute('select * from students where srno={}'.format(sr))
        printT(cursor.fetchall())
        print()
        print('new-session'.center(cols,'-'))
        return "5"
    printM(1)('promotion stoped.')
    printM(3)('enter "#" for menu or any other\
key for another promotion :',end='')
    key=input()
    if key=='#':
        print('returning to menu...'.center(cols))
        sleep(1)
        return '#'
    return '5'

def removeStudentScreen():
    global cols,lines,half,screenState,connection,cursor,administratorPassword
    if screenState!='6':
        clear()
        extendScreen()
        print('\n\n')
        print('you can return to main menu anytime by entering "#" in any input or ctrl+C'.center(cols))
        screenState='6'
        print()
    else:
        print('\n\n')    
    sr=False
    while (not sr):
        print()
        printM(1)('ENTER ≥ 4 Digit SR. No. : ',end='')
        sr=input()
        try:
            sr=int(sr)
            if len(str(sr))<4:
                1/0
            break
        except:
            print()
            if (sr=='#'):
                print('returning to menu...'.center(cols))
                sleep(1)
                return '#'
            printM(2)('please enter a non zero ≥4 digit integer ')
            printM(3)("or enter '#' to goto main menu")            
            sr=False
    
    #connection.reconnect()
    cursor.execute('select * from students where srno={}'.format(sr))
    a=cursor.fetchall()
    if a==[]:
        print('\n\n')
        printM(4)('there is no such student')
        return '6'
    printT(M=a)
    print()
    printM(1)('as this is very special tansaction so,')
    printM(1)('you need the administrator password')
    printM(1)('enter wrong password to abort the process ')
    printM(1)('ENTER ADMINISTRATOR PASSWORD : ',end='')
    key=input()
    if key==administratorPassword:
        cursor.execute('delete from students where srno={}'.format(sr))
        print()
        printM(2)('deletion complete',end='\n\n')
        print()
        printM(2)('enter to exit : ',end='')
        input()
        print('returning to menu ...'.center(cols))
        sleep(1)
        return '#'
    print()
    printM(1)('access denied!!'.center(cols),end='\n\n')
    sleep(1)
    print('returning to menu...'.center(cols))
    sleep(1)
    return '#'

def gameScreen():
    global cols,lines,screenState
    if screenState!='7':
        clear()
        extendScreen()
        print('\n\n\n')
        print('you can return to main menu anytime by entering "#" in any input or ctrl+C'.center(cols))
        print('\n')
    else:
        print('\n\n')
        print('NEW GAME'.center(cols,'-'))
        print('\n\n')
    screenState='7'
    printM(2)('you will be asked 10 multiplication table ques.')
    printM(2)('enter to continue or enter "#" to menu :',end='')
    key=input()
    if key=='#':
        print('\n\n\n')
        print('returning to menu...'.center(cols))
        sleep(1)
        return '#'
    print('\n')   
    trt=0
    tco=0
    for i in range(10):
        a=randint(12,19)
        b=randint(2,9)
        printM(2)('{}x{}='.format(a,b),end='')
        ti=monotonic()
        ans=input()
        tf=monotonic()
        lap=(tf-ti)
        del tf,ti
        if ans==str(a*b):
            printM(5)('correct !!','\n')
            trt+=lap
            tco+=1
            del lap
        elif ans=='#':
            print('\n\n\n')
            print('returning to menu...'.center(cols))
            return ans
        else:
            printM(5)('wrong',' ',a*b,'\n')
    print('\n\n')
    printM(2)('your score :'+'{}/{}'.format(tco,10))
    if tco==0:
        printM(2)('your average response time : infinite seconds')
    else:
        printM(2)('your average response time : {} second'.format(trt/tco))
    return '7'

def aboutProjectScreen():
    clear()
    constrictScreen()
    print('\n\n\n')
    printM(2)('AUTHOR OF THE APPLICATION     :  RAJ YADAV')
    printM(2)('DATE OF INITIATION OF PROJECT :  25 NOV 2020 WEDNESDAY')
    printM(2)('DATE OF COMPLETION OF PROJECT :  26 DEC 2020 SATURDAY')
    printM(2)('COMPILED ON                   :  26 DEC 2020 SATURDAY')
    printM(2)('COMPILED BY                   :  pyinstaller 4.1')
    printM(2)('TOTAL No. OF DAYS TAKEN       :  32 DAYS')
    printM(2)('PROJECT MADE FOR              :  CLASS 12 BOARD PRACTICAL')
    printM(2)('TOPIC OF PROJECT              :  SCHOOL STUDENTS RECORD MANAGEMENT SYSTEM')
    printM(2)('PROGRAMMING LANGUAGE USED     :  PYTHON 3.7')
    print('\n\n')
    printM(3)('other details of author :')
    printM(4)('NAME    : RAJ YADAV')
    printM(4)("CLASS   : 12 A1'a'" )
    printM(4)('STREAM  : MATHEMATICS')
    printM(4)('ROLL No.: 21')
    print('\n\n')
    printM(4)('enter to continue :',end='')
    input()
    return '#'

def menu():
    global cols,lines,screenState
    screenState='#'
    constrictScreen()
    clear()
    print('\n'*4)
    print('chose one of the given key:      '.center(cols))
    print('\n\n')
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('key','task'))
    print()
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('1 .','submit fees'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('2 .','get list of students in a paricular class'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('3 .','admission of a student'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('4 .','get list of all students'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('5 .','promote a student'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('6 .','T.C./eject student'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('7 .','play quiz'))
    print((('{}'.ljust(6)+'{}'.ljust(20)).center(cols)).format('8 .','about project'))
    print('\n\n')
    key=input('enter any one key or enter to exit :'.rjust(cols//2))
    return key
def invalidKeyHandle():
    global cols,half    
    clear()
    constrictScreen()
    print(half*'\n')
    print('invalid key'.center(cols))
    sleep(1)
    return '#'

def Exit():
    global connection,cols,half
    clear()
    constrictScreen()
    print('\n'*half)
    print('you are going to exit ....'.center(cols))
    sleep(1)
    return 'break'

funcDict={

    '#':menu,
    '1':submitFeeScreen,
    '2':queryScreen,
    '3':admissionScreen,
    '4':getListScreen,
    '5':promoteStudentScreen,
    '6':removeStudentScreen,
    '7':gameScreen,
    '8':aboutProjectScreen,
    '':Exit    
        }

if __name__ == "__main__":
    key=connect()    
    while 1:
        try :
            key=funcDict[key]()
            if key=='break':
                break
        except KeyError:
            key=invalidKeyHandle()
        except:
            key="#"
