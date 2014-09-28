"""
[Virtual] Ward Round implementations
"""
import datetime

from opal.models import Episode

from wardround import WardRound

from renal.models import RRT

class DialysisToday(WardRound):
    name        = "Dialysis Today"
    description = 'Patients on Haemodialysis whose treatment plan is active today.'

    @staticmethod
    def episodes():
        tld = datetime.date.today().strftime("%a").lower()
        kwargs = {'rrt__day_{0}'.format(tld): True}
        return Episode.objects.filter(active=True, **kwargs)
