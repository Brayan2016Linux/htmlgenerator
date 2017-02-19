function iniciar() {
    var elemento = document.getElementById('lienzo');
    lienzo = elemento.getContext('2d');
    //lienzo.fillStyle = "#000099";
    //lienzo.strokeStyle = "#990000";

    //var gradiente = lienzo.createLinearGradient(0,0,10,100);
    //gradiente.addColorStop(0.5, '#0000FF');
    //gradiente.addColorStop(1, '#000000');
    //lienzo.fillStyle = gradiente;

    //lienzo.strokeRect(100,100,120,120);
    //lienzo.fillRect(110, 110, 100, 100);
    //lienzo.clearRect(120, 120, 80, 80);

    //lienzo.fillRect(10, 10, 100, 100);
    //lienzo.fillRect(150, 10, 200, 100);

    lienzo.beginPath();
    lienzo.moveTo(100, 100);
    lienzo.lineTo(200, 200);
    lienzo.lineTo(100, 200);
    //lienzo.closePath();
    //lienzo.stroke();
    //lienzo.fill();
    //lienzo.clip();

    //lienzo.beginPath();

    for(f=0; f<300; f = f+10) {
        lienzo.moveTo(0, f);
        lienzo.lineTo(500, f);
    }

    //lienzo.stroke();

    //lienzo.arc(100, 100, 50, 0, Math.PI*2, false);
    //lienzo.stroke();

    lienzo.lineWidth = 10;
    lienzo.lineCap = "round";
    var radianes = Math.PI/180*45;
    lienzo.arc(100, 100, 50, 0, radianes, false);
    //lienzo.stroke();

    lienzo.lineWidth = 5;
    lienzo.lineJoin = "miter";

    lienzo.beginPath();
    lienzo.moveTo(50,50);
    lienzo.quadraticCurveTo(100, 125, 50, 200);
    lienzo.moveTo(250, 50);
    lienzo.bezierCurveTo(200, 125, 300, 125, 250, 200);
    lienzo.stroke();

    lienzo.shadowColor = "rgba(0,0,0,0.5)";
    lienzo.shadowOffsetX = 4;
    lienzo.shadowOffsetY = 4;
    lienzo.shadowBlur = 5;
    
    lienzo.font = "bold 50px verdana, sans-serif";
    lienzo.textAlign="start";
    lienzo.fillText("Mi mensaje", 100, 100);

    lienzo.save();
    var tamano = lienzo.measureText("Mi mensaje");
    lienzo.strokeRect(100, 100, tamano.width, 24);

    lienzo.fillText("PRUEBA", 50, 70);
    lienzo.translate(50,70);
    lienzo.rotate(Math.PI/180*45);
    lienzo.fillText("PRUEBA", 0, 0);
    lienzo.rotate(-Math.PI/180*45);
    lienzo.translate(0,100);
    lienzo.scale(2,2);
    lienzo.fillText("PRUEBA", 0, 0);
    lienzo.setTransform(1,0,0,10,0,0);
    lienzo.fillText("PRUEBA1", 100, 20);
    lienzo.restore();
    lienzo.fillText("PRUEBA2", 100, 20);

}

window.addEventListener('load', iniciar, false);