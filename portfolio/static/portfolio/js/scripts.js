
/* Diferentes Disiplinas */

const timeElement = document.querySelector(".time");
const dateElement = document.querySelector(".date");
const body = document.querySelector('body');

const butaoDarkMode = document.getElementById('butaoDarkMode');
butaoDarkMode.onclick = function () {
    butaoDarkMode.classList.toggle('active');
    body.classList.toggle('active');



}


/**
 * 
 * @param {Date} date 
 */
function formatTime(date) {

    const hours12 = date.getHours() % 12 || 12;
    const minutes = date.getMinutes();
    const isAm = date.getHours() < 12;

    return `${hours12.toString().padStart(2, "0")}:${minutes
        .toString()
        .padStart(2, "0")} ${isAm ? "AM" : "PM"}`;
}

function formatDate(date) {
    const DIAS = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabádo"];
    const MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

    return `${DIAS[date.getDay()]}, ${MESES[date.getMonth()]
        } ${date.getDate()} ${date.getFullYear()}`;
}

setInterval(() => {
    const now = new Date();
    timeElement.innerHTML = formatTime(now);
    dateElement.innerHTML = formatDate(now);
}, 200);