# Tarea 1: Señales, Sistemas y Procesamiento Digital de Señales

**Instituto Tecnológico de Costa Rica**  
Escuela de Ingeniería Electrónica  
Carrera de Maestría en Electrónica  
Procesamiento Digital de Señales

## Descripción

Solución de la Tarea 1 que incluye:

1. **Muestreo y aliasing en señales musicales** - Análisis de sistemas de grabación de audio
2. **Visualización de una señal y su alias** - Programa Python para graficar señales
3. **Aliasing para recuperar información de una señal modulada** - Técnicas de demodulación
4. **Cuantización y representación en punto fijo** - Análisis de cuantización de señales
5. **Investigación de un caso de conducción temeraria** - Análisis forense de video

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes)
- Sistema operativo Linux (Ubuntu, Debian, Fedora, etc.)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tarea1-pds.git
cd tarea1-pds
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
tarea1_pds/
├── README.md               # Este archivo
├── requirements.txt        # Dependencias Python
├── .gitignore               # Archivos ignorados por Git
├── src/
│   ├── problema_2.py       # Visualización de señal y alias
│   ├── problema_3.py       # Aliasing para señal modulada
│   ├── problema_4.py       # Cuantización y punto fijo
│   ├── problema_5.py       # Caso de conducción temeraria
│   └── utils.py            # Funciones auxiliares
└── docs/
    ├── enunciado.pdf       # Enunciado de la tarea (entregado por el profesor)
    ├── informe.tex         # Fuente LaTeX del reporte
    ├── informe.pdf         # Reporte con respuestas teóricas (compilado)
    └── figuras/            # Gráficas generadas por los scripts (ej. figura_problema2.png)
```


## Ejecución

### Problema 2: Visualización de señal y alias

```bash
python src/problema_2.py
```

Parámetros de entrada:
- Frecuencia natural F (Hz)
- Frecuencia de muestreo Fs (Hz)
- Número de ciclos a mostrar

### Problema 3: Aliasing para señal modulada

```bash
python src/problema_3.py
```

### Problema 4: Cuantización y punto fijo

```bash
python src/problema_4.py
```

### Problema 5: Conducción temeraria

```bash
python src/problema_5.py
```

## Detalles de Implementación

### Problema 1: Muestreo y Aliasing en Señales Musicales

- Frecuencia de muestreo: 8 kHz
- Rango de frecuencias: 0 Hz a 4 kHz (Nyquist)
- Análisis de notas musicales y aliasing

### Problema 2: Visualización

Se grafican simultáneamente:
- Señal original
- Señal alias (si aplica)
- Muestras capturadas
- Rango de frecuencias: -Fs/2 a Fs/2

### Problema 3: Demodulación

- Señal modulada: x(t) = [1 + 0.5cos(2π100t)] cos(2π1000t)
- Portadora: 1000 Hz
- Información: 100 Hz
- Técnica: Aprovechamiento de aliasing controlado

### Problema 4: Cuantización

- Rango de entrada: -3V a +3V
- Procesador: 8 bits
- Formato de punto fijo: Qm.n

### Problema 5: Análisis Forense

- Video: Garmin Dash Cam Mini 2
- Carretera: Autopista Florencio del Castillo
- Análisis: Velocidad del vehículo a partir de geolocalización

## Dependencias

Ver `requirements.txt` para la lista completa de librerías Python.

Principales:
- **numpy** - Cálculos numéricos
- **matplotlib** - Visualización de gráficos
- **scipy** - Procesamiento de señales

## Autor

[Tu nombre aquí]

## Fecha de Entrega

20 de septiembre de 2026

## Notas

- El código debe ejecutarse en un sistema operativo Linux
- Todos los scripts incluyen documentación y comentarios
- Se incluye un informe PDF con las respuestas teóricas detalladas