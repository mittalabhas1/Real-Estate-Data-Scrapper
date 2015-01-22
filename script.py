from splinter import Browser
from time import sleep

browser = Browser()

# KEYWORD
CITY = 'Bangalore'
LOCALITY = '(All)'

# VARIABLES
BUY = False
RENT = True
OWNER = True
BUILDER = False
DEALER = False
BEDROOM = True
BEDROOM_NO = 2

def acres(website):

	# WEBSITE
	WEBSITE = 'http://www.99acres.com'

	# KEYWORD
	KEYWORD_KEY = 'keyword'
	KEYWORD = CITY+' '+LOCALITY

	# XPATHS
	def GetBedroomXPath(bedrooms):
		if bedrooms < 1 or not isinstance(bedrooms, int):
			return '//*[@id="s_bedroom_num"]/div/div[2]/div/div/a[1]'
		if bedrooms > 9:
			bedrooms = 10
		return '//*[@id="bd_'+str(bedrooms)+'"]'

	BUY_XPATH = '//*[@id="ResBuyTab"]'
	RENT_XPATH = '//*[@id="ResRentTab"]'
	
	POSTED_BY_XPATH = '//*[@id="posted_by_wrap"]/div[2]/a'
	BEDROOM_XPATH = '//*[@id="bedroom_num_wrap"]/div[2]/a'
	
	OWNER_XPATH = '//*[@id="p_o"]'
	BUILDER_XPATH = '//*[@id="p_a"]'
	DEALER_XPATH = '//*[@id="p_b"]'
	
	SUBMIT_XPATH = '//*[@id="submit_query"]'

	# COUNT
	COUNT = 'input#PROP_COUNT'

	# VISIT WEBSITE
	browser.visit(WEBSITE)

	# BUY OR RENT
	if BUY:
		browser.find_by_xpath(BUY_XPATH).click()
	elif RENT:
		browser.find_by_xpath(RENT_XPATH).click()

	# FILING KEYWORD
	browser.fill(KEYWORD_KEY, KEYWORD)

	# BEDROOMS
	if BEDROOM:
		browser.find_by_xpath(BEDROOM_XPATH).click()
		browser.find_by_xpath(GetBedroomXPath(BEDROOM_NO)).click()

	# POSTED BY
	browser.find_by_xpath(POSTED_BY_XPATH).click()
	if OWNER:
		browser.find_by_xpath(OWNER_XPATH).click()
	elif BUILDER:
		browser.find_by_xpath(BUILDER_XPATH).click()
	elif DEALER:
		browser.find_by_xpath(DEALER_XPATH).click()
	
	# SUBMIT
	browser.find_by_xpath(SUBMIT_XPATH).click()
	
	# WAITING TO LOAD
	while not browser.is_element_present_by_css(COUNT, wait_time=10):
		pass

	# GETTING THE VALUE
	properties = browser.find_by_css(COUNT).value

	# PRINTING VALUE
	print properties

	# BROWSER QUIT
	browser.quit()

def magicBricks():

	# WEBSITE
	WEBSITE = 'http://www.magicbricks.com'

	# KEYWORD
	KEYWORD_KEY = 'keyword'
	KEYWORD = CITY

	# XPATHS
	def GetBedroomXPath(bedrooms):
		if bedrooms < 1 or not isinstance(bedrooms, int):
			return '//*[@id="inputbedrooms"]'
		if bedrooms > 5:
			return '//*[@id="bedrooms_11705-11706-11707-11708-11709-11710"]'
		return '//*[@id="bedrooms_1170'+str(bedrooms-1)+'"]'

	BUY_XPATH = '//*[@id="buyTab"]'
	RENT_XPATH = '//*[@id="rentTab"]'
	
	POSTED_BY_XPATH = '//*[@id="inputinputListings"]'
	BEDROOM_XPATH = '//*[@id="inputbedrooms"]'

	OWNER_XPATH = '//*[@id="inputListings_I"]'
	BUILDER_XPATH = '//*[@id="inputListings_A"]'
	DEALER_XPATH = '//*[@id="inputListings_B"]'

	BUY_PROPERTY_XPATH = '//*[@id="buy_propertyType"]'
	BUY_FLAT_XPATH = '//*[@id="propType_buy_chk_10002_10003_10021_10022"]'
	BUY_HOUSE_XPATH = '//*[@id="propType_buy_chk_10001_10017"]'
	BUY_PLOT_XPATH = '//*[@id="propType_buy_chk_10000"]'

	RENT_PROPERTY_XPATH = '//*[@id="rent_propertyType"]'
	RENT_FLAT_XPATH = '//*[@id="propType_rent_chk_10002_10003_10021_10022_10020"]'
	RENT_HOUSE_XPATH = '//*[@id="propType_rent_chk_10001_10017"]'
	RENT_PLOT_XPATH = '//*[@id="propType_rent_chk_10050_10053"]'

	SUBMIT_XPATH = '//*[@id="btnPropertySearch"]'

	# COUNT
	COUNT = '#resultDiv > div.srpTabAndSort > div.srpTabs > ul > li:nth-child(1) > a > span'

	# VISIT WEBSITE
	browser.visit(WEBSITE)

	# BUY OR RENT
	if BUY:
		browser.find_by_xpath(BUY_XPATH).click()
	elif RENT:
		browser.find_by_xpath(RENT_XPATH).click()

	# FILING KEYWORD
	browser.fill(KEYWORD_KEY, KEYWORD)

	# PROPERTY TYPE
	if BUY:
		browser.find_by_xpath(BUY_PROPERTY_XPATH).click()
		browser.find_by_xpath(BUY_FLAT_XPATH).check()
		browser.find_by_xpath(BUY_HOUSE_XPATH).check()
		browser.find_by_xpath(BUY_PLOT_XPATH).check()
	elif RENT:
		browser.find_by_xpath(RENT_PROPERTY_XPATH).click()
		browser.find_by_xpath(RENT_FLAT_XPATH).check()
		browser.find_by_xpath(RENT_HOUSE_XPATH).check()
		browser.find_by_xpath(RENT_PLOT_XPATH).check()

	# SUBMIT
	browser.find_by_xpath(SUBMIT_XPATH).click()

	# WAITING TO LOAD
	while not browser.is_element_present_by_css(COUNT, wait_time=10):
		pass

	# GETTING THE INITIAL VALUE
	properties = browser.find_by_css(COUNT).value

	# BEDROOMS
	if BEDROOM:
		browser.find_by_xpath(BEDROOM_XPATH).click()
		browser.find_by_xpath(GetBedroomXPath(BEDROOM_NO)).check()

	# POSTED BY
	browser.find_by_xpath(POSTED_BY_XPATH).click()
	if OWNER:
		browser.find_by_xpath(OWNER_XPATH).click()	
	elif BUILDER:
		browser.find_by_xpath(BUILDER_XPATH).click()
	elif DEALER:
		browser.find_by_xpath(DEALER_XPATH).click()

	# PUT TO SLEEP
	sleep(2)

	# GETTING THE VALUE
	properties = browser.find_by_css(COUNT).value

	# PRINTING VALUE
	print properties

	# BROWSER QUIT
	browser.quit()

# acres()
magicBricks()