import subprocess

from seriousbot.support_for_bot import TestsPathsWin, TestsPathsUnix


class CallWinTests:
    def bot_login():
        arg = ["pytest", "-vm admin", TestsPathsWin.login_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_fail_login():
        arg = ["pytest", "-vm admin_fail", TestsPathsWin.login_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_partner_login():
        arg = ["pytest", "-vm admin_partner", TestsPathsWin.login_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_admin_tiket():
        arg = ["pytest", "-vm admin", TestsPathsWin.tickets_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_partner_tiket():
        arg = ["pytest", "-vm partner", TestsPathsWin.tickets_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_category():
        arg = ["pytest", "-vm create", TestsPathsWin.category_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_country():
        arg = ["pytest", "-vm create", TestsPathsWin.country_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_create_source():
        arg = ["pytest", "-vm create", TestsPathsWin.source_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_create_stream():
        arg = ["pytest", "-vm create", TestsPathsWin.stream_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_create_operator():
        arg = ["pytest", "-vm create", TestsPathsWin.operator_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_date():
        arg = ["pytest", "-vm date", TestsPathsWin.stat_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_transition():
        arg = ["pytest", "-vm transition", TestsPathsWin.stat_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_unic():
        arg = ["pytest", "-vm unic", TestsPathsWin.stat_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_traffback():
        arg = ["pytest", "-vm traffback", TestsPathsWin.stat_win_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

class CallUnixTest:
    def bot_login():
        arg = ["pytest", "-vm admin", TestsPathsUnix.login_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_fail_login():
        arg = ["pytest", "-vm admin_fail", TestsPathsUnix.login_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_partner_login():
        arg = ["pytest", "-vm admin_partner", TestsPathsUnix.login_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_admin_tiket():
        arg = ["pytest", "-vm admin", TestsPathsUnix.tickets_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_partner_tiket():
        arg = ["pytest", "-vm partner", TestsPathsUnix.tickets_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_category():
        arg = ["pytest", "-vm create", TestsPathsUnix.category_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_country():
        arg = ["pytest", "-vm create", TestsPathsUnix.country_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_create_source():
        arg = ["pytest", "-vm create", TestsPathsUnix.source_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_create_stream():
        arg = ["pytest", "-vm create", TestsPathsUnix.stream_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_create_operator():
        arg = ["pytest", "-vm create", TestsPathsUnix.operator_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_date():
        arg = ["pytest", "-vm date", TestsPathsUnix.stat_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_transition():
        arg = ["pytest", "-vm transition", TestsPathsUnix.stat_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_unic():
        arg = ["pytest", "-vm unic", TestsPathsUnix.stat_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result

    def bot_stat_traffback():
        arg = ["pytest", "-vm traffback", TestsPathsUnix.stat_ux_tst]
        answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
        result = answer.communicate()
        return result
