#!/usr/bin/env python3
"""
Script para mezclar PDFs alfabéticamente y enumerar páginas con color, alineación y fuente personalizables
Versión con manejo mejorado de errores de diccionario PyPDF2, selección de color, alineación y fuente
"""

import os
import glob
from pathlib import Path
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, blue, green, black, purple
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import tempfile
import io
import warnings


def get_color_choice():
    """
    Permite al usuario seleccionar el color del número de página
    """
    colors = {
        '1': ('Rojo', red),
        '2': ('Azul', blue),
        '3': ('Verde', green),
        '4': ('Negro', black),
        '5': ('Morado', purple)
    }
    
    print("\nSelecciona el color para los números de página:")
    for key, (name, _) in colors.items():
        print(f"  {key}. {name}")
    
    while True:
        choice = input("\nIngresa tu selección (1-5): ").strip()
        if choice in colors:
            color_name, color_obj = colors[choice]
            print(f"Color seleccionado: {color_name}")
            return color_obj
        else:
            print("Selección inválida. Por favor ingresa un número del 1 al 5.")


def get_alignment_choice():
    """
    Permite al usuario seleccionar la alineación del número de página
    """
    alignments = {
        '1': ('Izquierda', 'left'),
        '2': ('Centro', 'center'),
        '3': ('Derecha', 'right')
    }
    
    print("\nSelecciona la alineación para los números de página:")
    for key, (name, _) in alignments.items():
        print(f"  {key}. {name}")
    
    while True:
        choice = input("\nIngresa tu selección (1-3): ").strip()
        if choice in alignments:
            alignment_name, alignment_value = alignments[choice]
            print(f"Alineación seleccionada: {alignment_name}")
            return alignment_value
        else:
            print("Selección inválida. Por favor ingresa un número del 1 al 3.")


def get_font_choice():
    """
    Permite al usuario seleccionar la fuente del número de página
    """
    fonts = {
        '1': ('Helvetica (Normal)', 'Helvetica'),
        '2': ('Helvetica Bold (Negrita)', 'Helvetica-Bold'),
        '3': ('Times Roman', 'Times-Roman'),
        '4': ('Times Bold (Times Negrita)', 'Times-Bold'),
        '5': ('Courier (Monoespaciada)', 'Courier')
    }
    
    print("\nSelecciona la fuente para los números de página:")
    for key, (name, _) in fonts.items():
        print(f"  {key}. {name}")
    
    while True:
        choice = input("\nIngresa tu selección (1-5): ").strip()
        if choice in fonts:
            font_name, font_value = fonts[choice]
            print(f"Fuente seleccionada: {font_name}")
            return font_value
        else:
            print("Selección inválida. Por favor ingresa un número del 1 al 5.")


def extract_sorting_key(filename):
    """
    Extrae una clave de ordenamiento del nombre del archivo para manejar diferentes nomenclaturas
    """
    import re
    basename = os.path.basename(filename)
    
    # Patrones de búsqueda en orden de prioridad
    patterns = [
        # Patrón 1: Número al inicio (ej: "1. A1 VCT.pdf", "25. T3 1. Carta R MARMO.pdf")
        r'^(\d+)\.',
        
        # Patrón 2: Letra seguida de número (ej: "A1 VCT.pdf", "T1 1 Lista.pdf")
        r'^([A-Z]+)(\d+)',
        
        # Patrón 3: Solo letra al inicio (ej: "A VCT.pdf")
        r'^([A-Z]+)',
        
        # Patrón 4: Número en cualquier parte del nombre
        r'(\d+)',
    ]
    
    # Intentar cada patrón
    for i, pattern in enumerate(patterns):
        match = re.search(pattern, basename)
        if match:
            if i == 0:  # Número al inicio con punto
                return (0, int(match.group(1)), 0, basename.lower())
            elif i == 1:  # Letra + número
                letter_part = match.group(1)
                number_part = int(match.group(2))
                # Convertir letras a números (A=1, B=2, etc.)
                letter_value = sum((ord(c) - ord('A') + 1) * (26 ** (len(letter_part) - j - 1)) 
                                 for j, c in enumerate(letter_part))
                return (1, letter_value, number_part, basename.lower())
            elif i == 2:  # Solo letra
                letter_part = match.group(1)
                letter_value = sum((ord(c) - ord('A') + 1) * (26 ** (len(letter_part) - j - 1)) 
                                 for j, c in enumerate(letter_part))
                return (2, letter_value, 0, basename.lower())
            elif i == 3:  # Número en cualquier parte
                return (3, int(match.group(1)), 0, basename.lower())
    
    # Si no se encuentra ningún patrón, ordenar alfabéticamente al final
    return (4, 0, 0, basename.lower())


