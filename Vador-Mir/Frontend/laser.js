let normalCursor = "url('curseur0.png') 0 0, auto";
let currentCursor = normalCursor;
let count = 0;
let jeu = false;
  window.addEventListener("keydown", function(event) {
      // Vérifie si la touche est "k" ou "K"
      if (event.key.toLowerCase() === "k") {
        if(jeu == true){
        document.body.style.cursor = "auto";
        jeu = false;
        }else{
          count =0;
          document.body.style.cursor =  "url('../css/curseur0.png') 0 0, auto";
          jeu = true;
           function creerCible(x, y) {
      const cible = document.createElement("div");
      cible.classList.add("cible");
      cible.style.left = x + "px";
      cible.style.top = y + "px";
      document.body.appendChild(cible);
    }
         for (let i = 0; i < 30; i++) {
        const x = Math.random() * (window.innerWidth - 80);
        const y = Math.random() * (window.innerHeight - 80);
        creerCible(x, y);
      }
      }
    }
  });
document.addEventListener('keydown', (event) => {
  if (event.key.toLowerCase() === 'r' && jeu ==true) {
    count = (count + 1) % 4;

    if (count === 0) currentCursor = "url('../css/curseur0.png') 0 0, auto";
    if (count === 1) currentCursor = "url('../css/curseur1.png') 0 0, auto";
    if (count === 2) currentCursor = "url('../css/curseur2.png') 0 0, auto";
    if (count === 3) currentCursor = "url('../css/curseur3.png') 0 0, auto";

    // applique le curseur au body
    document.body.style.cursor = currentCursor;
  }
});
document.addEventListener("click", (event) => {
  // Créer un pixel rouge
  if(jeu === false)return;
  let tmp = count;
  const pixel = document.createElement("div");
  pixel.className = "pixel";
  pixel.style.position = "absolute";
  pixel.style.width = "4px";
  pixel.style.height = "4px";
  pixel.style.background = "red";
  pixel.style.left = event.clientX + "px";
  pixel.style.top = event.clientY + "px";

  document.body.appendChild(pixel);

  let x = event.clientX;
  let y = event.clientY;

const speed = 2; // pixels par frame

function move() {

  if(tmp==0){
    x -= speed; // vers la gauche
    y -= speed; // vers le haut
    pixel.style.left = x + "px";
    pixel.style.top = y + "px";
  }
  if(tmp ==1){
    x += speed; // vers la droite
    y -= speed; // vers le haut
    pixel.style.left = x + "px";
    pixel.style.top = y + "px";
  }
    if(tmp ==2){
    x += speed; // vers la droite
    y += speed; // vers le bas
    pixel.style.left = x + "px";
    pixel.style.top = y + "px";
  }
   if(tmp ==3){
    x -= speed; // vers la gauche
    y += speed; // vers le bas
    pixel.style.left = x + "px";
    pixel.style.top = y + "px";      
  }
  if ((x > 0 && x<window.innerWidth) && (y < window.innerHeight && y>0)) {
    requestAnimationFrame(move);
  } else {
    pixel.remove();
     // Ajouter une image d’explosion
      const explosion = document.createElement("img");
      explosion.src = "../css/explosion.png"; // mets ici ton image d’explosion
      explosion.className = "explosion";
      explosion.style.left = x + "px";
      explosion.style.top = y + "px";
      document.body.appendChild(explosion);

      // Supprimer l’explosion après 1 seconde
      setTimeout(() => explosion.remove(), 100);
  }
}
move();

});
setInterval(checkCollisions, 20);
function checkCollisions() {
      if(jeu == false)return;
      const pixelRect = pixel.getBoundingClientRect();
      const cibles = document.querySelectorAll(".cible");

      cibles.forEach(cible => {
        const cibleRect = cible.getBoundingClientRect();

        // Test de collision rectangle
        if (
          pixelRect.left < cibleRect.right &&
          pixelRect.right > cibleRect.left &&
          pixelRect.top < cibleRect.bottom &&
          pixelRect.bottom > cibleRect.top
        ) {
          cible.remove(); // supprimer la cible si touchée
        }
        }
      )};
