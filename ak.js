const pics = ["images/o.jpg","images/osho.jpeg","images/osho3.jpg"];
let i=0;
window.onload = function() {
    setInterval(() => {
        i=(i + 1) % pics.length;
        document.getElementById("right").src = pics[i];
    },3000);
};