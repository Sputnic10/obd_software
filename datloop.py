import time

#define criteria

datf = open("Demo-DataFile.dat","r")
print("Time to run program: ")
criteria = time.time() + int(input())

#loops program
while(time.time() < criteria):
	datf = open("Demo-DataFile.dat","r").readlines()
	
	#modifications to file?
	
	print(datf)
	print("\n\n")
print("done")