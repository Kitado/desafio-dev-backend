const routes = require('express').Router();
const SearchController = require('./controllers/Search');
const ProfessionController = require('./controllers/Profession');

routes.post('/profession', ProfessionController.store);
routes.get('/search', SearchController.search);

module.exports = routes;
