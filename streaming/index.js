const ws = require('nodejs-websocket');

const server = ws.createServer((conn) => {
  conn.on('text', (message) => {
    if (message.command === 'search') {
      //
    }
  });
  conn.on('close', (code, reason) => {
    console.log(code, reason);
  });
}).listen(3000);

function broadcast(message) {
  server.connections.forEach((connection) => {
    connection.sendText(message);
  });
}
