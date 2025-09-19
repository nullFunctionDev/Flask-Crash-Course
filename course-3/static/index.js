// Our three emoji boxes
const laughingBox = document.getElementById("laughingBox");
const scaredBox = document.getElementById("scaredBox");
const madBox = document.getElementById("madBox");


// Change the color of the laughing box when hovering over, back to default when leaving div
laughingBox.addEventListener("mouseover", () => {
    laughingBox.style.backgroundColor = "lightblue";
});

laughingBox.addEventListener("mouseleave", () => {
    laughingBox.style.backgroundColor = "lightgreen";
});


// Change the emoji and color of the scared box on hover, revert back when leaving
scaredBox.addEventListener("mouseover", () => {
    scaredBox.textContent = "💀";
    scaredBox.style.backgroundColor = "purple";
});

scaredBox.addEventListener("mouseleave", () => {
    scaredBox.textContent = "😧";
    scaredBox.style.backgroundColor = "lightyellow";
});


// For the mad face, lets do this when we click it, make it a toggle button
let toggle = 1;

madBox.addEventListener("mousedown", () => {
    if (toggle == 1) {
        toggle = 2;
        madBox.textContent = "😁";
        madBox.style.backgroundColor = "lightpink";
    } else {
        toggle = 1;
        madBox.textContent = "😡";
        madBox.style.backgroundColor = "red";
    }
});