import { createServer } from 'nodejs-websocket';
import mongoose from 'mongoose';
// eslint-disable-next-line import/extensions
import { search, defaultError } from './src/websocket.js';
import connect from './src/database.js';

connect();

const server = createServer((conn) => {
  conn.on('text', (message) => {
    const msg = JSON.parse(message);
    switch (msg.type) {
      case 'search':
        search(conn, msg.data);
        break;
      default:
        defaultError(conn, msg);
        break;
    }
  });
  conn.on('close', (code, reason) => {
    console.log(`Disconnection code: ${code} ${reason}`);
  });
}).listen(3000);

function broadcast(message) {
  server.connections.forEach((connection) => {
    connection.sendText(message);
  });
}
