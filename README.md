# Tarea 1: Señales, Sistemas y Procesamiento Digital de Señales

**Instituto Tecnológico de Costa Rica**
Escuela de Ingeniería Electrónica
Carrera de Maestría en Electrónica
Procesamiento Digital de Señales

| | |
|---|---|
| **Fecha de asignación** | 14 de septiembre de 2026 |
| **Fecha de entrega** | 20 de septiembre de 2026, antes de las 23:59 |
| **Modalidad** | Individual |
| **Autor** | Fabio Jaramillo Cordero |

## Descripción

Solución de la Tarea 1, compuesta por 5 problemas. Los Problemas 2 y 3 requieren un programa en Python (incluido en `src/`); los Problemas 1, 4 y 5 son de análisis teórico/técnico y su desarrollo completo está en el informe (`docs/informe.pdf`), sin código asociado.

1. **Muestreo y aliasing en señales musicales** — análisis teórico (sin código; ver informe).
2. **Visualización de una señal y su alias** — programa en Python (`src/problema_2.py`).
3. **Aliasing para recuperar información de una señal modulada** — programa en Python (`src/problema_3.py`).
4. **Cuantización y representación en punto fijo** — análisis teórico (sin código; ver informe).
5. **Investigación de un caso de conducción temeraria** — informe técnico (sin código; ver informe).

## Estructura del Proyecto

```
tarea1_pds/
├── README.md               # Este archivo
├── requirements.txt        # Dependencias Python
├── .gitignore              # Archivos ignorados por Git
├── src/
│   ├── problema_2.py       # Visualización de señal y alias
│   └── problema_3.py       # Aliasing para recuperar señal modulada
└── docs/
    ├── enunciado.pdf       # Enunciado de la tarea (entregado por el profesor)
    ├── informe.tex         # Fuente LaTeX del reporte (los 5 problemas)
    ├── informe.pdf         # Reporte compilado, con todas las respuestas
    └── figuras/            # Gráficas generadas por src/problema_2.py y src/problema_3.py
```

## Requisitos

- Python 3.8 o superior y pip
- Sistema operativo de software libre basado en Linux (Ubuntu, Kubuntu, Debian, Fedora, Omarchy, entre otros)
- (Opcional, solo para recompilar el informe) una distribución de TeX Live con `latexmk`

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jfabiojc/Tarea1-PDS.git
cd Tarea1-PDS
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

### Problema 2: Visualización de una señal y su alias

```bash
python src/problema_2.py
```

Solicita interactivamente:
- Frecuencia natural `F` de la señal (Hz)
- Frecuencia de muestreo `Fs` (Hz)
- Número de ciclos de la señal original a mostrar

Genera `docs/figuras/figura_problema2.png` con la señal original, su alias (si aplica) y las muestras tomadas, con el eje temporal en segundos.

### Problema 3: Aliasing para recuperar una señal modulada

```bash
python src/problema_3.py
```

No requiere parámetros de entrada: reproduce el desarrollo completo del problema (incisos a-e) con la señal modulada del enunciado, imprime los resultados numéricos en consola y genera:
- `docs/figuras/figura_problema3_d.png`: señal modulada, sus muestras, y comparación entre la información original y la recuperada.
- `docs/figuras/figura_problema3_e.png`: comparación de la recuperación para las distintas fases de la portadora.

## Construcción del informe (PDF)

El reporte (`docs/informe.pdf`) ya está compilado y versionado en el repositorio. Para reconstruirlo a partir del fuente LaTeX:

```bash
# Instalar una distribución de TeX Live con los paquetes usados
# (ejemplo en distribuciones basadas en Debian/Ubuntu):
sudo apt install texlive-latex-extra texlive-fonts-recommended latexmk

cd docs
latexmk -pdf informe.tex
```

Paquetes LaTeX utilizados: `inputenc`, `amsmath`, `amssymb`, `graphicx`, `float`, `booktabs`, `fancyhdr`, `xcolor` (incluidos en `texlive-latex-extra`).

## Dependencias de Python

Ver `requirements.txt` para la lista completa con versiones mínimas.

- **numpy** — cálculos numéricos
- **matplotlib** — generación de gráficas
- **scipy** — filtrado digital (usado en `problema_3.py`, módulo `scipy.signal`)

## Detalles de Implementación

### Problema 1: Muestreo y Aliasing en Señales Musicales
Análisis teórico. Sistema de grabación a `Fs = 8 kHz`, frecuencia de plegado 4 kHz. Incluye el cálculo de la nota más aguda grabable, el análisis de aliasing al grabar Mi♭8 en píccolo, y una investigación sobre filtros anti-aliasing. Ver `docs/informe.pdf`, Problema 1.

### Problema 2: Visualización de una Señal y su Alias
`src/problema_2.py` grafica una señal senoidal de frecuencia `F`, su alias en el rango `[-Fs/2, Fs/2]` (si aplica) y las muestras tomadas a `Fs`, con las unidades de tiempo indicadas en el eje horizontal.

### Problema 3: Aliasing para Recuperar una Señal Modulada
Señal modulada `x(t) = [1 + 0.5cos(2π·100t)]·cos(2π·1000t)` (portadora 1000 Hz, información 100 Hz). `src/problema_3.py` muestrea a `Fs = 800 Hz` (aliasing intencional) y recupera el tono de 100 Hz con un filtro pasa-bajo Butterworth de orden 8, evaluando además el efecto de una fase desconocida en la portadora.

### Problema 4: Cuantización y Representación en Punto Fijo
Análisis teórico. Sensor de `-3 V` a `+3 V` con procesador de 8 bits: cuantización uniforme, formato de punto fijo Qm.n de máxima resolución, aritmética en punto fijo (suma y multiplicación) y relación señal a ruido de cuantización para cada formato. Ver `docs/informe.pdf`, Problema 4.

### Problema 5: Investigación de un Caso de Conducción Temeraria
Informe técnico. Estimación de la velocidad de un vehículo combinando una medición de video submuestreado (cámara Garmin Dash Cam Mini 2, autopista Florencio del Castillo) con datos de geolocalización por radiogonía, incluyendo supuestos, fuentes consultadas, incertidumbre y limitaciones de la evidencia. Ver `docs/informe.pdf`, Problema 5.

## Checklist de entrega (según el enunciado)

- [x] Reporte en PDF con todas las respuestas (`docs/informe.pdf`)
- [x] Código fuente de los problemas que lo requieren (`src/`)
- [x] README con instrucciones de instalación, construcción y ejecución
- [x] Acceso al repositorio otorgado al usuario **`michaelgruner`** en GitHub/GitLab
- [x] Respaldo en ZIP/TAR del repositorio subido a TEC Digital antes del 20 de septiembre de 2026, 23:59

## Notas

- El código se probó en un sistema operativo Linux, tal como exige el enunciado.
- Los Problemas 1, 4 y 5 no requieren código: el enunciado solo pide programa en Python para los Problemas 2 y 3 (incisos explícitos "realice un programa en Python" / "compruebe su resultado en Python").
