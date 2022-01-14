from core.core_mt import BaseMt
from urllib.parse import urlencode
from core.links import LinksReqNotify
from random import randint


class Request_stuff(BaseMt):
    def click_id_take(self):
        click = BaseMt.just_click(self)
        text = click.json()
        click_id = text["context"]["id"]
        return click_id


class Request_methods:
    def sub_on_request(self):
        head_link = f'{LinksReqNotify.notify_test}'
        params = {
            'sum': '30',
            'transaction_type': 'on',
            'transaction_id': f'{randint(10000000, 99999999)}',
            'operator_id': '1',
            'label1': f'{self}',
            'click_id': '4b6cf84033d7438_bcfc003632cab4a3a091e0199a3d8766',
            'deferred': '0'
        }
        valid_link = f'{head_link}{urlencode(params)}'
        return valid_link

    def sub_off_request(self):
        head_link = f'{LinksReqNotify.notify_test}'
        params = {
            'sum': '30',
            'transaction_type': 'off',
            'transaction_id': f'{randint(10000000, 99999999)}',
            'operator_id': '1',
            'label1': f'{self}',
            'click_id': '4b6cf84033d7438_bcfc003632cab4a3a091e0199a3d8766',
            'deferred': '0'
        }
        valid_link = f'{head_link}{urlencode(params)}'
        return valid_link

    def sub_rebill_request(self):
        head_link = f'{LinksReqNotify.notify_test}'
        params = {
            'sum': '30',
            'transaction_type': 'rebill',
            'transaction_id': f'{randint(10000000, 99999999)}',
            'operator_id': '1',
            'label1': f'{self}',
            'click_id': '4b6cf84033d7438_bcfc003632cab4a3a091e0199a3d8766',
            'deferred': '0'
        }
        valid_link = f'{head_link}{urlencode(params)}'
        return valid_link
