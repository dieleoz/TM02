#!/usr/bin/env python3
"""
Script de Setup para Proyecto Real - Template TM02
Personaliza el template con datos del proyecto específico
"""

import os
import sys
import shutil
from datetime import datetime
import argparse

def setup_proyecto_real(nombre_proyecto, codigo_proyecto, cliente="", fecha_entrega=""):
    """
    Configura el template TM02 para un proyecto real específico
    """
    print(f"🚀 Configurando Template TM02 para: {nombre_proyecto}")
    
    # 1. Crear estructura personalizada
    crear_estructura_proyecto(nombre_proyecto, codigo_proyecto)
    
    # 2. Personalizar plantillas
    personalizar_plantillas(nombre_proyecto, codigo_proyecto, cliente)
    
    # 3. Configurar scripts
    configurar_scripts(codigo_proyecto)
    
    # 4. Generar documentos iniciales
    generar_documentos_iniciales(nombre_proyecto, codigo_proyecto, cliente, fecha_entrega)
    
    # 5. Limpiar ejemplos
    limpiar_ejemplos()
    
    print("✅ Setup completado exitosamente!")
    print(f"📁 Proyecto configurado: {nombre_proyecto}")
    print("🎯 Próximo paso: Cargar contratos en carpetas I. y II.")

def crear_estructura_proyecto(nombre, codigo):
    """Crea estructura de carpetas personalizada"""
    carpetas = [
        f"I. Contratos Base - {codigo}/",
        f"II. Contratos Anexos - {codigo}/", 
        f"III. Ingenieria Conceptual - {nombre}/",
        f"VII. Documentos Transversales - {codigo}/",
        f"ENTREGABLES - {codigo}/"
    ]
    
    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)
        print(f"📁 Creada: {carpeta}")

def personalizar_plantillas(nombre, codigo, cliente):
    """Personaliza plantillas con datos del proyecto"""
    plantillas = [
        "templates/PLANTILLA_T01_FICHA_SISTEMA.md",
        "templates/PLANTILLA_T02_ANALISIS_REQUISITOS.md", 
        "templates/PLANTILLA_T03_ARQUITECTURA_SISTEMA.md",
        "templates/PLANTILLA_T04_ESTIMACION_COSTOS.md"
    ]
    
    for plantilla in plantillas:
        if os.path.exists(plantilla):
            personalizar_archivo(plantilla, nombre, codigo, cliente)

def personalizar_archivo(archivo, nombre, codigo, cliente):
    """Reemplaza placeholders en archivo con datos reales"""
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Reemplazos
    contenido = contenido.replace("[NOMBRE_PROYECTO]", nombre)
    contenido = contenido.replace("[CODIGO_PROYECTO]", codigo)
    contenido = contenido.replace("[CLIENTE]", cliente)
    contenido = contenido.replace("[FECHA_HOY]", datetime.now().strftime("%Y-%m-%d"))
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print(f"✏️  Personalizado: {archivo}")

def configurar_scripts(codigo):
    """Configura scripts con código del proyecto"""
    config_file = f"scripts/config_{codigo}.py"
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(f"""# Configuración del Proyecto {codigo}
CODIGO_PROYECTO = "{codigo}"
CARPETA_CONTRATOS = "I. Contratos Base - {codigo}/"
CARPETA_ANEXOS = "II. Contratos Anexos - {codigo}/"
CARPETA_ENTREGABLES = "ENTREGABLES - {codigo}/"
""")
    print(f"⚙️  Configurado: {config_file}")

def generar_documentos_iniciales(nombre, codigo, cliente, fecha_entrega):
    """Genera documentos iniciales del proyecto"""
    
    # Plan de trabajo
    plan_trabajo = f"""# 📋 PLAN DE TRABAJO - {nombre}

## 📊 INFORMACIÓN DEL PROYECTO
- **Proyecto**: {nombre}
- **Código**: {codigo}
- **Cliente**: {cliente}
- **Fecha Inicio**: {datetime.now().strftime("%Y-%m-%d")}
- **Fecha Entrega IC**: {fecha_entrega}
- **Metodología**: Punto 42 TM02

## 🎯 OBJETIVOS
- [ ] Ingeniería conceptual completa en 5 días
- [ ] Documentación sistemática y trazable
- [ ] Identificación temprana de riesgos
- [ ] Estimaciones precisas de costos y tiempos

## 📅 CRONOGRAMA
- **Día 1**: Setup y carga de contratos
- **Día 2**: Validación y extracción de metadatos  
- **Día 3-4**: Análisis de sistemas y requisitos
- **Día 5**: Consolidación y entrega

## 📋 ENTREGABLES
- [ ] Fichas de sistemas (T01)
- [ ] Análisis de requisitos (T02)
- [ ] Arquitectura de sistemas (T03)
- [ ] Estimaciones de costos (T04)
- [ ] Documentos consolidados
"""
    
    with open(f"PLAN_TRABAJO_{codigo}.md", 'w', encoding='utf-8') as f:
        f.write(plan_trabajo)
    
    print(f"📋 Generado: PLAN_TRABAJO_{codigo}.md")

def limpiar_ejemplos():
    """Limpia archivos de ejemplo que no se necesitan"""
    if os.path.exists("0.0 REFERENCIA_TM01/"):
        shutil.rmtree("0.0 REFERENCIA_TM01/")
        print("🧹 Limpiado: Carpeta de referencia TM01")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Setup Template TM02 para proyecto real')
    parser.add_argument('--nombre', required=True, help='Nombre del proyecto')
    parser.add_argument('--codigo', required=True, help='Código del proyecto')
    parser.add_argument('--cliente', default='', help='Nombre del cliente')
    parser.add_argument('--fecha-entrega', default='', help='Fecha de entrega (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    setup_proyecto_real(
        args.nombre, 
        args.codigo, 
        args.cliente, 
        args.fecha_entrega
    )