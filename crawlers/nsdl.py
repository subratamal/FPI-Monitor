import datetime
import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException,\
    NoSuchElementException, UnexpectedAlertPresentException


class NSDLArchiveParser:
    NUMBER_OF_TRIES = 3
    UAPE_COUNT_INITIALIZER = 0

    browser = webdriver.Chrome()
    browser.get('https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx')
    assert 'Archive' in browser.find_element_by_xpath('//*[@id="mainContent"]/div[2]').get_attribute('innerHTML')

    @staticmethod
    def generate_archive_page():

        try:
            cur_date = datetime.datetime.now().strftime('%d-%b-%Y')
            hddn_date_input_selector = '#hdnDate'
            txt_data_input_selector = '#txtDate'
            hddn_date_script = 'document.querySelector("{0}").value = "{2}"; document.querySelector("{1}").value ' \
                               '= "{2}";'.format(hddn_date_input_selector, txt_data_input_selector, cur_date)
            print(hddn_date_script)

            view_report_btn_xpath = '//*[@id="btnSubmit1"]/div[2]'
            view_report_btn = NSDLArchiveParser.browser.find_element(By.XPATH, view_report_btn_xpath)
            view_report_btn.click()
            assert('Daily Trends in FPI Investments upto $cur_date', cur_date) in \
                NSDLArchiveParser.browser.find_element(By.XPATH, '//*[@id="dvArchiveData"]/table[1]/tbody/tr[1]/th')\
                .get_attribute('innerHTML')

            NSDLArchiveParser.browser.close()
        except ElementNotInteractableException as enie:
            print(enie)
        except ElementNotVisibleException as enve:
            print(enve)
        except NoSuchElementException as nsee:
            print(nsee)
        except UnexpectedAlertPresentException as uape:
            print(uape)
            if (NSDLArchiveParser.UAPE_COUNT_INITIALIZER < NSDLArchiveParser.NUMBER_OF_TRIES) and ("Please enter Date" in uape.msg):
                NSDLArchiveParser.UAPE_COUNT_INITIALIZER += 1
                nsdlArchiveParser.generate_archive_page()


nsdlArchiveParser = NSDLArchiveParser()
nsdlArchiveParser.generate_archive_page()

# class NSDLCrawler(scrapy.Spider):
#
#     name = 'NSDLCrawler'
#     start_urls = ['https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx']
#
#     def __init__(self):
#         super().__init__()
#         pass
#
#     def parse(self, response):
#         pass


