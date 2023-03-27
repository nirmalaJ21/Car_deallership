
vehicles_to_compare = []
class Vechile():

    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine…')
        self.engine_on = True

    def make_noise(self):
        print('“Beep beep!”')


class Truck(Vechile):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print('Loading the truck bed…')
        self.cargo = True


class Bike(Vechile):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom vroom!')


def choice_Truck_bike(choiceTB, vehicles_to_compare):

        trucks = [Truck('Toyota', 12, 34), Truck('Ford', 122, 342), Truck('Chevy', 1222, 3422)]
        bikes = [Bike('Harley', 12, 34, 300), Bike('Ducati', 12, 34, 400), Bike('Honda', 12, 34, 500)]

        if choiceTB == 't':
            for i, truck in enumerate(trucks):
                print(f"{i + 1}: {truck.make} with {truck.miles} miles costs {truck.price}")
            while True:
                print('Would you like to compare one of these vehicles today? (y/n)')
                choice_cmp = input()
                if choice_cmp == 'y':
                    while True:
                        print('Which vehicle would you like to compare? (Please list number)')
                        choice_num = int(input()) - 1
                        if choice_num in range(len(trucks)):
                            truck = trucks.pop(choice_num)
                            vehicles_to_compare.append(truck)
                            print(f"{truck.make} added!")
                            break
                        else:
                            print("Invalid choice. Please select a number from the list.")
                    print('Would you like to compare your vehicle now? (y/n)')
                    choice_veh = input()
                    if choice_veh == 'y':
                        return (choice_veh, vehicles_to_compare)
                    else:
                        return (choice_veh, vehicles_to_compare)
                elif choice_cmp == 'n':
                    return (choice_veh, vehicles_to_compare)
                else:
                    print('Please select y or n')

        else:
            for i, bike in enumerate(bikes):
                print(
                    f"{i + 1}: {bike.make} with {bike.miles} miles and a top speed of {bike.top_speed} miles costs {bike.price}")
            while True:
                print('Would you like to compare one of these vehicles today? (y/n)')
                choice_cmp = input()
                if choice_cmp == 'y':
                    while True:
                        print('Which vehicle would you like to compare? (Please list number)')
                        choice_num = int(input()) - 1
                        if choice_num in range(len(bikes)):
                            bike = bikes.pop(choice_num)
                            vehicles_to_compare.append(bike)
                            print(f"{bike.make} added!")
                            break
                        else:
                            print("Invalid choice. Please select a number from the list.")
                    print('Would you like to compare your vehicle now? (y/n)')
                    choice_veh = input()
                    if choice_veh == 'y':
                        return (choice_veh, vehicles_to_compare)
                    else:
                        return (choice_veh, vehicles_to_compare)
                elif choice_cmp == 'n':
                    return (choice_veh, vehicles_to_compare)
                else:
                    print('Please select y or n')


def compare_vehicles(vehicles):
    truck_cmp =Truck('l',1,2)
    bike1 = Bike('H', 1, 2, 23)
    # Check if there are at least two vehicles to compare
    if len(vehicles) < 2:
        print("Please add at least two vehicles to compare.")
        return

    # Compare the attributes of each vehicle
    for i in range(len(vehicles)-1):
        for j in range(i+1, len(vehicles)):
            print(f"Comparing {vehicles[i].make} with {vehicles[j].make}:")
            print(f'{vehicles[i].make }with {vehicles[i].miles} miles cost{vehicles[i].price}')
            if vehicles[i].make =='Toyota' or vehicles[i].make =='Ford' or vehicles[i].make =='Chevy' :
                truck_cmp.make_noise()

            else:
                bike1.make_noise()

            print(f"{vehicles[j].make} with {vehicles[j].miles} miles cost{vehicles[j].price} .")
            if vehicles[j].make == 'Hareley' or vehicles[j].make == 'Ducati' or vehicles[j].make  == 'Honda' :
                bike1.make_noise()

            else:
                truck_cmp.make_noise()

    # Ask the user if they want to purchase a vehicle
    while True:
        print('Would you like to purchase a vehicle? (y/n)')
        choice_purchase = input()
        if choice_purchase == 'y':
            while True:
                print('Which vehicle would you like to purchase? (Please list number)')
                for i, vehicle in enumerate(vehicles):
                    print(f"{i + 1}: {vehicle.make} with {vehicle.miles} miles costs {vehicle.price}")
                choice_num = int(input()) - 1
                if choice_num in range(len(vehicles)):
                    vehicle = vehicles[choice_num]
                    print(f"You have purchased the {vehicle.make}!")
                    return
                else:
                    print("Invalid choice. Please select a number from the list.")
        elif choice_purchase == 'n':
            return
        else:
            print('Please select y or n')



    # print('Thank you and have a nice day!')

choice_truck1 = ''
print('Hello')
print('Welcome to GC Bikes & Trucks!')
while True:
  print('Would you like to view bikes or Trucks(b or t)')
  choice_truck = input()
    # if choice_truck == 'y':
  choice_truck1,vehicles_to_compare = choice_Truck_bike(choice_truck, vehicles_to_compare)
  # print(f'After retunring choice trcuk {choice_truck1}')
  if choice_truck1 == 'n':
        continue
  else :
        compare_vehicles(vehicles_to_compare)
        print('Thank you have a nice day!')
        break




