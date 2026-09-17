# Tarea 1: Señales, Sistemas y Procesamiento Digital de Señales

**Institución**: Instituto Tecnológico de Costa Rica  
**Escuela**: Ingeniería Electrónica  
**Carrera**: Maestría en Electrónica  
**Curso**: Procesamiento Digital de Señales  
**Fecha de Asignación**: 14 de septiembre de 2026  
**Fecha de Entrega**: 20 de septiembre de 2026  

---

## 📋 Descripción General

Esta tarea aborda conceptos fundamentales del procesamiento digital de señales, incluyendo muestreo, aliasing, cuantización y aplicaciones prácticas. Los problemas incluyen:

1. **Muestreo y aliasing en señales musicales** - Análisis del teorema de Nyquist aplicado a instrumentos musicales
2. **Visualización de una señal y su alias** - Programa interactivo en Python para visualizar fenómenos de aliasing
3. **Aliasing para recuperar información de una señal modulada** - Técnicas de submuestreo intencional
4. **Cuantización y representación en punto fijo** - Análisis de formatos numéricos Qm.n
5. **Investigación de un caso de conducción temeraria** - Aplicación práctica de procesamiento digital en análisis forense

---

## 🚀 Requisitos Previos

### Software Requerido
- **Python** 3.8 o superior
- **Sistema Operativo**: Linux (Ubuntu, Debian, Fedora, Kubuntu, Omarchy u otro basado en Linux)
- **Git** (para clonar y gestionar el repositorio)

### Dependencias Python
- `numpy` - Computación numérica
- `matplotlib` - Visualización de gráficos
- `scipy` - Procesamiento científico
- `ipython` - Consola interactiva (opcional)

---

## 📦 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/[tu_usuario]/tarea1-procesamiento-digital.git
cd tarea1-procesamiento-digital
```

### 2. Crear un Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # En Linux/Mac
# O en Windows:
# venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Alternativamente, instala manualmente:

```bash
pip install numpy matplotlib scipy ipython
```

### 4. Verificar Instalación

```bash
python -c "import numpy, matplotlib, scipy; print('✓ Dependencias instaladas correctamente')"
```

---

## 📁 Estructura del Proyecto

```
tarea1-procesamiento-digital/
│
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos ignorados por git
│
├── informe/
│   └── tarea1_informe.pdf       # Informe técnico completo
│
├── src/
│   ├── __init__.py
│   ├── problema1.py             # Muestreo y aliasing en señales musicales
│   ├── problema2.py             # Visualización de señales y alias
│   ├── problema3.py             # Aliasing en señales moduladas
│   ├── problema4.py             # Cuantización y punto fijo
│   ├── problema5.py             # Análisis de caso forense
│   └── utils.py                 # Funciones auxiliares
│
├── notebooks/                   # (Opcional) Jupyter notebooks
│   └── analisis_problemas.ipynb
│
├── resultados/                  # Gráficos y datos generados
│   ├── problema2_grafico.png
│   ├── problema3_grafico.png
│   └── datos_recuperados.csv
│
└── tests/                       # (Opcional) Pruebas unitarias
    └── test_funciones.py
```

---

## 🔧 Uso y Ejecución

### Ejecutar Problema Específico

Cada problema se puede ejecutar de forma independiente:

```bash
# Problema 1: Preguntas teóricas sobre muestreo en audio
python src/problema1.py

# Problema 2: Visualización interactiva de señales
python src/problema2.py --frecuencia 5/7 --fs 1 --ciclos 8

# Problema 3: Recuperación de señal modulada
python src/problema3.py

# Problema 4: Cuantización y punto fijo
python src/problema4.py

# Problema 5: Análisis forense
python src/problema5.py
```

### Parámetros de Línea de Comandos (Problema 2)

El programa de visualización acepta parámetros:

```bash
python src/problema2.py \
    --frecuencia 440 \      # Frecuencia de la señal (Hz)
    --fs 1000 \             # Frecuencia de muestreo (Hz)
    --ciclos 5              # Número de ciclos a mostrar
