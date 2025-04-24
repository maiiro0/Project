let rockDiv = document.getElementById("rockDiv");
let paperDiv = document.getElementById("paperDiv");
let scissorsDiv = document.getElementById("scissorsDiv");
let userScoreSpan = document.getElementById("userScore");
let computerScoreSpan = document.getElementById("computerScore");

let options = ['rock','paper','scissors'];
let userScore = 0;
let computerScore = 0;

rockDiv.addEventListener("mouseover",hoverIsOn);
rockDiv.addEventListener("mouseout",hoverIsOff);
paperDiv.addEventListener("mouseover",hoverIsOn);
paperDiv.addEventListener("mouseout",hoverIsOff);
scissorsDiv.addEventListener("mouseover",hoverIsOn);
scissorsDiv.addEventListener("mouseout",hoverIsOff);

rockDiv.addEventListener('mousedown',function() {startGame('rock')});
paperDiv.addEventListener('mousedown',function() {startGame('paper')});
scissorsDiv.addEventListener('mousedown',function() {startGame('scissors')});

function hoverIsOn(pEvent){
    if(pEvent.target.className == "rps"){
        pEvent.target.style.backgroundColor='black';
        pEvent.target.style.transition = "0.4s";
        pEvent.target.style.cursor = "pointer";
    }
}

function hoverIsOff(pEvent){
    if(pEvent.target.className == "rps"){
        pEvent.target.style.backgroundColor= 'transparent' ;
    }
}

function startGame(pUserSelection) {
    let userChoice = pUserSelection;
    console.log("User:" + userChoice);

    let randomNumber = Math.floor(Math.random() * 3);
    console.log("random Number:" + randomNumber);

    let computerChoice = options[randomNumber];
    console.log("Computer: " + computerChoice);
    rockPaperScissors(userChoice, computerChoice);
}

function rockPaperScissors(puserChoice, pcomputerChoice) {
    let result = puserChoice + pcomputerChoice;
    if (result == 'rockrock' || result == 'paperpaper' || result == 'scissorsscissors'){
        console.log("Its a draw...");
    }

    if (result == 'rockscissors' || result == 'paperrock' || result == 'scissorspaper'){
        console.log("Good job. You Won !");

        userScore = userScore + 1;
        userScoreSpan.textContent = userScore;
    }

    if (result == 'scissorsrock' || result == 'rockpaper' || result == 'paperscissors'){
        console.log("Not so bad but enough. Try again");

        computerScore = computerScore + 1;
        computerScoreSpan.textContent = computerScore;
    }
}