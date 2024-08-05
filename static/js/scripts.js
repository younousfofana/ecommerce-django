const element = document.getElementById('productImage');
// Animation d'apparition
setTimeout(() => {
    element.classList.add('visible');
}, 100);  // Attendez un peu pour que le navigateur ait le temps de rendre la page avant de démarrer l'animation

// Animation de clic
element.addEventListener('click', (e) => {
    element.style.transition = 'transform 0.3s ease';
    element.style.transform = 'scale(0.8)';
    element.style.zIndex = '10';
});

// Animation de sortie de la souris
element.addEventListener('mouseleave', (e) => {
    element.style.transition = 'transform 0.3s ease';
    element.style.transform = 'scale(1)';
    element.style.zIndex = 'auto';
});

const cardButton = document.getElementById('cardButton');
const orderButton = document.getElementById('orderButton');

setTimeout(()=>{
    cardButton.classList.add('grow-from-bottom');
    orderButton.classList.add('grow-from-top');
}, 100);

const subProductName = document.getElementById('subProductName');

setTimeout(()=>{
    subProductName.classList.add('slide-from-right');
}, 100)

const description = document.getElementById('description');

setTimeout(()=>{
    description.classList.add('slide-from-bottom');
}, 100);

const subDescription1 = document.getElementById('subDescription1');
const subDescription2 = document.getElementById('subDescription2');

setTimeout(()=>{
    subDescription1.classList.add('slide-from-bottom');
}, 200);

setTimeout(()=>{
    subDescription2.classList.add('slide-from-bottom');  
}, 300)

const card = document.getElementById('card');
setTimeout(()=>{
    card.classList.add('slide-card-from-bottom');
}, 100);

const videoDescription = document.getElementById('videoDescription');
setTimeout(()=>{
    videoDescription.classList.add('slide-card-from-bottom');
}, 100);

const subtitleProduct = document.getElementById('subtitleProduct');
setTimeout(()=>{
    subtitleProduct.classList.add('slide-from-top');
},100);