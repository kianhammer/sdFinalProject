document.addEventListener("DOMContentLoaded", function() {
    getPlayerStats();
});

function getPlayerStats() {
    URL = "/stats/fetch";

    //fetch(URL).then( response => response.json()).then( data => addDataToTable(data["data"]) );
}

function addDataToTable(playerData) {
    var table = document.getElementById("statsTable");
    
    console.log(playerData);

    console.log("length =" + playerData.length)
    for(var i = 0; i < playerData.length; i++)
        var row = table.insertRow(i+1); // skip over header
        console.log("row = " + playerData[i])
        for(var j = 0; j < 3; j++) {
            var cell = row.insertCell(j);
            console.log("playerData[i][j] = " + playerData[i][j])
            cell.innerHTML = playerData[i][j]
        }

    console.log(playerData);
}