import PyPDF2
import os
import re

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n\n"
            
            return text
    except Exception as e:
        print(f"Error al leer {pdf_path}: {e}")
        return None

def clean_and_convert_to_markdown(text, title):
    if not text:
        return ""
    
    # Limpiar el contenido
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        # Filtrar líneas de página y líneas vacías
        if line and not re.match(r'^Página \d+ de \d+$', line):
            # Limpiar puntos de relleno y números de página al final
            clean_line = re.sub(r'\.{2,}\s*\d*$', '', line).strip()
            if clean_line:
                cleaned_lines.append(clean_line)
    
    # Procesar el contenido
    markdown_content = []
    markdown_content.append(f"# {title}")
    markdown_content.append("")
    markdown_content.append("---")
    markdown_content.append("")
    
    i = 0
    while i < len(cleaned_lines):
        line = cleaned_lines[i]
        
        # Saltar encabezados repetitivos
        if any(header in line for header in ["REPÚBLICA DE COLOMBIA", "MINISTERIO DE TRANSPORTE", "AGENCIA NACIONAL DE INFRAESTRUCTURA"]):
            i += 1
            continue
        
        # Detectar títulos de capítulos y apéndices
        if (re.match(r'CAPÍTULO\s+[IVX]+', line) or 
            re.match(r'APÉNDICE\s+', line) or
            re.match(r'AP\d+', line)):
            markdown_content.append(f"\n## {line}")
            markdown_content.append("")
            i += 1
            continue
        
        # Detectar definiciones numeradas con comillas
        if re.match(r'^\d+\.\d+\s+".*"', line):
            match = re.match(r'^(\d+\.\d+)\s+"([^"]+)"(.*)$', line)
            if match:
                num, term, rest = match.groups()
                markdown_content.append(f"### {num} {term}")
                if rest.strip():
                    markdown_content.append(f"{rest.strip()}")
                markdown_content.append("")
            i += 1
            continue
        
        # Detectar numeración de secciones
        if re.match(r'^\d+\.\s+[A-Z]', line):
            markdown_content.append(f"\n### {line}")
            markdown_content.append("")
            i += 1
            continue
        
        # Detectar secciones principales (todo en mayúsculas)
        if line.isupper() and len(line) > 3 and not re.match(r'^\d+\.\d+', line):
            markdown_content.append(f"\n## {line}")
            markdown_content.append("")
            i += 1
            continue
        
        # Detectar subsecciones que terminan en ":"
        if line.endswith(':'):
            markdown_content.append(f"\n### {line}")
            markdown_content.append("")
            i += 1
            continue
        
        # Líneas normales
        if line:
            markdown_content.append(line)
            markdown_content.append("")
        
        i += 1
    
    return '\n'.join(markdown_content)

def process_apendices_tecnicos():
    # Directorio de apéndices técnicos
    tecnicos_dir = "0.0 contrrato en pdf/Apéndices Técnicos"
    
    # Obtener solo los archivos PDF
    pdf_files = []
    for file in os.listdir(tecnicos_dir):
        if file.endswith('.pdf'):
            pdf_files.append(os.path.join(tecnicos_dir, file))
    
    # Procesar cada PDF
    all_content = []
    all_content.append("# APÉNDICES TÉCNICOS - CONTRATO DE CONCESIÓN")
    all_content.append("")
    all_content.append("---")
    all_content.append("")
    
    for pdf_file in sorted(pdf_files):
        print(f"Procesando: {pdf_file}")
        
        # Extraer nombre del archivo para el título
        filename = os.path.basename(pdf_file)
        title = filename.replace('.pdf', '').replace('_', ' ').upper()
        
        # Extraer texto
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            # Convertir a markdown
            markdown_content = clean_and_convert_to_markdown(text, title)
            all_content.append(markdown_content)
            all_content.append("\n---\n")
        else:
            all_content.append(f"# {title}")
            all_content.append("*Error: No se pudo extraer texto de este archivo*")
            all_content.append("\n---\n")
    
    # Guardar todo en un archivo
    output_file = "apendices_tecnicos.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_content))
    
    print(f"\nTodos los apéndices técnicos convertidos a: {output_file}")

if __name__ == "__main__":
    process_apendices_tecnicos()