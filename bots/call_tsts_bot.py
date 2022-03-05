import subprocess

from bots.support_for_bot import ConsolePaths, TestsPathsWin


class CallableTsts:
    def bot_login():
        arg = [ConsolePaths.shell, "pytest -v -m admin", TestsPathsWin.login_test]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_admin_tiket():
        arg = [ConsolePaths.shell, "pytest -v -m admin", TestsPathsWin.tickets_test]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date

    def bot_partner_tiket():
        arg = [ConsolePaths.shell, "pytest -v -m partner", TestsPathsWin.tickets_test]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        date = answer.communicate()
        return date