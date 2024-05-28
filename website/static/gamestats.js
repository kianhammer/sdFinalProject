function updateGame(data) {
    the_json = data;
    
    statsDisplay = "";
    for (var key in data){
        statsDisplay = statsDisplay + "The game " + key + ": " + data[key] + "<br>";
    }

    the_answer = document.getElementById("game_stats_display");
    the_answer.innerHTML = statsDisplay; 
    
    score = the_json['score'];
    opponent = the_json['opponent'];
    date = the_json['date'];
    cutBreaks = the_json['cutBreaks'];
    cutHolds = the_json['cutHolds'];
    oppBreaks = the_json['oppBreaks'];
    oppHolds = the_json['oppHolds'];
    completeHucks = the_json['completeHucks'];
    incompleteHucks = the_json['incompleteHucks'];
    endzoneScores = the_json['endzoneScores'];
    endzoneNotScores = the_json['endzoneNotScores'];
    blocksForced = the_json['blocksForced'];
    blocksUnforced = the_json['blocksUnforced'];
    turnoversForced = the_json['turnoversForced'];
    turnoversUnforced = the_json['turnoversUnforced'];
    
    

}





function fetchGame() {
    the_game = document.getElementById("change_game_input").value;

    console.log(the_game);
    
    URL = "/stats/game/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}
