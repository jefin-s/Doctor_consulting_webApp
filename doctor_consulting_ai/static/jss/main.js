// hero swiper slider

const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
     speed:3000,
    effect:'cube',
    // slidesperview:2,  
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  autoplay:{
        delay:3000,
    },
  });

  //mobile menu 
  let mobileMenuicon = document.querySelector('header .fa-bars')
  let menuItem=document.querySelector('header .menu ')
  mobileMenuicon.addEventListener('click',function(){
    menuItem.classList.toggle  ('open');  
    
  });