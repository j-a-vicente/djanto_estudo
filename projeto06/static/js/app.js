// app.js

function toggleTheme() {
    // Seleciona os elementos navbar e sidenav
    var navbar = document.querySelector('.navbar');
    var sidenav = document.querySelector('.sb-sidenav');

    // Alterna entre os temas
    if (navbar.classList.contains('navbar-dark')) {
        // Se o tema for dark, muda para light
        navbar.classList.remove('navbar-dark', 'bg-dark');
        navbar.classList.add('navbar-light', 'bg-light');
        sidenav.classList.remove('sb-sidenav-dark');
        sidenav.classList.add('sb-sidenav-light');
        // Muda o ícone para a lua
        document.getElementById('theme-icon').classList.remove('fa-sun');
        document.getElementById('theme-icon').classList.add('fa-moon');
    } else {
        // Se o tema for light, muda para dark
        navbar.classList.remove('navbar-light', 'bg-light');
        navbar.classList.add('navbar-dark', 'bg-dark');
        sidenav.classList.remove('sb-sidenav-light');
        sidenav.classList.add('sb-sidenav-dark');
        // Muda o ícone para o sol
        document.getElementById('theme-icon').classList.remove('fa-moon');
        document.getElementById('theme-icon').classList.add('fa-sun');
    }
}


// ServerHost
document.addEventListener("DOMContentLoaded", function() {
    var serverHostsLink = document.getElementById("serverHostsLink");
    if (serverHostsLink) {
        serverHostsLink.addEventListener("click", function(event) {
            event.preventDefault();
            $.get(serverHostUrl, function(data) {
                $('#apresentacao-container').html(data);
            });
        });
    }
});


