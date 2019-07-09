'use strict';

const express = require('express');
const mysql = require('mysql');
// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
const db = mysql.createConnection({
	host: "localhost",
	user:"root",
	password: "",
	database: "latihan"	
	});
var sql = "select * from docker2 order by id desc limit 1";
app.get('/', (req, res) => {
  	

	db.query(sql, function(err, result){
	result.forEach(data1 => {
	res.send(`${data1.id} \t ${data1.time}`);	
	});
	});	

	
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
