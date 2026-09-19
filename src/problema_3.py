#!/usr/bin/env python3
"""
Problema 3: Aliasing para recuperar la información de una señal modulada
Procesamiento Digital de Señales - Tarea 1
 
Objetivo:
Recuperar muestras del tono de información (100 Hz) de una señal modulada
mediante el uso inteligente del aliasing con una frecuencia de muestreo 
adecuadamente elegida.
 
Señal modulada: x(t) = [1 + 0.5*cos(2π*100t)] * cos(2π*1000t)
Información deseada: m(t) = cos(2π*100t) (100 Hz)
Portadora: 1000 Hz
"""
 
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os
 
 
def problema_3_parte_a():
    """
    Parte a) Descomponer x(t) en tonos puros usando identidades trigonométricas
    
    Tenemos: x(t) = [1 + 0.5*cos(2π*100t)] * cos(2π*1000t)
    
    Expandiendo: x(t) = cos(2π*1000t) + 0.5*cos(2π*100t)*cos(2π*1000t)
    
    Usando: cos(A)*cos(B) = 0.5*[cos(A-B) + cos(A+B)]
    
    cos(2π*100t)*cos(2π*1000t) = 0.5*[cos(2π*900t) + cos(2π*1100t)]
    
    Entonces: x(t) = cos(2π*1000t) + 0.25*[cos(2π*900t) + cos(2π*1100t)]
    
    Componentes:
    - f1 = 900 Hz, amplitud A1 = 0.25
    - f2 = 1000 Hz, amplitud A2 = 1.0 (portadora)
    - f3 = 1100 Hz, amplitud A3 = 0.25
    
    Frecuencia de Nyquist = 2 * fmax = 2 * 1100 = 2200 Hz
    """
    
    print("\n" + "="*70)
    print("PROBLEMA 3 - PARTE a) DESCOMPOSICIÓN EN TONOS PUROS")
    print("="*70)
    
    print("\nSeñal original: x(t) = [1 + 0.5*cos(2π*100t)] * cos(2π*1000t)")
    print("\nExpandiendo con identidades trigonométricas:")
    print("x(t) = cos(2π*1000t) + 0.5*cos(2π*100t)*cos(2π*1000t)")
    print("\nUsando: cos(A)*cos(B) = 0.5*[cos(A-B) + cos(A+B)]")
    print("x(t) = cos(2π*1000t) + 0.25*cos(2π*900t) + 0.25*cos(2π*1100t)")
    
    # Tonos puros
    tonos = [
        {"frecuencia": 900, "amplitud": 0.25, "descripcion": "Banda lateral inferior"},
        {"frecuencia": 1000, "amplitud": 1.0, "descripcion": "Portadora"},
        {"frecuencia": 1100, "amplitud": 0.25, "descripcion": "Banda lateral superior"}
    ]
    
    print("\n" + "-"*70)
    print("COMPONENTES DE FRECUENCIA")
    print("-"*70)
    print(f"{'Número':<8} {'Frecuencia (Hz)':<20} {'Amplitud':<15} {'Descripción':<20}")
    print("-"*70)
    
    f_max = 0
    for i, tono in enumerate(tonos, 1):
        print(f"{i:<8} {tono['frecuencia']:<20} {tono['amplitud']:<15.2f} {tono['descripcion']:<20}")
        f_max = max(f_max, tono['frecuencia'])
    
    f_nyquist = 2 * f_max
    print("-"*70)
    print(f"\nFrecuencia máxima (fmax): {f_max} Hz")
    print(f"Frecuencia de Nyquist: {f_nyquist} Hz")
    print(f"\nPara evitar aliasing sin intención, se requeriría Fs > {f_nyquist} Hz")
    
    return tonos, f_nyquist
 
 
