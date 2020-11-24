


class Product:
    '''This class allows one to input information regarding
    products to be sold at various departments of a music store. 
    Example stores:  Guitar Center, Sam Ash, etc.'''

    department = 'Music Store'
    sold = 0

    def __init__(self):
        self.product_details = []

    def register(self,name,price,model,serial_num,store_location,store_phone):
        conditions = True
        if len(str(store_phone)) > 10 or len(str(store_phone)) < 10:
            print("Invalid phone number. Please make sure the number is 10 digits with no dashes.")
            conditions = False
        
        if conditions == True:
            print("You have successfully registered your item.")
            Product.sold += 1
            self.product_details = [name,price,model,serial_num,store_location,store_phone]
            with open(f"{name}-{serial_num}.txt", "w") as f:
                for products in self.product_details:
                    f.write(str(products)+"\n")
                f.close()
        
    def display(self):
        print(f'The {self.name} {self.model} model is ${self.price}. Serial number: {self.serial_num} located at the {self.store_location}.')

    def calculate_tax(self):
        return self.price * 0.095

    def total_price_with_tax(self):
        return self.calculate_tax() + self.price

    @classmethod
    def show_sold(cls):
        print(f'Total number of {cls.department} sold is: {cls.sold}')

    def contact_information(self):
        print(f'Product: {self.name}  Model: {self.model} Serial Number: {self.serial_num} was purchased at {self.store_location}: {self.store_phone}')


class Keyboards_Midi(Product):
    
    department = 'Keyboards & Midi'

    def __init__(self):
        super().__init__()
        
class Guitars(Product):
    
    department = 'Guitars'

    def __init__(self):
        super().__init__()

class Basses(Product):
    
    department = 'Basses'

    def __init__(self):
        super().__init__()


class Amps_Effects(Product):
    
    department = 'Amps & Effects'

    def __init__(self):
        super().__init__()

class Drums(Product):
    
    department = 'Drums'

    def __init__(self):
        super().__init__()

class Recording(Product):
    
    department = 'Recording'

    def __init__(self):
        super().__init__()


class Software(Product):
    
    department = 'Software'

    def __init__(self):
        super().__init__()


class Mics_Wireless(Product):
    
    department = 'Mics & Wireless'

    def __init__(self):
        super().__init__()


class Live_Sound(Product):
    
    department = 'Live Sound'

    def __init__(self):
        super().__init__()


class Dj(Product):
    
    department = 'DJ'

    def __init__(self):
        super().__init__()

class Lighting(Product):
    
    department = 'Lighting'

    def __init__(self):
        super().__init__()

class Accessories(Product):
    
    department = 'Accessories'

    def __init__(self):
        super().__init__()

class Band_Orchestra(Product):
    
    department = 'Band & Orchestra'

    def __init__(self):
        super().__init__()

class Platinum(Product):
    
    department = 'Platinum'

    def __init__(self):
        super().__init__()

