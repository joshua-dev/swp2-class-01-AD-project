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
      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT') query[book.id] = book.data();
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
  var titles = new Array();
  const keyWord = req.query.title;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().title !== '')
          titles.push(book.data().title);
      });

      const mostSimilar = stringSimilarity.findBestMatch(keyWord, titles);
      const bestMatchTitle = mostSimilar.bestMatch.target;

      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().title === bestMatchTitle) {
          query.result = book.data();
          res.send(query);
          return;
        }
      });

      res.send(query);
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of books that has the highest string similarity with the author from request, send to Clinet
exports.searchByAuthor = functions.https.onRequest((req, res) => {
  var query = {};
  var authors = new Array();
  const keyWord = req.query.author;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().author !== '')
          authors.push(book.data().author);
      });

      const mostSimilar = stringSimilarity.findBestMatch(keyWord, authors);
      const bestMatchAuthor = mostSimilar.bestMatch.target;

      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().author === bestMatchAuthor) {
          query.result = book.data();
          res.send(query);
          return;
        }
      });

      res.send(query);
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of books that has the highest string similarity with the publisher from request, send to Clinet
exports.searchByPublisher = functions.https.onRequest((req, res) => {
  var query = {};
  var publishers = new Array();
  const keyWord = req.query.publisher;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().publisher !== '')
          publishers.push(book.data().publisher);
      });

      const mostSimilar = stringSimilarity.findBestMatch(keyWord, publishers);
      const bestMatchPublisher = mostSimilar.bestMatch.target;

      snapshot.forEach(book => {
        if (
          book.id !== 'DEFAULT' &&
          book.data().publisher === bestMatchPublisher
        ) {
          query.result = book.data();
          res.send(query);
          return;
        }
      });

      res.send(query);
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of book from request, set the field 'available' of the book 'true' on Database
exports.borrow = functions.https.onRequest((req, res) => {
  var query = {
    result: 0
  };

  const title = req.query.title;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().title === title) {
          db.collection('Books')
            .doc(book.id)
            .update({
              available: false
            });
          query.result = 1;
          res.send(query);
          return;
        }
      });
      res.send(query);
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});

// Get the data of book from request, set the field 'onLoan' of the book 'available' on Database
exports.giveBack = functions.https.onRequest((req, res) => {
  var query = {
    result: 0
  };

  const title = req.query.title;

  db.collection('Books')
    .get()
    .then(snapshot => {
      snapshot.forEach(book => {
        if (book.id !== 'DEFAULT' && book.data().title === title) {
          db.collection('Books')
            .doc(book.id)
            .update({
              available: true
            });
          query.result = 1;
          res.send(query);
          return;
        }
      });
      res.send(query);
      return;
    })
    .catch(err => {
      console.log('Error getting documents: ', err);
    });
});