def problema_3_parte_b():
    """
    Parte b) Elegir frecuencia de muestreo para recuperar 100 Hz sin aliasing
    
    Estrategia: Usar aliasing inteligente para traer los componentes de alta
    frecuencia al rango de baja frecuencia.
    
    Con Fs = 800 Hz:
    - 900 Hz → alias a 900 - 800 = 100 Hz (esto queremos)
    - 1000 Hz → alias a 1000 - 800 = 200 Hz (lo eliminamos con filtro)
    - 1100 Hz → alias a 1100 - 800 = 300 Hz (lo eliminamos con filtro)
    
    Con un filtro pasa-bajo a ~150 Hz recuperamos solo el tono de 100 Hz.
    """
    
    print("\n" + "="*70)
    print("PROBLEMA 3 - PARTE b) ELECCIÓN DE FRECUENCIA DE MUESTREO")
    print("="*70)
    
    # Componentes originales (del apartado a)
    f1, f2, f3 = 900, 1000, 1100
    
    print("\nComponentes a muestrear:")
    print(f"  f1 = {f1} Hz (amplitud 0.25)")
    print(f"  f2 = {f2} Hz (amplitud 1.0) - PORTADORA (queremos eliminar)")
    print(f"  f3 = {f3} Hz (amplitud 0.25)")
    
    print("\nObjetivo:")
    print("  - Traer el componente de 900 Hz al rango de 100 Hz (mediante aliasing)")
    print("  - Eliminar la portadora de 1000 Hz")
    print("  - Sin aliasing en el componente de 100 Hz recuperado")
    
    # Frecuencia de muestreo elegida
    Fs = 800  # Hz
    
    print(f"\n{'PROPUESTA:':<30} Fs = {Fs} Hz")
    print(f"{'Frecuencia de Nyquist:':<30} Fs/2 = {Fs/2} Hz")
    
    print("\nAnálisis de aliasing con Fs = 800 Hz:")
    print("-"*70)
    print(f"{'Componente original':<25} {'Frecuencia alias':<25} {'Resultado':<20}")
    print("-"*70)
    
    # Calcular alias
    f1_alias = f1 - np.floor(f1/Fs) * Fs
    if f1_alias > Fs/2:
        f1_alias = Fs - f1_alias
    
    f2_alias = f2 - np.floor(f2/Fs) * Fs
    if f2_alias > Fs/2:
        f2_alias = Fs - f2_alias
    
    f3_alias = f3 - np.floor(f3/Fs) * Fs
    if f3_alias > Fs/2:
        f3_alias = Fs - f3_alias
    
    print(f"900 Hz{'':<19} {f1_alias:<25} ✓ Queremos esto")
    print(f"1000 Hz{'':<18} {f2_alias:<25} ✗ Eliminar con filtro")
    print(f"1100 Hz{'':<18} {f3_alias:<25} ✗ Eliminar con filtro")
    
    print("\n" + "-"*70)
    print("JUSTIFICACIÓN:")
    print("-"*70)
    print(f"1. El componente de 900 Hz se alias a 100 Hz mediante:")
    print(f"   f_alias = 900 - 1·800 = 100 Hz")
    print(f"\n2. El componente de 1000 Hz se alias a 200 Hz")
    print(f"\n3. El componente de 1100 Hz se alias a 300 Hz")
    print(f"\n4. Con un filtro pasa-bajo digital con frecuencia de corte ~150 Hz,")
    print(f"   se atenúan los componentes de 200 Hz y 300 Hz, manteniendo solo 100 Hz")
    print(f"\n5. No hay aliasing del componente de 100 Hz porque 100 Hz < Fs/2 = 400 Hz")
    
    return Fs, [f1_alias, f2_alias, f3_alias]
 
 
