// $(document).ready(function(){
//     // au clic sur un lien
//     $('a[href^="#"]').click(function(evt){
//        // bloquer le comportement par défaut: on ne rechargera pas la page
//        evt.preventDefault(); 
//        // enregistre la valeur de l'attribut  href dans la variable target
//  var target = $(this).attr('href');
//        /* le sélecteur $(html, body) permet de corriger un bug sur chrome 
//        et safari (webkit) */
//  $('html, body')
//        // on arrête toutes les animations en cours 
//        .stop()
//        /* on fait maintenant l'animation vers le haut (scrollTop) vers 
//         notre ancre target */
//        .animate({scrollTop: $(target).offset().top}, 1050 );
//     });
// });



// SideNav Button Initialization
// $(".button-collapse").sideNav();
 
// var sideNavScrollbar = document.querySelector('.custom-scrollbar');
// Ps.initialize(sideNavScrollbar);