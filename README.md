# Mezclador y Numerador de PDFs

Este script en Python permite mezclar múltiples PDFs de un folder de forma alfabética y luego enumerar todas las páginas del 1 a N en color rojo.

## Características

- � **Ordenamiento numérico**: Los PDFs se procesan según el número que aparece al inicio del nombre del archivo (1, 2, 3, ... no 1, 10, 11, 2, 20...)
- 📑 **Mezclado automático**: Combina todos los PDFs en un solo documento
- 🔢 **Numeración en rojo**: Agrega números de página en color rojo en la esquina inferior derecha
- ⚡ **Manejo de errores**: Continúa el procesamiento aunque algunos PDFs tengan problemas
- 📊 **Progreso detallado**: Muestra el progreso del procesamiento

## Requisitos

- Python 3.7+
- PyPDF2
- reportlab

## Instalación

1. Clona o descarga este proyecto
2. Instala las dependencias:
```bash
pip install PyPDF2 reportlab
```

## Uso

### Opción 1: Ejecutar el script principal
```bash
python main.py
```
El script te pedirá la ruta del folder que contiene los PDFs.

### Opción 2: Crear PDFs de prueba primero
```bash
python test_pdfs_creator.py
python main.py
```
Cuando te pida el folder, ingresa: `test_pdfs`

## Funcionamiento

1. **Búsqueda**: El script busca todos los archivos `.pdf` en el folder especificado
2. **Ordenamiento**: Los archivos se ordenan numéricamente según el número que aparece al inicio del nombre del archivo
3. **Mezclado**: Se combinan todos los PDFs en un solo documento, preservando el orden numérico correcto
4. **Numeración**: Se agregan números de página en color rojo (fuente Helvetica-Bold, tamaño 12)
5. **Guardado**: El resultado se guarda con un timestamp para evitar sobrescribir archivos

## Archivos de salida

El script genera un archivo con el formato:
```
final_numbered_pdfs_YYYYMMDD_HHMMSS.pdf
```

## Ejemplo de uso

```
============================================================
   MEZCLADOR Y NUMERADOR DE PDFs
============================================================

Ingresa la ruta del folder con los PDFs: ./mi_folder

Archivos PDF encontrados y ordenados por número:
  1. 1. Documento_A.pdf (número extraído: 1)
  2. 2. Documento_B.pdf (número extraído: 2)
  3. 3. Manual_Usuario.pdf (número extraído: 3)

Mezclando PDFs...
  ✓ Agregado: Documento_A.pdf (3 páginas)
  ✓ Agregado: Documento_B.pdf (2 páginas)
  ✓ Agregado: Manual_Usuario.pdf (5 páginas)

✓ PDF mezclado guardado: merged_pdfs_20240825_143022.pdf
  Total de páginas: 10

Agregando números de página en color rojo...
  Procesadas 10/10 páginas

✓ PDF con numeración completado: final_numbered_pdfs_20240825_143022.pdf

============================================================
   ¡PROCESO COMPLETADO EXITOSAMENTE!
============================================================
Archivo final: final_numbered_pdfs_20240825_143022.pdf
Total de páginas numeradas: 10
```

## Características técnicas

- **Formato de numeración**: Helvetica-Bold, 12pt, color rojo
- **Posición**: Esquina inferior derecha (50px desde el borde derecho, 30px desde abajo)
- **Manejo de PDFs encriptados**: Intenta procesar PDFs con protección básica
- **Preservación de calidad**: Mantiene la calidad original de los documentos
- **Limpieza automática**: Elimina archivos temporales después del procesamiento

## Solución de problemas

- **"No se encontraron archivos PDF"**: Verifica que el folder contenga archivos .pdf
- **"Error procesando PDF"**: Algunos PDFs pueden estar corruptos o muy protegidos
- **Problemas de permisos**: Asegúrate de tener permisos de lectura en el folder de origen y escritura en el de destino

## Licencia

Este proyecto es de uso libre. Puedes modificarlo según tus necesidades.
