import PyPDF2
import sys
import os

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
        print(f"Error al leer el PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_file = "0.0 contrrato en pdf/3 PARTE GENERAL PUBLICAS TRONCAL SIN MARCAS ADENDA 7.pdf"
    
    if os.path.exists(pdf_file):
        print("Extrayendo texto del PDF...")
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            # Guardar como .txt
            txt_file = "contrato_extraido.txt"
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Texto extraído y guardado en: {txt_file}")
            
            # Mostrar las primeras líneas
            lines = text.split('\n')[:20]
            print("\nPrimeras líneas del texto extraído:")
            print("-" * 50)
            for line in lines:
                if line.strip():
                    print(line.strip())
        else:
            print("No se pudo extraer texto del PDF")
    else:
        print(f"No se encontró el archivo: {pdf_file}")