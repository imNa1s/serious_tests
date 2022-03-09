import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd()


class TestsPathsWin:
    login_win_tst = Path(dir_path, 'tests', 'Test_login.py')
    tickets_win_tst = Path(dir_path, 'tests', 'Test_send_tickets.py')
    category_win_tst = Path(dir_path, 'tests', 'Test_category.py')
    country_win_tst = Path(dir_path, 'tests', 'Test_country.py')
    source_win_tst = Path(dir_path,  'tests', 'Test_create_source.py')
    stream_win_tst = Path(dir_path,  'tests', 'Test_create_stream.py')
    operator_win_tst = Path(dir_path,  'tests', 'Test_operator.py')
    stat_win_tst = Path(dir_path,  'tests', 'Test_main_statistic.py')


class TestsPathsUnix:
    login_ux_tst = Path(dir_path, 'tests', 'Test_login.py')
    tickets_ux_tst = Path(dir_path, 'tests', 'Test_send_tickets.py')
    category_ux_tst = Path(dir_path, 'tests', 'Test_category.py')
    country_ux_tst = Path(dir_path, 'tests', 'Test_country.py')
    source_ux_tst = Path(dir_path,  'tests', 'Test_create_source.py')
    stream_ux_tst = Path(dir_path,  'tests', 'Test_create_stream.py')
    operator_ux_tst = Path(dir_path,  'tests', 'Test_operator.py')
    stat_ux_tst = Path(dir_path,  'tests', 'Test_main_statistic.py')
