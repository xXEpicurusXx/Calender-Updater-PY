# variables for work completed 


nouns = [
"床",
"フローリング",
"キッチン",
"巾木",
"バニヤ",
"ボード",
"枠",
"壁",
"天井",
"下地",
"パネル",
"洗面台",
"トイレ",
"カップボード",
"お風呂"]

locations = [
" ",
"玄関",
"キッチン",
"トイレ",
"お風呂",
"洗面所",
"部屋",
"和室"]

verbs = [
"設える",
"はがす", 
"解体",
"レベル調整する"]

work = []

def calender_program():

# Beginning of program interface 
    print("Welcome to the calender translater and organizer assistant.")
    print("Lets get started!\n")

    # asking for the daily hours of operation 
    hours = input("Was the hours of operations from 0630 - 1730? \n")
    if hours != "n":
        hours = "0630 - 1730"

    else:
        hours_worked = input("Please input the hours of operation worked: \n")
        hours = hours_worked


    # Asking for overtime worked 
    time = input("Is there additional overtime?\n")
    if time != "y":
        time = 2

    else:
        overtime = input("How many additional overtime ours was worked for the day?\n")
        overtime_total = + int(overtime) + (2)
        time = overtime_total

    # Asking about work completed for the day 
    #while loop here
    end_of_program = False

    while not end_of_program: 

        print("\nFrom the list of locations pick the associated number for the work completed:")
        for i in locations:
            print(locations.index(i) +1, end=" ")
            print(" ",i)
        location = locations[int(input("\nmake a selection: \n")) -1]



        print("\nFrom the list of nouns pick the associated number for the work completed: \n")
        for ii in nouns:
            print(nouns.index(ii) +1, end=" ")
            print(" ",ii)
        noun = nouns[int(input("\nmake a selection: \n")) -1]

        print("\nFrom the list of verbs pick the associated number for the work completed: \n")
        for iii in verbs:
            print(verbs.index(iii) +1, end=" ")
            print(" ",iii)
        verb = verbs[int(input("\nmake a selection: \n"))- 1]  

        work_completed = (location + "で" + noun + "を" + verb)
        work.append(work_completed) 

        more_work = input("Any additional work completed?: \n")
        if more_work != "y":
            end_of_program = True



    # for additional information section, 
    # if no then N/A
    # if yes then input data



    print("Copy this and add it to the calender...\n")

    print("時間")
    print(hours)

    print("\n残業")
    print(time)

    print("\n完成した仕事")
    for iiii in work:
        #print(work.index(iiii) +1, end=" ")
        print(iiii)


    print("\nその他の注意事項")
    print("n/a")
# for additional information section, 
# if no then N/A
# if yes then input data

calender_program()