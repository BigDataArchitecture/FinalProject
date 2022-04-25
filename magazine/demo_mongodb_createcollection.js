var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority";

var a = ""

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("UserData");
    dbo.collection("Google_News").find({}).toArray(function(err, result) {
      if (err) throw err;
      console.log(result[1]['news_title'])
      console.log(result[1]['news_top_image'])
      db.close();
    });
  });

