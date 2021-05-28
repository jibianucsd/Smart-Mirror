document.addEventListener("DOMContentLoaded", (event) => {
    document.querySelector('#info').addEventListener("submit", function(e){
        var todo = document.getElementById("todo").value;
        var data = {f: todo};
        fetch(
        '/add_visitor',
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
    })
});