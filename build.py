from splinter import Browser

def getLatestBuildVersion():
# RETURNS THE LATEST VERSION OF THE SOFTWARE AVAILABLE TO DOWNLOAD

	# WEBSITE
	WEBSITE = 'http://mittalabhas1.github.io/Real-Estate-Data-Scrapper/'

	# VERSION
	VERSION = 'div#version'

	# VISIT WEBSITE
	browser = Browser('phantomjs')
	browser.visit(WEBSITE)

	# GETTING THE VALUE
	version = browser.find_by_css(VERSION).value

	# QUIT BROWSER
	browser.quit()

	# RETURN VALUE
	return version

def getCurrentBuildVersion():
# RETURNS THE CURRENT VERSION OF THE SOFTWARE

	# RETURN VALUE
	return 'v0.1'