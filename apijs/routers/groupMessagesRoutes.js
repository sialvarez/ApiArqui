var express = require('express');
var request = require('request');
router = express.Router();

router

  .get('/api', function(req, res){
    request.get('https://jsonplaceholder.typicode.com/todos/1', function (error, response, body) {
      res.send(response && response.statusCode + " " +body);
    });
  })
  
  .get('/:group_id/messages', (req, res) => {
    res.send("Enviando de vuelta todos los mensajes del grupo!")
  })

  .get('/:group_id/messages/:message_id', (req, res) => {
    res.send("Enviando de vuelta el mensaje con id " + req.params.message_id + " del grupo!")
  })

  .post('/:group_id/messages', (req, res) => {
    res.send("Creando un nuevo mensaje de grupo!")
  })

  .patch('/:group_id/messages/:message_id', (req, res) => {
    res.send("Editando un mensaje de grupo")
  })

  .patch('/:group_id/messages/:message_id/replies/:reply_id', (req, res) => {
    res.send("Editando un reply de mensaje de grupo!")
  })

module.exports = router;
