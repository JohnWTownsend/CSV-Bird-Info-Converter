import csv
from Tkinter import *
import tkFileDialog
from datetime import datetime


def commaCheck(string):
	new = ""
	for char in range(len(string)):
		if string[char] == ",":
			new += ";"
		else:
			new += string[char]
	return "".join(new)	


class BirdEntry: # just in case cName, count, state, county, date
	def __init__(self, cName, count, county, loc, date, breed, scomm):
		if cName == "Orchard Orioloe":
			self.cName = "Orchard Oriole"
			print "Changed Oriole"
		elif cName == "White-winged Junco":
			self.cName = "Dark-eyed Junco"
			print "Changed Junco"
		elif cName == "LeConte's Sparrow":
			self.cName = "Le Conte's Sparrow"
			print "LeConte change"
		elif cName == "McGillivray's Warlber":
			self.cName = "MacGillivray's Warbler"
			print "MAC change"
		else:	
			self.cName = cName
		
		try:
			self.count = int(count)
		except ValueError:
			self.count = 0
		
		self.county = county
		
		loc = commaCheck(loc)	
		self.loc = loc	
		
		self.date = date

		breed = commaCheck(breed)
		self.breed = breed

		scomm = commaCheck(scomm)
		self.scomm = scomm

class Window:

	def __init__(self, master):
		self.fp = StringVar()
		self.fp.set("")
		self.ftp = StringVar()
		self.ftp.set("")
		self.textVar = StringVar()
		self.textVar.set("")

		self.button_cfp = Button(root, text = "Select Original File", command = self.changeFilePath, width=20).grid(row=0, column=0)
		self.label_cfp = Label(root, textvariable = self.fp, width=20).grid(row=0, column=1)
		
		self.button_cwp = Button(root, text = "Select New File", command = self.changeWritePath,width=20).grid(row=1, column = 0)
		self.label_cwp = Label(root, textvariable = self.ftp, width=20).grid(row=1, column=1)
		
		self.startDateLabel = Label(root, text="Start Date MM/DD/YYYY (Optional)").grid(row=2, column=0)
		self.startDate = Entry(root)
		self.startDate.grid(row=2, column=1)

		self.endDateLabel = Label(root, text="End Date MM/DD/YYYY (Optional)").grid(row=3, column=0)
		self.endDate = Entry(root)
		self.endDate.grid(row=3, column=1)

		self.label_obsId = Label(root, text="Observer ID").grid(row=4, column=0)
		self.text_obsId = Entry(root)
		self.text_obsId.grid(row=4, column=1)
		
		self.button_run = Button(root, text = "Run", command = self.run).grid(row=5, column=1)
		
		self.label_err = Label(root, textvariable=self.textVar, fg="red").grid(row=6, column=0)

	def changeFilePath(self):
		self.filePath = tkFileDialog.askopenfilename(filetypes=[("CSV files","*.csv")])
		self.dBfile = open(self.filePath, "rb")
		self.reader = csv.reader(self.dBfile)
		k = self.filePath.rfind("/")
		self.fp.set(self.filePath[k+1:])

	def changeWritePath(self):
		self.fileToPath = tkFileDialog.asksaveasfilename(filetypes=[("CSV files","*.csv")])
		self.outdBfile = open(self.fileToPath, "wb")
		self.writer = csv.writer(self.outdBfile, delimiter=",")
		k = self.fileToPath.rfind("/")
		print self.fileToPath
		self.ftp.set(self.fileToPath[k+1: ])

	def isWithinDates(self,rowdate):
		if(startDate == "" and endDate == ""):
			return True
		try:
			checkdate = datetime.strptime(rowdate, '%m-%d-%Y')
		except:
			return False
		try:
			start = datetime.strptime(self.startDate.get(), '%m/%d/%Y')
		except:
			try:
				end = datetime.strptime(self.endDate.get(), '%m/%d/%Y')
			except:
				return True
			if checkdate < end:
				return True
			else:
				return False
		try:
			end = datetime.strptime(self.endDate.get(), '%m/%d/%Y')
		except:
			if checkdate >= start:
				return True
			else:
				return False
		if checkdate <= end and checkdate >= start:
			return True


	def run(self):
		
		structArr = []
		mydict = dict()
		rownum = 0
		actualRow = 0
		opened = 1
		try:
			self.textVar.set(" ")
			root.update_idletasks()	
			
			for row in self.reader:
				if rownum == 0:
					self.writer.writerow([row[1], row[10], row[6], row[7], row[18], "UserID", row[4] , row[19]] )
				else:
					if row[5] == "US-SD":# and self.isWithinDates(row[10]):
						print "I here"
						curHashString = row[1] + row[6] + row[10]	#gets the date bird was entered
						
						if len(row) < 21:
							for i in range(21-len(row)):
								row.append("")
						if mydict.has_key(curHashString):		#if bird was entered at sameish time as another of same species
							try:
								mydict[curHashString].count += int(row[4])
							except ValueError:
								mydict[curHashString].count += 0
								print "ValueError"
						else:
							structArr.append(BirdEntry(row[1], row[4], row[6], row[7], row[10], row[18] , row[19]))
							current = len(structArr)-1
							mydict[curHashString] = structArr[current]
							actualRow += 1
							print actualRow
				rownum += 1			
		except:
			self.textVar.set("No read and/or write file specified")
			root.update_idletasks()
			opened = 0
		if opened == 1:	
			print "done"
			for i in range(actualRow-2):
				self.writer.writerow([structArr[i].cName, structArr[i].date, structArr[i].county, structArr[i].loc, structArr[i].breed, self.text_obsId.get(), structArr[i].count, structArr[i].scomm])
			self.outdBfile.close()
			self.dBfile.close()

winWidth = 400
winHeight = 400

root = Tk()
b = Window(root)
root.geometry("400x200+200+200") 
root.mainloop()