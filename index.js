var http = require('http');
var port = process.env.port || 1337;
var express = require('express');
var path = require('path');

var application = express();

application.use(express.static(path.join(__dirname, 'public')));

application.listen(port);
