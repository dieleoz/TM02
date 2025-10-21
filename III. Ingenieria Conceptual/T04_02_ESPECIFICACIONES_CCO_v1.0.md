# T04_02: ESPECIFICACIONES TÉCNICAS - CENTRO DE CONTROL OPERACIONAL (CCO)
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Centro de Control Operacional  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  
**Referencia T01:** T01_02_FICHA_SISTEMA_CCO_v1.0.md  
**Referencia T03:** T03_02_ARQUITECTURA_CCO_v1.0.md  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | 21/10/2025 | Creación inicial | Ingeniero de Sistemas |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | Centro de Control Operacional |
| **Categoría** | ITS - Gestión y Control |
| **Código interno** | T04-02-v1.0 |
| **Cantidad total** | 1 CCO principal + 1 CCO respaldo |
| **CAPEX estimado** | USD $3,200,000 |
| **Documentos base** | T01_02, T02_02, T03_02, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Servidores y equipos de cómputo
- ✅ Sistema SCADA y software de gestión
- ✅ Videowall y sistemas de visualización
- ✅ Equipos de comunicaciones y red
- ✅ Sistemas de respaldo y contingencia

**Este documento NO especifica:**
- ❌ Obras civiles del edificio CCO (ver T05)
- ❌ Mobiliario y ergonomía (ver T05)
- ❌ Integración con sistemas externos (ver T04_14)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 2.1.1 | CCO operativo 24/7/365 |
| **Apéndice Técnico 2** | 3.2.4 | Disponibilidad mínima 99.8% |
| **Apéndice Técnico 3** | 4.1.1 | Integración con todos los sistemas |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **RETIE** | Reglamento Técnico Instalaciones Eléctricas | Data center |
| **Ley 1581/2012** | Protección de Datos Personales | Manejo de información |
| **Decreto 1078/2015** | Sector TIC | Comunicaciones |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **ISO 27001** | Gestión de Seguridad de la Información | Data center |
| **TIA-942** | Telecommunications Infrastructure Standard | Data center |
| **ITIL v4** | Information Technology Infrastructure Library | Gestión de servicios |### 2.3 
Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **ISO 27001** | Organismo certificador | ✅ Sí | Seguridad información |
| **TIER III** | Uptime Institute | ⏳ Opcional | Data center |
| **Energy Star** | EPA | ⏳ Opcional | Eficiencia energética |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura operación** | 18°C a 27°C | TIA-942 |
| **Humedad relativa** | 40-60% | TIA-942 |
| **Clasificación sísmica** | Zona de amenaza alta | NSR-10 |
| **Protección contra incendio** | Sistema FM-200 o equivalente | NFPA 2001 |
| **Control de acceso** | Biométrico + tarjeta | - |

### 3.2 Requisitos Eléctricos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Tensión nominal** | 208/120 VAC, 60 Hz | RETIE |
| **Calidad de energía** | THD <5% | IEEE 519 |
| **Factor de potencia** | ≥0.95 | RETIE |
| **Consumo total estimado** | 150 kW | - |
| **Respaldo UPS** | 30 minutos + generador | TIA-942 |
| **Generador de emergencia** | 200 kVA mínimo | - |

### 3.3 Requisitos de Comunicaciones

| Parámetro | Especificación | Protocolo |
|:----------|:---------------|:----------|
| **Conectividad principal** | 2 x 10 Gbps redundante | - |
| **Conectividad respaldo** | 2 x 1 Gbps | - |
| **Red interna** | 40 Gbps backbone | IEEE 802.3 |
| **Latencia máxima** | <10 ms a cualquier sistema | - |
| **Disponibilidad red** | ≥99.9% | SLA |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Servidores Principales

#### 4.1.1 Descripción General

Servidores de alta disponibilidad para alojar el sistema SCADA, bases de datos, aplicaciones de gestión y servicios críticos del CCO.

#### 4.1.2 Especificaciones Técnicas