def problema_3_parte_c():
    """
    Parte c) Expresión de x[n] después del plegado y operaciones para recuperar m[n]
    
    Después del plegado con Fs = 800 Hz:
    x[n] = 0.25*cos(π*n/4) + cos(π*n/2) + 0.25*cos(3π*n/4)
    
    Para recuperar m[n] = cos(π*n/4), podemos:
    1. Aplicar un filtro pasa-bajo digital
    2. O tomar muestras cada 2 puntos: m[n] = x[2n]
       (porque cos(π*n/2) = 0 en los índices pares)
    """
    
    print("\n" + "="*70)
    print("PROBLEMA 3 - PARTE c) EXPRESIÓN DE x[n] Y RECUPERACIÓN DE m[n]")
    print("="*70)
    
    print("\nDespués del muestreo con Fs = 800 Hz, los alias son:")
    print("  f1_alias = 100 Hz → 0.25*cos(2π*100*n/800) = 0.25*cos(π*n/4)")
    print("  f2_alias = 200 Hz → 1.0*cos(2π*200*n/800) = cos(π*n/2)")
    print("  f3_alias = 300 Hz → 0.25*cos(2π*300*n/800) = 0.25*cos(3π*n/4)")
    
    print("\nExpresión de x[n] (suma de componentes alias):")
    print("x[n] = 0.25·cos(π·n/4) + cos(π·n/2) + 0.25·cos(3π·n/4)")
    
    print("\nPara recuperar m[n] = cos(π·n/4):")
    print("\nOpción 1: Aplicar filtro pasa-bajo digital")
    print("  - Elimina componentes de 200 Hz y 300 Hz")
    print("  - Mantiene solo 100 Hz")
    
    print("\nOpción 2 (MÁS SIMPLE): Tomar muestras cada 2 puntos")
    print("  - m[n] = x[2n]")
    print("  - Porque: cos(π·(2n)/2) = cos(π·n) = ±1 periódicamente")
    print("  - En los índices pares, el término de 200 Hz es ±1")
    print("  - Necesitamos una estrategia mejor...")
    
    print("\nOpción 3 (CORRECTA): Usar operación de filtrado simple")
    print("  Aplicar promedio móvil o filtro pasa-bajo")
    print("  m[n] ≈ x[n] filtrado con frecuencia de corte < 150 Hz")
    
    print("\n" + "-"*70)
    print("OPERACIONES ARITMÉTICAS:")
    print("-"*70)
    print("\n1. Muestrear x(t) a Fs = 800 Hz para obtener x[n]")
    print("\n2. Aplicar filtro pasa-bajo digital con:")
    print("   - Frecuencia de corte: ~150 Hz")
    print("   - O usar promedio móvil: y[n] = (x[n] + x[n-1])/2")
    print("\n3. El resultado será aproximadamente m[n] = cos(2π*100*n/800)")
    
    return None
 
 
