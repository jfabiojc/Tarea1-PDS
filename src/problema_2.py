#!/usr/bin/env python3
"""
Problema 2: Visualización de una señal y su alias
Procesamiento Digital de Señales - Tarea 1
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def calcular_alias(f, fs):
    """
    Calcula la frecuencia alias de una señal.
    
    El alias es la frecuencia dentro del rango -Fs/2 a Fs/2 que representa
    la señal después del muestreo.
    """
    # Traer la frecuencia al rango [-Fs/2, Fs/2]
    f_alias = f
    
    # Si f está fuera del rango de Nyquist, aplicar plegado
    while f_alias > fs / 2:
        f_alias = fs - f_alias
        if f_alias <= fs / 2:
            break
        f_alias = -f_alias
    
    while f_alias < -fs / 2:
        f_alias = -fs - f_alias
        if f_alias >= -fs / 2:
            break
        f_alias = -f_alias
    
    return f_alias

def graficar_señal_y_alias(f, fs, num_ciclos):
    """
    Grafica una señal sinusoidal, su alias y las muestras.
    
    Parámetros:
    -----------
    f : float
        Frecuencia de la señal en Hz
    fs : float
        Frecuencia de muestreo en Hz
    num_ciclos : float
        Número de ciclos a mostrar
    """
    
    # Calcular el tiempo total a mostrar
    tiempo_total = num_ciclos / f if f > 0 else 1
    
    # Crear eje de tiempo continuo para la gráfica
    t = np.linspace(0, tiempo_total, 10000)
    
    # Señal original (sinusoidal)
    x = np.sin(2 * np.pi * f * t)
    
    # Instantes de muestreo
    n_muestras = int(fs * tiempo_total) + 1
    n = np.arange(n_muestras)
    t_muestras = n / fs
    
    # Muestras de la señal original
    x_muestras = np.sin(2 * np.pi * f * t_muestras)
    
    # Calcular alias
    f_alias = calcular_alias(f, fs)
    
    # Señal alias (para graficar)
    x_alias = np.sin(2 * np.pi * f_alias * t)
    
    # Crear figura con dos subgráficas
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Primera gráfica: señal original y alias
    ax1.plot(t, x, 'b-', label=f'Señal original: F = {f} Hz', linewidth=2)
    if abs(f_alias - f) > 0.01:  # Si hay alias diferente
        ax1.plot(t, x_alias, 'r--', label=f'Alias: F_alias = {f_alias:.2f} Hz', linewidth=2)
    ax1.plot(t_muestras, x_muestras, 'ko', markersize=6, label='Muestras de señal original')
    
    ax1.set_xlabel('Tiempo (s)', fontsize=12)
    ax1.set_ylabel('Amplitud', fontsize=12)
    ax1.set_title(f'Señal Original vs Alias\n(F = {f} Hz, Fs = {fs} Hz, Nyquist = {fs/2} Hz)', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    ax1.set_xlim([0, tiempo_total])
    
    # Segunda gráfica: solo muestras y reconstrucción
    ax2.stem(t_muestras, x_muestras, basefmt=' ')
    ax2.plot(t, x_alias, 'r--', label='Señal que se interpreta', linewidth=2, alpha=0.7)
    ax2.plot(t_muestras, x_muestras, 'ko', markersize=8)
    
    ax2.set_xlabel('Tiempo (s)', fontsize=12)
    ax2.set_ylabel('Amplitud', fontsize=12)
    ax2.set_title('Muestras y Señal Interpretada', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.set_xlim([0, tiempo_total])
    
    plt.tight_layout()
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'figuras')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'figura_problema2.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfica guardada: {output_path}")
    plt.show()
    
    # Información en consola
    print("\n" + "="*60)
    print("RESULTADO DEL PROBLEMA 2")
    print("="*60)
    print(f"Frecuencia de la señal (F):        {f} Hz")
    print(f"Frecuencia de muestreo (Fs):      {fs} Hz")
    print(f"Frecuencia de Nyquist (Fs/2):     {fs/2} Hz")
    print(f"Número de ciclos mostrados:       {num_ciclos}")
    print(f"Tiempo total mostrado:             {tiempo_total:.4f} s")
    print(f"Número de muestras:                {n_muestras}")
    print(f"Frecuencia del alias:              {f_alias:.2f} Hz")
    print(f"\nMuestras tomadas:")
    print(f"{'Índice':<8} {'Tiempo (s)':<15} {'Muestra':<15}")
    print("-" * 40)
    for i in range(min(10, len(t_muestras))):
        print(f"{i:<8} {t_muestras[i]:<15.6f} {x_muestras[i]:<15.6f}")
    if n_muestras > 10:
        print(f"{'...':<8}")
    print("="*60 + "\n")


def main():
    """
    Función principal: solicita parámetros al usuario
    """
    print("\n" + "="*60)
    print("PROBLEMA 2: VISUALIZACIÓN DE SEÑAL Y SU ALIAS")
    print("="*60)
    
    try:
        # Entrada del usuario
        f = float(input("\nIngrese la frecuencia F de la señal (Hz): "))
        fs = float(input("Ingrese la frecuencia de muestreo Fs (Hz): "))
        num_ciclos = float(input("Ingrese el número de ciclos a mostrar: "))
        
        # Validaciones
        if f <= 0:
            raise ValueError("La frecuencia F debe ser positiva")
        if fs <= 0:
            raise ValueError("La frecuencia de muestreo Fs debe ser positiva")
        if num_ciclos <= 0:
            raise ValueError("El número de ciclos debe ser positivo")
        
        # Generar gráfica
        graficar_señal_y_alias(f, fs, num_ciclos)
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("Abortando...")


if __name__ == "__main__":
    main()