from core.core_mt import BaseMt
from core.locators import StatsLocators


class TakeSubStatsMt(BaseMt, StatsLocators):
    def go_to_sub_statistic(self):
        assert self.is_element_present(*StatsLocators.statistic_button), "can't find button statistic"
        self.find_el_click(*StatsLocators.statistic_button)
        assert self.is_element_present(*StatsLocators.main_statistic), "can't find all stat's button"
        self.find_el_click(*StatsLocators.main_statistic)
        assert self.is_element_present(*StatsLocators.sub_statistic), "can't find sub stat's button"
        self.find_el_click(*StatsLocators.sub_statistic)

    def sub_date_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[0]
        table = table.get_text()
        return table

    def sub_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[1]
        table = table.find_all('span')[0]
        table = table.get_text()
        return table

    def sub_active_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[2]
        table = table.get_text()
        return table

    def unsub_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[3]
        table = table.get_text()
        return table

    def unsub_1st_30min_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[4]
        table = table.get_text()
        return table

    def unsub_1st_day_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[5]
        table = table.get_text()
        return table

    def sub_rebill_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[6]
        table = table.get_text()
        return table

    def rebill_on_abonent_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[7]
        table = table.get_text()
        return table

    def sub_price_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[8]
        table = table.get_text()
        return table

    def sub_buyout_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[9]
        table = table.get_text()
        return table

    def sub_rebill_buyout_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[10]
        table = table.get_text()
        return table

    def sub_partner_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[11]
        table = table.get_text()
        return table

    def sub_system_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[0]
        table = table.find_all('td')[12]
        table = table.get_text()
        return table

    def sub_all_pay_take(self, soup):
        table = soup.find_all('tbody')[1]
        table = table.find_all('tr')[1]
        table = table.find_all('td')[13]
        table = table.get_text()
        return table
