//
const readline = require('readline');
const fs = require('fs');
//
//
var async = require('async'),
    mongo = require('mongodb'),
    ObjectID = mongo.ObjectID;
//
//data 
//
let rawdata = fs.readFileSync('google-scraper-jobs-remote-MA.json')
let modata = JSON.parse(rawdata);
console.log(modata);


//console.log(require('./datajson-mu.js'));
//var modata = require('./datajson-mu.js');

//
var heure = new Date();
var now = new Date();
var isoString = now.toISOString();

var isodate = new Date(isoString);




const transformdata = (json) => { 

json = JSON.parse(JSON.stringify(json).split('"summary":').join('"description":'));
//jsonscraped = jsonscraped.replace("\"summary\":", "\"description\":");
//add missing fields 
//
//json = json[0];
console.log(json);
//adding _id 
var id = new ObjectID();
var idstr = id.toString();
console.log("idrstr", idstr);
console.log(typeof idstr);
json._id=idstr;
json.userId="qRofzWAQpCqJp9kXC";
json.userName="Anas Boukharta";
json.status="active";

jsonheure=isodate;
json.createdAt=jsonheure;

json.htmlDescription=json.htmlDescription.replace(/\n/g, "<br />");  

json.htmlDescription=json.htmlDescription;
json.description=json.description;
json.updatedAt=jsonheure;
json.remote=true;
json.jobtype="Full Time";

delete json.salary;
delete json.isEasyApply;
delete postDate;
console.log(json);

  return json;}
//convert data json to json 
//
//

//
//transform all the array of data scraped with map 
//

var map1 = modata.map(transformdata);

console.log(map1);
//push to server ?

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('push to server database? ', (answer) => {
  // TODO: Log the answer in a database
 
  if(answer=='Y'||answer=='y'){
  // push
  pushtodb(map1);
  }


  rl.close();
});

const pushtodb = (json)=>{ 
//push it to server 
//
//
var fs = require("fs");
var mongoose = require('mongoose');
var tunnel = require('tunnel-ssh');
var MongoClient = require('mongodb').MongoClient;
//===== db connection =====

var config = {
    username:'root',
    password:'H1gR1S3q',
    host:'128.199.35.13',
    agent : process.env.SSH_AUTH_SOCK,
    port:22,
    dstPort:27017,
    localHost:'127.0.0.1',
    localPort:27000
};

var server = tunnel(config, function (error, server) {
    if(error){
        console.log("SSH connection error: " + error);
    }
    mongoose.connect('mongodb://localhost:27000/khidma');

    var db = mongoose.connection;
    db.on('error', console.error.bind(console, 'DB connection error:'));
    db.once('open', function() {
        // we're connected!
        console.log("DB connection successful");
       
        db.collection("jobs").insert(json, function(err, res) {
        if (err) throw err;
        console.log("Document inserted");
        
        }); 

        db.close();
        console.log("db closed");
      // console.log(server);
    
});
});
}
