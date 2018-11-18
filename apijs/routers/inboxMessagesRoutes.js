var express = require('express');
var request = require('request');
router = express.Router();

router

  .get('/api', function(req, res){
    request.get('https://jsonplaceholder.typicode.com/todos/1', function (error, response, body) {
      res.send(response && response.statusCode + " " +body);
    });
  })

  .get('/', (req, res) => {
    res.send("Devoliendo todos los mensajes escritos y recibidos por usuario !!")
  })

  .get('/:message_id', (req, res) => {
    res.send("Delvolviendo mensaje con id igual a " + req.params.message_id);
  })

  .get('/recieved', (req, res) => {
    res.send("Devoliendo todos los mensajes recibidos por usuario !!")
  })

  .get('/sent', (req, res) => {
    res.send("Devoliendo todos los mensajes escritos por usuario !!")
  })

  .get('/sent/:message_id', (req, res) => {
    res.send("Delvolviendo mensaje enviado con id igual a " + req.params.message_id);
  })
  
  .get('/recieved/:message_id', (req, res) => {
    res.send("Delvolviendo mensaje recibido con id igual a " + req.params.message_id);
  })

  .post('/sent', (req, res) => {
    recipients = req.params.recipients;
    content = req.params.content;
    res.send("Creando mensaje! para los usuarios " + recipients + " con el contenido " + content);
  })

  .post('/recieved/:message_id', (req, res) => {
    content = req.params.message;
    res.send("Respondiendo mensaje con id " + req.params.message_id + " con el contenido " + message);
  })

  .post('/recieved/:message_id/upvote', (req, res) => {
    res.send("Upvoteando el mensaje con id " + req.params.message_id + "!");
  })

  .post('/sent/:message_id/upvote', (req, res) => {
    res.send("Upvoteando el mensaje con id " + req.params.message_id + "!");
  })

  .post('/recieved/:message_id/downvote', (req, res) => {
    res.send("Downvoteando el mensaje con id " + req.params.message_id + "!");
  })

  .post('/sent/:message_id/downvote', (req, res) => {
    res.send("Downvoteando el mensaje con id " + req.params.message_id + "!");
  })

  .post('/recieved/:message_id/replies/:reply_id/upvote', (req, res) => {
    res.send("Upvoteando la respuesta con id " + req.params.reply_id + "!");
  })

  .post('/sent/:message_id/replies/:reply_id/upvote', (req, res) => {
    res.send("Upvoteando la respuesta con id " + req.params.reply_id + "!");
  })

  .post('/recieved/:message_id/replies/:reply_id/downvote', (req, res) => {
    res.send("Downvoteando la respuesta con id " + req.params.reply_id + "!");
  })

  .post('/sent/:message_id/replies/:reply_id/downvote', (req, res) => {
    res.send("Downvoteando la respuesta con id " + req.params.reply_id + "!");
  })

  .patch('/inbox/recieved/:message_id', (req, res) => {
    res.send("Editando el mensaje con id " + req.params.message_id + "!");
  })

  .patch('/inbox/sent/:message_id', (req, res) => {
    res.send("Editando el mensaje con id " + req.params.message_id + "!");
  })

  .patch('/inbox/recieved/:message_id/replies/:reply_id', (req, res) => {
    res.send("Editando la respuesta con id " + req.params.reply_id + "!");
  })

  .patch('/inbox/sent/:message_id/replies/:reply_id', (req, res) => {
    res.send("Editando la respuesta con id " + req.params.reply_id + "!");
  });

module.exports = router;