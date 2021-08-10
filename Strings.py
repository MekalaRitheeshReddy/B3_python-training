sample = "Ritheesh Reddy"

"""

R   i   t   h   e   e   s   h    R e   d   d  y
0   1   2   3   4   5   6   7    8  9 10  11 12  13

"""

print("it will print all the content in string",sample)


print(sample[0])

print(sample[3])

print(sample[1:12])

print(sample[4:7])

print(sample[3:])

print(sample[0:])


#LENGTH OF STRING
print("length of string:",len(sample))

#upper
a = "avinash"
print("using upper method:",a.upper())

#replace
b = "Ritheesh"
print(b.replace("e","a"))

#capitalize
#isnumaric
#isalpha
#split

#string concardination
print(a + " " + b)

#format

string1 = "Avinash"
string2 = "python"


text = "Hi,{1} welcome to,{0}"
text = "Hi,{} welcome to,{}"

print(text.format(string2,string1))



