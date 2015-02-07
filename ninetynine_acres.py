from splinter import Browser
from time import sleep

def acres(browser, type, city, locality, posted_by, bedrooms):

	# WEBSITE
	WEBSITE = 'http://www.99acres.com'

	# KEYWORD
	KEYWORD_KEY = 'keyword'
	KEYWORD = city+' '+locality

	# XPATHS
	def GetBedroomXPath(bedroom_no):
		if bedroom_no < 1 or not isinstance(bedroom_no, int):
			return '//*[@id="s_bedroom_num"]/div/div[2]/div/div/a[1]'
		if bedroom_no > 9:
			bedroom_no = 10
		return '//*[@id="bd_'+str(bedroom_no)+'"]'

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
	if type == 'buy':
		browser.find_by_xpath(BUY_XPATH).click()
	elif type == 'rent':
		browser.find_by_xpath(RENT_XPATH).click()

	# FILING KEYWORD
	browser.fill(KEYWORD_KEY, KEYWORD)

	# BEDROOMS
	if not (not bedrooms):
		browser.find_by_xpath(BEDROOM_XPATH).click()
		browser.find_by_xpath(GetBedroomXPath(int(bedrooms))).click()

	# POSTED BY
	browser.find_by_xpath(POSTED_BY_XPATH).click()
	if posted_by == 'owner':
		browser.find_by_xpath(OWNER_XPATH).click()
	elif posted_by == 'builder':
		browser.find_by_xpath(BUILDER_XPATH).click()
	elif posted_by == 'dealer':
		browser.find_by_xpath(DEALER_XPATH).click()
	
	# SUBMIT
	browser.find_by_xpath(SUBMIT_XPATH).click()
	
	# WAITING TO LOAD
	while not browser.is_element_present_by_css(COUNT, wait_time=10):
		pass

	# GETTING THE VALUE
	properties = browser.find_by_css(COUNT).value

	# RETURN VALUE
	return int(properties)