def get_pdf_files(folder_path):
    """
    Obtiene todos los archivos PDF de un folder y los ordena por nomenclatura inteligente
    """
    if not os.path.exists(folder_path):
        raise ValueError(f"El folder {folder_path} no existe")
    
    # Buscar todos los archivos PDF
    pdf_pattern = os.path.join(folder_path, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        raise ValueError(f"No se encontraron archivos PDF en {folder_path}")
    
    # Ordenar por clave de ordenamiento inteligente
    pdf_files.sort(key=extract_sorting_key)
    
    print(f"Archivos PDF encontrados y ordenados por nomenclatura:")
    for i, pdf_file in enumerate(pdf_files, 1):
        filename = os.path.basename(pdf_file)
        sort_key = extract_sorting_key(pdf_file)
        print(f"  {i:2d}. {filename} (clave: {sort_key})")
    
    return pdf_files


def merge_pdfs(pdf_files, output_path):
    """
    Mezcla múltiples PDFs en uno solo
    """
    merger = PyPDF2.PdfWriter()
    
    print("\nMezclando PDFs...")
    
    for pdf_file in pdf_files:
        try:
            # Suprimir warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                
                with open(pdf_file, 'rb') as file:
                    # Usar strict=False para ser más tolerante con PDFs malformados
                    reader = PyPDF2.PdfReader(file, strict=False)
                    
                    # Verificar que el PDF no esté corrupto
                    if reader.is_encrypted:
                        print(f"Advertencia: {os.path.basename(pdf_file)} está encriptado, intentando procesar...")
                        try:
                            reader.decrypt("")
                        except:
                            print(f"  ✗ No se pudo descifrar {os.path.basename(pdf_file)}")
                            continue
                    
                    # Agregar todas las páginas del PDF actual
                    for page_num in range(len(reader.pages)):
                        try:
                            page = reader.pages[page_num]
                            merger.add_page(page)
                        except Exception as page_error:
                            print(f"  ⚠ Error en página {page_num + 1} de {os.path.basename(pdf_file)}: {str(page_error)}")
                            continue
                    
                    print(f"  ✓ Agregado: {os.path.basename(pdf_file)} ({len(reader.pages)} páginas)")
                
        except Exception as e:
            print(f"  ✗ Error procesando {os.path.basename(pdf_file)}: {str(e)}")
            continue
    
    # Guardar el PDF mezclado
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
    
    total_pages = len(merger.pages)
    print(f"\n✓ PDF mezclado guardado: {output_path}")
    print(f"  Total de páginas: {total_pages}")
    
    return total_pages


def create_page_number_overlay(page_number, page_width, page_height, color=red, alignment='right', font='Helvetica-Bold'):
    """
    Crea una superposición con el número de página en el color, alineación y fuente especificados
    """
    packet = io.BytesIO()
    
    # Crear un canvas temporal
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))
    
    # Configurar el texto
    c.setFillColor(color)
    c.setFont(font, 12)
    
    # Calcular posición según la alineación
    y_position = 30
    page_number_str = str(page_number)
    
    if alignment == 'left':
        x_position = 50
    elif alignment == 'center':
        # Calcular el ancho aproximado del texto para centrarlo
        text_width = c.stringWidth(page_number_str, font, 12)
        x_position = (page_width - text_width) / 2
    else:  # 'right' por defecto
        x_position = page_width - 50
    
    c.drawString(x_position, y_position, page_number_str)
    c.save()
    
    packet.seek(0)
    return PyPDF2.PdfReader(packet)


