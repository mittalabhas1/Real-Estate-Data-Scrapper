import wx, os, csv, time
from script import *

class mainFrame(wx.Frame):

	def __init__(self,parent,title):

		#Global variables
		self.dirname = os.getcwd()
		self.filename = ""

		wx.Frame.__init__(self,parent,title=title,size=(600,150))
		
		# self.CreateStatusBar()
		filemenu = wx.Menu()

		menu_about = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
		self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)

		menu_open = filemenu.Append(wx.ID_OPEN, "&Open File","Open a new file")
		self.Bind(wx.EVT_MENU, self.OnOpen, menu_open)

		filemenu.AppendSeparator()
		menu_exit = filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")
		self.Bind(wx.EVT_MENU,self.OnExit, menu_exit)

		menuBar = wx.MenuBar()
		# Adding the "filemenu" to the MenuBar
		menuBar.Append(filemenu,"&File")
		# Adding the MenuBar to the Frame content.
		self.SetMenuBar(menuBar)

		#Panel 
		panel = wx.Panel(self,size=(600,100))

		self.filepath = wx.StaticText(panel, label="Choose a file", pos=(40,50))
		self.openButton =wx.Button(panel, wx.ID_OPEN, "Open File", pos=(300,45))
		self.Bind(wx.EVT_BUTTON, self.OnOpen,self.openButton)
		self.openButton.SetDefault()

		self.startButton = wx.Button(panel, wx.ID_FILE, "Run Parity Generator", pos=(400,45))
		self.Bind(wx.EVT_BUTTON, self.OnStart, self.startButton)

		#Progress Bar
		self.progressbar = wx.Gauge(panel,wx.ID_STATIC,size=(500,30),pos=(50,100))

		self.Show(True)
		
	def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
		dlg = wx.MessageDialog(self,"Real Estate Parity Generator", "About", wx.OK)
		# Show it
		dlg.ShowModal()
		# finally destroy it when finished.
		dlg.Destroy()

	def OnExit(self,e):
		self.Close(True)

	def OnOpen(self,e):
		dlg = wx.FileDialog(self, "Choose a CSV file to run parity", self.dirname,self.filename, "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			self.filepath.SetLabel("File: "+self.filename)
		dlg.Destroy()
		row_count = sum(1 for row in csv.reader(open(self.dirname+'/'+self.filename)))
		self.progressbar.SetValue(0)
		self.progressbar.SetRange(row_count)

	def OnStart(self,e):
		if self.filename == "":
			dlg = wx.MessageDialog(self,"Please choose a valid CSV file to continue","Error",wx.OK)
			dlg.ShowModal() # Show it
			dlg.Destroy() # finally destroy it when finished.
		else:
			print self.dirname+'/'+self.filename
			localtime = time.asctime(time.localtime(time.time()))
			readfile = open(self.dirname+'/'+self.filename,'rb')
			writefile = open(self.dirname+'/'+localtime+'.csv','wb')
			fread = csv.reader(readfile)
			fwrite = csv.writer(writefile)
			BROWSER = Browser()
			val=0 #value for progress bar
			for row in fread:

				def check_bedroom(bedrooms):
					if bedrooms != '':
						if int(bedrooms) > 0:
							return int(bedrooms)
						else:
							return False
					else:
						return False

				TYPE = row[0].lower()
				CITY = row[1]
				LOCALITY = row[2]
				POSTED_BY = row[4].lower()
				BEDROOMS = check_bedroom(row[3])
				
				ac = acres(BROWSER, TYPE,CITY,LOCALITY,POSTED_BY,BEDROOMS)
				mb = magicBricks(BROWSER, TYPE,CITY,LOCALITY,POSTED_BY,BEDROOMS)

				fwrite.writerow(row+[ac]+[mb])

				self.progressbar.SetValue(val+1) #Update the progress bar
				val += 1
			
			BROWSER.quit()

			dlg = wx.MessageDialog(self,"Please check the results in "+ localtime+'.csv',"Download Completed!",wx.OK)
			dlg.ShowModal()
			dlg.Destroy()

app=wx.App(False)
frame = mainFrame(None,"Real Estate Data Scrapper")
app.MainLoop()
