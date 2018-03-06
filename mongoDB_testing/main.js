console.log("Hello World!");

var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/ktest5');
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
console.log("Connected to database!");

var arxainSchema = mongoose.Schema({
  authors: [String], 
  comments: String,
  category: [String],
  contract: String,
  keywords: [String],
  revision: String,
  submitter: String,
  summary: String, 
  timestamp: String,
  title: String
});

//  arxainSchema.plugin(searchable);


var arxain = mongoose.model('arXain', arxainSchema, 'arxain'); 


//  arxain.find({ contract: /.*3aff89fe564ad9031a6adaead2ce8e7f63ba8db788979f3dfd57987147d83be0.*/ }, function(err, data){
arxain.find({ authors: /.*Wichmann.*/}, function(err, data){
  if(!err){
    var outputs = [];
    if(data.length == 0)
      console.log("no search results")
    else{
      for(d in data){
        var datum = JSON.parse(JSON.stringify(data[d]));
        outputs.push(datum);
      }
      console.log(outputs)
      db.close();
    }
  }
  else{
    console.log("Error"+err.message);
  }
  console.log("got query");
  db.close();
});
