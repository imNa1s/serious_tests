import time
import pytest

from core.links import SiteLinks
from core.ready_function import login_pass
from core.ready_function import transition


@pytest.mark.stats
@pytest.mark.transition
def test_transitions(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    transition(browser, browser.current_url)
    time.sleep(1)
