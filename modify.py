import os
for file in os.listdir('/Churn-Model'):
    if file.endswith('.py'):
        myfile = file
        print(file)

print('Modifying file : ',myfile )

f = open(myfile,"r")
filedata = f.read()
f.close()

newdata = filedata.replace('epochs=','epochs=2*')
newdata = newdata.split("\n")
newdata.insert(25,"import keras")
newdata = "\n".join(newdata)

f = open(myfile,"w")
f.write(newdata)
f.close()