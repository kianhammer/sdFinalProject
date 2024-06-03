/* File contributers: Kian */
function fetchGame() {
    the_game = document.getElementById("change_game_input").value;

    console.log(the_game);
    
    URL = "/stats/game/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}

function updateGame(data) {      
    
    updateGameHeader(data);
    updateGameFlow(data);
    updateHucks(data);
    updateEndzone(data);
    updateBlocks(data);
    updateTurnovers(data);

}

function updateGameHeader(data){
    inputGameDescription = document.getElementById("inputGameDescription");
    gameHeader = document.getElementById("gameHeader");

    inputGameDescription.innerHTML = "Pick A Different Game To See Its Statistics";

    gameHeaderText = "<br> Carleton vs " + data['opponent'];
    gameHeaderText = gameHeaderText + "<br> " + data['date'];
    gameHeaderText = gameHeaderText + "<br><br> Final Score: <br>" + data['score'] + "<br><br>";
    gameHeader.innerHTML = gameHeaderText;
}

function updateGameFlow(data){
    // Make the bar visible
    document.getElementById("gameFlowBar").style = "width: 80%;";
    
    gameFlowTitle = document.getElementById("gameFlowTitle");
    gameFlowDescription = document.getElementById("gameFlowDescription");

    gameFlowTitle.innerHTML = "Game Flow:";
    gameFlowDescription.innerHTML = data['opponent'] + " Breaks: " + data['oppBreaks'] + "  |  " + data['opponent'] + " Holds: " + data['oppHolds'] + "  |  CUT Holds: " + data['cutHolds'] + "  |  CUT Breaks: " + data['cutBreaks'] + "<br> <br> <br> <br>";
    
    oppBreaks_bar = document.getElementById("oppBreaks_bar");
    oppHolds_bar = document.getElementById("oppHolds_bar");
    cutHolds_bar = document.getElementById("cutHolds_bar");
    cutBreaks_bar = document.getElementById("cutBreaks_bar");
    // Set the lengths of the inner bars for each stat
    oppBreaks_bar.style = "width: " + 100 * data['oppBreaks']/data['points'] + "%";
    oppHolds_bar.style = "width: " + 100 * data['oppHolds']/data['points'] + "%";
    cutHolds_bar.style = "width: " + 100 * data['cutHolds']/data['points'] + "%";
    cutBreaks_bar.style = "width: " + 100 * data['cutBreaks']/data['points'] + "%";
}

function updateHucks(data){
    document.getElementById("hucksBar").style = "width: 80%;";
    
    hucksTitle = document.getElementById("hucksTitle");
    hucksDescription = document.getElementById("hucksDescription");

    hucksTitle.innerHTML = "Hucks:";
    hucksDescription.innerHTML = "Incomplete Hucks: " + data['incompleteHucks'] + "  |  Complete Hucks: " + data['completeHucks'] + "<br> <br> <br> <br>";

    totalHucks = data['incompleteHucks'] + data['completeHucks'];
    hucksIncomplete_bar = document.getElementById("hucksIncomplete_bar");
    hucksComplete_bar = document.getElementById("hucksComplete_bar");
    
    if(totalHucks == 0){
        hucksIncomplete_bar.style = "width: 0%";
        hucksComplete_bar.style = "width: 0%";
        return;
    }
    
    hucksIncomplete_bar.style = "width: " + 100 * data['incompleteHucks']/totalHucks + "%";
    hucksComplete_bar.style = "width: " + 100 * data['completeHucks']/totalHucks + "%";
}

function updateEndzone(data){
    document.getElementById("endzoneBar").style = "width: 80%;";
    
    endzoneTitle = document.getElementById("endzoneTitle");
    endzoneDescription = document.getElementById("endzoneDescription");

    endzoneTitle.innerHTML = "Endzone:";
    endzoneDescription.innerHTML = "Endzones Not Scored: " + data['endzoneNotScores'] + "  |  Endzones Scored: " + data['endzoneScores'] + "<br> <br> <br> <br>";

    totalEndzoneChances = data['endzoneNotScores'] + data['endzoneScores'];
    endzoneNotScores_bar = document.getElementById("endzoneNotScores_bar");
    endzoneScores_bar = document.getElementById("endzoneScores_bar");
    
    if(totalEndzoneChances == 0){
        endzoneNotScores_bar.style = "width: 0%";
        endzoneScores_bar.style = "width: 0%";
        return;
    }
    
    endzoneNotScores_bar.style = "width: " + 100 * data['endzoneNotScores']/totalEndzoneChances + "%";
    endzoneScores_bar.style = "width: " + 100 * data['endzoneScores']/totalEndzoneChances + "%";
}

function updateBlocks(data){
    document.getElementById("blocksBar").style = "width: 80%;";
    
    blocksTitle = document.getElementById("blocksTitle");
    blocksDescription = document.getElementById("blocksDescription");

    blocksTitle.innerHTML = "Blocks:";
    blocksDescription.innerHTML = "Unforced Blocks: " + data['blocksUnforced'] + "  |  Forced Blocks: " + data['blocksForced'] + "<br> <br> <br> <br>";

    totalBlocks = data['blocksUnforced'] + data['blocksForced'];
    blocksUnforced_bar = document.getElementById("blocksUnforced_bar");
    blocksForced_bar = document.getElementById("blocksForced_bar");
    
    if(totalBlocks == 0){
        blocksUnforced_bar.style = "width: 0%";
        blocksForced_bar.style = "width: 0%";
        return;
    }
    
    blocksUnforced_bar.style = "width: " + 100 * data['blocksUnforced']/totalBlocks + "%";
    blocksForced_bar.style = "width: " + 100 * data['blocksForced']/totalBlocks + "%";
}

function updateTurnovers(data){
    document.getElementById("turnoversBar").style = "width: 80%;";
    
    turnoversTitle = document.getElementById("turnoversTitle");
    turnoversDescription = document.getElementById("turnoversDescription");

    turnoversTitle.innerHTML = "Turnovers:";
    turnoversDescription.innerHTML = "Unforced Turnovers: " + data['turnoversUnforced'] + "  |  Forced Turnovers: " + data['turnoversForced'] + "<br> <br> <br> <br>";

    totalTurnovers = data['turnoversUnforced'] + data['turnoversForced'];
    turnoversUnforced_bar = document.getElementById("turnoversUnforced_bar");
    turnoversForced_bar = document.getElementById("turnoversForced_bar");
    
    if(totalTurnovers == 0){
        turnoversUnforced_bar.style = "width: 0%";
        turnoversForced_bar.style = "width: 0%";
        return;
    }
    
    turnoversUnforced_bar.style = "width: " + 100 * data['turnoversUnforced']/totalTurnovers + "%";
    turnoversForced_bar.style = "width: " + 100 * data['turnoversForced']/totalTurnovers + "%";
}
