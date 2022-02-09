from core.core_mt import BaseMt
from core.locators import StatsLocators


class SubStatsMt(BaseMt, StatsLocators):
    def sub_date_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[0]
        table = table.get_text()
        return table

    def sub_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[1]
        table = table.get_text()
        return table

    def sub_active_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[2]
        table = table.get_text()
        return table

    def unsub_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[3]
        table = table.get_text()
        return table

    def unsub_1st_day_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[4]
        table = table.get_text()
        return table

    def sub_rebill_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[5]
        table = table.get_text()
        return table

    def rebill_on_abonent_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[6]
        table = table.get_text()
        return table

    def sub_price_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[7]
        table = table.get_text()
        return table

    def sub_buyout_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[8]
        table = table.get_text()
        return table

    def sub_rebill_buyout_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[9]
        table = table.get_text()
        return table

    def sub_partner_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[10]
        table = table.get_text()
        return table

    def sub_system_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[11]
        table = table.get_text()
        return table

    def sub_all_pay_take(self, soup):
        table = soup.find_all('tr')[2]
        table = table.find_all('td')[12]
        table = table.get_text()
        return table
