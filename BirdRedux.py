
import csv
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.filedialog import *
from datetime import datetime
from BirdEntry import *
from Functions import *

class Window:

    def __init__(self, master):
    	self.text_readPath = StringVar()
        self.text_readPath.set("")
        self.btn_changeReadPath = Button(root, text = "Select Original File", command = self.changeReadPath, width=20).grid(row=0, column=0)
        self.lbl_changeReadPath = Label(root, textvariable = self.text_readPath, width=20).grid(row=0, column=1)

        self.text_writePath = StringVar()
        self.text_writePath.set("")
        self.btn_changeWritePath = Button(root, text = "Select New File", command = self.changeWritePath,width=20).grid(row=1, column = 0)
        self.lbl_changeWritePath = Label(root, textvariable = self.text_writePath, width=20).grid(row=1, column=1)

        self.text_nameChangePath = StringVar()
        self.text_nameChangePath.set("")
        self.btn_changeNameChangePath = Button(root, text = "Select Name Change File", command = self.changeNameChangePath,width=20).grid(row=2, column = 0)
        self.lbl_changeNameChangePath = Label(root, textvariable = self.text_nameChangePath, width=20).grid(row=2, column=1)

        
        self.text_err = StringVar()
        self.text_err.set("")
        self.lbl_err = Label(root, textvariable=self.text_err, fg="red").grid(row=7, column=0)

        self.lbl_startDate = Label(root, text="Start Date MM/DD/YYYY (Optional)").grid(row=3, column=0)
        self.startDate = Entry(root)
        self.startDate.grid(row=3, column=1)

        self.lbl_endDate = Label(root, text="End Date MM/DD/YYYY (Optional)").grid(row=4, column=0)
        self.endDate = Entry(root)
        self.endDate.grid(row=4, column=1)

        self.label_obsId = Label(root, text="Observer ID").grid(row=5, column=0)
        self.obsId = Entry(root)
        self.obsId.grid(row=5, column=1)
        
        self.btn_run = Button(root, text = "Run", command = self.run).grid(row=6, column=1)
        
        self.prog_bar = Progressbar(root, orient="horizontal", length=100, mode="determinate", value=0)
        self.prog_bar.grid(row=7, column=1)

        self.hasReadFile = False
        self.hasWriteFile = False
        self.hasNameChangeFile = False

    def changeReadPath(self):
        self.filePath = askopenfilename(filetypes=[("CSV files","*.csv")])
        self.readFile = open(self.filePath, "rt")
        self.reader = csv.reader(self.readFile)
        k = self.filePath.rfind("/")
        self.text_readPath.set(self.filePath[k+1:])
        self.hasReadFile = True

    def changeWritePath(self):
        self.fileToPath = asksaveasfilename(filetypes=[("CSV files","*.csv")])
        self.writeFile = open(self.fileToPath, "wb")
        self.writer = csv.writer(self.writeFile, delimiter=",")
        k = self.fileToPath.rfind("/")
        self.text_writePath.set(self.fileToPath[k+1: ])
        self.hasWriteFile = True

    def changeNameChangePath(self):
        self.text_nameChangePath.set(askopenfilename(filetypes=[("Text files", "*.txt")]))
        self.nameChange = open(self.text_nameChangePath.get(), "rt")
        self.hasNameChangeFile = True

    def run(self):
        structArr = []
        mydict = dict()
        rownum = 0
        nonDupCount = 0
        root.update_idletasks() 
        self.prog_bar["value"] = 0

        if (self.hasReadFile and self.hasWriteFile and self.hasNameChangeFile):
            populateCommonNameDict(self.nameChange)
            self.text_err.set("")
            self.prog_bar["maximum"] = self.reader.line_num
            
            self.writer.writerow(["Common Name", "Date", "County", "Location", "Breeding Code", "UserID", "Count" , "Species Comments"] )
            for row in self.reader:
                self.prog_bar["value"] += 1

                if IsRowInSD(row) and row:
                    for i in range(20 - len(row)): #pad end of row
                        row.append("")

                    birdEntry = BirdEntry(row[1], row[4], row[6], row[7], row[10], row[18] , row[19])
                    birdHash = birdEntry.commonName + birdEntry.county + birdEntry.date

                    if birdHash in mydict:
                        mydict[birdHash].count += birdEntry.count
                    else:
                        structArr.append(birdEntry)
                        mydict[birdHash] = structArr[nonDupCount]
                        nonDupCount += 1
                        
                rownum += 1

            for i in range(nonDupCount):
                bird = structArr[i]
                if IsValidBird(bird):
                    self.writer.writerow([bird.commonName, bird.date, bird.county, bird.loc, bird.breed, self.obsId.get(), bird.count, bird.scomm])

            print ("Done!")
        else:
            self.text_err.set("One of the files isn't set.")
    def on_closing():
        self.writeFile.close()
        self.readFile.close()
        

winWidth = 400
winHeight = 400
root = Tk()
b = Window(root)
root.geometry("400x200+200+200") 
root.mainloop()