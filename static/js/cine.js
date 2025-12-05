/************   ESTRUCTURAS DE DATOS   ************/
function crearAsientos() {
    const seats = [];
    for (let i = 1; i <= 16; i++) {
        
        seats.push({
            num: i.toString(),
            status: "disponible", // "disponible" | "ocupado"
            nombre: null,
            iteracion: 0
        });
    }

    return seats;

}


const movies = [
    { id: 1, letra:"A", title: "El Teléfono Negro 2", time: "2:00 PM", price: 80, posterCentral: posterCentralTelneg ,imagen: posterTelneg, seats: crearAsientos() },
    { id: 2, letra:"B", title: "PAW PATROL: ESPECIAL DE NAVIDAD", time: "5:00 PM", posterCentral: posterCentralPawpatrol, price: 75, seats: crearAsientos(), imagen: posterPawpatrol},
    { id: 3, letra:"C", title: "A pesar de ti", time: "8:00 PM", price: 70, seats: crearAsientos(), posterCentral: posterCentralApesardeti, imagen: posterApesardeti }
];

let currentMovie = movies[0];   // película seleccionada
let selectedSeat = null;        // asiento seleccionado en la película actual

/************   PELÍCULAS (panel izquierdo)   ************/
const movieList = document.getElementById("movieList");

let counter = 0;
function renderMovies() {
    movieList.innerHTML = "";
    movies.forEach(movie => {
        const item = document.createElement("div");
        item.classList.add("movie-item");
        if (movie.id === currentMovie.id) item.classList.add("active");

        item.addEventListener("click", () => {
            currentMovie = movie;         // cambiamos de película
            selectedSeat = null;          // limpiamos selección
            document.getElementById("asiento").value = "";
            document.getElementById("precio").value = movie.price;
            renderMovies();
            updateCenterMovie();
            renderSeats();                // ahora mostramos los asientos de ESTA película
            
        });

        
        let posterCentral = document.getElementById("central-poster");
        posterCentral.setAttribute('src', movies[currentMovie.id-1].posterCentral)
        

        const poster = document.createElement("img");
        poster.classList.add("movie-posterr");
        poster.setAttribute("src", movies[counter].imagen)
        counter += 1;
        if (counter == movies.length){
            counter = 0;
        }


        const info = document.createElement("div");
        info.classList.add("movie-info");

        const title = document.createElement("div");
        title.classList.add("movie-title");
        title.textContent = "- " + movie.title;

        const time = document.createElement("div");
        time.classList.add("movie-time");
        time.textContent = movie.time;

        info.appendChild(title);
        info.appendChild(time);
        item.appendChild(poster);
        item.appendChild(info);
        movieList.appendChild(item);
    });
}

function updateCenterMovie() {
    document.getElementById("movieTitleCenter").textContent = currentMovie.title;
    document.getElementById("movieTimeCenter").textContent =
        currentMovie.time.toLowerCase();
}

/************   ASIENTOS (panel central)   ************/
const seatsGrid = document.getElementById("seatsGrid");

function renderSeats() {
    seatsGrid.innerHTML = "";
    const seats = currentMovie.seats;  // asientos de la película actual

    seats.forEach(seat => {
        const div = document.createElement("div");
        div.classList.add("seat");
        //seat.num += currentMovie.letra;

        if (seat.iteracion != 1){
        seat.num = seat.num + currentMovie.letra;
        seat.iteracion++;
        }
        div.textContent = seat.num;

        if (seat.status === "ocupado") {
            div.classList.add("ocupado");
        } else if (selectedSeat && selectedSeat.num === seat.num) {
            div.classList.add("seleccionado");
        } else {
            div.classList.add("disponible");
        }

        div.addEventListener("click", () => onSeatClick(seat));
        seatsGrid.appendChild(div);
    });
}

function onSeatClick(seat) {
    if (seat.status === "ocupado") {
        alert("Este asiento ya está ocupado para esta función.");
        return;
    }

    selectedSeat = seat;
    document.getElementById("asiento").value = seat.num;

    const nombre = document.getElementById("nombre").value || "Sin nombre";

    const alerta = document.getElementById("alerta");
    alerta.innerHTML = `
        <div class="alerta-title">Datos del asiento</div>
        Nombre: ${nombre}<br>
        Asiento: ${seat.num}<br>
        Película: ${currentMovie.title}<br>
        Horario: ${currentMovie.time}
    `;

    alert(
        `Nombre: ${nombre}\nAsiento: ${seat.num}\nPelícula: ${currentMovie.title}\nHorario: ${currentMovie.time}`
    );

    renderSeats();
}

/************   BOTÓN GUARDAR   ************/
document.getElementById("btnGuardar").addEventListener("click", () => {
    if (!selectedSeat) {
        alert("Primero selecciona un asiento.");
        return;
    }

    

    const nombre = document.getElementById("nombre").value.trim();
    if (!nombre) {
        alert("Ingresa un nombre para completar la reserva.");
        return;
    }

    const email = document.getElementById("email").value.trim();
    if (!email) {
        alert("Ingresa un email para completar la reserva.");
        return;
    }

    // marcamos ocupado SOLO en la película actual
    selectedSeat.status = "ocupado";
    selectedSeat.nombre = nombre;
    const pelicula = currentMovie.title;

    alert(`Reserva guardada:\n${nombre} - Asiento ${selectedSeat.num}\nPelícula: ${currentMovie.title}`);
    const numeroAsiento = selectedSeat.num
    selectedSeat = null;

    

    fetch("/save_cliente", {
        method : "POST",
        headers : {"Content-Type" :  "application/json"},
        body: JSON.stringify({
            nombre: nombre,
            email: email,
            asiento: numeroAsiento,
            pelicula: pelicula
        })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject();
        }
    })
    .then(result => {
        if (result.success) {
            alert("El registro se guardo de manera correcta")
        } else{
            alert("El registro no se pudo guardar correctamnte")
        }
    })
    .catch(error => {
        console.error("Error: ", error)
    })



    //TODO agregar boton de eliminar

    document.getElementById("asiento").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("email").value = "";
    renderSeats();
});

/************   INICIALIZAR INTERFAZ   ************/
renderMovies();
updateCenterMovie();
document.getElementById("precio").value = currentMovie.price;
renderSeats();