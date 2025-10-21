import re

def convert_to_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Limpiar el contenido
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('Página') and line != 'de 288':
            cleaned_lines.append(line)
    
    # Procesar el contenido
    markdown_content = []
    
    # Título principal
    markdown_content.append("# CONTRATO DE CONCESIÓN BAJO EL ESQUEMA DE APP")
    markdown_content.append("")
    markdown_content.append("**REPÚBLICA DE COLOMBIA**")
    markdown_content.append("**MINISTERIO DE TRANSPORTE**")
    markdown_content.append("**AGENCIA NACIONAL DE INFRAESTRUCTURA**")
    markdown_content.append("")
    
    # Procesar el resto del contenido
    in_definitions = False
    current_section = ""
    
    for line in cleaned_lines:
        # Detectar títulos de capítulos
        if re.match(r'CAPÍTULO\s+[IVX]+', line):
            markdown_content.append(f"\n## {line}")
            markdown_content.append("")
            in_definitions = True if "Definiciones" in line else False
            continue
        
        # Detectar definiciones numeradas
        if in_definitions and re.match(r'^\d+\.\d+\s+".*"', line):
            # Extraer número y término
            match = re.match(r'^(\d+\.\d+)\s+"([^"]+)"(.*)$', line)
            if match:
                num, term, rest = match.groups()
                markdown_content.append(f"### {num} {term}")
                if rest.strip():
                    markdown_content.append(rest.strip())
                markdown_content.append("")
            continue
        
        # Detectar secciones principales
        if line.isupper() and len(line) > 5:
            markdown_content.append(f"\n## {line}")
            markdown_content.append("")
            continue
        
        # Detectar subsecciones
        if line.endswith(':') and not line.startswith('Entre:'):
            markdown_content.append(f"\n### {line}")
            markdown_content.append("")
            continue
        
        # Líneas normales
        if line:
            markdown_content.append(line)
            markdown_content.append("")
    
    # Escribir el archivo markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"Archivo convertido a Markdown: {output_file}")

if __name__ == "__main__":
    convert_to_markdown("contrato_extraido.txt", "contrato.md")