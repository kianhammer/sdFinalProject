document.addEventListener("DOMContentLoaded", function() {
    getPlayerStats();
});

function getPlayerStats() {
    URL = "/stats/fetch";

    fetch(URL).then( response => response.json()).then( data => addPlayerToTable(data) );
}

function addPlayerToTable(playerData) {
    var table = document.getElementById("statsTable");

    var row = table.insertRow(0);

    var playerCell = row.insertCell(0);
    var pointsCell = row.insertCell(1);
    var holdsCell = row.insertCell(2);

    playerCell.innerHTML = playerData.player;
    pointsCell.innerHTML = playerData.points;
    holdsCell.innerHTML = playerData.holds;
    
    console.log(playerData);
}