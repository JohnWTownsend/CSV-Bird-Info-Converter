
import csv
from tkinter import *
from tkinter.filedialog import *
from datetime import datetime
from BirdEntry import *
from Functions import *
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
		self.filePath = askopenfilename(filetypes=[("CSV files","*.csv")])
		self.dBfile = open(self.filePath, "rt")
		self.reader = csv.reader(self.dBfile)
		k = self.filePath.rfind("/")
		self.fp.set(self.filePath[k+1:])

	def changeWritePath(self):
		self.fileToPath = asksaveasfilename(filetypes=[("CSV files","*.csv")])
		self.outdBfile = open(self.fileToPath, "wt", newline='')
		self.writer = csv.writer(self.outdBfile, delimiter=",")
		k = self.fileToPath.rfind("/")
		print (self.fileToPath)
		self.ftp.set(self.fileToPath[k+1: ])

	def isWithinDates(self,rowdate):
		if(startDate == "" and endDate == ""):
			return True
		if checkdate <= end and checkdate >= start:
			return True


	def run(self):
		
		structArr = []
		mydict = dict()
		rownum = 0
		actualRow = 0
		root.update_idletasks()	
			
		for row in self.reader:
			if rownum == 0:
				self.writer.writerow(["Common Name", "Date", "County", "Location", "Breeding Code", "UserID", "Count" , "Species Comments"] )
				if any(char.isdigit() for char in row):
					if IsRowInSD(row):
						for i in range(20 - len(row)):
							row.append("")

						birdEntry = BirdEntry(row[1], row[4], row[6], row[7], row[10], row[18] , row[19])
						curHashString = birdEntry.cName + birdEntry.county + birdEntry.date

						if curHashString in mydict:
							mydict[curHashString].count += birdEntry.count
						else:
							structArr.append(birdEntry)
							mydict[curHashString] = structArr[actualRow]
							actualRow += 1
			else:
				if IsRowInSD(row):
					for i in range(20 - len(row)):
						row.append("")

					birdEntry = BirdEntry(row[1], row[4], row[6], row[7], row[10], row[18] , row[19])
					curHashString = birdEntry.cName + birdEntry.county + birdEntry.date

					if curHashString in mydict:
						mydict[curHashString].count += birdEntry.count
					else:
						structArr.append(birdEntry)
						mydict[curHashString] = structArr[actualRow]
						actualRow += 1
			rownum += 1

		for i in range(actualRow):
			if IsValidBird(structArr[i]):
				self.writer.writerow([structArr[i].cName, structArr[i].date, structArr[i].county, structArr[i].loc, structArr[i].breed, self.text_obsId.get(), structArr[i].count, structArr[i].scomm])
		self.outdBfile.close()
		self.dBfile.close()
		print ("Done!")

winWidth = 400
winHeight = 400

root = Tk()
b = Window(root)
root.geometry("400x200+200+200") 
root.mainloop()