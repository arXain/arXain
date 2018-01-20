# Testing out arXain with some fake papers
I have uploaded three papers to my ipns peer ID. They can be accessed with an IPFS node running, or through the gateway. This looks like

My PeerID
* QmQWbdLsDw3f4k2x2K8d9bjRLCaKHNEjP3nLPdgEhnyks5

The paper ID and equivalent hashes are given by
* genesis-paper -- QmecxvdKg2LdVF38XUpKMmDcwgRsLdvmwbsGdhZV1m5LKy
* second-paper -- Qme6EB9sDPcogJSFRpPB1Xh6WFADphzmLQ4f78DUKe7irZ
* third-paper -- QmXmBR6ZGNRqYDsv5tAWES78LJpxNRgr3vppX5chXHHBUw

With IPFS node active, one could access the genesis paper directory by entering the following in a browser
``
http://localhost:8080/ipfs/QmecxvdKg2LdVF38XUpKMmDcwgRsLdvmwbsGdhZV1m5LKy
``

One could directly get the contents of ``meta.json`` with the address
``
http://localhost:8080/ipfs/QmecxvdKg2LdVF38XUpKMmDcwgRsLdvmwbsGdhZV1m5LKy/meta.json
``

A similar query for the pdf is made by jsut changing the end chunk to ``genesis-paper.pdf``.

Let's say that only the paperID is available, and we don't have access to the direct hash. We can still interact with the data, by going through the PeerID. To get the meta data, enter the following
``
http://localhost:8080/ipns/QmQWbdLsDw3f4k2x2K8d9bjRLCaKHNEjP3nLPdgEhnyks5/genesis-paper/meta.json
``

Note: we are now looking at /ipns/, which uses the PeerID as a look up (similar to how DNS works for http) and means that we can always return to this address, even if the underlaying data has changed and has different hashes.

A generalized query for fetching meta data would thus look like
``
http://localhost:8080/ipns/<submitter PeerID>/<doi>/meta.json
``

JQuery should be plug and play when interacting with the meta.json calls.

# Notes
* We will need to make sure that we include the IPFS PeerID (which comes from ipfs name publish <directory hash>)