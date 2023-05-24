
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

const classes = [
    {
        number: 1,
        title: 'Fundamentos de Física',
        description: 'Referente a fundamentos de física, unidade curricular do 1º ano, 1º semestre.',
        instructor: 'Não ',
        date: 'January 1, 2023'
    },
    {
        number: 2,
        title: 'Fundamentos de Programação',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Pedro Alves',
        date: 'January 8, 2023'
    },
    {
        number: 3,
        title: 'Matemática Discreta',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Jane Smith',
        date: 'January 8, 2023'
    },
    {
        number: 5,
        title: 'Matemática I',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Jane Smith',
        date: 'January 8, 2023'
    },
    {
        number: 6,
        title: 'Sistemas Digitais',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Jane Smith',
        date: 'January 8, 2023'
    },
    {
        number: 7,
        title: 'Algoritmos e Estruturas de Dados',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Jane Smith',
        date: 'January 8, 2023'
    },
    {
        number: 8,
        title: 'Arquitetura de Computadores',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Jane Smith',
        date: 'January 8, 2023'
    },
    {
        number: 9,
        title: 'Competências Comportamentais',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Diogo Morgado',
        date: 'January 8, 2023'
    },
    {
        number: 10,
        title: 'Linguagens de Programação I',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Pedro Serra',
        date: 'January 8, 2023'
    },
    {
        number: 11,
        title: 'Matemática II',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Alexander Mikovic',
        date: 'January 8, 2023'
    },
    {
        number: 12,
        title: 'Álgebra Linear',
        description: 'In this class, you will learn the basics of CSS and how to style your web pages.',
        instructor: 'Jane Smith',
        ects: 6,
        anoLetivo: 2020,
        anoCurricular: 1,
        ranking: 5,
        semestre: '1ºSemestre',

    },

    // Add more classes here as needed
];

// Loop through the classes array and create a button for each class
classes.forEach((classInfo) => {
    const button = document.createElement('button');
    button.textContent = `Unidade Curricular ${classInfo.number}: ${classInfo.title}`;
    // When the button is clicked, display the details for the corresponding class
    button.addEventListener('click', () => {
        displayClassDetails(classInfo);
    });
    classButtonsContainer.appendChild(button);
});

// Function to display the details for a given class
function displayClassDetails(classInfo) {
    classDetailsContainer.innerHTML = `
        <p><strong>Cadeira:</strong> ${classInfo.number}</p>
        <p><strong>Nome da Cadeira:</strong> ${classInfo.title}</p>
        <p><strong>Descrição:</strong> ${classInfo.description}</p>
        <p><strong>Docentes:</strong> ${classInfo.instructor}</p>
        <p><strong>ECTS:</strong> ${classInfo.ects}</p>
        <p><strong>Ano Letivo:</strong> ${classInfo.anoLetivo}</p>
        <p><strong>Ano Letivo:</strong> ${classInfo.anoCurricular}</p>
        
    `;
    // Show the class details section
    document.querySelector('.class-details').style.display = 'block';
}
courseList.addEventListener('click', function (e) {
    if (e.target.tagName === 'H3') {
        const details = e.target.nextElementSibling;
        if (details.style.display === 'block') {
            details.style.display = 'none';
        } else {
            courseDetails.forEach(function (detail) {
                detail.style.display = 'none';
            });
            details.style.display = 'block';
        }
    }
});