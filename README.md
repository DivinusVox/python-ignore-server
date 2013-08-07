python-ignore-server
====================

A simple proof of concept for a listener to ignore requests from exchange auto-discover

Currently runs on port specififed via '-p'.
Ports 1 - 1023 require elevated privileges, use sudo.

Example:
```sudo ./server.py -p 443```

Afterwards, direct requests to port 443 and be amazed at how it doesn't care.

Troubleshooting
---------------
If your server crashes and fails to unbind the port, you can use fuser to force
close the port being held open. (This is rare since adding interrupt handling)

```sudo fuser -k 443/tcp```
Where 443 is the port in question.
