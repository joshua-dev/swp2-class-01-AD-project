// Runtime: Node.js 8
// firebase version: 7.10.0

// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require('firebase-functions');

// The Firebase Admin SDK to access the Firebase Realtime Database.
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

// Get Database from Cloud Firestore
let db = admin.firestore();

// Get string-similarity module
const stringSimilarity = require('string-similarity');

// Get the title of all books in Database, send to Client
exports.showAll = functions.https.onRequest((req, res) => {
  var query = {};

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(doc => {
        query[doc.id] = doc.data();
      });

      res.send(query);

      // Should return Promise
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the title of all available books in Database, send to Client
exports.showAvailables = functions.https.onRequest((req, res) => {
  var query = {};

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.data().available === true && book.id !== 'DEFAULT')
          query[book.id] = book.data();
      });

      res.send(query);

      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the title of all books on loan in Database, send to Client
exports.showNotAvailables = functions.https.onRequest((req, res) => {
  var query = {};

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.data().available === false && book.id !== 'DEFAULT')
          query[book.id] = book.data();
      });

      res.send(query);

      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of books that has the highest string similarity with the title from request, send to Client
exports.searchByTitle = functions.https.onRequest((req, res) => {
  var query = {};
  for (key in Object.keys(req)) console.log(key);

  const keyWord = req.title;
  var output_title = '';
  var output_similarity = 0;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        var similarity = stringSimilarity.compareTwoStrings(
          keyWord,
          book.data().title
        );
        if (similarity > output_similarity) {
          output_title = book.data().title;
          output_similarity = similarity;
        }
      });

      query.title = output_title;
      res.send(query);
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of books that has the highest string similarity with the author from request, send to Clinet
exports.searchByAuthor = functions.https.onRequest(async (req, res) => {
  var query = {};
  const keyWord = req.body.text.author;

  db.collection('Books')
    .get()
    .then(snapshot => {
      var authors = new Array();

      snapshot.forEach(book => authors.push(book.data().author));
      const mostSimilar = stringSimilarity.findBestMatch(keyWord, authors);

      query.result = mostSimilar;

      res.send(JSON.stringify(query));

      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of books that has the highest string similarity with the publisher from request, send to Clinet
exports.searchByPublisher = functions.https.onRequest(async (req, res) => {
  var query = {};
  const keyWord = req.body.text.publisher;

  db.collection('Books')
    .get()
    .then(snapshot => {
      var publishers = new Array();

      snapshot.forEach(book => authors.push(book.data().publisher));
      const mostSimilar = stringSimilarity.findBestMatch(keyWord, publishers);

      query.result = mostSimilar;

      res.send(JSON.stringify(query));

      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of book from request, set the field 'available' of the book 'true' on Database
exports.borrow = functions.https.onRequest(async (req, res) => {
  var query = {
    result: 1
  };

  const title = req.body.text.title;
  const author = req.body.text.author;
  const publisher = req.body.text.publisher;
  const lender = req.body.text.publisher;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        const id = book.id();
        const data = book.data();
        if (
          data.title === title &&
          data.author === author &&
          data.publisher === publisher
        ) {
          if (data.availalbe === 0) query.result = 0;
          else
            db.collection('Books')
              .doc(id)
              .set({
                availalbe: 0
              });
          return;
        }
      });

      res.send(JSON.stringify(query));

      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of book from request, set the field 'onLoan' of the book 'available' on Database
exports.giveBack = functions.https.onRequest(async (req, res) => {
  var query = {
    result: 1
  };

  const title = req.body.text.title;
  const author = req.body.text.author;
  const publisher = req.body.text.publisher;
  const lender = req.body.text.publisher;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        const id = book.id();
        const data = book.data();
        if (
          data.title === title &&
          data.author === author &&
          data.publisher === publisher
        ) {
          if (data.availalbe === 1) query.result = 0;
          else
            db.collection('Books')
              .doc(id)
              .set({
                availalbe: 1
              });
          return;
        }
      });

      res.send(JSON.stringify(query));

      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});
