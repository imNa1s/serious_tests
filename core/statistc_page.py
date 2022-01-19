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
        return table, print(table)
