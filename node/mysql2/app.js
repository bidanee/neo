var mysql = require('mysql2/promise');
const env = require('dotenv').config({ path: "../../.env" }); 

const db =async() => {
    try{
        let connection = await mysql.createConnection({
            host: process.env.host,
            user: process.env.user,
            port: process.env.port,
            password: process.env.password,
            database: process.env.database    
        })
        
        let [rows, fields] = await connection.query('select * from st_info');
        console.log(rows);
        
        let data = {
            st_id:"202489",
            name:"Moon",
            dept:"Computer"
        }
        
        let insertId = data.st_id;

        // insert query
        [rows, fields] = await connection.query("insert into st_info set ?", data);
        console.log("\nData is inserted : " + insertId);

        // select * query for inserted data
        [rows, fields] = await connection.query("select * from st_info where st_id = ?", insertId);
        console.log(rows);

        // update query
        [rows, fields] = await connection.query("update st_info set dept = ? where st_id = ?", ["Game",insertId]);
        console.log("\nData is updated : " + insertId);

        // select * query for updated data
        [rows, fields] = await connection.query("select * from st_info where st_id = ?", insertId);
        console.log(rows);

        // delete query
        [rows, fields] = await connection.query("delete from st_info where st_id = ?", insertId);
        console.log("\nData is deleted : " + insertId);

        // select * query for deleted data
        [rows, fields] = await connection.query("select * from st_info where st_id = ?", insertId);
        console.log(rows);

    } catch (err) {
        console.log(err)
    }
}

db();

