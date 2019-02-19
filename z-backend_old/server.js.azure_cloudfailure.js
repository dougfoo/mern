const mongoose = require("mongoose");
const express = require("express");
const bodyParser = require("body-parser");
const logger = require("morgan");
const Data = require("./data");
const mongo = require('mongodb');
const API_PORT = 3001;
const app = express();
const router = express.Router();

console.log("router established");

// this is our MongoDB database
// const dbRoute = "mongodb://jelo:a9bc839993@ds151382.mlab.com:51382/jelotest";
// const dbRoute = "mongodb://dougfoo:IvcAZYAWii0tr509XsHreWoUQ8rV00IVJ67k6VXdN73HJ2HU5vAmUuFKQAexhfyfqJEuBXWGE9ROGwBt9wFBFw==@dougfoo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb";

const password = encodeURIComponent("IvcAZYAWii0tr509XsHreWoUQ8rV00IVJ67k6VXdN73HJ2HU5vAmUuFKQAexhfyfqJEuBXWGE9ROGwBt9wFBFw==");
const dbRoute = "mongodb://dougfoo:"+password+"@dougfoo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb";
const MongoClient = mongo.MongoClient;

MongoClient.connect(dbRoute, 
    { useNewUrlParser: true }, 
    function (err, client) {
        if (err != null) console.log(err);
        console.log(client);
    // const adminDb = client.db('foodatabase').admin();
    // // List all the available databases
    // adminDb.listDatabases(function (err, dbs) {
    //     console.log(dbs.databases.length);
    //     console.log(dbs.databases);
    //     client.close();
    // });
});

// problems w/ Mongoose so i deleted

/*
mongoose.connect('mongodb://dougfoo.documents.azure.com:10255/foodatabase?ssl=true&replicaSet=globaldb', {
    auth: {
        user: 'dougfoo',
        password: 'IvcAZYAWii0tr509XsHreWoUQ8rV00IVJ67k6VXdN73HJ2HU5vAmUuFKQAexhfyfqJEuBXWGE9ROGwBt9wFBFw%3D%3D',
    }
}).catch (err => {
    console.log(err);
});

let db = mongoose.connection;
console.log("db connected");

db.once("open", () => console.log("connected to the database"));

db.on("error", console.error.bind(console, "MongoDB connection error:"));
*/

// (optional) only made for logging and
// bodyParser, parses the request body to be a readable json format
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(logger("dev"));

// this is our get method
// this method fetches all available data in our database
router.get("/getData", (req, res) => {
  Data.find((err, data) => {
    if (err) return res.json({ success: false, error: err });
    return res.json({ success: true, data: data });
  });
});

// this is our update method
// this method overwrites existing data in our database
router.post("/updateData", (req, res) => {
  const { id, update } = req.body;
  Data.findOneAndUpdate(id, update, err => {
    if (err) return res.json({ success: false, error: err });
    return res.json({ success: true });
  });
});

// this is our delete method
// this method removes existing data in our database
router.delete("/deleteData", (req, res) => {
  const { id } = req.body;
  Data.findOneAndDelete(id, err => {
    if (err) return res.send(err);
    return res.json({ success: true });
  });
});

// this is our create methid
// this method adds new data in our database
router.post("/putData", (req, res) => {
  let data = new Data();

  const { id, message } = req.body;

  if ((!id && id !== 0) || !message) {
    return res.json({
      success: false,
      error: "INVALID INPUTS"
    });
  }
  data.message = message;
  data.id = id;
  data.save(err => {
    if (err) return res.json({ success: false, error: err });
    return res.json({ success: true });
  });
});

// append /api for our http requests
app.use("/api", router);

// launch our backend into a port
app.listen(API_PORT, () => console.log(`LISTENING ON PORT ${API_PORT}`));