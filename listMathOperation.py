'''
Created on Feb 23, 2015

@author: Jarvis
'''
'''
Created on Feb 23, 2015

@author: Jarvis
'''
import MySQLdb
import re
import math

class Calculater:
    count = 0
    
    def __init__(self):
        Calculater.count+=1
    def setnumbers(self,num1,num2):
        self.num1=num1
        self.num2=num2
         
    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        if self.num1>self.num2:
            return self.num1-self.num2
        else:
            return self.num2-self.num1
    
    def multiply(self):
        return self.num1*self.num2
    
    def divide(self):   
        return self.num1/self.num2
    
    def setnumbr(self,numbr):
        self.numbr=numbr
    
    def sqr(self):
        return self.numbr*self.numbr
    
    def cube(self):
        return self.numbr*self.numbr*self.numbr
    
    def setname(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def setoperation(self,opr):
        self.opr=opr
    
    def setresult(self,res):
        self.res=res
    def sqrt(self):
        temp=math.pow(self.numbr, 1.0/2)
        return temp
    def cubert(self):
        temp=math.pow(self.numbr, 1.0/3)
        return temp
    def log(self):
        temp=math.log(self.numbr)
        return temp
    def sin(self):
        temp=math.sin(self.numbr)
        return temp
    def cos(self):
        temp=math.cos(self.numbr)
        return temp
    def tan(self):
        temp=math.tan(self.numbr)
        return temp
        
    def logdetails1234(self):
        db = MySQLdb.connect("localhost","pythonuser","python","pythondb")
        cursor = db.cursor()
        sql="""INSERT INTO APPLICATION_USAGE(FNAME,
            LNAME, OPERATION_NAME, NUMBER1, NUMBER2, RESULT)
            VALUES ('%s', '%s', '%s', '%f', '%f', '%f');""" % (self.fname,self.lname,self.opr,self.num1,self.num2,self.res)
        try:
            cursor.execute(sql)
            db.commit()
            return 1
        except Exception ,err:
            print"Message from db -- error inserting data",err
            db.rollback()
            return 0
        db.close()
        
    def logdetails56(self):
      
        db = MySQLdb.connect("localhost","pythonuser","python","pythondb")
        cursor = db.cursor()
        sql="""INSERT INTO APPLICATION_USAGE(FNAME,
            LNAME, OPERATION_NAME, RESULT, NUMBER)
            VALUES ('%s', '%s', '%s', '%f','%f');""" % (self.fname,self.lname,self.opr,self.res,self.numbr)
         
        try:
            cursor.execute(sql)
            db.commit()
            return 1
        except Exception ,err:
            print"Message from db -- error inserting data",err
            db.rollback()
            return 0
        db.close()  
        
    def viewcontents(self):
        db = MySQLdb.connect("localhost","pythonuser","python","pythondb")
        cursor = db.cursor()
        sql ="SELECT  * FROM APPLICATION_USAGE WHERE FNAME = '%s';" % (self.fname)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                data1 = row[1]
                data2 = row[2]
                data3 = row[3]
                data4 = row[4]
                data5 = row[5]
                data6 = row[6]
                data7 = row[8]
                if data7 == None:
                    print"First name = %s ,Last name = %s,Operation done = %s ,number1 = %f,number2 = %f ,result = %f" % (data1,data2,data3,data4,data5,data6)
                    print""
                elif data4 == None :
                    print"First name = %s ,Last name = %s,Operation done = %s ,result = %f, number = %f" % (data1,data2,data3,data6,data7)
                    print""
                    
            return 1
        except Exception,e:
            print"Message from db -- error fetching data", e
            return 0
        db.close()     

try:
    fname=raw_input("Please enter your first name  :: ")
    if re.match(r'\d',fname):
        print "Sorry !! first name must contain alphabets only\n"
        print"Application stopped!!"
        exit()
    elif fname == "":
        print "Sorry !! first name can not be blank\n"
        print"Application stopped!!"
        exit()    
    lname=raw_input("Please enter your last name  :: ")
    if re.match(r'\d',lname):
        print "Sorry !! last name must contain alphabets only\n"
        print"Application stopped!!"
        exit()
          
    while True:
        
        print "\nWelcome "+fname+" to my Simple Calculator Application\n"
        print "1). Addition"
        print "2). Subtraction"
        print "3). Multiplication"
        print "4). Division"
        print "5). Square"
        print "6). Cube"
        print "7). Square Root"
        print "8). Cube Root"
        print "9). Log"
        print "10). Sin"
        print "11). Cos"
        print "12). Tan"
        print ""
        choice = int(raw_input("Enter your choice :: "))
        print ""
        if (choice==1 or choice==2 or choice==3 or choice==4):
            num1 = float(raw_input("Enter a non zero number :: "))
            num2 = float(raw_input("Enter a non zero  number :: "))
            obj1 = Calculater();
            obj1.setnumbers(num1, num2)
            print""
            print "You entered  :: " , num1,"&", num2
            print ""
        else:
            numbr =float(raw_input("Enter a non zero number :: "))
            obj1 = Calculater();
            obj1.setnumbr(numbr)
            print""
            print "You entered  :: " ,numbr
            print ""
            
        if choice == 1:
            opr = "ADDITION"
            obj1.setoperation(opr)
            obj1.setname(fname, lname)
            result = float(obj1.add());
            obj1.setresult(result)
            print "Addition of ", num1,"&", num2, "is", result,"\n"
        elif choice == 2:
            opr = "SUBTRACTION"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.subtract());
            obj1.setresult(result)
            print "Subtraction of ", num1,"&", num2, "is", result,"\n"
        elif choice == 3:
            opr = "MULTIPLICATION"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.multiply());
            obj1.setresult(result)
            print "multiplication of ", num1,"&", num2, "is", result,"\n"
        elif choice == 4:
            opr = "DIVISION"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.divide());
            obj1.setresult(result)
            print "division of ", num1,"&", num2, "is", result,"\n"
        elif choice == 5:
            opr = "SQUARE"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.sqr())
            obj1.setresult(result)
            print "square of ", numbr,"is", result,"\n"
        elif choice == 6:
            opr = "CUBE"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.cube())
            obj1.setresult(result)
            print "cube of ", numbr,"is", result,"\n"
        elif choice == 7:
            opr = "SQUARE ROOT"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result =float(obj1.sqrt())
            obj1.setresult(result)
            print "square root of ", numbr,"is", result,"\n"
        elif choice == 8:
            opr = "CUBE ROOT"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.cubert())
            obj1.setresult(result)
            print "cube root of ", numbr,"is", result,"\n"
        elif choice == 9:
            opr = "LOG"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.log())
            obj1.setresult(result)
            print "log of ", numbr,"is", result,"\n"
        elif choice == 10:
            opr = "SIN"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.sin())
            obj1.setresult(result)
            print "sin of ", numbr,"is", result,"\n"
        elif choice == 11:
            opr = "COS"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.cos())
            obj1.setresult(result)
            print "cos of ", numbr,"is", result,"\n"
        elif choice == 12:
            opr = "TAN"
            obj1.setname(fname, lname)
            obj1.setoperation(opr)
            result = float(obj1.tan())
            obj1.setresult(result)
            print "tan of ", numbr,"is", result,"\n"
            
        try: 
            print"Hey ",fname,"!!"
            print "" 
            store=raw_input("Do you want to store your application usage ?? Y/N : ")
            if store.lower()=="y":
                if (choice==1 or choice==2 or choice==3 or choice==4):
                    status = obj1.logdetails1234()
                else:
                    status = obj1.logdetails56()
                if status == 1:
                    print"Stored details successfully ::"
                    view=raw_input("Do you Want to see the the inserted data?? Y/N :: ")
                    if view.lower()=="y":
                        status=obj1.viewcontents()
                                         
                    option = raw_input("Do you want to continue?? Y/N  : ")
                    if option.lower()=="y":
                        print""
                        print "One more time\n"
                        continue
                    else:
                        if Calculater.count==1:
                            print ""
                            print fname,"You have used my Application: "  ,Calculater.count,"time.\n"
                            print"Thanks " +fname+ " ,Application Stopped !!"
                            break
                        else:
                            print ""
                            print fname,"You have used the Application: "  ,Calculater.count,"times.\n"
                            print"Thanks " +fname+ " ,Application Stopped !!"
                            break
                elif status==0:
                    print"Database Insertion error"
            else: 
                option = raw_input("Do you want to continue?? Y/N  : ")
                if option.lower()=="y":
                    print""
                    print "One more time\n"
                    continue
                else:
                    if Calculater.count==1:
                        print ""
                        print fname,"You have used my Application: "  ,Calculater.count,"time.\n"
                        print"Thanks " +fname+ " ,Application Stopped !!"
                        break
                    else:
                        print ""
                        print fname,"You have used the Application: "  ,Calculater.count,"times.\n"
                        print"Thanks " +fname+ " ,Application Stopped !!"
                        break
           
        except:
            print"Oops!! Wrong input dear"
            print"Closing Application .."
            break      
except Exception,err:
    print err
    print"Oops!! Wrong input\n" 
    print"Application stopped!!"
          
           
    
    
    
 


        
