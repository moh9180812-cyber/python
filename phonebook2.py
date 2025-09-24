people = [
    {"name":"ali","number":"0107464354638"}
]
name = input("Name :")
for person in people :
    if person["name"]==name :
        number = person["number"]
        print(f"found :{number}")
        break
