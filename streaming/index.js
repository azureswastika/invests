var ws = require("nodejs-websocket")

var server = ws.createServer(function (conn) {
    // on connection
    conn.on("text", function (str) {
        // on message
    })
    conn.on("close", function (code, reason) {
        // on close
    })
}).listen(3000)
