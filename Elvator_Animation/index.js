const express = require('express')
const path = require('path')


const app = express();

var i = 1;
var open = false;
var close = false;

app.use(express.json());
app.use(express.urlencoded({ extended: false }))
app.use(express.static(path.join(__dirname, 'public')));

app.post('/get_i', (req, res) => {
    res.json({
        "i": i,
        "open": open,
        "close": close
    })
    setTimeout(() => {
        open = false
        close = false
    }, 10)
});
app.post('/change', (req, res) => {
    i = req.body.text
    res.json(i)
});
app.post('/door', (req, res) => {
    const data = req.body.text
    open = data == "o" ? true : false
    close = data == "c" ? true : false
    res.json("ok")
});



app.listen(5000, () => console.log('Server started'))
