window.addEventListener("load", () => {
    let lon;
    let lat;
    let temperature = document.querySelector(".temp");
    let summary = document.querySelector(".summary");
    let loc = document.querySelector(".location");
    const kelvin = 273;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
        lon = position.coords.longitude;
        console.log(lon);
        lat = position.coords.latitude;
        const base = 
        `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&` + `lon=${lon}&appid=e19c3e3e82c8211fb4b268df78a7ae8e`;

        fetch(base)
            .then((response) => {
            return response.json();
            })
            .then((data) => {
            var city = data.name.replace("(historical)", "");
            temperature.innerHTML = Math.floor(data.main.temp - kelvin) + "°C " + city;
            });
        });
    }
});