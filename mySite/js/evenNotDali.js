let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

let isDrawing = false;
let drawColor = "black";
let drawWidth =  "2";
let restoreArray = [];
let index = -1;

canvas.addEventListener("mousedown", start);
canvas.addEventListener("mousemove", draw);
canvas.addEventListener("mouseup", stopDraw);
fix_dpi();

updateCanvasSize();
window.onresize = updateCanvasSize();

function start(pEvent) {
    isDrawing = true;
    ctx.beginPath();
    ctx.moveTo(pEvent.clientX - canvas.getBoundingClientRect().left,
            pEvent.clientY - canvas.getBoundingClientRect().top);
}

function draw(pEvent) {
    if(isDrawing){
        //ctx.lineTo(pEvent.clientX, pEvent.clientY);
        ctx.lineTo(pEvent.clientX - canvas.getBoundingClientRect().left,
                pEvent.clientY - canvas.getBoundingClientRect().top);
        ctx.strokeStyle = drawColor;
        ctx.lineCap = "round";
        ctx.lineJoin = "round";
        ctx.lineWidth = drawWidth;
        ctx.stroke();
    }
}

function stopDraw() {
    isDrawing = false;

    restoreArray.push(ctx.getImageData(0,0,canvas.width, canvas.height));
    index = index + 1;
}

function updateCanvasSize() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientWidth * 0.5;
}

function changeColor(pElement) {
    drawColor = pElement.style.background;
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";

    restoreArray = [];
    index = -1;
}

function saveImage() {
    let dataUrl = canvas.toDataURL("image/png");
    let downloadLink = document.createElement('a');
    let imageName = prompt("Please choose a name for your painting", "My paint")
    downloadLink.href = dataUrl;
    downloadLink.download = imageName;
    downloadLink.click();
    downloadLink.delete;
}

function undoLast() {
    if(index <= 0) {
        clearCanvas();
    }
    else{
        index--
        restoreArray.pop();
        ctx.putImageData(restoreArray[index],0,0);
    }
}

//fix_dpi();
//ctx.beginPath();

//ctx.beginPath()
//ctx.lineWidth = '5';
//ctx.strokeStyle = "green";
//ctx.moveTo(50,0);
//ctx.lineTo(50, canvas.height);
//ctx.stroke();

//ctx.font = "50px Comic Sans MS";
//ctx.fillStyle = "orange";
//ctx.textAlign = "center";
//ctx.fillText("Be cool", canvas.width/2, canvas.height/2);

//ctx.fillStyle = "red";
//ctx.fillRect(canvas.width/2, canvas.height/2, 80, 80);