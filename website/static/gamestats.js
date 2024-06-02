function updateGame(data) {      
    statsDisplay = "";
    for (var key in data){
        statsDisplay = statsDisplay + "The game " + key + ": " + data[key] + "<br>";
    }

    the_answer = document.getElementById("game_stats_display");
    the_answer.innerHTML = statsDisplay;  
    
    updateGameFlow(data);
    updateHucks(data);
    updateEndzone(data);
    updateBlocks(data);
    updateTurnovers(data);

}

function updateGameFlow(data){
    document.getElementById("gameFlowBar").style = "border: solid";
    
    gameFlowTitle = document.getElementById("gameFlowTitle");
    gameFlowDescription = document.getElementById("gameFlowDescription");

    gameFlowTitle.innerHTML = "Game Flow:";
    gameFlowDescription.innerHTML = data['opponent'] + " Breaks: " + data['oppBreaks'] + "  |  " + data['opponent'] + " Holds: " + data['oppHolds'] + "  |  CUT Holds: " + data['cutHolds'] + "  |  CUT Breaks: " + data['cutBreaks'] + "<br> <br>";
    
    oppBreaks_bar = document.getElementById("oppBreaks_bar");
    oppHolds_bar = document.getElementById("oppHolds_bar");
    cutHolds_bar = document.getElementById("cutHolds_bar");
    cutBreaks_bar = document.getElementById("cutBreaks_bar");
    oppBreaks_bar.style = "width: " + 100 * data['oppBreaks']/data['points'] + "%";
    oppHolds_bar.style = "width: " + 100 * data['oppHolds']/data['points'] + "%";
    cutHolds_bar.style = "width: " + 100 * data['cutHolds']/data['points'] + "%";
    cutBreaks_bar.style = "width: " + 100 * data['cutBreaks']/data['points'] + "%";
}

function updateHucks(data){
    document.getElementById("hucksBar").style = "border: solid";
    
    hucksTitle = document.getElementById("hucksTitle");
    hucksDescription = document.getElementById("hucksDescription");

    hucksTitle.innerHTML = "Hucks:";
    hucksDescription.innerHTML = "Incomplete Hucks: " + data['incompleteHucks'] + "  |  Complete Hucks: " + data['completeHucks'] + "<br> <br>";

    totalHucks = data['incompleteHucks'] + data['completeHucks'];
    hucksIncomplete_bar = document.getElementById("hucksIncomplete_bar");
    hucksComplete_bar = document.getElementById("hucksComplete_bar");
    hucksIncomplete_bar.style = "width: " + 100 * data['incompleteHucks']/totalHucks + "%";
    hucksComplete_bar.style = "width: " + 100 * data['completeHucks']/totalHucks + "%";
}

function updateEndzone(data){
    document.getElementById("endzoneBar").style = "border: solid";
    
    endzoneTitle = document.getElementById("endzoneTitle");
    endzoneDescription = document.getElementById("endzoneDescription");

    endzoneTitle.innerHTML = "Endzone:";
    endzoneDescription.innerHTML = "Endzones Not Scored: " + data['endzoneNotScores'] + "  |  Endzones Scores: " + data['endzoneScores'] + "<br> <br>";

    totalEndzoneChances = data['endzoneNotScores'] + data['endzoneScores'];
    endzoneNotScores_bar = document.getElementById("endzoneNotScores_bar");
    endzoneScores_bar = document.getElementById("endzoneScores_bar");
    endzoneNotScores_bar.style = "width: " + 100 * data['endzoneNotScores']/totalEndzoneChances + "%";
    endzoneScores_bar.style = "width: " + 100 * data['endzoneScores']/totalEndzoneChances + "%";
}

function updateBlocks(data){
    document.getElementById("blocksBar").style = "border: solid";
    
    blocksTitle = document.getElementById("blocksTitle");
    blocksDescription = document.getElementById("blocksDescription");

    blocksTitle.innerHTML = "Blocks:";
    blocksDescription.innerHTML = "Unforced Blocks: " + data['blocksUnforced'] + "  |  Forced Blocks: " + data['blocksForced'] + "<br> <br>";

    totalBlocks = data['blocksUnforced'] + data['blocksForced'];
    blocksUnforced_bar = document.getElementById("blocksUnforced_bar");
    blocksForced_bar = document.getElementById("blocksForced_bar");
    blocksUnforced_bar.style = "width: " + 100 * data['blocksUnforced']/totalBlocks + "%";
    blocksForced_bar.style = "width: " + 100 * data['blocksForced']/totalBlocks + "%";
}

function updateTurnovers(data){
    document.getElementById("turnoversBar").style = "border: solid";
    
    turnoversTitle = document.getElementById("turnoversTitle");
    turnoversDescription = document.getElementById("turnoversDescription");

    turnoversTitle.innerHTML = "Turnovers:";
    turnoversDescription.innerHTML = "Unforced Turnovers: " + data['turnoversUnforced'] + "  |  Forced Turnovers: " + data['turnoversForced'] + "<br> <br>";

    totalTurnovers = data['turnoversUnforced'] + data['turnoversForced'];
    turnoversUnforced_bar = document.getElementById("turnoversUnforced_bar");
    turnoversForced_bar = document.getElementById("turnoversForced_bar");
    turnoversUnforced_bar.style = "width: " + 100 * data['turnoversUnforced']/totalTurnovers + "%";
    turnoversForced_bar.style = "width: " + 100 * data['turnoversForced']/totalTurnovers + "%";
}

function fetchGame() {
    the_game = document.getElementById("change_game_input").value;

    console.log(the_game);
    
    URL = "/stats/game/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}
