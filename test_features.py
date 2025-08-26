#!/usr/bin/env python3
"""
Script de prueba para demostrar las nuevas funcionalidades de color y alineación
"""

from main import get_color_choice, get_alignment_choice

def test_selections():
    """
    Función de prueba para mostrar las opciones disponibles
    """
    print("=" * 60)
    print("   PRUEBA DE SELECCIONES DE COLOR Y ALINEACIÓN")
    print("=" * 60)
    
    print("\n--- OPCIONES DISPONIBLES ---")
    
    print("\nColores disponibles:")
    print("  1. Rojo")
    print("  2. Azul") 
    print("  3. Verde")
    print("  4. Negro")
    print("  5. Morado")
    
    print("\nAlineaciones disponibles:")
    print("  1. Izquierda")
    print("  2. Centro")
    print("  3. Derecha")
    
    print("\nEjemplo de uso:")
    print("El usuario puede seleccionar cualquier combinación de color y alineación")
    print("para personalizar completamente la apariencia de los números de página.")

if __name__ == "__main__":
    test_selections()
