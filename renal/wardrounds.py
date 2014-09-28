"""
[Virtual] Ward Round implementations
"""
import datetime

from wardround import WardRound


class DialysisToday(WardRound):
    name        = "Dialysis Today"
    description = 'Patients on Haemodialysis whose treatment plan is active today.'

    @staticmethod
    def episodes():
        from opal.models import Episode
        from renal.models import RRT

        tld = datetime.date.today().strftime("%a").lower()
        kwargs = {'rrt__day_{0}'.format(tld): True}
        return Episode.objects.filter(active=True, **kwargs)
