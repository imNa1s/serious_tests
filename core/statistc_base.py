from core.core_mt import BaseMt
from core.locators import StatsLocators
from bs4 import BeautifulSoup


class StatsMt(BaseMt, StatsLocators):
    def go_to_statistic(self):
        assert self.is_element_present(*StatsLocators.statistic_button), "can't find"
        self.find_el_click(*StatsLocators.statistic_button)
        assert self.is_element_present(*StatsLocators.main_statistic), "can't find"
        self.find_el_click(*StatsLocators.main_statistic)

    def save_stats(self):
        page_txt = self.browser.page_source
        soup = BeautifulSoup(page_txt, 'html.parser')
        return soup

    def transition_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[1]
        table = table.get_text()
        return table

    def unic_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[2]
        table = table.get_text()
        return table

    def traffback_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[3]
        table = table.get_text()
        return table

    def subscribe_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[4]
        table = table.get_text()
        return table

    def conversion_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[5]
        table = table.get_text()
        return table

    def unsubscribe_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[6]
        table = table.get_text()
        return table

    def rebill_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[7]
        table = table.get_text()
        return table

    def buyout_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[8]
        table = table.get_text()
        return table
    def NK_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[9]
        table = table.get_text()
        return table

    def ERK_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[10]
        table = table.get_text()
        return table

    def partner_pay_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[11]
        table = table.get_text()
        return table

    def system_pay_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[12]
        table = table.get_text()
        return table

    def all_pay_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[13]
        table = table.get_text()
        return table

    def complaints_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[14]
        table = table.get_text()
        return table
