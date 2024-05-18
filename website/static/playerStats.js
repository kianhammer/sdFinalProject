document.addEventListener("DOMContentLoaded", function() {
    getPlayerStats();
});

function getPlayerStats() {
    URL = "/stats/fetch";

    fetch(URL).then( response => response.json()).then( data => addDataToTable(data["data"]) );
}

function addDataToTable(playerData) {
    var table = document.getElementById("statsTable");
    
    console.log(playerData);

    for(var i = 0; i < playerData.length; i++)
        var row = table.insertRow(i+1); // skip over header
        for(var j = 0; j < playerData[i].length; j++) {
            var cell = row.insertCell(j);
            cell.innerHTML = playerData[i][j]
        }

    console.log(playerData);
}