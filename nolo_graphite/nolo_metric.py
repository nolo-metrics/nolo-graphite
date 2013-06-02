class NoloMetric:
    '''Value object for metrics
    '''
    def __init__(self, hostname, date, plugin, metric, value):
       self.hostname = hostname.lower()
       self.date = date
       self.plugin = plugin
       self.metric = metric
       self.value = value

    def __str__(self):
        return "%s.%s %s hostname=%s date=%s" % (self.plugin, self.metric, self.value, self.hostname, self.date.strftime('%s'))
