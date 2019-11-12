const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World! <h1>Demo App Version 02<h1>'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
