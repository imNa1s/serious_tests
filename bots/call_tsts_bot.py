import subprocess

from bots.support_for_bot import ConsolePaths, TestsPathsWin, TestsPathsUnix


class CallWinTests:
    def bot_login():
        arg = [ConsolePaths.shell, "pytest -v -m admin", TestsPathsWin.login_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_admin_tiket():
        arg = [ConsolePaths.shell, "pytest -v -m admin", TestsPathsWin.tickets_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_partner_tiket():
        arg = [ConsolePaths.shell, "pytest -v -m partner", TestsPathsWin.tickets_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date


class CallUnixTest:
    def bot_login():
        arg = [ConsolePaths.console, "pytest -v -m admin", TestsPathsUnix.login_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_admin_tiket():
        arg = [ConsolePaths.console, "pytest -v -m admin", TestsPathsUnix.tickets_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_partner_tiket():
        arg = [ConsolePaths.console, "pytest -v -m partner", TestsPathsUnix.tickets_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date
