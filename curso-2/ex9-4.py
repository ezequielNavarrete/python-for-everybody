"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent
the greatest number of mail messages. The program looks for 'From ' lines and takes 
the second word of those lines as the person who sent the mail. The program creates 
a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic=dict()
for lines in handle:
    linea=lines.rstrip()
    if linea.startswith("From"):
        words=linea.split()
        if len(words)>2:
            dic[words[1]]=dic.get(words[1],0)+1
bigOneKey=None
bigOneValue=None
for key in dic:
    if bigOneKey is None or dic[key]>bigOneValue:
        bigOneKey=key
        bigOneValue=dic[key]

print(bigOneKey,bigOneValue)