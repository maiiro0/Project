let canvas  = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
let dropdown = document.getElementById("animations")
dropdown.addEventListener('change', setState);

const CANVAS_WIDTH = canvas.width = 700;
const CANVAS_HEIGHT = canvas.height = 480;
const SPRITE_WIDTH = 680;
const SPRITE_HEIGHT = 475;
const SPRITE_FRAMES = {
    "Idle": {frames: 10},
    "Jump": {frames:10},
    "Run": {frames:8, soundSrc: "./sounds/dragonBreathingRunning.mp3"},
    "Shoot": {frames:3},
    "Dead": {frames:10},
    "Slide": {frames:5},
    "Melee": {frames:7},
};

let playerState = "Idle";
let frame = 1;

let playerImage = new Image();
let sound = new Audio();
//playerImage.src = "images/girl/" + playerState + " " + "(" + frame + ")" + ".png";
//playerImage.onload = animate;

function setState(pEvent) {
    playerState = pEvent.target.value;
    sound.pause();
    sound.src =  SPRITE_FRAMES[playerState].soundSrc;
    sound.loop = true;
    sound.play();
}

function animate() {
    let numOfFrames = SPRITE_FRAMES[playerState].frames;
    playerImage.src = "images/girl/" + playerState + " " + "(" + frame + ")" + ".png";
    playerImage.onload = () =>{
        ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
        ctx.drawImage(playerImage, 10, 40, SPRITE_WIDTH, SPRITE_HEIGHT);

        if(frame < numOfFrames){
            frame++;
        }
        else{
            frame = 1;
        }
    
    }

    setTimeout(function() {requestAnimationFrame(animate);}, 200)
}

animate()