**arXain local node API documentation**

Below are the current commands and required arguments for interacting with the arXain local node API. This is assuming that the instructions in SETUP.md have been followed.

By default, the local node should be running on port 5000. So all commands should be sent in the form of an http GET request to:

```
http://127.0.0.1:5000/<api-endpoint>
```

WARNING: error handling with the local api is dubious at best. If you send an incorrect directory, or the ipfs daemon is not running strange responses or HTTP errors will be thrown.


**Endpoints**

/init/arxain

No fields, this checks whether the arxain directoy structure has been made, and creates it if it hasn't. Primarily a setup endpoint that will only be called once.

Example submission

```
http://127.0.0.1:5000/init/arxain

{
  "Path": "/Users/davidhopper/.arXain-data",
  "Success": true
}
```

/init/author?author_id="insert-author-id"

the field author_id should correspond to the unique identifier of the author to be created. This is usually the ethereum address hash. This returns a json object with the following fields upon a success

Inputs:

author_id: the unique author identifier, most likely the wallet address.

Outputs:

Success: whether the directory was created

authorID: the author ID returned

localDirectory: the full path locally that the author's repository has been created at

peerID: the IPFS ipns name resolving hash that anyone can view their entire manuscript and comment history at. This is reserved for future use.

Example submission

```
http://127.0.0.1:5000/init/author?author_id=0x12345

{  
  "Success": true,   
  "authorID": "0x12345",   
  "localDirectory": "/Users/username/.arXain-data/authors/0x12345"
  "peerID": "QmYGNMRLKbqjRRcShrqwpL9dSbgD4RsPNGFbycQ7Kb8SQS"  
}
```

/submit/manuscript?author_id="insert-author-id"&paper_id="insert-paper-id"&paper_directory="insert-full-path-to-manuscript-directory"

Inputs:

author_id: the author_id that should be initialized already

paper_id: the unique identifier for the paper to be submitted

paper_directory: the full path to the local copy of the manuscript directory

Outputs:
Success: whether the IPFS submission was successful or not

Hash: the IPFS hash for the current version directory ```<hash>/doi-name.pdf``` would return the document, ```<hash>/meta.json``` would return the meta data

Version: which version of the document this was submitted as.

Example submission and return

```
http://127.0.0.1:5000/submit/manuscript?author_id=0x100&paper_id=1x000&paper_directory=/Users/davidhopper/arXain/test_submissions/genesis-article/

{
  "Hash": "QmZetfrKQ6UwQtqa8WgHMiNG466744712YZfYJEowezw8L",
  "Success": true,
  "Version": "v1"
}
```

/submit/revision?author_id="insert-author-id"&paper_id="insert-paper-id"&paper_directory="insert-full-path-to-revision-directory"

Inputs:

author_id: the author_id that should be initialized already

paper_id: the unique identifier for the paper to be submitted

paper_directory: the full path to the local copy of the manuscript directory

Outputs:
Success: whether the IPFS submission was successful or not

Hash: the IPFS hash for the current version directory ```<hash>/doi-name.pdf``` would return the document, ```<hash>/meta.json``` would return the meta data

Version: which version of the document this was submitted as.
This will return an error if the submitting author has not been initialized, or if the paper has not already been submitted.

Example submission and return
```
http://127.0.0.1:5000/submit/revision?author_id=0x100&paper_id=1x000&paper_directory=/Users/davidhopper/arXain/test_submissions/genesis-article/

{
  "Hash": "QmZetfrKQ6UwQtqa8WgHMiNG466744712YZfYJEowezw8L",
  "Success": true,
  "Version": "v2"
}
```

/submit/comment?author_id="insert-author-id"&paper_id="insert-paper-id"&comment_directory="insert-full-path-to-comment-directory"

Inputs:

author_id: the author_id that should be initialized already

paper_id: the unique identifier for the paper to be submitted

comment_directory: the full path to the local copy of the comment directory

Outputs:
Success: whether the IPFS submission was successful or not

Hash: the IPFS hash for the directory containing the comment

Version: the comment number for this particular manuscript. Formatted as "v#"

Example submission and return
```
http://127.0.0.1:5000/submit/comment?author_id=0x5321&paper_id=1x000&comment_directory=/Users/davidhopper/arXain/test_submissions/genesis-review/

{
  "Hash": "QmUKn49pcWMm8cjyrgYLbwmQxv7xzprVVsJ2WE3jmMVdyj",
  "Success": true,
  "Version": "v1"
}
```
