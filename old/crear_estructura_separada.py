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
        if line and not re.match(r'^Página \d+ de \d+$', line):
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
        
        # Detectar títulos de capítulos
        if (re.match(r'CAPÍTULO\s+[IVX]+', line) or 
            re.match(r'APÉNDICE\s+', line)):
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

def crear_estructura_separada():
    # 1. Crear Parte General (ya tenemos contrato_final.md)
    print("1. Creando 1_Parte_General_v1.0.md...")
    try:
        with open("contrato_final.md", 'r', encoding='utf-8') as f:
            contenido_general = f.read()
        
        with open("1_Parte_General_v1.0.md", 'w', encoding='utf-8') as f:
            f.write(contenido_general)
        print("✓ 1_Parte_General_v1.0.md creado")
    except:
        print("✗ Error creando Parte General")
    
    # 2. Crear Parte Especial (del segundo PDF)
    print("2. Procesando Parte Especial...")
    pdf_especial = "0.0 contrrato en pdf/5 ANEXO 1 - PARTE ESPECIAL CONCESIÓN 2 - ADENDA 7 SIN MARCAS.pdf"
    
    if os.path.exists(pdf_especial):
        text = extract_text_from_pdf(pdf_especial)
        if text:
            markdown_content = clean_and_convert_to_markdown(text, "PARTE ESPECIAL - CONCESIÓN")
            with open("2_Parte_Especial_v1.0.md", 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print("✓ 2_Parte_Especial_v1.0.md creado")
        else:
            print("✗ Error extrayendo texto de Parte Especial")
    else:
        print("✗ No se encontró el PDF de Parte Especial")
    
    # 3. Crear Apéndices Financieros individuales
    print("3. Creando Apéndices Financieros individuales...")
    financieros_dir = "0.0 contrrato en pdf/Apéndices Financieros"
    
    apendices_financieros = {
        "Apendice Financiero 1 INFORMACION FINANCIERA.pdf": "AF1_Informacion_Financiera_v1.0.md",
        "Apendice Financiero 2 CESION ESPECIAL DE LA RETRIBUCION.pdf": "AF2_Cesion_Especial_Retribucion_v1.0.md",
        "Apendice Financiero 3 PORTADA.pdf": "AF3_Polizas_Portada_v1.0.md",
        "Apendice Financiero 3.1 POLIZA DE CUMPLIMIENTO.pdf": "AF3.1_Poliza_Cumplimiento_v1.0.md",
        "Apendice Financiero 3.2 POLIZA RESPONSABILIDAD CIVIL.pdf": "AF3.2_Poliza_Responsabilidad_Civil_v1.0.md",
        "Apendice Financiero 3.3 POLIZA OBRAS CIVILES.pdf": "AF3.3_Poliza_Obras_Civiles_v1.0.md"
    }
    
    for pdf_file, md_file in apendices_financieros.items():
        pdf_path = os.path.join(financieros_dir, pdf_file)
        if os.path.exists(pdf_path):
            text = extract_text_from_pdf(pdf_path)
            if text:
                title = pdf_file.replace('.pdf', '').replace('_', ' ').upper()
                markdown_content = clean_and_convert_to_markdown(text, title)
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                print(f"✓ {md_file} creado")
            else:
                print(f"✗ Error extrayendo texto de {pdf_file}")
        else:
            print(f"✗ No se encontró {pdf_file}")
    
    # 4. Crear Apéndices Técnicos individuales
    print("4. Creando Apéndices Técnicos individuales...")
    tecnicos_dir = "0.0 contrrato en pdf/Apéndices Técnicos"
    
    apendices_tecnicos = {
        "1. AP1 _Alcance C2_.pdf": "AT1_Alcance_Proyecto_v1.0.md",
        "2. AP2 - Condiciones para la operación y mantenimiento C2.pdf": "AT2_Operacion_Mantenimiento_v1.0.md",
        "3. AP3 - Especificaciones Generales C2.pdf": "AT3_Especificaciones_Generales_v1.0.md",
        "3.1 AP3-Anexo.  Plan Gestión Riesgo Desastres.pdf": "AT3_Anexo_Plan_Gestion_Riesgo_Desastres_v1.0.md",
        "4. AP4 - Indicadores C2.pdf": "AT4_Indicadores_v1.0.md",
        "5. AP 5 Interferencia de Redes.pdf": "AT5_Interferencia_Redes_v1.0.md",
        "6. AP6- Apéndice Ambiental C2.pdf": "AT6_Gestion_Ambiental_v1.0.md",
        "7. AP7 - Gestión Predial.pdf": "AT7_Gestion_Predial_v1.0.md",
        "7.2 Anexo2_plano_predial_AT7.pdf": "AT7_Anexo2_Plano_Predial_v1.0.md",
        "8. AP8 - Gestión Social.pdf": "AT8_Gestion_Social_v1.0.md",
        "9. AP9 -   Plan de Obra.pdf": "AT9_Plan_Obra_v1.0.md"
    }
    
    for pdf_file, md_file in apendices_tecnicos.items():
        pdf_path = os.path.join(tecnicos_dir, pdf_file)
        if os.path.exists(pdf_path):
            text = extract_text_from_pdf(pdf_path)
            if text:
                title = pdf_file.replace('.pdf', '').replace('_', ' ').upper()
                markdown_content = clean_and_convert_to_markdown(text, title)
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                print(f"✓ {md_file} creado")
            else:
                print(f"✗ Error extrayendo texto de {pdf_file}")
        else:
            print(f"✗ No se encontró {pdf_file}")
    
    print("\n¡Estructura separada creada exitosamente!")

if __name__ == "__main__":
    crear_estructura_separada()