import csv, sys, tabulate, time, tkinter
# -----------------------------------------------------------
def main():
    _data = get_csv_list()
     #print(_data)
    _sublists = generate_groups(_data)
    print(_sublists)
    #print(_sublists[1][2][0]) #output hammond
    group_numbers = give_group_numbers(_sublists)

# -----------------------------------------------------------
# csv change to list with 2-ples (name,timing)
# def open_csv_file
def get_csv_list():
    filename = input("Choose Classlist: ")
    file = open(filename)
    reader = csv.reader(file)
    data=list(reader)
    return data
#print(data)
#print(data[1][0])
# -----------------------------------------------------------
# groups - input number of pax per group and divide given list into groups of n pax. Each being a 2 -ple
# def split_in_groups credits: https://theprogrammingexpert.com/python-split-list-into-n-sublists/
# find out what is the yield() function
def generate_groups(li_st):
    n = input("How many groups do you want? ")
    length_sub_list = len(li_st) // int(n) # floor division
    list_of_groups = []
    for i in range(0, len(li_st), length_sub_list): # range(start, stop, step)
        list_of_groups.append(li_st[i : i+length_sub_list])
    return list_of_groups
# -----------------------------------------------------------
# enumerate the groupps with group numbers
def give_group_numbers(_list2):
    return len(_list2)
# -----------------------------------------------------------
# stopwatch => start, stop and split
# https://www.youtube.com/watch?v=mdfuJPGLhPM
#def stopwatch:
# maybe just skip the stopwatch

# select group number based on above grouping and use stopwatch

# first group click names and split timings with a timing for each pax
# followed by 2nd, 3rd, 4th groups etc

# timing will be given and input back into 2-ple's second parameter

# output all 2-ples back into list and back into csv

if __name__ == "__main__":
    main()