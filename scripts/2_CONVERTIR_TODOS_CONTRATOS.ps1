# Script para convertir todos los contratos PDF/TXT a Markdown
# Proyecto APP - Nuevo Contrato Vial
# Fecha: 21/10/2025

Write-Host "=== CONVERSIÓN MASIVA DE CONTRATOS ===" -ForegroundColor Green

# Verificar si Pandoc está instalado
if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Pandoc no está instalado" -ForegroundColor Red
    Write-Host "Instalar con: winget install Pandoc" -ForegroundColor Yellow
    exit 1
}

# Carpetas de origen y destino
$carpetaOrigen = "0.0 contrrato en pdf"
$carpetaContrato = "I. Contrato General"
$carpetaApendices = "II. Apendices Tecnicos"

Write-Host "Buscando archivos en: $carpetaOrigen" -ForegroundColor Yellow

# Verificar que existe la carpeta de origen
if (-not (Test-Path $carpetaOrigen)) {
    Write-Host "ERROR: No se encuentra la carpeta '$carpetaOrigen'" -ForegroundColor Red
    Write-Host "Crear la carpeta y colocar los archivos PDF/TXT del contrato" -ForegroundColor Yellow
    exit 1
}

# Crear carpetas de destino si no existen
if (-not (Test-Path $carpetaContrato)) {
    New-Item -ItemType Directory -Path $carpetaContrato -Force
    Write-Host "Creada carpeta: $carpetaContrato" -ForegroundColor Green
}

if (-not (Test-Path $carpetaApendices)) {
    New-Item -ItemType Directory -Path $carpetaApendices -Force
    Write-Host "Creada carpeta: $carpetaApendices" -ForegroundColor Green
}

# Buscar archivos para convertir
$archivos = Get-ChildItem -Path $carpetaOrigen -Include "*.txt", "*.pdf", "*.docx" -Recurse

if ($archivos.Count -eq 0) {
    Write-Host "No se encontraron archivos para convertir en '$carpetaOrigen'" -ForegroundColor Yellow
    Write-Host "Formatos soportados: .txt, .pdf, .docx" -ForegroundColor Yellow
    exit 0
}

Write-Host "Encontrados $($archivos.Count) archivos para convertir" -ForegroundColor Green

$convertidos = 0
$errores = 0

foreach ($archivo in $archivos) {
    Write-Host "`nProcesando: $($archivo.Name)" -ForegroundColor Cyan
    
    # Determinar carpeta de destino basado en el nombre
    $carpetaDestino = $carpetaApendices
    if ($archivo.Name -match "parte.*general|contrato.*general|general") {
        $carpetaDestino = $carpetaContrato
    } elseif ($archivo.Name -match "parte.*especial|contrato.*especial|especial") {
        $carpetaDestino = $carpetaContrato
    }
    
    # Generar nombre de archivo de salida
    $nombreBase = [System.IO.Path]::GetFileNameWithoutExtension($archivo.Name)
    $nombreSalida = "$nombreBase" + "_v1.0.md"
    $rutaSalida = Join-Path $carpetaDestino $nombreSalida
    
    try {
        # Convertir según el tipo de archivo
        switch ($archivo.Extension.ToLower()) {
            ".txt" {
                # Para archivos TXT, usar pandoc con formato mejorado
                pandoc "$($archivo.FullName)" -f plain -t markdown --wrap=none -o "$rutaSalida"
            }
            ".pdf" {
                Write-Host "  ADVERTENCIA: Conversión PDF requiere OCR manual" -ForegroundColor Yellow
                Write-Host "  Recomendación: Convertir PDF a TXT primero" -ForegroundColor Yellow
                continue
            }
            ".docx" {
                # Para archivos DOCX
                pandoc "$($archivo.FullName)" -f docx -t markdown --wrap=none -o "$rutaSalida"
            }
        }
        
        # Verificar que se creó el archivo
        if (Test-Path $rutaSalida) {
            # Agregar encabezado Punto 42
            $contenidoOriginal = Get-Content $rutaSalida -Raw -Encoding UTF8
            $encabezado = @"
# $nombreBase
## Proyecto APP [NOMBRE_PROYECTO]

**Fecha de conversión:** $(Get-Date -Format "dd/MM/yyyy")  
**Archivo origen:** $($archivo.Name)  
**Versión:** 1.0  
**Estado:** ✅ Convertido a Markdown  

---

$contenidoOriginal
"@
            $encabezado | Out-File -FilePath $rutaSalida -Encoding UTF8
            
            Write-Host "  ✅ Convertido: $nombreSalida" -ForegroundColor Green
            $convertidos++
        } else {
            Write-Host "  ❌ Error: No se pudo crear el archivo" -ForegroundColor Red
            $errores++
        }
    }
    catch {
        Write-Host "  ❌ Error al convertir: $($_.Exception.Message)" -ForegroundColor Red
        $errores++
    }
}

# Resumen final
Write-Host "`n=== RESUMEN DE CONVERSIÓN ===" -ForegroundColor Green
Write-Host "Archivos procesados: $($archivos.Count)" -ForegroundColor White
Write-Host "Convertidos exitosamente: $convertidos" -ForegroundColor Green
Write-Host "Errores: $errores" -ForegroundColor Red

if ($convertidos -gt 0) {
    Write-Host "`nArchivos convertidos guardados en:" -ForegroundColor Yellow
    Write-Host "- $carpetaContrato" -ForegroundColor Cyan
    Write-Host "- $carpetaApendices" -ForegroundColor Cyan
    
    Write-Host "`nPróximos pasos:" -ForegroundColor Yellow
    Write-Host "1. Revisar archivos convertidos manualmente" -ForegroundColor White
    Write-Host "2. Corregir formato si es necesario" -ForegroundColor White
    Write-Host "3. Ejecutar análisis de AT1 (Apéndice Técnico 1)" -ForegroundColor White
    Write-Host "4. Iniciar Fase 1: Análisis Contractual" -ForegroundColor White
}

Write-Host "`n=== CONVERSIÓN COMPLETADA ===" -ForegroundColor Green