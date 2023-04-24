import time
file = open(time.strftime('%d.%m.%y %X') +'.txt',"w")

def testfunction():
    for i in range(5):
        print("This is just a function that prints 'this is just a function' for i times...")


start = time.time()
testfunction()
end = time.time()
result = end-start
result = format(result)


file.write('Running time of the program – ')
file.write(result)
file.close()
