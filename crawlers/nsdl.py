from datetime import datetime, timedelta
# import scrapy
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

    def __init__(self, start_date=datetime.today(), duration_in_days=0):
        self.start_date = start_date
        self.duration_in_days = duration_in_days

    def boot(self):
        self.date_range_calc()
        self.process_archive_page()

    def generate_archive_page(self, date=datetime.today().strftime("%d-%b-%Y")):
        print(date)

        try:
            hddn_date_input_selector = '#hdnDate'
            txt_data_input_selector = '#txtDate'
            hddn_date_script = 'document.querySelector("{0}").value = "{2}"; document.querySelector("{1}").value ' \
                               '= "{2}";'.format(hddn_date_input_selector, txt_data_input_selector, date)
            print(hddn_date_script)
            NSDLArchiveParser.browser.execute_script(hddn_date_script)

            view_report_btn_xpath = '//*[@id="btnSubmit1"]/div[2]'
            view_report_btn = NSDLArchiveParser.browser.find_element(By.XPATH, view_report_btn_xpath)
            view_report_btn.click()

            daily_trends_header = NSDLArchiveParser.browser.find_element(
                By.XPATH, '//*[@id="dvArchiveData"]/table[1]/tbody/tr[1]/th')
            assert 'Daily Trends in FPI Investments upto {}'.format(date) in \
                daily_trends_header.get_attribute('innerHTML')

            # NSDLArchiveParser.browser.close()
        except ElementNotInteractableException as enie:
            print(enie)
        except ElementNotVisibleException as enve:
            print(enve)
        except NoSuchElementException as nsee:
            print(nsee)
        except UnexpectedAlertPresentException as uape:
            print(uape)
            if NSDLArchiveParser.UAPE_COUNT_INITIALIZER < NSDLArchiveParser.NUMBER_OF_TRIES and \
                    "Please enter Date" in uape.msg:
                NSDLArchiveParser.UAPE_COUNT_INITIALIZER += 1
                NSDLArchiveParser.generate_archive_page()

    def date_range_calc(self):

        self.calc_ranges = [
            "2017-Oct-13",
            "2017-Oct-31",
            "2017-Nov-30",
            "2017-Dec-31",
            "2018-Jan-31",
            "2018-Feb-28",
            "2018-Mar-12"
        ]

    def process_archive_page(self):

        for date in self.calc_ranges:
            self.generate_archive_page(date)

            # sample_json_structure= [{
            #     "Reporting Date": "04-Dec-2017",
            #     "Debt/Equity": "Equity",
            #     "Investment Route": "",
            #     "Gross Purchases(Rs Crore)": "",
            #     "Gross Sales(Rs Crore)": "",
            #     "Net Investment (Rs Crore)": "",
            #     "Net Investment US($) million": ""
            # }]



nsdlArchiveParser = NSDLArchiveParser(duration_in_days=180)
nsdlArchiveParser.boot()
# nsdlArchiveParser.process_archive_page()

# print(arrow.get('June was born in May 1980', 'MMM YYYY').format("MMMM-DDDD-dddd-YYYY"))
#



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


