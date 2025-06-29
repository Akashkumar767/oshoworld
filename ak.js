const pics = ["images/o1.jpg","images/osho.jpg","images/osho4.jpg"];
let i=0;
window.onload = function() {
    setInterval(() => {
        i=(i + 1) % pics.length;
        document.getElementById("right").src = pics[i];
    },4000);
};