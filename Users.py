class User():
    def __init__(self,first_name,last_name,age,location,password):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
        self.password=password
        self.login_attempts=0

    def describe_user(self):
        description=self.first_name+" "+self.last_name+" is "+str(self.age)+"  years old and lives in "+self.location
        return description
    
    def greet_user(self):
        greet="welcome "+ self.first_name+" "+self.last_name
        print(greet)

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

    def read_login_attempts(self):
        print("the user has had "+str(self.login_attempts)+" attempts")

first_user=User("Fomonyuytar","Joseph",21,"Buea",1234)
my_user=User("John","Doe",45,"Molyko",23564)

first_user.greet_user()
print(first_user.describe_user())
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.read_login_attempts()
first_user.reset_login_attempts()
first_user.read_login_attempts()



my_user.greet_user()
print(my_user.describe_user())
