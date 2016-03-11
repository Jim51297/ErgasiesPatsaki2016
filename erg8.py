table = []

#to arxeio table.txt einai kai auto anebasmeno sto github!
file_in = open("table1.txt")
for line in file_in:
	line = line.replace('""' , "")
	a = line.split(",")
	a[7] = "0"
	table.append(a)


file_in.close()


rotate1 = zip(*table[::1])
for i in range(8):
    print rotate1[i]
print "\n"
rotate2 = zip(*rotate1[::1])
for i in range(8):
    print rotate2[i]
print "\n"
rotate3 = zip(*rotate2[::1])
for i in range(8):
    print rotate3[i]

#source:
#http://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
