from device_factory import DeviceFactory
from configuration_management import ConfigurationManagement



device_list = []
while True:
    configuration_management = ConfigurationManagement()
    device_factory = DeviceFactory() 

    print("\n--- smart device system ---") 
    print("1. Add Device")
    print("2. View All Devices")
    print("3. Turn ON Device")
    print("4. Turn OFF Device")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        print("\n Device Type：light / fan / air conditioner / heater")
        device_type = input("Enter the device type: ")
        device_name = input("Enter the device name: ")
        device = device_factory.create_product(device_type, device_name)
        device_list.append(device) 
        print(f"{device_name} added successfully.")

    elif choice == '2': 
        if not device_list:
            print("No devices added yet.")
        else:
            print("\n--- Device List ---")
            for index, device in enumerate(device_list, start=1):
                print(f"{index}.Device Kind: {device.kind},  Device Name: {device.name}, Status: {device.status}")

    elif choice == '3':
        device_index = int(input("Enter the device index to turn on: ")) - 1
        if 0 <= device_index < len(device_list):
            device_list[device_index].turn_on()
            print(f"{device_list[device_index].name} turned on.")
        else:
            print("Invalid device index.") 
    elif choice == '4':
        device_index = int(input("Enter the device index to turn off: ")) - 1
        if 0 <= device_index < len(device_list):
            device_list[device_index].turn_off()
            print(f"{device_list[device_index].name} turned off.")
        else:
            print("Invalid device index.") 
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")