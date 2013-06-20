import datetime
import json
import socket
import subprocess

from nolo_graphite.nolo_metric import NoloMetric

class NoloMetricCollector:
    '''
    '''
    def __init__(self, plugin, handler, config):
        self.plugin = plugin
        self.handler = handler
        self.config = config

    def run(self):
        metrics = self.collect_metrics()
        self.send_metrics(metrics)

    def collect_metrics(self):
        date = datetime.datetime.now()
        hostname = socket.getfqdn().split('.')[0]

        output = subprocess.check_output(["nolo-json", self.plugin])
        data = json.loads(output)

        metrics = []
        for plugin_name in data:
            for metric in data[plugin_name]:
                metrics.append(NoloMetric(hostname, date, plugin_name, metric['identifier'], metric['value']))
        return metrics

    def send_metrics(self, metrics):
        s = self.handler(self.config)
        s.connect()
        for m in metrics:
            s.send_metric(m)
        s.close()
