const navbarToggler = document.querySelector(".navbar-toggler");
const navbarMenu = document.querySelector(".navbar ul");
const navbarLinks = document.querySelectorAll(".navbar a");

navbarToggler.addEventListener("click", navbarTogglerClick);

function navbarTogglerClick() {
    navbarToggler.classList.toggle("open-navbar-toggler");
    navbarMenu.classList.toggle("open");
}

navbarLinks.forEach(elem => elem.addEventListener("click", navbarLinkClick));

function navbarLinkClick() {
    if (navbarMenu.classList.contains("open")) {
        navbarToggler.click();
    }
}

const genderChoises = document.querySelectorAll("#gender-choices .choice");
console.log(genderChoises);

for (let i = 0; i < genderChoises.length; i++) {
    const singleChoice = genderChoises[i];
    singleChoice.onclick = function(event) {
        const finalGenderChoise = event.target.id;
        window.localStorage.setItem("genderChoice", finalGenderChoise);
    };
    console.log(singleChoice);
}
