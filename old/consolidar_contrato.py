def consolidar_contrato():
    # Lista de archivos a consolidar
    archivos = [
        ("contrato_final.md", "PARTE GENERAL"),
        ("apendices_financieros.md", "APÉNDICES FINANCIEROS"),
        ("apendices_tecnicos.md", "APÉNDICES TÉCNICOS")
    ]
    
    # Contenido consolidado
    contenido_consolidado = []
    
    # Título principal
    contenido_consolidado.append("# CONTRATO DE CONCESIÓN COMPLETO")
    contenido_consolidado.append("## BAJO EL ESQUEMA DE APP")
    contenido_consolidado.append("")
    contenido_consolidado.append("**REPÚBLICA DE COLOMBIA**  ")
    contenido_consolidado.append("**MINISTERIO DE TRANSPORTE**  ")
    contenido_consolidado.append("**AGENCIA NACIONAL DE INFRAESTRUCTURA**")
    contenido_consolidado.append("")
    contenido_consolidado.append("---")
    contenido_consolidado.append("")
    
    # Tabla de contenido
    contenido_consolidado.append("## TABLA DE CONTENIDO")
    contenido_consolidado.append("")
    for i, (archivo, titulo) in enumerate(archivos, 1):
        contenido_consolidado.append(f"{i}. [{titulo}](#{titulo.lower().replace(' ', '-').replace('é', 'e').replace('í', 'i')})")
    contenido_consolidado.append("")
    contenido_consolidado.append("---")
    contenido_consolidado.append("")
    
    # Procesar cada archivo
    for archivo, titulo_seccion in archivos:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Agregar separador de sección
            contenido_consolidado.append(f"\n# {titulo_seccion}")
            contenido_consolidado.append("")
            contenido_consolidado.append("=" * 80)
            contenido_consolidado.append("")
            
            # Agregar contenido (saltando el primer título si existe)
            lineas = contenido.split('\n')
            saltear_primer_titulo = True
            
            for linea in lineas:
                if saltear_primer_titulo and linea.startswith('# '):
                    saltear_primer_titulo = False
                    continue
                contenido_consolidado.append(linea)
            
            contenido_consolidado.append("")
            contenido_consolidado.append("=" * 80)
            contenido_consolidado.append("")
            
        except FileNotFoundError:
            print(f"Advertencia: No se encontró el archivo {archivo}")
            contenido_consolidado.append(f"\n# {titulo_seccion}")
            contenido_consolidado.append("")
            contenido_consolidado.append("*Archivo no encontrado*")
            contenido_consolidado.append("")
    
    # Guardar archivo consolidado
    with open("contrato_completo.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(contenido_consolidado))
    
    print("Contrato completo consolidado en: contrato_completo.md")

if __name__ == "__main__":
    consolidar_contrato()