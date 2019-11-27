// Runtime: Node.js v12.13.0
// firebase --version: 7.8.1

// import admin SDK

// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require("firebase-functions");

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require("firebase-admin");
admin.initializeApp(functions.config().firebase);

// get Database from Cloud Firestore
let db = admin.firestore();

exports.get = functions.https.onRequest(async (req, res) => {
  let docRef = db.collection("Books");

  docRef
    .get()
    .then(snapshot => {
      snapshot.forEach(doc => {
        let info = doc.data();
        output = {
          title: info.title,
          author: info.author,
          owner: info.owner,
          lender: info.lender
        };

        console.log(output);
        res.send(output);
      });
      // Each then should return Promise
      return;
    })
    .catch(err => {
      console.log("Error getting documents", err);
    });
});
