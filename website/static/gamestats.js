function updateGame(data) {
    the_json = data;

    score = the_json['score'];
    
    the_answer = document.getElementById("game_stats_display");
    the_answer.innerHTML = "The game score: " + score; 

}

function fetchGame() {
    the_game = document.getElementById("change_game_input").value;

    console.log(the_game);
    
    URL = "/stats/game/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}
