var express = require('express')
const path = require('path')

var app = express();
app.use('/', express.static('dist'))

app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'dist', 'index.html'))
})

console.log('Server started.')
app.listen(80)
