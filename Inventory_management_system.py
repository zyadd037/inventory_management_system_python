from datetime import date 
class Product: # parent / based class
    def __init__(self,name,price,stock,low_stock_limit=10): # calling function if user wants to create a new obj
        
        self.name = name 
        self.price = price
        self.stock = stock 
        self.low_stock_limit = low_stock_limit

    @property # I used Getter method (Encapsulation) here to read the current stock
    def stock(self):
        return self._stock # '_' underscore used as a protector to prevent external access or calling fun from global class
    
    @stock.setter # here setter has been used for changing the current amount of stock and validiation
    def stock(self,value):
        if value < 0:
            raise ValueError("Stock cannot be negative")

        self._stock = value  # self._stock is the real variable which store stock's value

    
    @property 
    def price(self): # reading price and consider it as attribute
        return self._price

    @price.setter  
    def price(self,value):
        if value < 0 :   # checking if value is greater or smaller than zero
            raise ValueError("Price cannot be negative")

        self._price = value # creating a new variable can store the current price of product




    def add_stock(self,amount):  # addition fun 
        if amount <= 0: # checking if current amount is smaller or equal than zero
            raise ValueError("Amount must to be greater than or zero") # if condition achieves so python will directly raise understandable error with a clear msg

        self.stock += amount # adding method to sum stock with amount

    def remove_stock(self,amount): # remove stock
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if amount > self.stock:    #if current amount is greater than stock so this operation is faild 
            raise ValueError("there is not enough stock available") 

        self.stock -= amount # this method applied for minimizing the amount 

    def is_low_stock(self):   # function used to check if limitation stock is greater then stocks is required
        return self.stock <= self.low_stock_limit  

    
    def __str__(self): # __str__ used to make objects are organized and understandable instead of showing results randomly
        return (
            f"product:{self.name}\n"  
            f"price:{self.price}\n"  
            f"stock:{self.stock}"

        )


class PerishableProduct(Product): # child class
    def __init__(self , name ,price ,stock , expiry_date, low_stock_limit=10): 
        super().__init__(name,price,stock,low_stock_limit) # super() is used to ask of implement parent's class
        self.expiry_date = expiry_date # defines a new attribute

    def is_expired(self): # this fun is used for checking if product is expired or not 
        return self.expiry_date < date.today() # this line is showing if expiry date is older tham today's date so the product is not availavle for usage

    def remove_stock(self,amount): 
        if self.is_expired():
            raise ValueError ("Cannot sell expired product")

        super().remove_stock(amount) # implements constructor's parent classby removing all unless expiry products


    def __str__(self):
        return(
            f"{super().__str__()}\n" 
            f"Expiry date is {self.expiry_date}"
        )

class Inventory: # class responsible for managing products
    def __init__(self):
        self.products = {} # creating an empty dictionary to store different products , products names (key) , objects are values


    def add_product(self,product): # method for adding products and prevent reapiting products names
        if product.name in self.products: # checking products name in dictionary to search for required products and reach to it
            raise ValueError("product is already exist")
        self.products[product.name] = product # adding required product if it does not exist

    def restock_product(self,name,amount): # new function for changing product stock amounts
        if name not in self.products:
            raise ValueError("product not found")
        self.products[name].add_stock(amount)
    
    def sell_product(self,name,amount):
        if name not in self.products:
            raise ValueError("product is not found")
        self.products[name].remove_stock(amount)

    def low_inventory_alerts(self): # method used for chicking limitation of stock
        print("\nlow inventory alerts : ")
        #Boolean
        found = False # checking if product exists

        for product in self.products.values(): # checking every product by searching in dictionary and used values() for reaching to objects
            if product.is_low_stock():
                print(f" Warning {product.name} has only {product.stock} items only !")
                found = True 
            
        if not found:
                print("All proudcts have enough stock.")

    def generate_report(self): # creating fully report to get all products informations
        print("----------- Inventory Report -----------")

        if not self.products: 
            print("Inventory is empty!")
            return

        total_products = len(self.products) # checking number products 
        total_stock = 0

        for product in self.products.values():
            print(product)

            total_stock += product.stock

            if isinstance(product, PerishableProduct): # isinstance used to ask about prodcut statue
                if product.is_expired():
                    print("Status: Expired")
                else:
                    print("Status: Valid")

            if product.is_low_stock():
                print("Warning: Low stock")

            print("====== Results ======")
        print(f"Total products: {total_products}")
        print(f"Total items in stock: {total_stock}")
        print("----------------------------------------")



#Testing 
inventory = Inventory() # creating inventory obj 
Phone = Product("Phone",20000,15)
Mango = PerishableProduct(
    "Mango" , 100, 20, date(2026, 12, 15) # creating product has expiration date like product we added to program (mango)
)

inventory.add_product(Phone)    # function used for adding products to dictionary
inventory.add_product(Mango)

inventory.restock_product("Phone",5) # changing the amount of current stock by adding new amounts(5) , the phone stock was 15 and it becomes 20 (15+5)
inventory.sell_product("Mango",10) # this method has applied for removing amount of products by selling required product , mango stock was 20 and now its 10 (20-10)
inventory.low_inventory_alerts() # checking limitation of stocks ,phone stock became 20 and limitation is (10) and mango was 20 and became 10 so mango product has reached to limited stock
inventory.generate_report()


    