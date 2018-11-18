var express = require('express'),
router = express.Router();
var request = require('request');


router.get('/', function (req, res) {
  request({
    url: req.url,
    baseUrl: 'http://localhost:4000/users',
    method: req.method,
    json: true,
    headers: {
       'user': req.headers.user,
     }
    }, function (error, response, body) {
      try {
        res.send(body);
      } catch (error) {
        console.log('Ha ocurrido un error!');
        console.log(response.statusCode);
      }
    });
})

router.get('/:userId', function (req, res) {
  request({
    url: req.url,
    baseUrl: 'http://localhost:4000/users',
    method: req.method,
    json: true,
    headers: {
       'user': req.headers.user,
       'userId': req.params.userId,
     }
    }, function (error, response, body) {
      try {
        res.send(body);
      } catch (error) {
        console.log('Ha ocurrido un error!');
        console.log(response.statusCode);
      }
    });
})

router.get('/:userId/groups', function (req, res) {
  request({
    url: req.url,
    baseUrl: 'http://localhost:4000/users',
    method: req.method,
    json: true,
    headers: {
       'user': req.headers.user,
       'userId': req.params.userId,
     }
    }, function (error, response, body) {
      try {
        res.send(body);
      } catch (error) {
        console.log('Ha ocurrido un error!');
        console.log(response.statusCode);
      }
    });
})

router.post('/', function (req, res) {
  let body = '';
    req.on('data', chunk => {
        body += chunk.toString(); // convert Buffer to string
    });
    req.on('end', () => {
        console.log(body);
        request({
          url: req.url,
          baseUrl: 'http://localhost:4000/users',
          method: req.method,
          json: true,
          form: body,
          }, function (error, response, body) {
            try {
              res.send(body);
            } catch (error) {
              console.log('Ha ocurrido un error!');
              console.log(response.statusCode);
            }
          });
    });

})

router.post('/delete', function (req, res) {
  request({
    url: req.url,
    baseUrl: 'http://localhost:4000/users',
    method: req.method,
    json: true,
    headers: {
       'user': req.headers.user,
     }
    }, function (error, response, body) {
      try {
        res.send(body);
      } catch (error) {
        console.log('Ha ocurrido un error!');
        console.log(response.statusCode);
      }
    });
})


module.exports = router;
