from splinter import Browser

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
	browser.visit(website)

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

def magicBricks(website):

	# KEYWORD
	KEYWORD_XPATH = '//*[@id="refine_keyword"]'
	KEYWORD = CITY

	# XPATHS
	def GetBedroomXPath(bedrooms):
		if bedrooms < 1 or not isinstance(bedrooms, int):
			return '//*[@id="inputbedrooms"]'
		if bedrooms > 5:
			return '//*[@id="bedrooms_11705-11706-11707-11708-11709-11710"]'
		return '//*[@id="bedrooms_1170'+str(bedrooms-1)+'"]'

	BUY_URL = '/property-for-sale/'
	RENT_URL = '/property-for-rent/'
	
	POSTED_BY_XPATH = '//*[@id="inputinputListings"]'
	BEDROOM_XPATH = '//*[@id="inputbedrooms"]'
	PROPERTY_XPATH = '//*[@id="propertyType"]'

	OWNER_XPATH = '//*[@id="inputListings_I"]'
	BUILDER_XPATH = '//*[@id="inputListings_A"]'
	DEALER_XPATH = '//*[@id="inputListings_B"]'

	FLAT_XPATH = '//*[@id="propertyType_10002_10003_10021_10022_10020"]'
	HOUSE_XPATH = '//*[@id="propertyType_10001_10017"]'
	PLOT_XPATH = '//*[@id="propertyType_10050_10053"]'

	# COUNT
	COUNT = '#resultDiv > div.srpTabAndSort > div.srpTabs > ul > li:nth-child(1) > a > span'

	# VISIT WEBSITE
	if BUY:
		website = website + BUY_URL
	elif RENT:
		website = website + RENT_URL
	print website
	# exit(0)
	browser.visit(website)

	# FILING KEYWORD
	browser.find_by_xpath(KEYWORD_XPATH).fill(KEYWORD)

	# PROPERTY TYPE
	browser.find_by_xpath(PROPERTY_XPATH).click()
	browser.find_by_xpath(FLAT_XPATH).check()
	browser.find_by_xpath(HOUSE_XPATH).check()
	browser.find_by_xpath(PLOT_XPATH).check()

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
	
	# WAITING TO LOAD
	while not browser.is_element_present_by_css(COUNT, wait_time=10):
		pass

	# GETTING THE VALUE
	properties = browser.find_by_css(COUNT).value

	# PRINTING VALUE
	print properties

	# BROWSER QUIT
	browser.quit()

# DEFINITIONS
# WEBSITES = ['http://www.magicbricks.com']
# DEFINITIONS = [magicBricks(WEBSITES[0])]
# DEFINITIONS[0]
# DEFINITIONS[1]
# acres('http://www.99acres.com')
magicBricks('http://www.magicbricks.com')