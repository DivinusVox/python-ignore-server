python-ignore-server
====================

A simple proof of concept for a listener to ignore requests from exchange auto-discover

Currently runs on port specififed via '-p'.
Ports 1 - 1024 require elevated privileges, use sudo.

Example:
```sudo ./server.py -p 443```

Afterwards, direct requests to port 443 and be amazed at how it doesn't care.
