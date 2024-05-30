function updateGame(data) {      
    statsDisplay = "";
    for (var key in data){
        statsDisplay = statsDisplay + "The game " + key + ": " + data[key] + "<br>";
    }

    the_answer = document.getElementById("game_stats_display");
    the_answer.innerHTML = statsDisplay;  
    
    test_bar = document.getElementById("test_bar");
    test_bar.style = "width: " + 10 * data['oppBreaks']/data['points'] + "%";
}





function fetchGame() {
    the_game = document.getElementById("change_game_input").value;

    console.log(the_game);
    
    URL = "/stats/game/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}
