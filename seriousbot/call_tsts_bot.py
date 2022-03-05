import subprocess

from seriousbot.support_for_bot import TestsPathsWin, TestsPathsUnix


class CallWinTests:
    def bot_login():
        arg = ["pytest", "-vm admin", TestsPathsWin.login_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_admin_tiket():
        arg = ["pytest", "-vm admin", TestsPathsWin.tickets_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_partner_tiket():
        arg = ["pytest", "-v -m partner", TestsPathsWin.tickets_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date


class CallUnixTest:
    def bot_login():
        arg = ["pytest", "-v -m admin", TestsPathsUnix.login_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_admin_tiket():
        arg = ["pytest", "-v -m admin", TestsPathsUnix.tickets_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_partner_tiket():
        arg = ["pytest", "v -m partner", TestsPathsUnix.tickets_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date
