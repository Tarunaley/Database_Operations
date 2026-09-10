from abc import ABC,abstractmethod
class User(ABC):
    @abstractmethod
    def getdetails():
        pass 
class Customer(User):
    def getdetails(self,id,name,email,phone):
        self.id=id
        self.name=name
        self.email=email
        self.phone=phone
    
    def placeOrder(self):
class Admin(User):
    def getdetails(self,id,name,email,phone):
         self.id=id
         self.name=name
         self.email=email
         self.phone=phone
          
    def manageSystem():
class Owner(User):
    menu = {}

    def getdetails(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def addItems(self, item_id, item, price, category, isAvailable):
        menu[item_id] = [item, price, category, isAvailable]
    def removeItem(self,item_id):
        self.menu.pop(item_id,none)
    def updateItem(self,item_id):
        pass
    def displayItems(self):
        for key,value in self.menu:
            print(key," ",value)
class Order():
    
    
 


    

        
    