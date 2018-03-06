# MongoDB Testing

### Install instructions:

Please install

+ [Windows](https://docs.mongodb.com/getting-started/shell/tutorial/install-mongodb-on-windows/)
+ [Mac](https://docs.mongodb.com/getting-started/shell/tutorial/install-mongodb-on-os-x/)
+ [Linux](https://docs.mongodb.com/getting-started/shell/tutorial/install-on-linux/)

and for [Mongoose](http://mongoosejs.com/) 
+ npm install mongoose
+ make sure to have [node.js](https://nodejs.org/en/) installed

### Local Testing

If you want to rip your own arXiv testdata, install the following python3 packages:
+  json
+ hashlib
+ sha3
+ urllib
+ feedparser


##

After the mongoDB is installed and running,<br/>
`mongoimport --db test --collection arxain --drop --file testdata.json --jsonArray`<br/>
which adds a collection called arxain to a test database.
One can see this database by looking in the mongoDB:<br/>
`mongo`<br/> `show dbs`<br/>
and you should see:<br/>
`admin   0.000GB`<br/>
`config  0.000GB`<br/>
`test    0.001GB` <--- <br/> 
`local   0.000GB`<br/>

See mongoDB [docs](https://docs.mongodb.com/) or [tutorial](https://docs.mongodb.com/tutorials/) to see everything that you can do with the mongoDB shell<br/>Then just run:

`node main.js` 

to test the search. It looks right now for Wichmann in the authors field but you can change this. (this is barebones mongoose code)

