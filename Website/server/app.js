var express = require('express');
var app = express();

app.use('/', express.static('dist'));
console.log('Server started.')
app.listen(80);
