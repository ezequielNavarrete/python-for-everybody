fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
for line in fh:
    lin=line.rstrip()
    if lin.startswith("From"):
        aux=lin.split()
        if len(aux)>2:
            print(aux[1])
            count+=1
        
print("There were", count, "lines in the file with From as the first word")
