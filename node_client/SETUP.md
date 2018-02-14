**A quick install manual**

Make sure you have the following packages installed on a python3 environment
* ipfsapi
* flask
* requests

in arXain/node_client/pyXain run

```
pip install --editable .
```

to install the pyXain module.

in arXain/node_client/node run

```
pip install --editable .
export FLASK_APP=node
export FLASK_DEBUG=true
```

to start the local server, run

```
flask run
```

You also must run an ipfs daemon in a separate terminal

```
ipfs daemon
```

You can now view the landing page on (http:///127.0.0.1:5000)

Note: every time you open a new terminal session and want to run the node, you need to enter both of the export statements.
