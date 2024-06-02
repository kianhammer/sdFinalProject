function updateGame(data) {      
    statsDisplay = "";
    for (var key in data){
        statsDisplay = statsDisplay + "The game " + key + ": " + data[key] + "<br>";
    }

    the_answer = document.getElementById("game_stats_display");
    the_answer.innerHTML = statsDisplay;  
    
    updateGameFlow(data);
    updateHucks(data);

}

function updateGameFlow(data){
    gameFlowTitle = document.getElementById("gameFlowTitle");
    gameFlowDescription = document.getElementById("gameFlowDescription");

    gameFlowTitle.innerHTML = "Game Flow:";
    gameFlowDescription.innerHTML = data['opponent'] + " Breaks: " + data['oppBreaks'] + "  |  " + data['opponent'] + " Holds: " + data['oppHolds'] + "  |  CUT Holds: " + data['cutHolds'] + "  |  CUT Breaks: " + data['cutBreaks'];
    
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
    hucksTitle = document.getElementById("hucksTitle");
    hucksDescription = document.getElementById("hucksDescription");

    hucksTitle.innerHTML = "Hucks:";
    hucksDescription.innerHTML = "Incomplete Hucks: " + data['incompleteHucks'] + "  |  Complete Hucks: " + data['completeHucks'];

    totalHucks = data['incompleteHucks'] + data['completeHucks'];
    hucksIncomplete_bar = document.getElementById("hucksIncomplete_bar");
    hucksComplete_bar = document.getElementById("hucksComplete_bar");
    hucksIncomplete_bar.style = "width: " + 100 * data['incompleteHucks']/totalHucks + "%";
    hucksComplete_bar.style = "width: " + 100 * data['completeHucks']/totalHucks + "%";
}

function fetchGame() {
    the_game = document.getElementById("change_game_input").value;

    console.log(the_game);
    
    URL = "/stats/game/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}
