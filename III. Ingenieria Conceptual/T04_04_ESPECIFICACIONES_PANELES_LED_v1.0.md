# T04_04: ESPECIFICACIONES TÉCNICAS - PANELES LED DE MENSAJE VARIABLE
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Paneles LED de Mensaje Variable  
**Responsable:** Ingeniero de Sistemas ITS  
**Versión:** 1.0  
**Referencia T01:** T01_04_FICHA_SISTEMA_PANELES_LED_v1.0.md  
**Referencia T03:** T03_04_ARQUITECTURA_PANELES_LED_v1.0.md  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | 21/10/2025 | Creación inicial | Ingeniero de Sistemas ITS |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | Paneles LED de Mensaje Variable (PMV) |
| **Categoría** | ITS - Información al Usuario |
| **Código interno** | T04-04-v1.0 |
| **Cantidad total** | 18 paneles principales + 8 auxiliares |
| **CAPEX estimado** | USD $1,950,000 |
| **Documentos base** | T01_04, T02_04, T03_04, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Paneles LED de mensaje variable
- ✅ Sistemas de control y comunicación
- ✅ Estructuras de soporte y montaje
- ✅ Software de gestión de mensajes
- ✅ Sistemas de monitoreo y diagnóstico

**Este documento NO especifica:**
- ❌ Cimentaciones y obras civiles (ver T05)
- ❌ Acometidas eléctricas principales (ver T05)
- ❌ Integración con sistemas de tráfico (ver T04_02)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 4.3.2 | PMV en puntos estratégicos |
| **Apéndice Técnico 2** | 2.5.1 | Disponibilidad mínima 99% |
| **Apéndice Técnico 3** | 3.1.4 | Control remoto desde CCO |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **Manual de Señalización Vial** | INVIAS 2015 | Diseño y ubicación |
| **RETIE** | Reglamento Técnico Instalaciones Eléctricas | Instalaciones eléctricas |
| **Resolución 1885/2015** | Señalización vial | Especificaciones técnicas |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **NTCIP 1203** | Dynamic Message Signs | Protocolo de comunicación |
| **AASHTO** | Standard Specifications for Structural Supports | Estructuras de soporte |
| **IES RP-16** | Nomenclature and Definitions for Illuminating Engineering | Fotometría |### 2.
3 Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **Certificación NTCIP** | ITE | ✅ Sí | Protocolo de comunicación |
| **Certificación FCC** | FCC | ✅ Sí | Emisiones electromagnéticas |
| **Certificación CE** | Organismo Notificado | ✅ Sí | Compatibilidad electromagnética |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Clasificación de Paneles

#### 3.1.1 Paneles Principales (Tipo A)

**Ubicación:** Puntos estratégicos de información
**Características:**
- Tamaño: 4.0 x 2.0 metros
- Resolución: 160 x 80 píxeles
- Distancia de lectura: 800 metros
- Aplicación: Información general de tráfico

#### 3.1.2 Paneles Auxiliares (Tipo B)

**Ubicación:** Aproximaciones a peajes y salidas
**Características:**
- Tamaño: 2.4 x 1.2 metros
- Resolución: 96 x 48 píxeles
- Distancia de lectura: 400 metros
- Aplicación: Información específica de carriles

### 3.2 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura operación** | -20°C a +70°C | IEC 60068 |
| **Humedad relativa** | 0-95% sin condensación | IEC 60068 |
| **Protección IP** | IP65 frontal, IP54 posterior | IEC 60529 |
| **Resistencia a viento** | 200 km/h | AASHTO |
| **Resistencia UV** | Sin degradación 10 años | ASTM G154 |

### 3.3 Requisitos Ópticos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Luminancia mínima** | 8,000 cd/m² (día) | NTCIP 1203 |
| **Luminancia máxima** | 12,000 cd/m² | NTCIP 1203 |
| **Luminancia nocturna** | 200-800 cd/m² | NTCIP 1203 |
| **Uniformidad** | >80% | IES RP-16 |
| **Ángulo de visión** | ±30° horizontal, ±15° vertical | - |

