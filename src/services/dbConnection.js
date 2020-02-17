const mongoose = require('mongoose');

const URI = 'mongodb://localhost:27017/nodeapi';

const dbConnection = async () => {
  await mongoose
    .connect(URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
    .then(() => {
      console.log('DB connected');
    })
    .catch(err => {
      throw err;
    });
};

module.exports = dbConnection;
