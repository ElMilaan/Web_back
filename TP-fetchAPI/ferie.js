const btn = document.querySelector(".btn");
const container = document.querySelector(".container");
const menu = document.querySelector("#menu");
const CURRENT_YEAR = 2024;
let five_next_years = [];
let ul = document.createElement("ul");

/*************** FUNCTIONS *****************/

async function listFeries(year) {
    try {
        const response = await fetch(
            `https://calendrier.api.gouv.fr/jours-feries/metropole/${year}.json`
        );
        if (!response.ok) {
            throw new Error("Erreur lors de la récupération des données");
        }
        const data = await response.json();
        for (let e in data) {
            insertLi(`${e} -- ${data[e]}`);
        }
    } catch (error) {
        insertLi("Une erreur est survenue:", error.message);
    }
}

function insertLi(str) {
    let li = document.createElement("li");
    li.textContent = str;
    ul.appendChild(li);
}

function fiveNextYears() {
    for (let i = 0; i <= 5; i++) {
        five_next_years.push(CURRENT_YEAR + i);
    }
}

function createMenu() {
    for (let e in five_next_years) {
        let newOption = document.createElement("option");
        newOption.value = five_next_years[e];
        newOption.text = five_next_years[e];
        menu.appendChild(newOption);
    }
}

function verifyOption() {
    while (ul.firstChild) {
        ul.removeChild(ul.firstChild);
    }
    listFeries(menu.value);
}

/**************** PROGRAM *****************/

fiveNextYears();
createMenu();

listFeries(CURRENT_YEAR);
container.appendChild(ul);
