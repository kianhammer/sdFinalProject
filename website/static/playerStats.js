document.addEventListener("DOMContentLoaded", function() {
    getPlayerStats();
});

function getPlayerStats() {
    URL = "/stats/fetch";

    fetch(URL).then( response => response.json()).then( data => addPlayerToTable(data) );
}

function addPlayerToTable(playerData) {
    console.log(playerData);
}