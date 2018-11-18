var ping = require('ping');
// aqui poner la url del servidor
var hosts = ['google.com'];  // aqui se puede poner mas de una url para ping pero habria que cambiar la logica posterior

exports.pinger = function (req, res, next) {
    
  hosts.forEach(function(host){
    ping.sys.probe(host, function(isAlive){
        if (isAlive){
          var msg = 'host ' + host + ' is alive';
          console.log(msg);
          next();
        }
        else {
        var msg = 'host ' + host + ' is DEAD';
        next(new Error(msg));
        }
      });
  });

};