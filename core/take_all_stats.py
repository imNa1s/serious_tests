import time

from core.links import LinksReqTds
from core.ready_function import SubscribeMt
from core.statistc_base import StatsMt
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

    # def traffback_request(self, link):
    #     Page = StatsMt(self, link)
    #     Page.go_to_statistic()
    #     stats = Page.save_stats()
    #     stats_pars1 = Page.traffback_take(stats)
    #     SubscribeMt.traffback(LinksReqTds.tds_click_test_traffback)
    #     time.sleep(20)
    #     Page.ref()
    #     stats = Page.save_stats()
    #     stats_pars2 = Page.traffback_take(stats)
    #     print(f'\ntraffback before request {stats_pars1}, after request {stats_pars2}')
    #     assert stats_pars1 != stats_pars2, "they equal"

    def subscribe(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.subscribe_take(stats)
        SubscribeMt.sub_on(LinksReqTds.tds_click_test)
        time.sleep(40)
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
        assert stats_pars1 == stats_pars3, "they didn\'t equal"

    def unsub(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.unsubscribe_take(stats)
        SubscribeMt.sub_off(LinksReqTds.tds_click_test)
        time.sleep(40)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.unsubscribe_take(stats)
        print(f'\nunsub before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def make_rebill(self, link):
        Page = StatsMt(self, link)
        Page.go_to_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.rebill_take(stats)
        SubscribeMt.rebill(LinksReqTds.tds_click_test)
        time.sleep(30)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.rebill_take(stats)
        print(f'\nrebill before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

