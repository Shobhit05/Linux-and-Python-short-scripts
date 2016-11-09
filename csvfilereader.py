import csv


with open('something.csv') as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')

    dates=[]
    colors=[]

    for row in readcsv:
        print row
        color=row[3]
        date=row[1]

        colors.append(color)
        dates.append(date)


    print dates
    print colors

    


try:
    #some of ur code if it gives the  error now



except Exception,e:
    print(e)

print('sahdias')



print('''
so this is a
perfect exapmple of printing
the code in another line

''')