**Servidor SCADA Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Procesador** | 2 x Intel Xeon Gold 6248R o equivalente | Inspección técnica |
| **Memoria RAM** | 128 GB DDR4 ECC | Inspección técnica |
| **Almacenamiento** | 4 x 1.92 TB SSD NVMe RAID 10 | Prueba de rendimiento |
| **Redundancia** | Fuentes redundantes, ventiladores | Prueba de falla |
| **Conectividad** | 4 x 10 GbE + 2 x 1 GbE | Prueba de conectividad |

**Servidor Base de Datos:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Procesador** | 2 x Intel Xeon Gold 6258R o equivalente | Inspección técnica |
| **Memoria RAM** | 256 GB DDR4 ECC | Inspección técnica |
| **Almacenamiento** | 8 x 3.84 TB SSD NVMe RAID 10 | Prueba de rendimiento |
| **Backup storage** | 20 TB capacidad útil | Prueba de respaldo |
| **Conectividad** | 4 x 10 GbE + 2 x 1 GbE | Prueba de conectividad |

#### 4.1.3 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Dell Technologies** - Modelo: PowerEdge R750
2. **HPE** - Modelo: ProLiant DL380 Gen10 Plus
3. **Lenovo** - Modelo: ThinkSystem SR650 V2
4. **O equivalente** que cumpla especificaciones

### 4.2 Sistema de Almacenamiento

#### 4.2.1 Descripción General

Sistema de almacenamiento centralizado de alta disponibilidad para datos históricos, videos de CCTV, logs del sistema y respaldos.

#### 4.2.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Capacidad útil** | 500 TB | Inspección técnica |
| **Tipo de discos** | SSD + HDD híbrido | Inspección técnica |
| **RAID** | RAID 6 mínimo | Configuración |
| **Conectividad** | 16 Gbps FC o 25 GbE iSCSI | Prueba de rendimiento |
| **Replicación** | Síncrona a sitio respaldo | Prueba de replicación |

#### 4.2.3 Características Avanzadas

**Gestión de Datos:**
- Deduplicación automática
- Compresión en línea
- Snapshots programados
- Migración automática de datos

**Alta Disponibilidad:**
- Controladores redundantes
- Fuentes de poder redundantes
- Conectividad multipath
- Failover automático <30 segundos

### 4.3 Sistema de Visualización (Videowall)

#### 4.3.1 Descripción General

Sistema de videowall de alta resolución para visualización de mapas, videos de CCTV, estados de sistemas y información operacional crítica.

#### 4.3.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Configuración** | 3x3 pantallas (9 pantallas) | Inspección física |
| **Tamaño por pantalla** | 55" mínimo | Inspección física |
| **Resolución por pantalla** | 4K (3840x2160) | Prueba de imagen |
| **Brillo** | 500 cd/m² mínimo | Medición fotométrica |
| **Bezel** | <3.5 mm | Inspección física |
| **Tiempo de vida** | >60,000 horas | Certificado fabricante |

#### 4.3.3 Sistema de Control

**Procesador de Video:**
- Soporte para múltiples fuentes
- Escalado y procesamiento 4K
- Control por software
- Redundancia automática

**Software de Gestión:**
- Layouts predefinidos
- Rotación automática de contenido
- Control remoto
- Integración con SCADA

#### 4.3.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Samsung** - Modelo: UH55F-E
2. **LG** - Modelo: 55VH7F
3. **Christie** - Modelo: FHD551-X
4. **O equivalente** que cumpla especificaciones

### 4.4 Equipos de Red y Comunicaciones

#### 4.4.1 Descripción General

Infraestructura de red de alta disponibilidad para interconectar todos los sistemas del CCO y proporcionar conectividad con los sistemas de campo.

#### 4.4.2 Especificaciones Técnicas

**Switch Core Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Puertos 10 GbE** | 48 puertos mínimo | Inspección técnica |
| **Puertos 40 GbE** | 6 puertos mínimo | Inspección técnica |
| **Capacidad switching** | 1.28 Tbps | Especificación técnica |
| **Redundancia** | Fuentes y ventiladores redundantes | Prueba de falla |
| **Protocolos** | OSPF, BGP, MPLS, VLAN | Configuración |

