#!/usr/bin/python3

class Phone:
    username = "Kate"                # Публичное поле
    __serial_number = "11.22.33"     # Приватное поле
    __how_many_times_turned_on = 0   # Приватное поле

    def call(self):                  # Публичный метод
        print( "Ring-ring!" )

    def __turn_on(self):             # Приватный метод
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone._Phone__turn_on()
my_phone._Phone__serial_number = "44.55.66"
print( "New serial number is ", my_phone._Phone__serial_number )

my_phone = Phone()
print(my_phone.username)
print(my_phone.__serial_number)