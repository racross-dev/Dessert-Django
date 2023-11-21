const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');
const app = express();

app.use(cors()); // Habilitar CORS

// Configuración de la conexión a la base de datos
const connection = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  password: 'crossMYSQL87',
  database: 'piaprogra',
});

// Conectar a la base de datos
connection.connect();

// Ruta para mostrar la tabla de productos
app.get('/productos', (req, res) => {
  const query = 'SELECT * FROM Productos';
  connection.query(query, (error, results) => {
    if (error) throw error;
    res.json(results);
  });
});

// Cerrar la conexión a la base de datos cuando el servidor se apaga
app.on('exit', () => {
  connection.end();
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor de Node.js escuchando en el puerto ${PORT}`);
});
