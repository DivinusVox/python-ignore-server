python-ignore-server
====================

A simple proof of concept for a listener to ignore requests from exchange auto-discover

Currently runs on port 443 for use spoofing exchange auto discover, this
requires sudo to bind.

```sudo python server.py```

Afterwards, direct requests to port 443 and be amazed at how it doesn't care.
