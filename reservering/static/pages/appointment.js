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
    singleChoice.onclick = function (event) {
        const finalGenderChoise = event.target.id;
        window.localStorage.setItem("genderChoice", finalGenderChoise);
    };
    console.log(singleChoice);
}

const treatmentoptionchoices = document.querySelectorAll(".nav");


for (let i = 0; i < treatmentoptionchoices.length; i++) {
    const singleChoice = treatmentoptionchoices[i];
    singleChoice.onclick = function (event) {
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
    singleChoice.onclick = function (event) {
        const finalStylistChoise = event.target.id;
        window.localStorage.setItem("stylistChoice", finalStylistChoise);
    };
    console.log(singleChoice);
}

function dateselector() {
    var date = document.getElementById("dateform").getElementsByTagName("input")[0];
    getTimeslotAPI();
    console.log(date.value);
}

    function getTimeslotAPI() {
        fetch('/api/timeslot/', {
            method: 'GET',
            headers: {'Accept': 'application/json', 'Content-Type': 'application/json'}
        })
            .then((response) => {
                return response.json();
            })
            .then((result) => {
                    document.getElementById('timeslot').innerHTML = '';

                    if (!result['success']) {
                        for (var i = 0; i < result.length; i++) {
                            if (result[i].available === true) {
                                if (result[i].date === document.getElementById('id_my_date_field').value) {
                                    window.localStorage.setItem("date_id", result[i].date_id )
                                    document.getElementById('timeslot').innerHTML += '<a onclick="test(this)">' + result[i].time + '</a><br/>';
                                }
                            }
                        }
                    } else {
                        return null;
                    }
                }
            );
    }


    function test(tijd) {
        console.log(tijd.innerText);

    }

    function maak_afspraak() {

        // api call 1 (customer call)
        fetch('http://127.0.0.1:8000/api/customer/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                "firstname": document.getElementById("id_firstname").value,
                "lastname": document.getElementById("id_lastname").value,
                "phone": document.getElementById("id_phone").value,
                "e_mail": document.getElementById("id_e_mail").value,
            })
        })
            .then((response) => {
                return response.json();
            })
            .then((result) => {
                if (!result['success']) {
                    console.log(result);
                    fetch('http://127.0.0.1:8000/api/appointment/', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            "customer_id": parseInt(result.customer_id),
                            "stylist_id": parseInt(localStorage.getItem("stylistChoice")),
                            "date_id": parseInt(localStorage.getItem("date_id")),
                        })
                    })
                        .then((response) => {
                            return response.json();
                        })
                        .then((result) => {
                            if (!result['success']) {
                                console.log(result);

                            } else {
                                return null;
                            }
                        });

                } else {
                    return null;
                }
            });

        // api call 2 (appointment call)

    }