**Firewall de Seguridad:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Throughput** | 10 Gbps mínimo | Prueba de rendimiento |
| **Conexiones concurrentes** | 2,000,000 | Prueba de carga |
| **VPN tunnels** | 1,000 túneles | Configuración |
| **IPS/IDS** | Integrado | Prueba de seguridad |
| **Alta disponibilidad** | Activo-Pasivo | Prueba de failover |

#### 4.4.3 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Cisco** - Catalyst 9500 / ASA 5585-X
2. **Juniper** - EX4650 / SRX5800
3. **Arista** - 7280R3 / Fortinet FortiGate
4. **O equivalente** que cumpla especificaciones

### 4.5 Sistema SCADA

#### 4.5.1 Descripción General

Sistema de supervisión, control y adquisición de datos para monitoreo y control centralizado de todos los sistemas ITS de la autopista.

#### 4.5.2 Especificaciones Funcionales

| Función | Especificación Mínima | Método de Verificación |
|:--------|:---------------------|:-----------------------|
| **Puntos de I/O** | 50,000 puntos | Configuración |
| **Usuarios concurrentes** | 50 usuarios | Prueba de carga |
| **Tiempo de actualización** | <2 segundos | Medición temporal |
| **Retención de datos** | 5 años mínimo | Configuración BD |
| **Reportes** | Automáticos y manuales | Prueba funcional |

#### 4.5.3 Módulos del Sistema

**Módulo de Peajes:**
- Monitoreo de transacciones
- Estados de carriles
- Alarmas y eventos
- Reportes financieros

**Módulo de Tráfico:**
- Monitoreo de flujo vehicular
- Control de PMV
- Gestión de incidentes
- Análisis de congestión

**Módulo de CCTV:**
- Visualización de cámaras
- Grabación automática
- Detección de eventos
- Control PTZ

**Módulo de Emergencias:**
- Gestión de llamadas SOS
- Despacho de recursos
- Comunicación con entidades
- Seguimiento de incidentes

#### 4.5.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Schneider Electric** - Wonderware System Platform
2. **Siemens** - WinCC OA
3. **GE Digital** - iFIX
4. **O equivalente** que cumpla especificaciones

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con Sistemas de Campo

| Sistema | Protocolo | Interfaz | Datos |
|:--------|:----------|:---------|:------|
| **Estaciones de Peaje** | TCP/IP, IP/REV | Ethernet | Transacciones, estados |
| **Cámaras CCTV** | ONVIF, RTSP | IP | Video, PTZ, eventos |
| **Paneles LED** | NTCIP 1203 | TCP/IP | Mensajes, estados |
| **Postes SOS** | SIP, TCP/IP | VoIP | Audio, eventos |
| **Sensores Tráfico** | NTCIP 1202 | TCP/IP | Conteos, velocidades |

### 5.2 Integración con Sistemas Externos

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **Sistema Financiero** | Web Services SOAP/REST | Transacciones, conciliación |
| **Entidades de Emergencia** | SIP Trunking | Audio, datos de ubicación |
| **INVIAS** | FTP/SFTP | Reportes operacionales |
| **Meteorología** | API REST | Datos climáticos |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Sala de Servidores (Data Center)

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Área mínima** | 80 m² | TIA-942 |
| **Altura libre** | 3.0 m mínimo | TIA-942 |
| **Piso técnico** | 60 cm altura | TIA-942 |
| **Climatización** | Redundancia N+1 | TIA-942 |
| **Detección de incendio** | VESDA o equivalente | NFPA 72 |

### 6.2 Sala de Control

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Área mínima** | 120 m² | - |
| **Puestos de operación** | 6 puestos ergonómicos | - |
| **Iluminación** | 500 lux, sin reflejos | - |
| **Acústica** | <45 dB | - |
| **Climatización** | 22°C ±2°C | - |

### 6.3 Infraestructura Eléctrica

