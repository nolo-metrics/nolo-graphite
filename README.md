Nolo-Graphite
=============

`nolo-graphite` is an easy way to pipe your nolo plugins into graphite.

By default, the metric name will be the hostname followed by the
plugin name followed by the metric identifier. For example, if you
have this setup:

    % hostname
    app001
    % ./load
    one 1.23

Then running `nolo-graphite ./load` will submit a metric with the
identifier `app001.load.one` and value `1.23`.

Usage
-----

Create `/etc/nolo-graphite.conf`:

    [graphite]
    host=graphite.example.com

then you can run the plugin adapter

Options
-------

* `host`: carbon service hostname
* `port`: carbon service port, defaults to `2003`
* `protocol`: carbon service protocol, defaults to `plaintext`

TODO
----
* support pickle (:2004) protocol

    listOfMetricTuples = [(path, (timestamp, value)), ...]
    payload = pickle.dumps(listOfMetricTuples)
    header = struct.pack("!L", len(payload))
    message = header + payload

* amqp support
* configurable namespacing, see diamond's hostname_method