class Outlet(Product):
    
    department = 'Outlet'

    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    Product_object = Product()
    Keyboard_object = Keyboards_Midi()
    Guitars_object = Guitars()
    Basses_object = Basses()
    AmpsEffects_object = Amps_Effects()
    Drums_object = Drums()
    Recording_object = Recording()
    Software_object = Software()
    MicsWireless_object = Mics_Wireless()
    LiveSound_object = Live_Sound()
    Dj_ojbect = Dj()
    Lighting_object = Lighting()
    Accessories_object = Accessories()
    BandOrch_object = Band_Orchestra()
    Platinum_object = Platinum()
    Outlet_object = Outlet()

    def register_prompt(user):
        name = str(input("Enter product name: "))
        price = float(input("Enter product price: "))
        model = str(input("Enter product Model name: "))
        serial_num = str(input("Enter product Serial Number: "))
        store_location = str(input("Enter store location for this product: "))
        store_phone = int(input("Enter store phone number: "))
        if user == 1:
            return Keyboard_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 2:
            return Guitars_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 3:
            return Basses_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 4:
            return AmpsEffects_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 5:
            return Drums_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 6:
            return Recording_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 7:
            return Software_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 8:
            return MicsWireless_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 9:
            return LiveSound_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 10:
            return Dj_ojbect.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 11:
            return Lighting_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 12:
            return Accessories_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 13:
            return BandOrch_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 14:
            return Platinum_object.register(name,price,model,serial_num,store_location,store_phone)
        elif user == 15:
            return Outlet_object.register(name,price,model,serial_num,store_location,store_phone)
        else:
            return Product_object.register(name,price,model,serial_num,store_location,store_phone)
        

    department_names = ['Product','Keyboards & Midi','Guitars','Basses','Amps & Effects','Drums','Recording','Software','Mics & Wireless',
                        'Live Sound','DJ','Lighting','Accessories','Band & Orchestra','Platinum','Outlet']


    print("Welcome to the Guitar Center product inventory!")
    print("Press the number that corresponds with the department for your product.")
    print("Or Press '0' to quit")
    print("[1]Keyboards & Midi   [2]Guitars     [3]Basses       [4]Amps & Effects")
    print("[5]Drums              [6]Recording   [7]Software     [8]Mics & Wireless")
    print("[9]Live Sound         [10]DJ         [11]Lighting    [12]Accessories")
    print("[13]Band & Orchestra  [14]Platinum   [15]Outlet      [0]Quit")
    user = int(input("Which department does your product belong to? Choose 1 through 12 now: "))

    if user == 0:
        exit()

    if user == 1: #keyboards & Midi
        print(f"Logging into {department_names[1]}...")
        register_prompt(user)
        print(Keyboards_Midi.show_sold())
        

    if user == 2: #Guitars
        print(f"Logging into {department_names[2]}...")
        register_prompt(user)
        print(Guitars.show_sold())
        
    if user == 3: #Basses
        print(f"Logging into {department_names[3]}...")
        register_prompt(user)
        print(Basses.show_sold())

    if user == 4:  #Amps & Effects
        print(f"Logging into {department_names[4]}...")
        register_prompt(user)
        print(Amps_Effects.show_sold())

    if user == 5:  #Drums
        print(f"Logging into {department_names[5]}...")
        register_prompt(user)
        print(Drums.show_sold())

    if user == 6:  # Recording
        print(f"Logging into {department_names[6]}...")
        register_prompt(user)
        print(Recording.show_sold())

    if user == 7:  #Software
        print(f"Logging into {department_names[7]}...")
        register_prompt(user)
        print(Software.show_sold())

    if user == 8: #Mics & Wireless
        print(f"Logging into {department_names[8]}...")
        register_prompt(user)
        print(Mics_Wireless.show_sold())

    if user == 9:  #Live Sound
        print(f"Logging into {department_names[9]}...")
        register_prompt(user)
        print(Live_Sound.show_sold())

    if user == 10: #DJ
        print(f"Logging into {department_names[10]}...")
        register_prompt(user)
        print(Dj.show_sold())

    if user == 11:  #Lighting
        print(f"Logging into {department_names[11]}...")
        register_prompt(user)
        print(Lighting.show_sold())

    if user == 12:   #Accessories
        print(f"Logging into {department_names[12]}...")
        register_prompt(user)
        print(Accessories.show_sold())

    if user == 13:  #Band & Orchestra
        print(f"Logging into {department_names[13]}...")
        register_prompt(user)
        print(Basses.show_sold())

    if user == 14:  #Platinum
        print(f"Logging into {department_names[14]}...")
        register_prompt(user)
        print(Platinum.show_sold())

    if user == 15:
        print(f"Logging into {department_names[15]}...")
        register_prompt(user)
        print(Outlet.show_sold())









#name,price,model,serial_num,store_location,store_phone
#triton1 = Keyboards_Midi()
#triton1.register("Triton Extreme",1500, 'T-1000','X-123456789','GuitarCenter2400 West Hollywood','323-874-1060')
