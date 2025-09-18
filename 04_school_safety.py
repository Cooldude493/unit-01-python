
#Your Code Must Ask For:
#Which library area? (study room, computer lab, reading corner)
#What's the noise level? (number from 1-10)
#What time of day? (morning, lunch, afternoon)
#How many people are in the area?

#Rules You Must Code:
#Study rooms: noise ≤ 4
#Computer labs: noise ≤ 6
#Reading corners: noise ≤ 2
#During lunch: add +2 to all acceptable levels
#More than 10 people: add +1 to acceptable levels




#Test Your Code With These:
#Input: study room, 3, morning, 8 → Should PASS (within limit)
#Input: reading corner, 5, lunch, 15 → Should FAIL (too noisy even with adjustments)
#Input: computer lab, 7, afternoon, 12 → Should PASS (within adjusted limit)


library_area = input("Which library area? (study room, computer lab, reading corner): ").strip().lower()
noise_level = int(input("What's the noise level? (number from 1-10): ").strip())
time_of_day = input("What time of day? (morning, lunch, afternoon): ").strip().lower()
num_people = int(input("How many people are in the area?: ").strip()) # 23-26 Made the inputs to ask what library area, noise level, time of day, and number of people

study_room = 4
computer_lab = 6
reading_corner = 2 # 28-30 Set the base acceptable noise levels for each area


if num_people > 10:
    study_room += 1
    computer_lab += 1
    reading_corner += 1 # 33-36 Adjusted the acceptable noise levels if there are more than 10 people

if time_of_day == "lunch":
    study_room += 2
    computer_lab += 2
    reading_corner += 2 # 38-41 Adjusted the acceptable noise levels if it's lunch time

if library_area == "study room":
    if noise_level <= study_room:
        print("PASS: Noise level is acceptable in the study room.")
    else: 
        print("FAIL: Noise level is too high in the study room.") 


if library_area == "computer lab":
    if noise_level <= computer_lab:
        print("PASS: Noise level is acceptable in the computer lab.")
    else: 
        print("FAIL: Noise level is too high in the computer lab.")


if library_area == "reading corner":
    if noise_level <= reading_corner:
        print("PASS: Noise level is acceptable in the reading corner.")
    else:
        print("FAIL: Noise level is too high in the reading corner.") # 43-61 Checked the library area and compared the noise level to the acceptable level, printing whether it passed or failed the noise check






