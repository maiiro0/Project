const CANVAS = document.getElementById('canvas');
const CTX = CANVAS.getContext('2d');
const GAME_OVER_IMG_WIDTH = 960;
const GAME_OVER_IMG_HEIGHT = 574;
const GAME_OVER_IMG = new Image();
GAME_OVER_IMG.src = "./images/collector/GameOverMessage.png";
const BG_IMG = new Image();
BG_IMG.src = "./images/collector/bgImage.png";

const PLAYER = {
    img: new Image(),
    x: 200,
    y: 200,
    width: 25,
    height: 45,
    enlarge: 2.5,
    face: {
        "up": "./images/collector/yuki/up.png",
        "down": "./images/collector/yuki/down.png",
        "left": "./images/collector/yuki/left.png",
        "right": "./images/collector/yuki/right.png"
    },
    speed: 15,
};

PLAYER.img.src = PLAYER.face["down"];

const KEYS = {
    "ArrowUp": false,
    "ArrowDown": false,
    "ArrowRight": false,
    "ArrowLeft": false,
    "r": false,
};

updateCanvasSize();
window.onresize = updateCanvasSize();

let gameOverImgX = CANVAS.width / 2 - GAME_OVER_IMG_WIDTH / 2;
let gameOverImgY = CANVAS.height / 2 - GAME_OVER_IMG_HEIGHT / 2;
let time = 10;
let gameOn = true;

let pokemon1 = new Figure(CTX, "./images/collector/pokemons/pokemon1.png", "pikachu", 0.3);
let pokemon2 = new Figure(CTX, "./images/collector/pokemons/pokemon2.png", "giglipah", 0.3);
let pokemon3 = new Figure(CTX, "./images/collector/pokemons/pokemon3.png", "balbazaur", 0.5);
let pokemonsGroup = [pokemon1, pokemon2, pokemon3];

document.addEventListener('keydown', addKey);
document.addEventListener('keyup', removeKey);

function updateCanvasSize() {
    CANVAS.width = CANVAS.clientWidth;
    CANVAS.height = CANVAS.clientWidth * 0.5;
}

function writeText(text = "TEXT", color = "black", size = "30", font = "Arial", style = "", x = CANVAS.width / 2, y = CANVAS.height / 2) {
    CTX.font = style + " " + size + "px " + font;
    CTX.fillStyle = color;
    CTX.fillText(text, x, y);
}

function gameLoop() {
    if(gameOn == true){
        //CTX.clearRect(0, 0, CANVAS.width, CANVAS.height);
        CTX.drawImage(BG_IMG, 0, 0, CANVAS.width, CANVAS.height);
        writeText("Time: " + time, "black", 50, undefined, "bold", 1000, 70);
        drawFigure(PLAYER);
        controlPlayerMove();
        //pokemon1.draw();
        //pokemon2.draw();
        //pokemon3.draw();
        for(let i = 0; i < pokemonsGroup.length; i++){
            pokemonsGroup[i].draw();
            pokemonsGroup[i].moveToRandomLoc();
        }
        //timer();
        //setTimeout(function() {requestAnimationFrame(gameLoop);}, 1000);
        requestAnimationFrame(gameLoop);
    }
}
gameLoop();
setInterval(timer, 1000);

function timer() {
    if(time > 0){
        time--;
    }
    else{
        gameOver();
    }
}

function gameOver() {
    gameOn = false;

    CTX.clearRect(0, 0, CANVAS.width, CANVAS.height);
    CTX.drawImage(GAME_OVER_IMG, gameOverImgX, gameOverImgY, GAME_OVER_IMG_WIDTH, GAME_OVER_IMG_HEIGHT);
}

function addKey(pEvent) {
    KEYS[pEvent.key] = true;
}

function removeKey(pEvent) {
    KEYS[pEvent.key] = false;
    PLAYER.img.src = PLAYER.face["down"];
}

function controlPlayerMove() {
    if(KEYS["ArrowUp"] && PLAYER.y > 0){
        PLAYER.y = PLAYER.y - PLAYER.speed;
        PLAYER.img.src = PLAYER.face["up"];
    }

    if(KEYS["ArrowLeft"] && PLAYER.x > 0){
        PLAYER.x = PLAYER.x - PLAYER.speed;
        PLAYER.img.src = PLAYER.face["left"];
    }

    if(KEYS["ArrowDown"] && PLAYER.y < (CANVAS.height - PLAYER.height + PLAYER.enlarge)){
        PLAYER.y = PLAYER.y + PLAYER.speed;
        PLAYER.img.src = PLAYER.face["down"];
    }

    if(KEYS["ArrowRight"] && PLAYER.x < (CANVAS.width - PLAYER.width + PLAYER.enlarge)){
        PLAYER.x = PLAYER.x + PLAYER.speed;
        PLAYER.img.src = PLAYER.face["right"];
    }
}

