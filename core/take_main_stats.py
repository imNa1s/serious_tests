import time

from core.links import LinksReqTds
from core.ready_request_mt import SubscribeMt
from core.main_statistic_base import StatsMt
from datetime import datetime


class StatisticsMt:
    def stats_date(self, link):
        current_date = str(datetime.now().date())
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.date_take(stats)
        print(f'\ntoday\'s date - {current_date}, date last request - {stats_pars1}')
        assert stats_pars1 == current_date, "no request today"

    def transition(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.transition_take(stats)
        SubscribeMt.redirect_without_sub(LinksReqTds.tds_click_test)
        time.sleep(20)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.transition_take(stats)
        print(f'\ntransition before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def unic_request(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.unic_take(stats)
        SubscribeMt.redirect_without_sub(LinksReqTds.tds_click_test)
        time.sleep(20)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.unic_take(stats)
        print(f'\nunic user before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def traffback_request(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.traffback_take(stats)
        SubscribeMt.traffback(LinksReqTds.tds_click_test_traffback)
        time.sleep(20)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.traffback_take(stats)
        print(f'\ntraffback before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def subscribe(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.subscribe_take(stats)
        SubscribeMt.sub_on(LinksReqTds.tds_click_test)
        time.sleep(60)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.subscribe_take(stats)
        print(f'\nnumber of subscribe before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def conversion(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.unic_take(stats)
        stats_pars2 = Page.subscribe_take(stats)
        stats_pars3 = Page.conversion_take(stats)
        stats_pars1 = int(stats_pars1) / int(stats_pars2)
        stats_pars1 = str(round(stats_pars1, 1))
        stats_pars1 = f'1:{stats_pars1}'
        print(f'\nconversion {stats_pars1}, conversion on site {stats_pars3}')
        assert stats_pars1 == stats_pars3, f"they didn\'t equal {stats_pars1} != {stats_pars3}"

    def unsub(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.unsubscribe_take(stats)
        SubscribeMt.sub_off(LinksReqTds.tds_click_test)
        time.sleep(60)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.unsubscribe_take(stats)
        print(f'\nunsub before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, f"they equal {stats_pars1}={stats_pars2}"

    def make_rebill(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.rebill_take(stats)
        SubscribeMt.rebill(LinksReqTds.tds_click_test)
        time.sleep(60)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.rebill_take(stats)
        print(f'\nrebill before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def buyout(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.buyout_take(stats)
        SubscribeMt.sub_on(LinksReqTds.tds_click_test_1)
        time.sleep(80)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.buyout_take(stats)
        print(f'\nbuyout before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def NK(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.NK_take(stats)
        print(f'\nИК {stats_pars1}')

    def EPC(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.ERC_take(stats)
        print(f'\nEPC {stats_pars1}')

    def partner(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.partner_pay_take(stats)
        print(f'\npartner {stats_pars1}')

    def system_pay(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.system_pay_take(stats)
        print(f'\nsystem {stats_pars1}')

    def all_pay(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.all_pay_take(stats)
        print(f'\nall pays {stats_pars1}')

    def complaints(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.complaints_take(stats)
        print(f'\nnumber of user complaints {stats_pars1}')