def add_page_numbers(input_pdf_path, output_pdf_path, color=red, alignment='right', font='Helvetica-Bold'):
    """
    Agrega números de página en el color, alineación y fuente especificados al PDF
    """
    print(f"\nAgregando números de página con configuración personalizada...")
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        with open(input_pdf_path, 'rb') as input_file:
            # Usar strict=False para ser más tolerante con PDFs malformados
            reader = PyPDF2.PdfReader(input_file, strict=False)
            writer = PyPDF2.PdfWriter()
            
            total_pages = len(reader.pages)
            
            for page_num in range(total_pages):
                try:
                    page = reader.pages[page_num]
                    
                    # Obtener las dimensiones de la página
                    page_box = page.mediabox
                    page_width = float(page_box.width)
                    page_height = float(page_box.height)
                    
                    # Crear la superposición con el número de página
                    overlay_reader = create_page_number_overlay(page_num + 1, page_width, page_height, color, alignment, font)
                    overlay_page = overlay_reader.pages[0]
                    
                    # Combinar la página original con la superposición
                    page.merge_page(overlay_page)
                    writer.add_page(page)
                    
                    if (page_num + 1) % 10 == 0 or (page_num + 1) == total_pages:
                        print(f"  Procesadas {page_num + 1}/{total_pages} páginas")
                
                except Exception as page_error:
                    print(f"  ⚠ Error procesando página {page_num + 1}: {str(page_error)}")
                    # Agregar una página en blanco como fallback
                    try:
                        # Crear una página en blanco con dimensiones estándar
                        blank_page = writer.add_blank_page(width=612, height=792)
                        print(f"  → Página {page_num + 1} reemplazada con página en blanco")
                    except:
                        print(f"  → Saltando página {page_num + 1}")
                        continue
    
    # Guardar el PDF final
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)
    
    print(f"\n✓ PDF con numeración completado: {output_pdf_path}")


def main():
    """
    Función principal del script
    """
    print("=" * 60)
    print("   MEZCLADOR Y NUMERADOR DE PDFs")
    print("=" * 60)
    
    # Solicitar el folder de entrada
    folder_path = input("\nIngresa la ruta del folder con los PDFs: ").strip()
    
    # Si no se ingresa ruta, usar el directorio actual
    if not folder_path:
        folder_path = "./"
        
        
    
    # Convertir a ruta absoluta
    folder_path = os.path.abspath(folder_path)
    
    # Solicitar selección de color
    selected_color = get_color_choice()
    
    # Solicitar selección de alineación
    selected_alignment = get_alignment_choice()
    
    # Solicitar selección de fuente
    selected_font = get_font_choice()
    
    try:
        # Obtener archivos PDF ordenados alfabéticamente
        pdf_files = get_pdf_files(folder_path)
        
        # Generar nombres de archivos de salida
        timestamp = __import__('datetime').datetime.now().strftime("%Y%m%d_%H%M%S")
        merged_pdf = os.path.join(folder_path, f"merged_pdfs_{timestamp}.pdf")
        final_pdf = os.path.join(folder_path, f"final_numbered_pdfs_{timestamp}.pdf")
        
        # Mezclar PDFs
        total_pages = merge_pdfs(pdf_files, merged_pdf)
        
        # Agregar números de página
        add_page_numbers(merged_pdf, final_pdf, selected_color, selected_alignment, selected_font)
        
        # Limpiar archivo temporal
        os.remove(merged_pdf)
        
        print("\n" + "=" * 60)
        print("   ¡PROCESO COMPLETADO EXITOSAMENTE!")
        print("=" * 60)
        print(f"Archivo final: {final_pdf}")
        print(f"Total de páginas numeradas: {total_pages}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
