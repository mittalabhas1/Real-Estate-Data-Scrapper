import wx, os, csv
from script import *

class mainFrame(wx.Frame):

	def __init__(self,parent,title):

		#Global variables
		self.dirname = os.getcwd()
		self.filename = ""

		wx.Frame.__init__(self,parent,title=title,size=(300,100))
		#self.control = wx.TextCtrl(self)#,style=wx.TE_MULTILINE)

		self.CreateStatusBar()
		filemenu = wx.Menu()

		menu_about = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
		self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)

		menu_open = filemenu.Append(wx.ID_OPEN, "&Open File","Open a new file")
		self.Bind(wx.EVT_MENU, self.OnOpen, menu_open)

		filemenu.AppendSeparator()
		menu_exit = filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

		self.Bind(wx.EVT_MENU,self.OnExit, menu_exit)
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

		#Panel 
		panel = wx.Panel(self,size=(200,50))
		#self.quote = wx.StaticText(panel, label="File")

		self.openButton =wx.Button(panel, wx.ID_OPEN, "Open")
		self.Bind(wx.EVT_BUTTON, self.OnOpen,self.openButton)
		self.openButton.SetDefault()

		self.startButton = wx.Button(panel, wx.ID_FILE, "Start", pos=(100,0))
		self.Bind(wx.EVT_BUTTON, self.OnStart, self.startButton)

		self.Show(True)
		
	def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
		dlg = wx.MessageDialog(self,"Real Estate Dat Scrapper","Information about this",wx.OK)
		dlg.ShowModal() # Show it
		dlg.Destroy() # finally destroy it when finished.
        
	def OnExit(self,e):
		self.Close(True)
		
	def OnOpen(self,e):
		dlg = wx.FileDialog(self, "Choose a file to open", self.dirname,self.filename, "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
		dlg.Destroy()

	def OnStart(self,e):
		if self.filename == "":
			dlg = wx.MessageDialog(self,"Please choose a file","Choose a file for scraping",wx.OK)
			dlg.ShowModal() # Show it
			dlg.Destroy() # finally destroy it when finished.
		else:
			print self.dirname+'/'+self.filename
			readfile = open(self.dirname+'/'+self.filename,'rb')
			writefile = open(self.dirname+'/'+self.filename[:-4]+'result.csv','wb')
			fread = csv.reader(readfile)
			fwrite = csv.writer(writefile)
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

				BROWSER = Browser()
				ac = acres(BROWSER, TYPE,CITY,LOCALITY,POSTED_BY,BEDROOMS)
				mb = magicBricks(BROWSER, TYPE,CITY,LOCALITY,POSTED_BY,BEDROOMS)
				BROWSER.quit()

				fwrite.writerow(row+[ac]+[mb])
				dlg = wx.MessageDialog(self,"Download Completed! Please check the results in "+ self.filename[:-4]+'result.csv',"Results",wx.OK)
				dlg.ShowModal()


app=wx.App(False)
frame = mainFrame(None,"Real Estate Data Scrapper")
app.MainLoop()
