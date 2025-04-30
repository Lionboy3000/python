name=input("enter your own word: ")
char=input("enter letter to check")
i=0
count=0
while(i<len(name)):
    if(name[i]==char):
        count +=1
        i+=1
print(f"number of time that {char} is present in {name} is: {count}.")