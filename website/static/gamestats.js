function updateGame(data) {
    the_json = data;

    score = the_json['score'];
    
    the_answer = document.getElementById("game_stats_display");
    the_answer.innerHTML = "The game score: " + score; 

}

function fetchGame() {
    the_game = document.getElementById("game_input").value;

    URL = "/game/stats/" + the_game;

    fetch(URL).then( response => response.json()).then( data => updateGame(data) );

    console.log("hello");
    
    console.log(URL);
   
}
