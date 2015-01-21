from splinter import Browser

browser = Browser()

# KEYWORD
CITY = 'Bangalore'
LOCALITY = '(All)'
KEYWORD = CITY+' '+LOCALITY

# VARIABLES
BUY = True
RENT = False
OWNER = True
BUILDER = False
DEALER = False
BEDROOM = True
BEDROOM_NO = 2

def acres(website):

	# KEYWORD
	KEYWORD_KEY = 'keyword'

	# XPATHS
	def GetBedroomXPath(bedrooms):
		if bedrooms < 1 or not isinstance(bedrooms, int):
			return '//*[@id="s_bedroom_num"]/div/div[2]/div/div/a[1]'
		if bedrooms > 9:
			bedrooms = 10
		return '//*[@id="bd_'+str(bedrooms)+'"]'

	BUY_XPATH = '//*[@id="ResBuyTab"]'
	RENT_XPATH = '//*[@id="ResRentTab"]'
	OWNER_XPATH = '//*[@id="p_o"]'
	BUILDER_XPATH = '//*[@id="p_a"]'
	DEALER_XPATH = '//*[@id="p_b"]'
	POSTED_BY_XPATH = '//*[@id="posted_by_wrap"]/div[2]/a'
	BEDROOM_XPATH = '//*[@id="bedroom_num_wrap"]/div[2]/a'
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

# DEFINITIONS
WEBSITES = ['http://ww.99acres.com']
DEFINITIONS = [acres(WEBSITES[0])]
DEFINITIONS[0]