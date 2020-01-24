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

const treatmentoptionchoices = document.querySelectorAll(".nav");


for (let i = 0; i < treatmentoptionchoices.length; i++) {
    const singleChoice = treatmentoptionchoices[i];
    singleChoice.onclick = function(event) {
        const finalTreatmentoptionChoise = event.target.id;
        window.localStorage.setItem("treatmentoptionChoice", finalTreatmentoptionChoise);
    };
    console.log(singleChoice);
}

// const treatmentoptionschoices = document.querySelectorAll(".sub-nav");
//
// for (let i = 0; i < treatmentoptionschoices.length; i++) {
//     const singleChoice = treatmentoptionschoices[i].querySelectorAll("li");
//     for (let y = 0; y < singleChoice.length; y++) {
//         const singleOption = singleChoice[y];
//         console.log(singleOption);
//         singleOption.onclick = function (event) {
//             const finalTreatmentOptionChoise = event.target.id;
//             window.localStorage.setItem("treatmentoptionChoice", finalTreatmentOptionChoise);
//         };
//         console.log(singleChoice);
//     }
// }



const stylistchoices = document.querySelectorAll(".card.stylist");

for (let i = 0; i < stylistchoices.length; i++) {
    const singleChoice = stylistchoices[i];
    singleChoice.onclick = function(event) {
        const finalStylistChoise = event.target.id;
        window.localStorage.setItem("stylistChoice", finalStylistChoise);
    };
    console.log(singleChoice);
}
function dateselector() {
    var date = document.getElementById("dateform").getElementsByTagName("input")[0];
    console.log(date.value);
}
