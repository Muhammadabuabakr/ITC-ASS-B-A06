## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR cumulative_marks() FUNCTION GOES HERE ###
def cumulative_marks(string):
	"""This function change format of roll_number then read the name of student and 
	at last add the number of student.After that it append all data into new list """
    lst =[]
    lst1 = []
    d_marks = {}
    marks = 0

    if string == None:
        return None

    for i in string:
        roll_no = i[0]
        batch = i[0][1:3]
        p = i[0][0].upper() + str('-')
        roll_no = batch + p + str(roll_no[3:])
        names = i[1]
        if len(i) >= 3:
            for j in i[2:]:
                if j == None or type(j) == str:
                    marks+=0
                else:
                    marks += j
                d_marks[roll_no] = marks
            marks = 0
        else:
            d_marks[roll_no] = marks
        lst = roll_no,names,d_marks[roll_no]
        lst1.append(lst)

    return lst1
#### End OF MARKER

if __name__ == '__main__':
    results = [
        ('p101111', 'Muhammad Amin', 64, 78.5, 89, 25, 99),
        ('p101112', 'Tehseen Khan', 14, 28.5, 83, 76),
        ('p101113', 'Tauqeer Ali', 87, None, 1.6)
    ]

#    print cumulative_marks(results)
    # output: [('10P-1111', 'Muhammad Amin', 355.5), ('10P-1112', 'Tehseen Khan', 201.5), ('10P-1113', 'Tauqeer Ali', 88.6)]

