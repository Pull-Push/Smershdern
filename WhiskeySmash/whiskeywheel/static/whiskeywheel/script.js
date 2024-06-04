function addPlayer() {
    var x = document.getElementById('player')
    if (x.style.display === "none") {
        x.style.display = "inline";
    }
}
function removePlayer() {
    var x = document.getElementById("player");
    if (x.style.display === "block") {
        x.style.display = "none";
    }
}