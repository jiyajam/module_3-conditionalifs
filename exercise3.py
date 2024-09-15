#####################1

length = int(input("please put in the length of a zander in centimeters: "))
size_limit = 42.0

if length >= size_limit:
    print ("The fish fulfills the size limit, have a good meal ! ")
else:
   difference = size_limit - length
   print(f"Release the fish back into the lake and it is {difference} centimeters shorter than the required size")


#####################2

cabin_class = str(input("please type in your cabin class for its description(LUX/A/B/C): ")).upper()
if cabin_class == "LUX":
    print("you have an upper-deck cabin with a balcony")
if cabin_class == 'A':
    print ( "you have a cabin above the car deck, equipped with a window.")
elif cabin_class == 'B':
    print ("you have a  windowless cabin above the car deck.")
elif cabin_class == 'C':
     print ("you have a windowless cabin below the car deck")
else :
    print ("Invalid cabin class")
           

#####################3

gender = str(input("please type in your gender(M/F): ")).upper()
haemoglobin_level = float(input("please type in your haemoglobin level: "))

if gender == 'M'and haemoglobin_level <= 134 :
        print ("haemoglobin is low")
elif gender == 'M'and 134 <= haemoglobin_level <= 167:
        print("haemoglobin is normal")
elif gender == 'M' and haemoglobin_level > 167 :
        print("haemoglobin is high")
else:
    if gender == 'F'and haemoglobin_level <= 117:
        print("haemoglobin is low")
    elif gender == 'F'and 117 <= haemoglobin_level <= 155:
        print("haemoglobin is normal")
    elif gender == 'F'and haemoglobin_level > 155 :
         print("haemoglobin is high")



####################4

year = int(input("please type in your YEAR: "))
if year % 400 == 0 or year % 4 ==0 and year % 100 != 0:
        print(f"year : {year} is a leap year")
else:
    print(f"year: {year} not a leap year")