```

### Ejecutar Todos los Programas

```bash
python src/main.py
```

---

## 📊 Descripción de Módulos

### `problema1.py`
- Cálculo de frecuencias de notas musicales usando la fórmula de temperamento igual
- Determinación de la nota más alta grabable con fs = 8 kHz
- Análisis del aliasing en notas de pícolo
- **Salida**: Cálculos impresos en consola

### `problema2.py`
- Generación interactiva de gráficos de señales sinusoidales
- Visualización de señal original, alias y muestras
- Parámetros configurables por usuario
- **Salida**: Gráfico guardado en `resultados/problema2_grafico.png`

### `problema3.py`
- Descomposición de señal modulada AM en componentes
- Selección óptima de frecuencia de muestreo
- Recuperación de tono de información mediante aliasing
- Análisis con fase desconocida de portadora
- **Salida**: Gráficos comparativos y valores numéricos

### `problema4.py`
- Análisis de cuantización uniforme
- Formato de punto fijo Qm.n
- Operaciones aritméticas en punto fijo
- Cálculo de SNR de cuantización
- **Salida**: Tablas de análisis y valores de SNR

### `problema5.py`
- Análisis de velocidad a partir de video recuperado
- Triangulación con datos de localización celular
- Estimación de velocidad con incertidumbre
- **Salida**: Informe técnico con conclusiones

### `utils.py`
- Funciones auxiliares reutilizables:
  - Cálculo de frecuencias musicales
  - Generación de señales sinusoidales
  - Cálculo de alias
  - Operaciones de punto fijo
  - Visualización común

---

## 📚 Dependencias Explicadas

| Paquete | Versión Mínima | Uso |
|---------|-----------------|-----|
| numpy | 1.21.0 | Operaciones numéricas y arrays |
| matplotlib | 3.4.0 | Generación de gráficos |
| scipy | 1.7.0 | Procesamiento de señales (filtros, FFT) |
| ipython | 7.0.0 | (Opcional) Consola interactiva mejorada |

Instalar todas al mismo tiempo:

```bash
pip install -r requirements.txt
```

---

## 🧪 Validación y Verificación

### Comprobar la Instalación

```bash
python -c "
import numpy as np
import matplotlib.pyplot as plt
import scipy
print('NumPy versión:', np.__version__)
print('Matplotlib versión:', matplotlib.__version__)
print('SciPy versión:', scipy.__version__)
print('✓ Todas las dependencias están correctamente instaladas')
"
```

### Ejecutar Pruebas (Opcional)

Si hay pruebas unitarias disponibles:

```bash
python -m pytest tests/
```

---

## 📖 Teoría y Conceptos Clave

### 1. Teorema de Nyquist
Para capturar correctamente una señal, la frecuencia de muestreo debe ser al menos el doble de la frecuencia máxima:
$$F_s \geq 2 \cdot F_{máx}$$

### 2. Aliasing
Cuando $F_s < 2 \cdot F_{máx}$, componentes de frecuencia alta aparecen como componentes de baja frecuencia:
$$F_{alias} = |F - k \cdot F_s|$$

### 3. Cuantización
Representación discreta de valores continuos con resolución:
$$\Delta = \frac{V_{máx} - V_{mín}}{2^{bits}}$$

### 4. Punto Fijo Qm.n
Formato con m bits enteros y n bits fraccionarios:
$$\text{Valor} = \frac{\text{Código entero}}{2^n}$$

---

## 📝 Notas Importantes

1. **Precisión**: Se usan cálculos con doble precisión por defecto
2. **Gráficos**: Se guardan en formato PNG con resolución 300 dpi
3. **Reproducibilidad**: Todos los cálculos usan semillas fijas para resultados consistentes
4. **Documentación**: El código incluye docstrings completos para todas las funciones

---

## 🔍 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'numpy'"

**Solución**: Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Error: "Permission denied" al ejecutar

**Solución**: Asegúrate de que el archivo es ejecutable:
```bash
chmod +x src/problema*.py
```

### Error: "matplotlib can't find Tcl/Tk"

**Solución** (en Debian/Ubuntu):
```bash
sudo apt-get install python3-tk
```

### Los gráficos no se muestran

**Solución**: Modifica `matplotlib` para usar backend no-GUI:
```python
import matplotlib
matplotlib.use('Agg')  # Agregar al inicio del script
```

---

## 📞 Contacto y Soporte

**Profesor**: michaelgruner  
**Repositorio**: GitHub  
**Plataforma de entrega**: TEC Digital

Para cuestiones técnicas, abre un issue en el repositorio o contacta directamente al profesor.

---

## 📄 Referencias

- Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-Time Signal Processing* (3rd ed.). Prentice Hall.
- Smith, S. W. (1999). *The Scientist and Engineer's Guide to Digital Signal Processing*. California Technical Publishing.
- Proakis, J. G., & Manolakis, D. G. (2007). *Digital Signal Processing: Principles, Algorithms, and Applications* (4th ed.). Prentice Hall.

---

## 📋 Checklist de Entrega

Antes de entregar, verifica que:

- [ ] Todo el código está en el repositorio
- [ ] README.md está completo y actualizado
- [ ] requirements.txt tiene todas las dependencias
- [ ] El código se ejecuta sin errores en Linux
- [ ] Los gráficos se generan correctamente
- [ ] El informe PDF está incluido
- [ ] Se ha compartido acceso con `michaelgruner`
- [ ] Se ha creado backup (ZIP/TAR) para TEC Digital
- [ ] Todos los archivos se subieron antes del 20 de sept. a las 23:59

---

## 📄 Licencia

Este proyecto es para propósitos académicos del Instituto Tecnológico de Costa Rica.

---

**Última actualización**: Septiembre 2026  
**Autor**: [Tu Nombre]  
**Estado**: En desarrollo ✓
