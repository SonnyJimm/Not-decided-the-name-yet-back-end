from backend import db
class Customer(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(20),nullable = False)
    age = db.Column(db.Integer,nullable = False)
    reason = db.Column(db.String(40),nullable = False)
    phone = db.Column(db.Integer,nullable = False)
    attemptedTime = db.Column(db.String(40),nullable = False)
    def __repr__(self):
        return f"Customer('{self.id},{self.name},{self.age},{self.reason},{self.phone},{self.attemptedTime},{self.givenTime}')"
    def todixt(self):
        return{
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "reason":self.reason,
            "phone_number":self.phone,
            "attemptedTime":self.attemptedTime
        }
