import socket

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

class GraphiteHandler:
    '''Metric Handler access to a graphite server
    '''
    def __init__(self, config):
        '''load host, port and protocol from config
        '''
        self.host = config.get('graphite','host').strip()

        try:
            self.port = config.getint('graphite','port')
        except ConfigParser.NoOptionError:
            self.port = 2003

        try:
            self.protocol = config.get('graphite', 'protocol')
        except ConfigParser.NoOptionError:
            self.protocol = 'plaintext'

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        '''initialize connection to graphite carbon server
        '''
        self.sock.connect((self.host, self.port))

    def send_metric(self, metric):
        '''send a NoloMetric to the graphite carbon server
        '''
        self.sock.sendall(self.__format_metric(metric))

    def close(self):
        '''close connection to graphite carbon server
        '''
        self.sock.close()

    def __str__(self):
        return "%s:%s:%s" % (self.protocol, self.host, self.port)

    def __format_metric(self, metric):
        '''serialize NoloMetric as needed for the carbon plaintext protocol
        '''
        return "test.%s.%s.%s %s %s\n" % (metric.hostname, metric.plugin, metric.metric, metric.value, metric.date.strftime('%s'))
