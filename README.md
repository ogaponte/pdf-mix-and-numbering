# Mezclador y Numerador de PDFs

Este script en Python permite mezclar múltiples PDFs de un folder de forma alfabética y luego enumerar todas las páginas del 1 a N con **color, alineación y fuente personalizables**.

## Características

- 🔢 **Ordenamiento inteligente**: Los PDFs se procesan según patrones inteligentes de nomenclatura (números, letras + números, etc.)
- 📑 **Mezclado automático**: Combina todos los PDFs en un solo documento
- 🎨 **Numeración personalizable**: 
  - **5 colores disponibles**: Rojo, Azul, Verde, Negro, Morado
  - **3 alineaciones**: Izquierda, Centro, Derecha  
  - **5 fuentes**: Helvetica, Helvetica-Bold, Times-Roman, Times-Bold, Courier
- ⚡ **Manejo robusto de errores**: Continúa el procesamiento aunque algunos PDFs tengan problemas
- 📊 **Progreso detallado**: Muestra el progreso del procesamiento y archivos problemáticos

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

```bash
python main.py
```

El script te guiará a través de las siguientes selecciones:

1. **Ruta del folder**: Especifica dónde están los PDFs
2. **Color del número**: Elige entre 5 colores (Rojo, Azul, Verde, Negro, Morado)
3. **Alineación**: Selecciona Izquierda, Centro o Derecha
4. **Fuente**: Escoge entre 5 fuentes diferentes

## Opciones de personalización

### Colores disponibles
1. **Rojo** (por defecto)
2. **Azul** 
3. **Verde**
4. **Negro**
5. **Morado**

### Alineaciones disponibles
1. **Izquierda** - Números en el borde izquierdo
2. **Centro** - Números centrados en la página
3. **Derecha** - Números en el borde derecho (por defecto)

### Fuentes disponibles
1. **Helvetica** - Fuente sans-serif normal
2. **Helvetica Bold** - Fuente sans-serif en negrita (por defecto)
3. **Times Roman** - Fuente serif clásica
4. **Times Bold** - Fuente serif en negrita
5. **Courier** - Fuente monoespaciada

## Funcionamiento

1. **Búsqueda**: El script busca todos los archivos `.pdf` en el folder especificado
2. **Ordenamiento**: Los archivos se ordenan usando patrones inteligentes de nomenclatura
3. **Personalización**: El usuario selecciona color, alineación y fuente
4. **Mezclado**: Se combinan todos los PDFs en un solo documento
5. **Numeración**: Se agregan números de página con la configuración elegida
6. **Guardado**: El resultado se guarda con un timestamp

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

Selecciona el color para los números de página:
  1. Rojo
  2. Azul
  3. Verde
  4. Negro
  5. Morado

Ingresa tu selección (1-5): 2
Color seleccionado: Azul

Selecciona la alineación para los números de página:
  1. Izquierda
  2. Centro
  3. Derecha

Ingresa tu selección (1-3): 2
Alineación seleccionada: Centro

Selecciona la fuente para los números de página:
  1. Helvetica (Normal)
  2. Helvetica Bold (Negrita)
  3. Times Roman
  4. Times Bold (Times Negrita)
  5. Courier (Monoespaciada)

Ingresa tu selección (1-5): 3
Fuente seleccionada: Times Roman

Archivos PDF encontrados y ordenados por nomenclatura:
  1. A1 VCT.pdf (clave: (1, 1, 1, 'a1 vct.pdf'))
  2. A2 VCT.pdf (clave: (1, 1, 2, 'a2 vct.pdf'))
  3. T1 Lista.pdf (clave: (1, 20, 1, 't1 lista.pdf'))

Mezclando PDFs...
  ✓ Agregado: A1 VCT.pdf (4 páginas)
  ✓ Agregado: A2 VCT.pdf (1 páginas)
  ✓ Agregado: T1 Lista.pdf (2 páginas)

✓ PDF mezclado guardado: merged_pdfs_20250825_143022.pdf
  Total de páginas: 7

Agregando números de página con configuración personalizada...
  Procesadas 7/7 páginas

✓ PDF con numeración completado: final_numbered_pdfs_20250825_143022.pdf

============================================================
   ¡PROCESO COMPLETADO EXITOSAMENTE!
============================================================
Archivo final: final_numbered_pdfs_20250825_143022.pdf
Total de páginas numeradas: 7
```

## Características técnicas

- **Tamaño de fuente**: 12pt (fijo)
- **Posición vertical**: 30px desde el borde inferior
- **Posición horizontal**: Configurable según alineación elegida
- **Manejo de PDFs encriptados**: Intenta procesar PDFs con protección básica
- **Manejo robusto de errores**: Usa `strict=False` para PDFs malformados
- **Preservación de calidad**: Mantiene la calidad original de los documentos
- **Limpieza automática**: Elimina archivos temporales después del procesamiento

## Patrones de ordenamiento soportados

El script reconoce automáticamente diferentes patrones de nomenclatura:
- **Número + punto**: `1. Documento.pdf`, `25. Archivo.pdf`
- **Letra + número**: `A1 Reporte.pdf`, `T10 Manual.pdf`
- **Solo letras**: `A Introducción.pdf`, `Z Conclusión.pdf`
- **Números en cualquier posición**: `Documento 15.pdf`

## Solución de problemas

- **"No se encontraron archivos PDF"**: Verifica que el folder contenga archivos .pdf
- **"Error procesando PDF"**: Algunos PDFs pueden estar corruptos o muy protegidos
- **"Selección inválida"**: Ingresa solo números dentro del rango especificado
- **Problemas de permisos**: Asegúrate de tener permisos de lectura en el folder de origen y escritura en el de destino

## Licencia

Este proyecto es de uso libre. Puedes modificarlo según tus necesidades.
