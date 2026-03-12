// -----------------------------
// CANVAS SETUP
// -----------------------------

const canvas = document.getElementById("algaeCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 420;
canvas.height = 420;

let algaeParticles = [];
let bubbles = [];

// -----------------------------
// CREATE ALGAE PARTICLES
// -----------------------------

function createAlgae(count){

algaeParticles=[];

for(let i=0;i<count;i++){

algaeParticles.push({

x:Math.random()*420,
y:Math.random()*420,
r:Math.random()*3+1,
speed:Math.random()*0.4+0.1

});

}

}

// -----------------------------
// CREATE BUBBLES
// -----------------------------

function createBubbles(){

for(let i=0;i<25;i++){

bubbles.push({

x:Math.random()*420,
y:420,
r:Math.random()*3+1,
speed:Math.random()*1+0.5

});

}

}

createBubbles();


// -----------------------------
// DRAW LOOP
// -----------------------------

function drawReactor(){

ctx.clearRect(0,0,420,420);

// algae
algaeParticles.forEach(p=>{

ctx.beginPath();
ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
ctx.fillStyle="lime";
ctx.fill();

p.y -= p.speed;

if(p.y < 0){
p.y = 420;
}

});

// bubbles
bubbles.forEach(b=>{

ctx.beginPath();
ctx.arc(b.x,b.y,b.r,0,Math.PI*2);
ctx.fillStyle="rgba(255,255,255,0.6)";
ctx.fill();

b.y -= b.speed;

if(b.y < 0){
b.y = 420;
}

});

requestAnimationFrame(drawReactor);

}

drawReactor();


// -----------------------------
// GROWTH GRAPH
// -----------------------------

let growthChart;

function initChart(){

const ctxChart = document.getElementById("growthChart").getContext("2d");

growthChart = new Chart(ctxChart,{

type:"line",

data:{
labels:[],
datasets:[{
label:"Biomass Growth",
data:[],
borderColor:"#00ff9d",
backgroundColor:"rgba(0,255,150,0.1)",
tension:0.4
}]
},

options:{
responsive:true,
plugins:{
legend:{display:true}
},
scales:{
x:{title:{display:true,text:"Simulation Step"}},
y:{title:{display:true,text:"Population"}}
}
}

});

}

initChart();

function updateGraph(value){

growthChart.data.labels.push(growthChart.data.labels.length);

growthChart.data.datasets[0].data.push(value);

growthChart.update();

}


// -----------------------------
// CO2 METER
// -----------------------------

function updateCO2Meter(efficiency){

const meter = document.getElementById("co2_fill");
const label = document.getElementById("co2_value");

meter.style.width = efficiency + "%";

label.innerText = efficiency + "%";

}


// -----------------------------
// SHOW OPTIMIZATION SUGGESTIONS
// -----------------------------

function showSuggestions(opt){

if(!opt) return;

document.getElementById("suggestions").innerHTML =

"<b>Suggested Optimal Parameters:</b><br><br>" +

"Light: " + opt.Light + "<br>" +
"Nitrate: " + opt.Nitrate + "<br>" +
"Iron: " + opt.Iron + "<br>" +
"Phosphate: " + opt.Phosphate + "<br>" +
"Temperature: " + opt.Temperature + "<br>" +
"pH: " + opt.pH + "<br>" +
"CO₂: " + opt.CO2;

}


// -----------------------------
// MAIN PREDICTION FUNCTION
// -----------------------------

function predict(){

const data = {

Light:document.getElementById("Light").value,
Nitrate:document.getElementById("Nitrate").value,
Iron:document.getElementById("Iron").value,
Phosphate:document.getElementById("Phosphate").value,
Temperature:document.getElementById("Temperature").value,
pH:document.getElementById("pH").value,
CO2:document.getElementById("CO2").value

};

fetch("/predict",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)

})

.then(res=>res.json())

.then(res=>{

const population = res.population;

document.getElementById("result").innerText = population;


// algae density scaling

let algaeCount = Math.min(Math.floor(population/8),900);

createAlgae(algaeCount);


// update graph

updateGraph(population);


// update CO2 meter

updateCO2Meter(res.co2_efficiency);


// show optimization suggestions

if(res.optimization){

showSuggestions(res.optimization);

}

})

.catch(err=>{

console.log(err);

});

}