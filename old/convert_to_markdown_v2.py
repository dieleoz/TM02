import re

def convert_to_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Limpiar el contenido
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        # Filtrar líneas de página y líneas vacías
        if line and not re.match(r'^Página \d+ de \d+$', line):
            cleaned_lines.append(line)
    
    # Procesar el contenido
    markdown_content = []
    
    # Título principal
    markdown_content.append("# CONTRATO DE CONCESIÓN BAJO EL ESQUEMA DE APP")
    markdown_content.append("")
    markdown_content.append("**REPÚBLICA DE COLOMBIA**  ")
    markdown_content.append("**MINISTERIO DE TRANSPORTE**  ")
    markdown_content.append("**AGENCIA NACIONAL DE INFRAESTRUCTURA**")
    markdown_content.append("")
    markdown_content.append("---")
    markdown_content.append("")
    
    skip_next = False
    i = 0
    
    while i < len(cleaned_lines):
        line = cleaned_lines[i]
        
        if skip_next:
            skip_next = False
            i += 1
            continue
        
        # Saltar líneas ya procesadas en el encabezado
        if any(header in line for header in ["REPÚBLICA DE COLOMBIA", "MINISTERIO DE TRANSPORTE", "AGENCIA NACIONAL DE INFRAESTRUCTURA"]):
            i += 1
            continue
        
        # Detectar títulos de capítulos
        if re.match(r'CAPÍTULO\s+[IVX]+', line):
            # Limpiar la línea de puntos y números de página
            clean_title = re.sub(r'\.+\s*\d+$', '', line).strip()
            markdown_content.append(f"\n## {clean_title}")
            markdown_content.append("")
            i += 1
            continue
        
        # Detectar definiciones numeradas con comillas
        if re.match(r'^\d+\.\d+\s+".*"', line):
            # Limpiar la línea de puntos y números de página
            clean_def = re.sub(r'\.+\s*\d+$', '', line).strip()
            match = re.match(r'^(\d+\.\d+)\s+"([^"]+)"(.*)$', clean_def)
            if match:
                num, term, rest = match.groups()
                markdown_content.append(f"### {num} {term}")
                if rest.strip():
                    markdown_content.append(f"{rest.strip()}")
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
        if line.endswith(':') and not line.startswith('Entre:'):
            markdown_content.append(f"\n### {line}")
            markdown_content.append("")
            i += 1
            continue
        
        # Líneas normales
        if line:
            # Limpiar puntos de relleno y números de página
            clean_line = re.sub(r'\.{3,}\s*\d+$', '', line).strip()
            if clean_line:
                markdown_content.append(clean_line)
                markdown_content.append("")
        
        i += 1
    
    # Escribir el archivo markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"Archivo convertido a Markdown: {output_file}")

if __name__ == "__main__":
    convert_to_markdown("contrato_extraido.txt", "contrato_v2.md")