### 3.4 Requisitos Eléctricos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Tensión nominal** | 120/208 VAC, 60 Hz | RETIE |
| **Variación de tensión** | ±10% | RETIE |
| **Factor de potencia** | ≥0.9 | RETIE |
| **Consumo máximo (Tipo A)** | 8 kW | - |
| **Consumo máximo (Tipo B)** | 3 kW | - |
| **Protección eléctrica** | IP65 | IEC 60529 |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Módulos LED

#### 4.1.1 Descripción General

Módulos LED de alta luminosidad para formar la matriz de píxeles del panel, con tecnología de montaje superficial y control individual de brillo.

#### 4.1.2 Especificaciones Técnicas

**LED Individual:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Tipo de LED** | SMD de alta potencia | Inspección técnica |
| **Color** | Ámbar (590-595 nm) | Espectrofotómetro |
| **Luminosidad** | 2,000 mcd mínimo | Medición fotométrica |
| **Vida útil** | 100,000 horas @ 70% | Certificado fabricante |
| **Temperatura de color** | 2200K ±200K | Medición colorimétrica |

**Módulo LED:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Configuración** | 16x16 LEDs por módulo | Inspección visual |
| **Pitch de píxel** | 25 mm | Medición física |
| **Consumo por módulo** | 80W máximo | Medición eléctrica |
| **Control de brillo** | 256 niveles mínimo | Prueba funcional |
| **Uniformidad** | ±5% entre LEDs | Medición fotométrica |

#### 4.1.3 Características de Construcción

**Materiales:**
- PCB: FR4 de alta calidad
- Máscara: Policarbonato UV resistente
- Sellado: Silicona grado automotriz
- Conectores: IP67 rated

**Diseño Térmico:**
- Disipación pasiva por aletas
- Temperatura de unión <85°C
- Coeficiente térmico compensado
- Protección contra sobrecalentamiento

#### 4.1.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Daktronics** - Modelo: Galaxy GX-20
2. **Watchfire** - Modelo: 25mm Outdoor
3. **Prism** - Modelo: AP-25
4. **O equivalente** que cumpla especificaciones

### 4.2 Sistema de Control

#### 4.2.1 Descripción General

Sistema de control inteligente para gestión de mensajes, monitoreo de estado, comunicación con CCO y diagnóstico automático.

#### 4.2.2 Especificaciones Técnicas

**Controlador Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Procesador** | ARM Cortex-A9 o superior | Inspección técnica |
| **Memoria RAM** | 2 GB mínimo | Inspección técnica |
| **Almacenamiento** | 32 GB SSD | Inspección técnica |
| **Interfaces** | Ethernet, RS-232, USB | Inspección física |
| **Protocolos** | NTCIP 1203, SNMP | Configuración |

**Funcionalidades:**
- Almacenamiento de 200 mensajes mínimo
- Programación de mensajes por horario
- Control automático de brillo por sensor
- Diagnóstico continuo de LEDs
- Registro de eventos y alarmas

#### 4.2.3 Software de Control

**Características del Software:**
- Interface gráfica intuitiva
- Editor de mensajes WYSIWYG
- Biblioteca de símbolos gráficos
- Programación de secuencias
- Reportes de estado y fallas

**Compatibilidad:**
- Protocolo NTCIP 1203 v03
- Integración con sistemas SCADA
- API para integración personalizada
- Actualizaciones remotas de firmware

### 4.3 Estructura de Soporte

#### 4.3.1 Descripción General

Estructura metálica para soporte del panel LED, diseñada para resistir cargas de viento y sísmicas según normativa local.

#### 4.3.2 Especificaciones Técnicas

**Estructura Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Material** | Acero galvanizado ASTM A572 Gr. 50 | Certificado de material |
| **Soldadura** | AWS D1.1 | Inspección visual + END |
| **Galvanizado** | ASTM A123 | Certificado de proceso |
| **Carga de viento** | 200 km/h | Cálculo estructural |
| **Factor de seguridad** | 2.5 mínimo | Cálculo estructural |

**Configuraciones:**
- **Tipo Pórtico:** Para paneles sobre calzada
- **Tipo Cantilever:** Para paneles laterales
- **Tipo Poste:** Para paneles auxiliares

#### 4.3.3 Accesorios de Montaje

