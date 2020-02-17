const http = require('http');

const app = require('./app');
const dbConnection = require('./services/dbConnection');

const server = http.Server(app);

const port = 3333;

server.listen(port, err => {
  if (err) {
    console.log('Error');
  }
  console.log(`Connected to http://localhost:${port}`);
});

dbConnection();
