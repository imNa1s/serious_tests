from core.request_stf import Request_stuff, Request_urls
from core.links import LinksReqTds
from core.core_mt import BaseMt
import requests
import pytest

click_id = Request_stuff.click_id_take(LinksReqTds.tds_click_test)


@pytest.mark.sub
@pytest.mark.on
def test_sub():
    request_link = Request_urls.sub_on_request_url(click_id)
    request = BaseMt.just_click(request_link)
    assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'


@pytest.mark.sub
@pytest.mark.off
def test_unsub():
    request_link = Request_urls.sub_off_request_url(click_id)
    request = BaseMt.just_click(request_link)
    assert request.status_code == requests.codes.ok, f'unsub didn\'t done, status code = {request.status_code}"'


@pytest.mark.sub
@pytest.mark.rebill
def test_rebill():
    request_link = Request_urls.sub_rebill_request_url(click_id)
    request = BaseMt.just_click(request_link)
    assert request.status_code == requests.codes.ok, f'resub didn\'t done, status code = {request.status_code}"'


@pytest.mark.sub
@pytest.mark.rebill
def test_rebill():
    request_link = Request_urls.sub_rebill_request_url(click_id)
    request = BaseMt.just_click(request_link)
    assert request.status_code == requests.codes.ok, f'resub didn\'t done, status code = {request.status_code}"'


@pytest.mark.sub
@pytest.mark.rebill
def test_click_id():
    click = Request_stuff.click_id_take(LinksReqTds.tds_click_test)
    click = len(click)
    assert click == 48, f'click id length = {click} exept = 48'