**Sistema de Fijación:**
- Tornillería acero inoxidable A4
- Arandelas de presión y planas
- Selladores estructurales
- Sistema anti-vibración

**Acceso para Mantenimiento:**
- Escalera con guarda-hombre
- Plataforma de trabajo
- Puntos de anclaje para arnés
- Iluminación de servicio

#### 4.3.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Valmont** - Modelo: Traffic Structures
2. **Pelco** - Modelo: Structural Products
3. **Sabre** - Modelo: Highway Structures
4. **O equivalente** que cumpla especificaciones

### 4.4 Sistema de Comunicación

#### 4.4.1 Descripción General

Sistema de comunicación para conectar cada panel con el CCO, permitiendo control remoto, monitoreo y diagnóstico.

#### 4.4.2 Especificaciones Técnicas

**Interfaz de Comunicación:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Medio físico** | Fibra óptica monomodo | Inspección técnica |
| **Velocidad** | 100 Mbps | Prueba de velocidad |
| **Protocolo** | TCP/IP sobre Ethernet | Configuración |
| **Latencia** | <100 ms | Medición temporal |
| **Disponibilidad** | 99% | Monitoreo estadístico |

**Protocolos Soportados:**
- NTCIP 1203 (Dynamic Message Signs)
- SNMP v2c/v3 (Gestión de red)
- HTTP/HTTPS (Interface web)
- FTP/SFTP (Transferencia de archivos)
- NTP (Sincronización de tiempo)

#### 4.4.3 Respaldo de Comunicación

**Enlace Celular 4G:**
- Módem industrial 4G/LTE
- Antenas MIMO de alta ganancia
- Redundancia automática
- Consumo de datos optimizado

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con CCO

| Aspecto | Requisito | Verificación |
|:--------|:----------|:-------------|
| **Protocolo** | NTCIP 1203 v03 | Prueba de compatibilidad |
| **Tiempo de respuesta** | <5 segundos | Medición temporal |
| **Actualización de estado** | Cada 30 segundos | Configuración |
| **Gestión de alarmas** | Tiempo real | Prueba funcional |

### 5.2 Integración con Otros Sistemas

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **Sistema de Tráfico** | TCP/IP | Estados de congestión |
| **Sistema Meteorológico** | API REST | Condiciones climáticas |
| **Sistema de Emergencias** | TCP/IP | Alertas y desvíos |
| **Sistema de Peajes** | TCP/IP | Estados de carriles |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Ubicación y Posicionamiento

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Altura sobre calzada** | 5.5-7.0 metros | Manual INVIAS |
| **Distancia lateral** | 2.0 metros mínimo | Manual INVIAS |
| **Ángulo de inclinación** | 0-15° hacia abajo | AASHTO |
| **Orientación** | Perpendicular al tráfico | Manual INVIAS |

### 6.2 Cimentaciones

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Concreto** | f'c = 28 MPa (4000 PSI) | ACI 318 |
| **Acero de refuerzo** | fy = 420 MPa (60 ksi) | ASTM A615 |
| **Profundidad mínima** | 3.0 metros | Estudio geotécnico |
| **Pernos de anclaje** | ASTM A307 Gr. B | AISC |

### 6.3 Instalaciones Eléctricas

| Parámetro | Especificación |
|:----------|:---------------|
| **Acometida** | 120/208 VAC, 60 Hz |
| **Calibre conductor** | AWG 6 mínimo |
| **Protección** | Breaker 50A + DPS |
| **Tablero local** | IP65, acero inoxidable |
| **Tierras** | <10 Ω resistencia |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas Ópticas

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Luminancia** | Verificar brillo | 8,000-12,000 cd/m² |
| **Uniformidad** | Verificar homogeneidad | >80% uniformidad |
| **Color** | Verificar cromaticidad | Ámbar 590-595 nm |
| **Ángulo de visión** | Verificar legibilidad | ±30° horizontal |

### 7.2 Pruebas Funcionales

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Comunicación NTCIP** | Verificar protocolo | 100% comandos soportados |
| **Control de brillo** | Verificar ajuste automático | 256 niveles mínimo |
| **Diagnóstico** | Verificar detección de fallas | 100% LEDs monitoreados |
| **Programación** | Verificar gestión de mensajes | 200 mensajes mínimo |

