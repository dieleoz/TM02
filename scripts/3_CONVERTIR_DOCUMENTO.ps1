# Script para convertir un documento individual a Markdown
# Proyecto APP - Nuevo Contrato Vial
# Fecha: 21/10/2025

param(
    [Parameter(Mandatory=$true)]
    [string]$ArchivoOrigen,
    
    [Parameter(Mandatory=$false)]
    [string]$ArchivoDestino = "",
    
    [Parameter(Mandatory=$false)]
    [string]$Carpeta = "II. Apendices Tecnicos"
)

Write-Host "=== CONVERSIÓN DE DOCUMENTO INDIVIDUAL ===" -ForegroundColor Green

# Verificar si Pandoc está instalado
if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Pandoc no está instalado" -ForegroundColor Red
    Write-Host "Instalar con: winget install Pandoc" -ForegroundColor Yellow
    exit 1
}

# Verificar que existe el archivo origen
if (-not (Test-Path $ArchivoOrigen)) {
    Write-Host "ERROR: No se encuentra el archivo '$ArchivoOrigen'" -ForegroundColor Red
    exit 1
}

$archivo = Get-Item $ArchivoOrigen
Write-Host "Procesando: $($archivo.Name)" -ForegroundColor Cyan

# Crear carpeta de destino si no existe
if (-not (Test-Path $Carpeta)) {
    New-Item -ItemType Directory -Path $Carpeta -Force
    Write-Host "Creada carpeta: $Carpeta" -ForegroundColor Green
}

# Generar nombre de archivo de salida si no se especificó
if ($ArchivoDestino -eq "") {
    $nombreBase = [System.IO.Path]::GetFileNameWithoutExtension($archivo.Name)
    $ArchivoDestino = "$nombreBase" + "_v1.0.md"
}

$rutaSalida = Join-Path $Carpeta $ArchivoDestino

Write-Host "Archivo destino: $rutaSalida" -ForegroundColor Yellow

try {
    # Convertir según el tipo de archivo
    switch ($archivo.Extension.ToLower()) {
        ".txt" {
            Write-Host "Convirtiendo archivo TXT..." -ForegroundColor Yellow
            pandoc "$($archivo.FullName)" -f plain -t markdown --wrap=none -o "$rutaSalida"
        }
        ".pdf" {
            Write-Host "ERROR: Conversión PDF no soportada directamente" -ForegroundColor Red
            Write-Host "Recomendación:" -ForegroundColor Yellow
            Write-Host "1. Usar OCR para convertir PDF a TXT" -ForegroundColor White
            Write-Host "2. Luego ejecutar este script con el archivo TXT" -ForegroundColor White
            exit 1
        }
        ".docx" {
            Write-Host "Convirtiendo archivo DOCX..." -ForegroundColor Yellow
            pandoc "$($archivo.FullName)" -f docx -t markdown --wrap=none -o "$rutaSalida"
        }
        ".md" {
            Write-Host "Copiando archivo Markdown..." -ForegroundColor Yellow
            Copy-Item $archivo.FullName $rutaSalida
        }
        default {
            Write-Host "ERROR: Formato no soportado: $($archivo.Extension)" -ForegroundColor Red
            Write-Host "Formatos soportados: .txt, .docx, .md" -ForegroundColor Yellow
            exit 1
        }
    }
    
    # Verificar que se creó el archivo
    if (Test-Path $rutaSalida) {
        # Agregar encabezado Punto 42
        $contenidoOriginal = Get-Content $rutaSalida -Raw -Encoding UTF8
        $nombreBase = [System.IO.Path]::GetFileNameWithoutExtension($archivo.Name)
        
        $encabezado = @"
# $nombreBase
## Proyecto APP [NOMBRE_PROYECTO]

**Fecha de conversión:** $(Get-Date -Format "dd/MM/yyyy HH:mm")  
**Archivo origen:** $($archivo.Name)  
**Versión:** 1.0  
**Estado:** ✅ Convertido a Markdown  
**Metodología:** Punto 42 v1.0  

---

$contenidoOriginal
"@
        $encabezado | Out-File -FilePath $rutaSalida -Encoding UTF8
        
        Write-Host "✅ Conversión exitosa" -ForegroundColor Green
        Write-Host "Archivo creado: $rutaSalida" -ForegroundColor Green
        
        # Mostrar estadísticas del archivo
        $lineas = (Get-Content $rutaSalida).Count
        $tamaño = (Get-Item $rutaSalida).Length
        Write-Host "Líneas: $lineas" -ForegroundColor White
        Write-Host "Tamaño: $([math]::Round($tamaño/1KB, 2)) KB" -ForegroundColor White
        
        # Sugerencias de próximos pasos
        Write-Host "`nPróximos pasos:" -ForegroundColor Yellow
        if ($nombreBase -match "AT1|Apendice.*1|Alcance") {
            Write-Host "🔥 CRÍTICO: Este parece ser AT1 (Apéndice Técnico 1)" -ForegroundColor Red
            Write-Host "1. Leer completamente para identificar sistemas obligatorios" -ForegroundColor White
            Write-Host "2. Extraer cantidades literales con número de página" -ForegroundColor White
            Write-Host "3. Crear matriz de requisitos contractuales" -ForegroundColor White
            Write-Host "4. Aplicar metodología de validación (5 fases)" -ForegroundColor White
        } else {
            Write-Host "1. Revisar formato y contenido" -ForegroundColor White
            Write-Host "2. Corregir errores de conversión si los hay" -ForegroundColor White
            Write-Host "3. Identificar información relevante para el proyecto" -ForegroundColor White
        }
        
    } else {
        Write-Host "❌ Error: No se pudo crear el archivo de destino" -ForegroundColor Red
        exit 1
    }
}
catch {
    Write-Host "❌ Error durante la conversión: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host "`n=== CONVERSIÓN COMPLETADA ===" -ForegroundColor Green

# Ejemplos de uso
Write-Host "`nEjemplos de uso:" -ForegroundColor Yellow
Write-Host ".\3_CONVERTIR_DOCUMENTO.ps1 -ArchivoOrigen 'archivo.txt'" -ForegroundColor Cyan
Write-Host ".\3_CONVERTIR_DOCUMENTO.ps1 -ArchivoOrigen 'AT1.docx' -Carpeta 'II. Apendices Tecnicos'" -ForegroundColor Cyan
Write-Host ".\3_CONVERTIR_DOCUMENTO.ps1 -ArchivoOrigen 'contrato.txt' -ArchivoDestino 'Contrato_Principal_v1.0.md'" -ForegroundColor Cyan