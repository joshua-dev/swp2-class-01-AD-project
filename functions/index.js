// Runtime: Node.js 8
// firebase --version: 7.8.1

// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require("firebase-functions");

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require("firebase-admin");
admin.initializeApp();

// Get Database from Cloud Firestore
const db = admin.firestore();

// Get string-similarity module
const stringSimilarity = require("string-similarity");

// Get the title of all books in Database, send to Client
exports.showAll = functions.https.onRequest(async (req, res) => {
  var query = {};
  var array = new Array();

  db.collection("Books")
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        array.push(book.data().title);
      });

      query.result = array;

      res.send(JSON.stringify(query));

      // Should return Promise
      return;
    })
    .catch(err => {
      console.log("Error getting documents: ", err);
    });
});

// Get the data of book that has the highest string similarity with the book in the request, send to Client
exports.search = functions.https.onRequest(async (req, res) => {
  var query = {};
  const keyWord = req.body.text.title;

  db.collection("Books")
    .get()
    .then(snapshot => {
      var titles = new Array();

      snapshot.forEach(book => titles.push(book.data().title));
      const mostSimilar = stringSimilarity.findBestMatch(keyWord, titles);

      query.result = mostSimilar;

      res.send(JSON.stringify(query));

      return;
    })
    .catch(err => {
      console.log("Error getting documents: ", err);
    });
});
