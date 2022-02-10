import time

from core.links import LinksReqTds
from core.ready_request_mt import SubscribeMt
from core.statistic.sub_statistic_base import TakeSubStatsMt
from datetime import datetime


class SubStatisticsMt:
    def sub_stats_date(self, link):
        current_date = str(datetime.now().date())
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_date_take(stats)
        print(f'\ntoday\'s date - {current_date}, date last request - {stats_pars1}')
        assert stats_pars1 == current_date, "no request today"

    def sub_stats_sub(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        time.sleep(1)
        stats = Page.save_stats()
        stats_pars1 = Page.sub_take(stats)
        SubscribeMt.sub_on(LinksReqTds.tds_click_test)
        time.sleep(60)
        Page.ref()
        stats = Page.save_stats()
        stats_pars2 = Page.sub_take(stats)
        print(f'\nnumber of subscribe before request {stats_pars1}, after request {stats_pars2}')
        assert stats_pars1 != stats_pars2, "they equal"

    def sub_stats_active(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_active_take(stats)
        print(f'\nnumber of active subscriber {stats_pars1}')

    def sub_stats_unsub(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.unsub_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_unsub_1st(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.unsub_1st_day_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_rebill(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_rebill_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_rebill_abonent(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.rebill_on_abonent_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_price(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_price_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_buyout(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_buyout_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_rebill_buyout(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_rebill_buyout_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_partner(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_partner_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_system(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_system_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')

    def sub_stats_all_pay(self, link):
        Page = TakeSubStatsMt(self, link)
        Page.go_to_sub_statistic()
        stats = Page.save_stats()
        stats_pars1 = Page.sub_all_pay_take(stats)
        print(f'\nnumber of unsub today {stats_pars1}')