const element = document.getElementById('productImage');
if(element){
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
}

const cardButton = document.getElementById('cardButton');
const orderButton = document.getElementById('orderButton');
if(cardButton && orderButton){
    setTimeout(()=>{
        cardButton.classList.add('grow-from-bottom');
        orderButton.classList.add('grow-from-top');
    }, 500);
}

const subProductName = document.getElementById('subProductName');
if(subProductName){
    setTimeout(()=>{
        subProductName.classList.add('slide-from-right');
    }, 100)
}

const description = document.getElementById('description');
if(description){
    setTimeout(()=>{
        description.classList.add('slide-from-bottom');
    }, 100);
}

const subDescription1 = document.getElementById('subDescription1');
const subDescription2 = document.getElementById('subDescription2');
if(subDescription1){
    setTimeout(()=>{
        subDescription1.classList.add('slide-from-bottom');
    }, 200);
}

if(subDescription2){
    setTimeout(()=>{
        subDescription2.classList.add('slide-from-bottom');  
    }, 300)
}

const card = document.getElementById('card');
if(card){
    setTimeout(()=>{
        card.classList.add('slide-card-from-bottom');
    }, 100);
}

const videoDescription = document.getElementById('videoDescription');
if(videoDescription){
    setTimeout(()=>{
        videoDescription.classList.add('slide-card-from-bottom');
    }, 100);
}

const subtitleProduct = document.getElementById('subtitleProduct');
if(subtitleProduct){
    setTimeout(()=>{
        subtitleProduct.classList.add('slide-from-top');
    },100);
}

const priceCard = document.getElementById('priceCard');
if(priceCard){
    setTimeout(()=>{
        priceCard.classList.add('disappear-to-apparear');
    }, 100);
}

const orderDetails = document.getElementById('orderDetails');
const soldBy = document.getElementById('soldBy');
if(orderDetails && soldBy){
    setTimeout(()=>{
        orderDetails.classList.add('slide-from-left');
        soldBy.classList.add('slide-from-left');
    }, 100)
}

document.addEventListener('DOMContentLoaded', function(){
    const categoryTitle = document.getElementById('categoryTitle');
    console.log('categoryTitle', categoryTitle);
    
    if (categoryTitle) {
        const text = categoryTitle.textContent;
        console.log("texte a afficher",text);
        categoryTitle.textContent = '';

        // Créez les <span> pour chaque lettre et les ajoutez à l'élément
        for(let i = 0; i < text.length; i++){
            const span = document.createElement('span');
            span.textContent = text[i];
            span.classList.add('hidden');
            categoryTitle.appendChild(span);
        }

        // Sélectionnez les spans créés et appliquez l'animation
        const spans = categoryTitle.querySelectorAll('span');
        spans.forEach((span, index)=>{
            setTimeout(() => {
                span.classList.remove('hidden');
                span.classList.add('visible');
            }, index * 100); // Modifiez cette valeur pour changer la vitesse
        });
    }
});
