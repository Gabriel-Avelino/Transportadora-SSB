const container = document.querySelector('.galery-wrapper'); // Selecione o contêiner do carrossel

let currentItem = 0;
const items = document.querySelectorAll('.item');

const maxItems = items.length;

function scrollToItem(index) {
    const item = items[index];
    const containerRect = container.getBoundingClientRect();
    const itemRect = item.getBoundingClientRect();
    
    const offsetLeft = itemRect.left - containerRect.left + container.scrollLeft - (containerRect.width / 2) + (itemRect.width / 2);
    
    container.scrollTo({
        left: offsetLeft,
        behavior: 'smooth'
    });
}


function carrossel(){
    currentItem++;

    if (currentItem >= maxItems) {
        currentItem = 0;
    } else if (currentItem < 0) {
        currentItem = maxItems - 1;
    }

    items.forEach(item => item.classList.remove('current-item'));

    scrollToItem(currentItem);

    items[currentItem].classList.add('current-item');
}

intervalId = setInterval(carrossel, 4800);