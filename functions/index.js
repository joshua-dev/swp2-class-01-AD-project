// Runtime: Node.js v12.13.0
// firebase --version: 7.8.1

// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require("firebase-functions");

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require("firebase-admin");
admin.initializeApp();

// get Database from Cloud Firestore
let db = admin.firestore();

exports.getLender = functions.https.onRequest(async (req, res) => {
  const title = req.body.text.title;
  var query = {
    lender: ""
  };

  db.collection("Books")
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        var data = book.data();
        if (data.title === title) {
          query.lender = data.lender;
        }
      });
      console.log("query: ", query);
      res.send(query);
      // should return Promise
      return;
    })
    .catch(err => {
      console.log("Error getting documents: ", err);
    });
});
