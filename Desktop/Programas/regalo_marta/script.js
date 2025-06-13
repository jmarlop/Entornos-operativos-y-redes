// Crear el objeto QR una vez y reutilizarlo
const qr = new QRious({
    element: document.getElementById('qr'),
    size: 200,
  });
  
  function generarQR() {
    let texto = document.getElementById('qrInput').value.trim();
  
    // Si parece una URL pero no tiene protocolo, se añade https://
    if (texto && !/^https?:\/\//i.test(texto) && texto.includes('.')) {
      texto = 'http://127.0.0.1:5500/index.html' + texto;
    }
  
    qr.value = texto;
  }
  
  // Población de selectores de mes y año
  window.onload = function () {
    const mesSelect = document.getElementById('mes');
    const anioSelect = document.getElementById('anio');
  
    const meses = [
      'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ];
  
    meses.forEach((mes, i) => {
      const option = document.createElement('option');
      option.value = i;
      option.textContent = mes;
      mesSelect.appendChild(option);
    });
  
    const anioActual = new Date().getFullYear();
    for (let i = anioActual - 10; i <= anioActual + 10; i++) {
      const option = document.createElement('option');
      option.value = i;
      option.textContent = i;
      anioSelect.appendChild(option);
    }
  };
  
  // Función para generar calendario
  function generarCalendario() {
    const mes = parseInt(document.getElementById('mes').value);
    const anio = parseInt(document.getElementById('anio').value);
    const calendario = document.getElementById('calendar');
  
    calendario.innerHTML = '';
  
    const fecha = new Date(anio, mes, 1);
    const primerDia = fecha.getDay();
    const diasMes = new Date(anio, mes + 1, 0).getDate();
  
    const tabla = document.createElement('table');
    const diasSemana = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
    const header = tabla.insertRow();
    diasSemana.forEach(dia => {
      const th = document.createElement('th');
      th.textContent = dia;
      header.appendChild(th);
    });
  
    let fila = tabla.insertRow();
    for (let i = 0; i < primerDia; i++) {
      fila.insertCell();
    }
  
    for (let dia = 1; dia <= diasMes; dia++) {
      if (fila.cells.length === 7) {
        fila = tabla.insertRow();
      }
      const celda = fila.insertCell();
      celda.textContent = dia;
    }
  
    calendario.appendChild(tabla);
  }
  