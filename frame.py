import wx
import os

class mainFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(200,100))
		self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
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
		self.Show(True)
		
	def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
		dlg = wx.MessageDialog(self,"Real Estate Dat Scrapper","Information about this",wx.OK)
		dlg.ShowModal() # Show it
		dlg.Destroy() # finally destroy it when finished.
        
	def OnExit(self,e):
		self.Close(True)
		
	def OnOpen(self,e):
		self.dirname = os.getcwd()
		self.filename = ""
		dlg = wx.FileDialog(self, "Choose a file to open", self.dirname,self.filename, "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
		dlg.Destroy()
	    


app=wx.App(False)
frame = mainFrame(None,"Real Estate Data Scrapper")
app.MainLoop()
