let score = 0;
let tot=0;
let red=0;
let ScoreBoard= document.getElementById("scoreBoard");
let message2= document.getElementById('MessageClic');
let message = document.getElementById("balloonsGallery");
let  restart=document.getElementById("Restart");

document.addEventListener('mouseover', startGame);
restart.addEventListener('mousedown', RestartGame);
document.getElementById("click").addEventListener('mousedown', TextHidden);

function startGame(pEvent) {
    if(pEvent.target.className == "yellowBalloon"){
        pEvent.target.style.visibility = "hidden";
        score = score + 1
        ScoreBoard.textContent = score;
        endGame();
    }else if(pEvent.target.className == "redBalloon"){
        pEvent.target.style.visibility = "hidden";
        score = score - 1;
        ScoreBoard.textContent = score;
        lose();
        alert("You should click on the yellow macarons");
    }
}

function RestartGame() {
    location.reload();
 }


 function TextHidden() {
    message2.value="Bravo tu as trouvé le bouton !";
    alert("Bravo tu as trouvé le bouton !")
 }

function endGame(){
    tot=tot+1
    if(tot==5){
        message.textContent = "Well done ! You won"
        message.style.backgroundColor = "green";
    }
}

function lose(){
    red=red-1
    if(red==-3){
        message.textContent = "You lose"
        message.style.backgroundColor = "red";
    }
}
