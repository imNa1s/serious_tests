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

