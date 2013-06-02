import datetime

from nolo_graphite.nolo_metric import NoloMetric

class TestNoloMetric:
    def test_one(self):
        # it's the end of the world
        date = datetime.datetime(1999, 12, 31, 23, 59, 59)
        metric = NoloMetric('host', date, 'plugin', 'metric', 'value')
        assert('plugin.metric value hostname=host date=946713599' ==
                metric.__str__())
