from backend import db
class Customer:
    def __init__(self,id,name,age,reason,phone,attemptedTime):
        self.id=id
        self.name=name
        self.age=age
        self.reason=reason
        self.phone=phone
        self.attemptedTime=attemptedTime
    def __repr__(self):
        return f"Customer('{self.id},{self.name},{self.age},{self.reason},{self.phone},{self.attemptedTime}')"
    def todixt(self):
        return{
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "reason":self.reason,
            "phone_number":self.phone,
            "attemptedTime":self.attemptedTime
        }
class CustomerDb:
    def __init__(self):
        with db:
            cursor=db.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS "customer"(
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "name"	VARCHAR(20) NOT NULL,
                "age"	INTEGER NOT NULL,
                "reason"	VARCHAR(40) NOT NULL,
                "phone"	INTEGER NOT NULL,
                "attemptedTime"	VARCHAR(40) NOT NULL
                )
                """)
            db.commit()
            cursor.close()
    def put(self,name,age,reason,phone,attemptedTime):
        with db:
            cursor=db.cursor()
            cursor.execute("INSERT INTO customer(name,age,reason,phone,attemptedTime) VALUES(?,?,?,?,?)",(name,age,reason,phone,attemptedTime))
            db.commit()
            cursor.close()
    def get(self):
        with db:
            cursor=db.cursor()
            cursor.execute("SELECT * FROM customer ORDER BY attemptedTime DESC")
            results = cursor.fetchall()
            customerList=[]
            for result in results:
                customer = Customer(id=result[0],name=result[1],age=result[2],reason=result[3],phone=result[4],attemptedTime=result[5])
                customerList.append(customer)
            cursor.close()
            return customerList