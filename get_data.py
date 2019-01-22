from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#browser options
options = webdriver.FirefoxOptions()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir",'C:\\Users\\dell i\\Desktop\\Academics\\MTech Project\\price forecasting')
options.set_preference("browser.helperApps.neverAsk.openFile", "application/vnd.ms-excel")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")


#fetching data from AEMO
driver = webdriver.Firefox(firefox_options = options)
driver.get('https://www.aemo.com.au/Electricity/National-Electricity-Market-NEM/Data-dashboard#aggregated-data')
tab = driver.find_element_by_id('dashADF')
year = webdriver.support.ui.Select(tab.find_element_by_xpath("//select[@data-type='year']"))
month = webdriver.support.ui.Select(tab.find_element_by_xpath("//select[@data-type='month']"))


year.select_by_value('2018')
month.select_by_value('March')
download_btn = tab.find_element_by_xpath("//*[contains(text(), 'Download Historic Data as .csv')]")
download_btn.click()
    
driver.close()
    
