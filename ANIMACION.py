import os
import time
import random
import Tkinter as tk





def main():
	

	L=[]
	pos=[0,10]
	for i in range(20):
		c=[]
		for j in range(20):
			c.append("_")
		L.append(c)

	def printMat(m):
		for j in range(len(m[0])):
			c=""
			for i in range(len(m)):
				c+= str(m[i][j])

			print c
	
	def printAnim(incx,incy):
		
		bContinue = True
		while(bContinue):		
			L[pos[0]][pos[1]]="O"
			printMat(L)
			L[pos[0]][pos[1]]="_"
			time.sleep(0.03)
			os.system('clear')
			pos[0]+=incx
			pos[1]+=incy
			
			if pos[0]>=len(L):
				pos[0]=pos[0]-1
				bContinue=False
	
			elif pos[0]<0:
				pos[0]=pos[0]+1
				bContinue=False

			if pos[1]>=len(L[0]):
				pos[1]=pos[1]-1
				bContinue=False
	
			elif pos[1]<0:
				pos[1]=pos[1]+1	
				bContinue=False
	
		L[pos[0]][pos[1]]="O"
		printMat(L)
		L[pos[0]][pos[1]]="_"

	def onKeyPress1(event):
	    printAnim(0,-1)
	def onKeyPress2(event):
	    printAnim(0,1)
	def onKeyPress3(event):
	    printAnim(-1,0)
	def onKeyPress4(event):
	    printAnim(1,0)
	
	root = tk.Tk()
	root.bind("w", onKeyPress1)
	root.bind("s", onKeyPress2)
	root.bind("a", onKeyPress3)
	root.bind("d", onKeyPress4)
	
	os.system('clear')
	L[pos[0]][pos[1]]="O"
	printMat(L)


	root.mainloop()
	

		
main()
