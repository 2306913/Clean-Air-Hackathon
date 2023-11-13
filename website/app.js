const exspress = require('express'); // import express
var path = require('path'); // import path

const app = exspress(); // create express app

app.use(exspress.static(path.join(__dirname, 'public'))); // set public folder as static folder for static file
 
app.listen(3000)

console.log('Server started at port 3000');

function log(req, res) { // log function
    console.log(req.ip + ' ' + new Date().toLocaleString() + ' ' + req.url);
}

app.get('/', (req, res) => { // root path
    res.sendFile('./views/index.html', { root: __dirname });
    // out put to the console "ip address" "time" "request"
    log(req, res);
}
);


app.use((req, res) => { // 404 page
    res.status(404).sendFile('./views/404.html', { root: __dirname });
    log(req, res);
}   
);