### 7.3 Pruebas Estructurales

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Carga estática** | Verificar resistencia | Factor seguridad 2.5 |
| **Vibración** | Verificar estabilidad | Sin resonancia crítica |
| **Fatiga** | Verificar durabilidad | 2,000,000 ciclos |
| **Corrosión** | Verificar protección | Sin corrosión visible |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos Técnicos

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Ficha técnica** | Especificaciones completas | Español | 3 copias + digital |
| **Manual de instalación** | Procedimientos de montaje | Español | 2 copias + digital |
| **Manual de operación** | Guía de usuario | Español | 5 copias + digital |
| **Manual de mantenimiento** | Procedimientos preventivos | Español | 3 copias + digital |
| **Planos estructurales** | Diseño de soportes | - | Digital (DWG + PDF) |
| **Software de gestión** | Aplicación de control | - | Licencias incluidas |

### 8.2 Certificados Requeridos

| Certificado | Emisor | Vigencia |
|:------------|:-------|:---------|
| **Certificación NTCIP** | ITE | Vigente |
| **Certificación FCC** | FCC | Vigente |
| **Certificación CE** | Organismo Notificado | Vigente |
| **Certificado estructural** | Ingeniero estructural | - |

### 8.3 Garantías

| Elemento | Garantía Mínima | Observaciones |
|:---------|:----------------|:--------------|
| **Módulos LED** | 60 meses | 70% luminosidad mínima |
| **Controlador** | 36 meses | Desde puesta en servicio |
| **Estructura** | 120 meses | Contra defectos de fabricación |
| **Software** | 36 meses | Actualizaciones incluidas |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza de pantalla** | Mensual | Contratista |
| **Verificación funcional** | Semanal | Contratista |
| **Inspección estructural** | Semestral | Ingeniero estructural |
| **Calibración fotométrica** | Anual | Especialista |
| **Actualización de software** | Según disponibilidad | Fabricante |

### 9.2 Diagnóstico Automático

| Parámetro | Monitoreo | Acción |
|:----------|:----------|:-------|
| **LEDs defectuosos** | Continuo | Alarma inmediata |
| **Temperatura** | Continuo | Alarma por sobrecalentamiento |
| **Consumo eléctrico** | Continuo | Alarma por anomalías |
| **Comunicación** | Continuo | Alarma por pérdida |

### 9.3 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **Módulos LED** | 10% del total | 30 días |
| **Controladores** | 2 unidades | 15 días |
| **Sensores de luz** | 4 unidades | 10 días |
| **Fuentes de poder** | 4 unidades | 15 días |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Panel LED Tipo A (4.0x2.0m) | und | 18 | $65,000 | $1,170,000 |
| 2 | Panel LED Tipo B (2.4x1.2m) | und | 8 | $35,000 | $280,000 |
| 3 | Estructura pórtico | und | 12 | $18,000 | $216,000 |
| 4 | Estructura cantilever | und | 8 | $12,000 | $96,000 |
| 5 | Estructura poste | und | 6 | $8,000 | $48,000 |
| 6 | Sistema de comunicación | und | 26 | $3,500 | $91,000 |
| 7 | Software de gestión | licencia | 1 | $25,000 | $25,000 |
| 8 | Instalación y puesta en marcha | lote | 1 | $180,000 | $180,000 |
| 9 | Capacitación y documentación | lote | 1 | $35,000 | $35,000 |
| 10 | Contingencias (5%) | lote | 1 | $117,050 | $117,050 |
| | | | | **TOTAL** | **$2,258,050** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Validar ubicaciones con estudio de visibilidad
- [ ] Solicitar cotizaciones de fabricantes especializados
- [ ] Coordinar con diseño estructural y cimentaciones
- [ ] Obtener permisos de instalación en vía
- [ ] Desarrollar plan de mensajes estándar
- [ ] Establecer procedimientos de operación

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Sistemas ITS | Especificaciones técnicas iniciales |

---

**Elaborado por:** Ingeniero de Sistemas ITS  
**Revisado por:** Coordinador Técnico  
**Aprobado por:** Gerente de Proyecto  

**Fecha de elaboración:** 21/10/2025  
**Próxima revisión:** 30/11/2025