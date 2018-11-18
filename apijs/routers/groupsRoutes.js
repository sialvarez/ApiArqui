var express = require('express'),
router = express.Router();
var ping = require('../utilidades');

router
  .get('/', ping.pinger, (req, res) => res.send("Aqui va la lista con todos los grupos!!"))

  .get('/:group_id', (req, res) => {
    res.send("Delvolviendo grupo con id igual a " + req.params.group_id);
  })

  .get('/:group_id/users', (req, res) => {
    res.send("Se muestran todos los usuarios del grupo con id " + req.params.group_id);
  })

  .post('/', (req, res) => {
    name = req.params.name;
    res.send("Se crea el grupo " + name);
  })

  .post('/:group_id', (req, res) => {
    group_id = req.params.group_id;
    users = req.params.users;
    res.send("Se agrega al grupo" + group_id + "los usuarios "+ users);
  })

  .post('/:group_id/remove', (req, res) => {
    group_id = req.params.group_id;
    users = req.params.users;
    res.send("Elimina del grupo" + group_id + "a los usuarios " + users);
  })

  .post('/:group_id/delete', (req, res) => {
    group_id = req.params.group_id;   
    res.send("Elimina el grupo" + group_id);
  })

module.exports = router;