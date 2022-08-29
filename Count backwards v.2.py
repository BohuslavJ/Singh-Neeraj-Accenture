'''
Created by: Bohuslav Juráš
Contact: Bohuslav.juras@seznam.cz
For: Singh Neeraj / Accenture
Applying for position: Test Automation Engineer
First task - "Count backwards"
This program is a bit more robust version of first task. To make it reusable and to try and simulate this program being
used by user who is not working with Python, most values are being inputted by user after prompt (all inputs have some
kind of explanation of what is asked from user) and there is validation of inputs. User can actually input as many
numbers and messages for these numbers as he wants and can customize list boundaries however he likes. However, this
program right now supports only one pair of inputs with customizable message - going to be fixed in new version to
support all inputs.
'''


# Function responsible for getting input variables from user and checking if they are in line with what is expected
# and needed for the rest of program
def input_validation(name):
    if name == "step":
        print("Please keep in mind that '-' symbol in step value means, that you would like to go backwards")
    val = input(f"Please give me {name} value for your test ---> ")
    number_of_tries = 1
    while not val.replace("-", "").isnumeric():
        if number_of_tries > 5:
            exit("You failed to provide correct value 5 times - exiting program")
        val = input(
            f"Please keep in mind that value should be numerical. Please give me new value for {name} ---> ")
        number_of_tries += 1
    return val


# Calling of previous function to get values for the range in which program is going to be printing results
start, stop, step = input_validation("start"), input_validation("stop"), input_validation("step")


# Function responsible for creating lists of dividing numbers and their custom messages which are going to be printed
# if program finds out, that current number in fact is dividable by number in list
def dividing_numbers_list_creator():

    # initialization of lists
    division_numbers, division_popup, division_numbers_pairs, division_popup_pairs = [], [], [], []
    print("To end input of number pairs type '0' ")

    # simple check which is here to give user a chance to jump out of input loop once he is done with inputs
    while "0" not in division_numbers:

        # calling of previous function to get and validate input
        division_numbers.append(input_validation("division number"))
        division_popup.append(input("Please give me message which you would like to display for this number ---> "))

    # lines which are going to be run once user provided his last input. Since we know that last value is going to be 0
    # and nothing can be divided by 0 we need to delete it from our list
    pop_index = division_numbers.index("0")
    division_numbers.pop(pop_index)
    division_popup.pop(pop_index)

    # block of code which lets user input a pair of numbers and customize message for them - this pair has higher
    # priority than single numbers and is going to be resolved first
    plurality = input(f"You inputed these numbers - {division_numbers},"
                      f" do you want to input case when they overlap? Type 'yes' if true ---> ")
    if plurality.lower() == "yes":
        division_numbers_pairs.append(input_validation("division numbers pair"))
        division_numbers_pairs.append(input_validation("division numbers pair"))
        division_popup_pairs.append(input("Please give me message which you would like to display for this pair ---> "))

    return division_numbers, division_numbers_pairs, division_popup, division_popup_pairs


# call of previous function to get rest of inputs which are needed
division_numbers, division_numbers_pairs, division_popup, division_popup_pairs = dividing_numbers_list_creator()


# simple loop which goes in range which user selected and checks if current number can be divided by any number in list.
# If true, instead of printing number, message will be printed. This spot would need some fine-tuning depending on
# clients needs, because there are different variation how to print - if we already found number from list which can
# divide, should we stop and print only it or check for all numbers?
tested_list = [x for x in range(int(start), int(stop)-1, int(step))]


for count in range(int(start), int(stop), int(step)):

    # control bool value which makes sure, that we are not printing any duplicates
    control = False

    # check if user input had a pair of numbers - could be done inside "dividing_numbers_list_creator" function as well
    if division_numbers_pairs != []:
        if count % int(division_numbers_pairs[0]) == 0 and count % int(division_numbers_pairs[1]) == 0:
            print(division_popup_pairs[0])
            continue
    for index, each in enumerate(division_numbers):
        if count % int(each) == 0:
            print(division_popup[index])
            control = True
            break
    if not control:
        print(count)
