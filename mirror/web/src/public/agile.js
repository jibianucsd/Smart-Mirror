document.addEventListener("DOMContentLoaded", (event) => {
    document.querySelector('#info').addEventListener("submit", function(e){
        var todo = document.getElementById("todo").value;
        var data = {f: todo};
        fetch(
        '/add_todolist',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        e.preventDefault();
    });
    
    document.querySelector('#del').addEventListener("submit", function(e){
        var mysql = require('mysql');
        var con = mysql.createConnection({
        host: "db-server",
        user: "admin",
        password: "ADMIN_PASSWORD",
        database: "the_db"
        });

        con.connect(function(err) {
        if (err) throw err;
        var sql = "DROP TABLE List";
        con.query(sql, function (err, result) {
            if (err) throw err;
            console.log("Table deleted");
        });
        });
    });

    
});