| Parámetro | Especificación |
|:----------|:---------------|
| **UPS principal** | 200 kVA, 30 min autonomía |
| **Generador** | 250 kVA, arranque automático |
| **Transferencia** | <10 segundos |
| **Tableros** | Redundancia A+B |
| **Tierras** | <1 Ω resistencia |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas de Infraestructura

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Prueba de UPS** | Verificar autonomía | 30 minutos mínimo |
| **Prueba de generador** | Verificar arranque automático | <10 segundos |
| **Prueba de climatización** | Verificar redundancia | N+1 operativo |
| **Prueba de red** | Verificar rendimiento | 10 Gbps sin pérdidas |

### 7.2 Pruebas de Software

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Prueba de carga** | Verificar capacidad | 50 usuarios concurrentes |
| **Prueba de integración** | Verificar conectividad | Todos los sistemas |
| **Prueba de failover** | Verificar redundancia | <30 segundos recuperación |
| **Prueba de seguridad** | Verificar protección | Sin vulnerabilidades críticas |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos Técnicos

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Arquitectura del sistema** | Diagramas y especificaciones | Español | 3 copias + digital |
| **Manual de instalación** | Procedimientos detallados | Español | 2 copias + digital |
| **Manual de operación** | Guía de usuario SCADA | Español | 5 copias + digital |
| **Manual de administración** | Configuración y mantenimiento | Español | 3 copias + digital |
| **Planos as-built** | Instalación final | - | Digital (DWG + PDF) |

### 8.2 Certificados y Garantías

| Certificado | Emisor | Vigencia |
|:------------|:-------|:---------|
| **ISO 27001** | Organismo certificador | 3 años |
| **Certificados de equipos** | Fabricantes | Según equipo |
| **Garantía de software** | 60 meses | Desde puesta en servicio |
| **Garantía de hardware** | 36 meses | Desde puesta en servicio |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza de equipos** | Mensual | Contratista |
| **Verificación de UPS** | Mensual | Contratista |
| **Prueba de generador** | Mensual | Contratista |
| **Actualización de software** | Trimestral | Fabricante |
| **Backup y restauración** | Diario/Semanal | Automático |

### 9.2 Soporte Técnico

| Nivel | Tiempo de Respuesta | Disponibilidad |
|:------|:-------------------|:---------------|
| **Nivel 1** | 15 minutos | 24/7/365 |
| **Nivel 2** | 2 horas | 24/7/365 |
| **Nivel 3** | 4 horas | Horario laboral |
| **Fabricante** | 8 horas | Según contrato |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Servidores principales | und | 6 | $45,000 | $270,000 |
| 2 | Sistema de almacenamiento | und | 2 | $180,000 | $360,000 |
| 3 | Videowall 3x3 | lote | 1 | $85,000 | $85,000 |
| 4 | Equipos de red | lote | 1 | $120,000 | $120,000 |
| 5 | Sistema SCADA | licencia | 1 | $450,000 | $450,000 |
| 6 | UPS y respaldo eléctrico | lote | 1 | $95,000 | $95,000 |
| 7 | Climatización data center | lote | 1 | $65,000 | $65,000 |
| 8 | Mobiliario y ergonomía | lote | 1 | $45,000 | $45,000 |
| 9 | Instalación y configuración | lote | 1 | $280,000 | $280,000 |
| 10 | Capacitación y documentación | lote | 1 | $55,000 | $55,000 |
| 11 | Contingencias (5%) | lote | 1 | $141,250 | $141,250 |
| | | | | **TOTAL** | **$1,966,250** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Validar arquitectura con especialistas en SCADA
- [ ] Solicitar cotizaciones de integradores certificados
- [ ] Definir cronograma de implementación por fases
- [ ] Coordinar con diseño de obras civiles del CCO
- [ ] Establecer acuerdos de soporte con fabricantes
- [ ] Planificar migración desde sistemas existentes

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Sistemas | Especificaciones técnicas iniciales |

---

**Elaborado por:** Ingeniero de Sistemas  
**Revisado por:** Coordinador Técnico  
**Aprobado por:** Gerente de Proyecto  

**Fecha de elaboración:** 21/10/2025  
**Próxima revisión:** 30/11/2025