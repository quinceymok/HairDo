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

const genderChoises = document.querySelectorAll(".card.choice");

for (let i = 0; i < genderChoises.length; i++) {
    const singleChoice = genderChoises[i];
    singleChoice.onclick = function(event) {
        const finalGenderChoise = event.target.id;
        window.localStorage.setItem("genderChoice", finalGenderChoise);
    };
    console.log(singleChoice);
}

const treatmentchoices = document.querySelectorAll(".card.treatment");


for (let i = 0; i < treatmentchoices.length; i++) {
    const singleChoice = treatmentchoices[i];
    singleChoice.onclick = function(event) {
        const finalTreatmentChoise = event.target.id;
        window.localStorage.setItem("treatmentChoice", finalTreatmentChoise);
    };
    console.log(singleChoice);
}


const stylistchoices = document.querySelectorAll(".card.stylist");

for (let i = 0; i < stylistchoices.length; i++) {
    const singleChoice = stylistchoices[i];
    singleChoice.onclick = function(event) {
        const finalStylistChoise = event.target.id;
        window.localStorage.setItem("stylistChoice", finalStylistChoise);
    };
    console.log(singleChoice);
}
