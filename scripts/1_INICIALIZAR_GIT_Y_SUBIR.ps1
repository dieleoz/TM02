# Script para inicializar Git y subir cambios
# Proyecto APP - Nuevo Contrato Vial
# Fecha: 21/10/2025

Write-Host "=== INICIALIZANDO GIT Y SUBIENDO CAMBIOS ===" -ForegroundColor Green

# Verificar si Git está instalado
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Git no está instalado o no está en el PATH" -ForegroundColor Red
    exit 1
}

# Verificar si estamos en un repositorio Git
if (-not (Test-Path ".git")) {
    Write-Host "Inicializando repositorio Git..." -ForegroundColor Yellow
    git init
    
    # Crear .gitignore básico
    @"
# Archivos temporales
*.tmp
*.temp
~*
.DS_Store
Thumbs.db

# Archivos de Office
*.docx
*.xlsx
*.pptx

# Archivos de backup
*.bak
*.backup
*~

# Carpetas de sistema
.vscode/
.idea/

# Archivos grandes (>100MB)
*.zip
*.rar
*.7z
*.iso

# Logs
*.log
logs/

# Archivos de configuración local
config.local.*
settings.local.*
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
    
    Write-Host "Repositorio Git inicializado" -ForegroundColor Green
}

# Agregar todos los archivos
Write-Host "Agregando archivos al staging..." -ForegroundColor Yellow
git add .

# Verificar el estado
Write-Host "Estado del repositorio:" -ForegroundColor Yellow
git status

# Crear commit con timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$commitMessage = "Actualización proyecto - $timestamp"

Write-Host "Creando commit: $commitMessage" -ForegroundColor Yellow
git commit -m "$commitMessage"

# Verificar si hay un remote configurado
$remotes = git remote
if ($remotes) {
    Write-Host "Remotes configurados:" -ForegroundColor Yellow
    git remote -v
    
    # Preguntar si quiere hacer push
    $push = Read-Host "¿Desea hacer push al repositorio remoto? (y/n)"
    if ($push -eq "y" -or $push -eq "Y") {
        Write-Host "Haciendo push..." -ForegroundColor Yellow
        git push
        Write-Host "Push completado" -ForegroundColor Green
    }
} else {
    Write-Host "No hay remotes configurados. Para configurar un remote:" -ForegroundColor Yellow
    Write-Host "git remote add origin <URL_DEL_REPOSITORIO>" -ForegroundColor Cyan
    Write-Host "git push -u origin main" -ForegroundColor Cyan
}

Write-Host "=== PROCESO COMPLETADO ===" -ForegroundColor Green
Write-Host "Archivos agregados y commit creado exitosamente" -ForegroundColor Green

# Mostrar log reciente
Write-Host "`nÚltimos commits:" -ForegroundColor Yellow
git log --oneline -5