def problema_3_parte_d():
    """
    Parte d) Comprobación en Python
    
    Gráficar:
    1. x(t) y sus muestras
    2. m(t) y las muestras recuperadas
    """
    
    print("\n" + "="*70)
    print("PROBLEMA 3 - PARTE d) COMPROBACIÓN EN PYTHON")
    print("="*70)
    
    # Parámetros
    Fs = 800  # Hz - Frecuencia de muestreo elegida
    f_info = 100  # Hz - Frecuencia de información
    f_carrier = 1000  # Hz - Portadora

    # Tiempo: se calcula sobre una ventana más amplia que los 3 ciclos que se
    # piden mostrar, para que el filtro (zero-phase, vía filtfilt) tenga
    # suficientes muestras de contexto y no aparezca el transitorio de borde
    # dentro de la región que se reporta.
    duration_show = 0.03    # 3 ciclos de 100 Hz (lo que pide el enunciado)
    duration_calc = 0.18    # ventana interna de cálculo
    t_offset = 0.06         # nos alejamos del borde antes de tomar los 3 ciclos a mostrar

    t_calc = np.arange(0, duration_calc, 1/Fs)          # instantes de muestreo (ventana completa)
    t_continuo = np.linspace(0, duration_show, 10000)   # para graficar x(t) suave (3 ciclos)

    # Señal modulada original (continua, solo para la gráfica de x(t))
    x_t = (1 + 0.5*np.cos(2*np.pi*f_info*t_continuo)) * np.cos(2*np.pi*f_carrier*t_continuo)

    # Muestras de x(t) sobre toda la ventana de cálculo
    x_muestras_calc = (1 + 0.5*np.cos(2*np.pi*f_info*t_calc)) * np.cos(2*np.pi*f_carrier*t_calc)

    # ===== RECUPERACIÓN: Filtro pasa-bajo =====
    # Se necesita un filtro más selectivo que uno de orden 4: los alias quedan
    # a 100, 200 y 300 Hz (separados solo 100 Hz entre sí), y la portadora
    # aliasada a 200 Hz tiene 4 veces la amplitud del tono de 100 Hz que se
    # quiere recuperar. Con corte en 110 Hz y orden 8 se logra suficiente
    # atenuación en 200/300 Hz sin distorsionar el tono deseado.
    freq_corte = 110  # Hz
    orden = 8
    freq_normalizada = np.clip(freq_corte / (Fs/2), 0.001, 0.999)
    b, a = signal.butter(orden, freq_normalizada, btype='low')

    # filtfilt aplica el filtro dos veces (adelante y atrás) para tener fase
    # cero, así que la ganancia real en 100 Hz es el cuadrado de |H(100 Hz)|.
    # Además, el tono de información llega con amplitud 0.25 dentro de x[n]
    # (no 1, como m(t)). Ambos efectos se corrigen con un único factor de
    # escala, calculado una sola vez y aplicado por igual en todos los casos
    # (así como en un sistema real no se conoce de antemano cuánto atenúa
    # el filtro ni la fase de la portadora).
    _, h100 = signal.freqz(b, a, worN=[2*np.pi*f_info/Fs])
    ganancia_100hz = np.abs(h100[0])
    factor_escala = 1 / (0.25 * ganancia_100hz**2)

    m_recuperadas_calc = signal.filtfilt(b, a, x_muestras_calc) * factor_escala

    # Nos quedamos solo con los 3 ciclos pedidos, ya lejos del borde
    mostrar = (t_calc >= t_offset) & (t_calc < t_offset + duration_show)
    t = t_calc[mostrar] - t_offset
    x_muestras = x_muestras_calc[mostrar]
    m_recuperadas = m_recuperadas_calc[mostrar]

    # Señal de información original
    m_t = np.cos(2*np.pi*f_info*t_continuo)
    m_muestras_real = np.cos(2*np.pi*f_info*t)
    
    # ===== GRÁFICAS =====
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))
    
    # Gráfica 1: Señal modulada x(t) y sus muestras
    ax = axes[0]
    ax.plot(t_continuo*1000, x_t, 'b-', linewidth=1.5, label='x(t) continua')
    ax.stem(t*1000, x_muestras, linefmt='ro', markerfmt='ro', basefmt=' ', 
            label=f'x[n] muestreadas (Fs={Fs} Hz)')
    ax.set_xlabel('Tiempo (ms)', fontsize=11)
    ax.set_ylabel('Amplitud', fontsize=11)
    ax.set_title('Señal Modulada Original: x(t) = [1 + 0.5·cos(2π·100t)]·cos(2π·1000t)', 
                 fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_xlim([0, duration_show*1000])

    # Gráfica 2: Información original m(t) y muestras recuperadas
    ax = axes[1]
    ax.plot(t_continuo*1000, m_t, 'g-', linewidth=2, label='m(t) original: cos(2π·100t)')
    ax.plot(t*1000, m_recuperadas, 'r--', linewidth=1.5, label='m[n] recuperadas (con filtro LPF)')
    ax.stem(t*1000, m_muestras_real, linefmt='bs', markerfmt='bs', basefmt=' ',
            label='m[n] directas')
    ax.set_xlabel('Tiempo (ms)', fontsize=11)
    ax.set_ylabel('Amplitud', fontsize=11)
    ax.set_title('Señal de Información: Original vs Recuperada (3 ciclos de 100 Hz)', 
                 fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_xlim([0, duration_show*1000])

    # Gráfica 3: Comparación de muestras recuperadas vs directas
    ax = axes[2]
    indices = np.arange(len(t))
    ax.bar(indices - 0.2, m_muestras_real, width=0.4, label='m[n] directo', alpha=0.7)
    ax.bar(indices + 0.2, m_recuperadas, width=0.4, label='m[n] recuperado', alpha=0.7)
    ax.set_xlabel('Índice de muestra [n]', fontsize=11)
    ax.set_ylabel('Amplitud', fontsize=11)
    ax.set_title('Comparación Numérica: Muestras Recuperadas vs Directas', 
                 fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.legend(fontsize=10)
    
    plt.tight_layout()
    
    # Guardar figura
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'figuras')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'figura_problema3_d.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfica guardada: {output_path}")
    plt.show()
    
    # ===== COMPARACIÓN NUMÉRICA =====
    print("\n" + "-"*70)
    print("COMPARACIÓN NUMÉRICA: Muestras recuperadas vs Directas")
    print("-"*70)
    print(f"\n{'Índice':<8} {'Tiempo (ms)':<12} {'Directo':<15} {'Recuperado':<15} {'Error':<15}")
    print("-"*70)
    
    error_absoluto = np.abs(m_muestras_real - m_recuperadas)
    error_relativo = error_absoluto / (np.abs(m_muestras_real) + 1e-10) * 100
    
    for i in range(len(t)):
        print(f"{i:<8} {t[i]*1000:<12.3f} {m_muestras_real[i]:<15.6f} {m_recuperadas[i]:<15.6f} "
              f"{error_absoluto[i]:<15.6e}")
    
    print("\n" + "-"*70)
    print("ESTADÍSTICAS DE ERROR")
    print("-"*70)
    print(f"Error absoluto máximo: {np.max(error_absoluto):.6e}")
    print(f"Error absoluto promedio: {np.mean(error_absoluto):.6e}")
    print(f"Error cuadrático medio: {np.sqrt(np.mean(error_absoluto**2)):.6e}")
    print(f"Correlación (debe ser ~1.0): {np.corrcoef(m_muestras_real, m_recuperadas)[0,1]:.6f}")
    
    return t, x_muestras, m_muestras_real, m_recuperadas
 
 
def problema_3_parte_e():
    """
    Parte e) Señal con fase desconocida en la portadora
    
    xϕ(t) = [1 + 0.5*cos(2π*100t)] * cos(2π*1000t + ϕ)
    
    Examinar ϕ = π/3 y ϕ = π/2
    """
    
    print("\n" + "="*70)
    print("PROBLEMA 3 - PARTE e) PORTADORA CON FASE DESCONOCIDA")
    print("="*70)
    
    print("\nSeñal con fase: xϕ(t) = [1 + 0.5·cos(2π·100t)]·cos(2π·1000t + ϕ)")
    
    # Parámetros
    Fs = 800  # Hz
    f_info = 100
    f_carrier = 1000
    duration_show = 0.03    # 3 ciclos de 100 Hz, lo que pide el enunciado
    duration_calc = 0.18    # ventana interna de cálculo (evita el transitorio de filtfilt)
    t_offset = 0.06

    t_calc = np.arange(0, duration_calc, 1/Fs)
    t_continuo = np.linspace(0, duration_show, 10000)

    mostrar = (t_calc >= t_offset) & (t_calc < t_offset + duration_show)
    t = t_calc[mostrar] - t_offset

    # Fases a examinar
    fases = [0, np.pi/3, np.pi/2, np.pi]
    
    # Crear figura con subplots para diferentes fases
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    print("\n" + "-"*70)
    print("ANÁLISIS MATEMÁTICO")
    print("-"*70)
    
    print("\nUsando identidades trigonométricas:")
    print("cos(2π·1000t + ϕ) = cos(2π·1000t)·cos(ϕ) - sin(2π·1000t)·sin(ϕ)")
    
    print("\nExpandiendo x_ϕ(t):")
    print("x_ϕ(t) = cos(ϕ)·cos(2π·1000t) + 0.5·cos(2π·100t)·cos(2π·1000t)·cos(ϕ)")
    print("       - sin(ϕ)·sin(2π·1000t) - 0.5·cos(2π·100t)·sin(2π·1000t)·sin(ϕ)")
    
    print("\nComponentes de frecuencia después del plegado:")
    print("- 100 Hz con amplitud: 0.25·cos(ϕ)")
    print("- 200 Hz con amplitud: cos(ϕ)")
    print("- 300 Hz con amplitud: 0.25·cos(ϕ)")
    print("- Componentes con sin(ϕ) en frecuencias diferentes")
    
    # Filtro para la recuperación: el mismo diseño y el mismo factor de
    # escala usados en la parte d), calibrados una sola vez para ϕ=0 y
    # aplicados sin cambios a cualquier fase (en un sistema real no se
    # conoce ϕ de antemano, así que no tendría sentido recalibrar por caso).
    freq_corte = 110
    orden = 8
    freq_normalizada = freq_corte / (Fs/2)
    b, a = signal.butter(orden, freq_normalizada, btype='low')
    _, h100 = signal.freqz(b, a, worN=[2*np.pi*f_info/Fs])
    ganancia_100hz = np.abs(h100[0])
    factor_escala = 1 / (0.25 * ganancia_100hz**2)

    # Resultados
    resultados = {}

    for idx, fase in enumerate(fases):
        # Señal con fase, calculada sobre la ventana completa y luego recortada
        x_phi_calc = (1 + 0.5*np.cos(2*np.pi*f_info*t_calc)) * np.cos(2*np.pi*f_carrier*t_calc + fase)
        x_phi_muestras = x_phi_calc[mostrar]

        # Recuperación con filtro (mismo procedimiento calibrado para ϕ=0)
        m_recuperada = signal.filtfilt(b, a, x_phi_calc)[mostrar] * factor_escala

        # Señal de información original (para comparación)
        m_t = np.cos(2*np.pi*f_info*t_continuo)
        m_muestras = np.cos(2*np.pi*f_info*t)
        
        # Almacenar resultados
        resultados[fase] = {
            'x_phi_muestras': x_phi_muestras,
            'm_recuperada': m_recuperada,
            'm_original': m_muestras
        }
        
        # Gráfica
        ax = axes[idx]
        ax.plot(t_continuo*1000, m_t, 'g-', linewidth=2, label='m(t) original')
        ax.plot(t*1000, m_recuperada, 'r--', linewidth=1.5, alpha=0.7, label='m[n] recuperada')
        ax.stem(t*1000, m_muestras, linefmt='bs', markerfmt='bs', basefmt=' ',
                label='m[n] directa')
        
        ax.set_xlabel('Tiempo (ms)', fontsize=10)
        ax.set_ylabel('Amplitud', fontsize=10)
        
        fase_grados = np.degrees(fase)
        ax.set_title(f'ϕ = {fase_grados:.1f}° (π·{fase/np.pi:.2f})', 
                     fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=9)
        ax.set_xlim([0, duration_show*1000])
    
    plt.tight_layout()
    
    # Guardar figura
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'figuras')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'figura_problema3_e.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfica guardada: {output_path}")
    plt.show()
    
    # Análisis para fases específicas
    print("\n" + "-"*70)
    print("ANÁLISIS PARA CASOS ESPECÍFICOS")
    print("-"*70)
    
    for fase in [0, np.pi/3, np.pi/2, np.pi]:
        fase_grados = np.degrees(fase)
        
        print(f"\nCaso: ϕ = {fase_grados:.1f}°")
        print(f"{'─'*50}")
        
        m_original = resultados[fase]['m_original']
        m_recuperada = resultados[fase]['m_recuperada']
        error = np.abs(m_original - m_recuperada)
        
        print(f"Error máximo: {np.max(error):.6e}")
        print(f"Error promedio: {np.mean(error):.6e}")
        print(f"Correlación: {np.corrcoef(m_original, m_recuperada)[0,1]:.6f}")
        
        # Mostrar primeras 5 muestras
        print(f"\nPrimeras 5 muestras:")
        print(f"{'n':<4} {'m_directo':<15} {'m_recuperado':<15} {'Error':<15}")
        for i in range(min(5, len(m_original))):
            print(f"{i:<4} {m_original[i]:<15.6f} {m_recuperada[i]:<15.6f} {error[i]:<15.6e}")
    
    # Conclusión
    print("\n" + "="*70)
    print("CONCLUSIÓN PARTE e)")
    print("="*70)
    print("""
¿El procedimiento permite recuperar la información para CUALQUIER fase?
 
RESPUESTA: NO completamente, pero el filtro pasa-bajo ayuda
 
EXPLICACIÓN:
 
1. El componente de 100 Hz tiene amplitud que depende de cos(ϕ):
   Amplitud de 100 Hz = 0.25·cos(ϕ)
   
2. Cuando ϕ = π/2:
   cos(π/2) = 0
   → El componente de 100 Hz desaparece completamente
   → No se puede recuperar m[n] sin información adicional
 
3. Para otras fases (ϕ ≠ π/2):
   → El componente de 100 Hz está presente
   → El filtro pasa-bajo lo recupera adecuadamente
   → Hay una pequeña distorsión pero se recupera la información
 
4. LIMITACIÓN FUNDAMENTAL:
   Si ϕ = π/2, la información se pierde porque la modulación
   se realiza con la portadora en cuadratura (90° desfase).
   
5. SOLUCIÓN:
   En sistemas reales de comunicaciones, se usan:
   - Demodulación coherente (sincronización de fase)
   - O se transmite la información tanto en fase como en cuadratura
     (modulación IQ: In-phase and Quadrature)
""")
 
 
def main():
    """Ejecutar todas las partes del problema 3"""
    
    print("\n" + "#"*70)
    print("# PROBLEMA 3: ALIASING PARA RECUPERAR SEÑAL MODULADA")
    print("# Tarea 1 - Procesamiento Digital de Señales")
    print("#"*70)
    
    # Parte a
    tonos, f_nyquist = problema_3_parte_a()
    
    # Parte b
    Fs, alias = problema_3_parte_b()
    
    # Parte c
    problema_3_parte_c()
    
    # Parte d
    problema_3_parte_d()
    
    # Parte e
    problema_3_parte_e()
    
    print("\n" + "#"*70)
    print("# FIN DEL PROBLEMA 3")
    print("#"*70 + "\n")
 
 
if __name__ == "__main__":
    main()
 