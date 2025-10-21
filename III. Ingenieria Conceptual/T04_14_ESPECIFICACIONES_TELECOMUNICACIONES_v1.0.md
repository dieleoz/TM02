# T04_14: ESPECIFICACIONES TÉCNICAS - SISTEMA DE TELECOMUNICACIONES
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Telecomunicaciones  
**Responsable:** Ingeniero de Telecomunicaciones  
**Versión:** 1.0  
**Referencia T01:** T01_14_FICHA_SISTEMA_TELECOMUNICACIONES_v1.0.md  
**Referencia T03:** T03_14_ARQUITECTURA_TELECOMUNICACIONES_v1.0.md  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | 21/10/2025 | Creación inicial | Ingeniero de Telecomunicaciones |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | Sistema de Telecomunicaciones |
| **Categoría** | Infraestructura de Comunicaciones |
| **Código interno** | T04-14-v1.0 |
| **Extensión total** | 85 km de autopista |
| **CAPEX estimado** | USD $4,800,000 |
| **Documentos base** | T01_14, T02_14, T03_14, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Red de fibra óptica troncal y distribución
- ✅ Equipos de transmisión y conmutación
- ✅ Sistemas de comunicación de voz y datos
- ✅ Enlaces de respaldo y redundancia
- ✅ Equipos de monitoreo y gestión de red

**Este documento NO especifica:**
- ❌ Canalizaciones y obras civiles (ver T05)
- ❌ Torres de comunicaciones (ver T05)
- ❌ Integración con operadores externos (ver T04_02)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 5.1.2 | Red de telecomunicaciones redundante |
| **Apéndice Técnico 2** | 3.4.1 | Disponibilidad mínima 99.9% |
| **Apéndice Técnico 3** | 4.2.3 | Capacidad para crecimiento futuro |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **Resolución CRC 5050/2016** | Redes de telecomunicaciones | Diseño de red |
| **RETIE** | Reglamento Técnico Instalaciones Eléctricas | Instalaciones |
| **Decreto 1078/2015** | Sector TIC | Licencias y permisos |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **ITU-T G.652** | Características de fibra óptica | Fibra monomodo |
| **IEEE 802.3** | Ethernet Standards | Equipos de red |
| **TIA-568** | Commercial Building Telecommunications | Cableado estructurado |### 2.3 C
ertificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **Homologación CRC** | CRC Colombia | ✅ Sí | Equipos de telecomunicaciones |
| **Certificación ITU-T** | ITU | ✅ Sí | Equipos de transmisión |
| **Certificación TIA** | TIA | ⏳ Opcional | Cableado estructurado |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Arquitectura de Red

#### 3.1.1 Topología General

**Red Troncal:**
- Topología: Anillo principal con anillos secundarios
- Tecnología: DWDM (Dense Wavelength Division Multiplexing)
- Capacidad: 40 Gbps por enlace
- Redundancia: Doble anillo con protección automática

**Red de Distribución:**
- Topología: Estrella desde nodos principales
- Tecnología: Ethernet sobre fibra
- Capacidad: 1-10 Gbps por enlace
- Cobertura: Todos los sistemas ITS

#### 3.1.2 Puntos de Presencia

| Tipo de Nodo | Cantidad | Ubicación | Función |
|:-------------|:---------|:----------|:--------|
| **Nodo Principal** | 2 | CCO + Respaldo | Concentración y gestión |
| **Nodo Secundario** | 8 | Estaciones de peaje | Distribución local |
| **Nodo de Acceso** | 25 | Puntos estratégicos | Conexión equipos campo |

### 3.2 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura operación** | -40°C a +70°C | ITU-T K.21 |
| **Humedad relativa** | 0-95% sin condensación | ITU-T K.21 |
| **Protección IP** | IP65 para exteriores | IEC 60529 |
| **Resistencia a rayos** | Protección Clase I | ITU-T K.56 |
| **Vibración** | Según IEC 60068-2-6 | IEC 60068 |

### 3.3 Requisitos Eléctricos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Tensión nominal** | -48 VDC (equipos) / 120 VAC (conversores) | ITU-T |
| **Variación de tensión** | ±10% | ITU-T |
| **Consumo total estimado** | 45 kW | - |
| **Respaldo baterías** | 8 horas mínimo | ITU-T |
| **Rectificadores** | Redundancia N+1 | ITU-T |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Red de Fibra Óptica

#### 4.1.1 Descripción General

Red de fibra óptica monomodo para interconectar todos los sistemas ITS con el CCO, proporcionando alta capacidad, baja latencia y máxima confiabilidad.

#### 4.1.2 Especificaciones de Fibra

**Fibra Óptica Monomodo:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Tipo** | ITU-T G.652.D | Certificado fabricante |
| **Diámetro del núcleo** | 9 μm ±0.4 μm | Medición óptica |
| **Diámetro del revestimiento** | 125 μm ±1 μm | Medición óptica |
| **Atenuación @ 1310 nm** | ≤0.35 dB/km | Medición OTDR |
| **Atenuación @ 1550 nm** | ≤0.22 dB/km | Medición OTDR |
| **Dispersión cromática** | ≤18 ps/(nm·km) @ 1550 nm | Medición especializada |

**Cable de Fibra Óptica:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Configuración troncal** | 144 fibras | Inspección física |
| **Configuración distribución** | 48 fibras | Inspección física |
| **Configuración acceso** | 12-24 fibras | Inspección física |
| **Cubierta exterior** | HDPE negro con UV | Inspección visual |
| **Elemento de tracción** | Aramida o FRP | Certificado fabricante |
| **Resistencia a tracción** | 2700 N | Ensayo mecánico |

#### 4.1.3 Instalación y Tendido

**Métodos de Instalación:**
- Ductos subterráneos: 80% del trazado
- Tendido aéreo: 15% del trazado
- Instalación directa enterrada: 5% del trazado

**Especificaciones de Instalación:**
| Parámetro | Especificación |
|:----------|:---------------|
| **Radio de curvatura mínimo** | 20 x diámetro del cable |
| **Tensión máxima de tendido** | 80% de la resistencia nominal |
| **Profundidad enterrado** | 80 cm mínimo |
| **Separación de energía** | 30 cm mínimo |

#### 4.1.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Corning** - Modelo: OptiSheath
2. **Prysmian** - Modelo: FlexRibbon
3. **Furukawa** - Modelo: Laserwave
4. **O equivalente** que cumpla especificaciones

### 4.2 Equipos de Transmisión DWDM

#### 4.2.1 Descripción General

Sistema DWDM (Dense Wavelength Division Multiplexing) para maximizar la capacidad de transmisión sobre la fibra óptica instalada.

#### 4.2.2 Especificaciones Técnicas

**Terminal DWDM:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Canales ópticos** | 80 canales (C-band) | Configuración |
| **Espaciado de canales** | 50 GHz (ITU-T Grid) | Analizador óptico |
| **Capacidad por canal** | 10 Gbps | Prueba de tráfico |
| **Alcance sin regeneración** | 80 km | Medición de potencia |
| **Potencia de salida** | +3 dBm por canal | Medidor de potencia |
| **Sensibilidad** | -28 dBm @ BER 10^-12 | Prueba de sensibilidad |

**Amplificadores Ópticos:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Tipo** | EDFA (Erbium Doped) | Inspección técnica |
| **Ganancia** | 15-25 dB variable | Medición óptica |
| **Potencia de salida** | +20 dBm | Medidor de potencia |
| **Figura de ruido** | <6 dB | Analizador óptico |
| **Control automático** | AGC + APC | Prueba funcional |

#### 4.2.3 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Huawei** - Modelo: OptiX OSN 8800
2. **Nokia** - Modelo: 1830 PSS
3. **Ciena** - Modelo: 6500 Series
4. **O equivalente** que cumpla especificaciones

### 4.3 Equipos de Conmutación Ethernet

#### 4.3.1 Descripción General

Switches Ethernet de alta capacidad para la conmutación de tráfico de datos entre todos los sistemas ITS.

#### 4.3.2 Especificaciones Técnicas

**Switch Core (CCO):**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Puertos 10 GbE** | 48 puertos | Inspección técnica |
| **Puertos 40 GbE** | 6 puertos | Inspección técnica |
| **Capacidad switching** | 1.28 Tbps | Especificación técnica |
| **Latencia** | <5 μs | Medición temporal |
| **Buffer de memoria** | 32 MB | Especificación técnica |
| **Redundancia** | Fuentes y supervisores redundantes | Prueba de falla |

**Switch de Distribución:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Puertos 1 GbE** | 24 puertos | Inspección técnica |
| **Puertos 10 GbE** | 4 puertos uplink | Inspección técnica |
| **Capacidad switching** | 128 Gbps | Especificación técnica |
| **PoE+** | 30W por puerto | Medición eléctrica |
| **Protocolos** | RSTP, OSPF, VLAN | Configuración |

#### 4.3.3 Características Avanzadas

**Calidad de Servicio (QoS):**
- Clasificación de tráfico por prioridad
- Limitación de ancho de banda
- Garantía de latencia para tráfico crítico
- Soporte para DiffServ

**Seguridad:**
- Control de acceso por puerto (802.1X)
- Listas de control de acceso (ACL)
- Protección contra ataques DoS
- Segmentación por VLAN

#### 4.3.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Cisco** - Catalyst 9500/9300 Series
2. **Juniper** - EX4650/EX3400 Series
3. **Arista** - 7280R3/7050X Series
4. **O equivalente** que cumpla especificaciones

### 4.4 Sistema de Comunicación de Voz

#### 4.4.1 Descripción General

Sistema VoIP (Voice over IP) para comunicaciones de voz entre el CCO, estaciones de peaje, equipos de emergencia y entidades externas.

#### 4.4.2 Especificaciones Técnicas

**Central Telefónica IP:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Extensiones** | 200 extensiones | Configuración |
| **Líneas troncales** | 30 líneas SIP | Configuración |
| **Llamadas concurrentes** | 100 llamadas | Prueba de carga |
| **Códecs soportados** | G.711, G.729, G.722 | Prueba de audio |
| **Calidad de voz** | MOS >4.0 | Medición objetiva |

**Teléfonos IP:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Pantalla** | LCD color 3.5" | Inspección visual |
| **Teclas programables** | 6 teclas mínimo | Inspección física |
| **PoE** | IEEE 802.3af | Medición eléctrica |
| **Códecs** | G.711, G.729 | Prueba de audio |
| **Manos libres** | Full-duplex | Prueba funcional |

#### 4.4.3 Funcionalidades Avanzadas

**Características del Sistema:**
- Grabación automática de llamadas
- Distribución automática de llamadas (ACD)
- Música en espera
- Transferencia de llamadas
- Conferencias multipunto

**Integración con Sistemas:**
- Integración con sistema de emergencias
- Notificaciones automáticas por eventos
- Interfaz con radio comunicaciones
- Registro de llamadas en base de datos

#### 4.4.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Avaya** - IP Office 500 V2
2. **Cisco** - Unified Communications Manager
3. **Asterisk** - FreePBX
4. **O equivalente** que cumpla especificaciones

### 4.5 Enlaces de Respaldo

#### 4.5.1 Descripción General

Enlaces de comunicación de respaldo para garantizar la continuidad del servicio en caso de falla de la red principal.

#### 4.5.2 Especificaciones Técnicas

**Enlace Satelital:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Capacidad** | 10 Mbps simétrico | Prueba de velocidad |
| **Latencia** | <600 ms | Medición temporal |
| **Disponibilidad** | 99.5% | SLA del proveedor |
| **Tiempo de conmutación** | <30 segundos | Prueba de failover |

**Enlace Celular 4G/5G:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Capacidad** | 50 Mbps down / 20 Mbps up | Prueba de velocidad |
| **Cobertura** | 100% del trazado | Medición de señal |
| **Redundancia** | 2 operadores diferentes | Configuración |
| **Tiempo de conmutación** | <10 segundos | Prueba de failover |

#### 4.5.3 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Hughes** - HT2000L (Satelital)
2. **Cradlepoint** - AER2200 (Celular)
3. **Peplink** - MAX HD4 (Multi-WAN)
4. **O equivalente** que cumpla especificaciones

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con Sistemas ITS

| Sistema | Tipo de Conexión | Ancho de Banda | Protocolo |
|:--------|:-----------------|:---------------|:----------|
| **Estaciones de Peaje** | Fibra óptica | 1 Gbps | TCP/IP, IP/REV |
| **Cámaras CCTV** | Fibra óptica | 100 Mbps c/u | RTSP, ONVIF |
| **Paneles LED** | Fibra óptica | 10 Mbps | NTCIP 1203 |
| **Postes SOS** | Fibra óptica | 2 Mbps | SIP, TCP/IP |
| **Sensores de Tráfico** | Fibra óptica | 1 Mbps | NTCIP 1202 |

### 5.2 Integración con Redes Externas

| Red Externa | Tipo de Interfaz | Capacidad | Uso |
|:------------|:-----------------|:----------|:----|
| **Internet** | Fibra óptica | 1 Gbps | Acceso general |
| **Red Corporativa** | VPN IPSec | 100 Mbps | Gestión remota |
| **Operadores Celulares** | Interfaces API | Variable | Respaldo |
| **Entidades de Emergencia** | SIP Trunking | 10 líneas | Comunicación |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Canalizaciones

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Ductos principales** | PVC 6" (150 mm) | RETIE |
| **Ductos secundarios** | PVC 4" (100 mm) | RETIE |
| **Profundidad mínima** | 80 cm | RETIE |
| **Separación de energía** | 30 cm mínimo | RETIE |
| **Cámaras de inspección** | Cada 150 m máximo | - |

### 6.2 Salas de Equipos

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Área mínima** | 20 m² por nodo | TIA-942 |
| **Altura libre** | 2.5 m mínimo | TIA-942 |
| **Climatización** | 22°C ±2°C | TIA-942 |
| **Humedad** | 45-55% | TIA-942 |
| **Protección IP** | IP54 mínimo | IEC 60529 |

### 6.3 Sistema de Energía

| Parámetro | Especificación |
|:----------|:---------------|
| **Tensión AC** | 120/208 VAC, 60 Hz |
| **Tensión DC** | -48 VDC para equipos |
| **Rectificadores** | Redundancia N+1 |
| **Baterías** | 8 horas autonomía |
| **Tierras** | <5 Ω resistencia |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas de Fibra Óptica

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **OTDR** | Verificar continuidad y atenuación | <0.35 dB/km @ 1310 nm |
| **Pérdidas de inserción** | Verificar conectores y empalmes | <0.3 dB por conector |
| **Reflectancia** | Verificar calidad de conectores | <-40 dB |
| **Longitud** | Verificar distancias | ±1% de la longitud real |

### 7.2 Pruebas de Equipos

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Throughput** | Verificar capacidad | 95% de la capacidad nominal |
| **Latencia** | Verificar retardo | <10 ms extremo a extremo |
| **Disponibilidad** | Verificar confiabilidad | >99.9% en 30 días |
| **Failover** | Verificar redundancia | <30 segundos recuperación |

### 7.3 Pruebas de Integración

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Conectividad end-to-end** | Verificar comunicación completa | 100% de los sistemas |
| **Calidad de voz** | Verificar VoIP | MOS >4.0 |
| **Video streaming** | Verificar CCTV | Sin pérdida de frames |
| **Protocolos ITS** | Verificar NTCIP, IP/REV | 100% compatibilidad |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos Técnicos

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Diseño de red** | Diagramas y topología | Español | 3 copias + digital |
| **Manual de instalación** | Procedimientos de instalación | Español | 2 copias + digital |
| **Manual de operación** | Guía de operación y mantenimiento | Español | 5 copias + digital |
| **Planos as-built** | Instalación final | - | Digital (DWG + PDF) |
| **Certificados de fibra** | Resultados de pruebas OTDR | - | Digital |

### 8.2 Software y Licencias

| Software | Descripción | Licencias | Vigencia |
|:---------|:------------|:----------|:---------|
| **Sistema de gestión** | NMS para monitoreo | 5 usuarios | Perpetua |
| **Software de pruebas** | Herramientas de diagnóstico | 2 licencias | 3 años |
| **Actualizaciones** | Firmware y software | Incluidas | 5 años |

### 8.3 Garantías

| Elemento | Garantía Mínima | Observaciones |
|:---------|:----------------|:--------------|
| **Fibra óptica** | 25 años | Contra defectos de fabricación |
| **Equipos activos** | 60 meses | Desde puesta en servicio |
| **Software** | 60 meses | Actualizaciones incluidas |
| **Instalación** | 24 meses | Mano de obra |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza de equipos** | Mensual | Contratista |
| **Verificación de alarmas** | Semanal | Contratista |
| **Pruebas de respaldo** | Mensual | Contratista |
| **Medición de potencia óptica** | Trimestral | Especialista |
| **Actualización de firmware** | Según disponibilidad | Fabricante |

### 9.2 Monitoreo y Gestión

| Parámetro | Umbral de Alarma | Acción |
|:----------|:-----------------|:-------|
| **Potencia óptica** | <-25 dBm | Alarma crítica |
| **Temperatura equipos** | >60°C | Alarma mayor |
| **Utilización de enlaces** | >80% | Alarma menor |
| **Pérdida de conectividad** | >30 segundos | Alarma crítica |

### 9.3 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **Transceptores ópticos** | 10% del total | 15 días |
| **Tarjetas de línea** | 2 por tipo | 30 días |
| **Fuentes de poder** | 2 unidades | 20 días |
| **Cables de fibra** | 2 km por tipo | 45 días |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Cable fibra óptica 144F | km | 85 | $8,500 | $722,500 |
| 2 | Cable fibra óptica 48F | km | 120 | $4,200 | $504,000 |
| 3 | Equipos DWDM | und | 4 | $180,000 | $720,000 |
| 4 | Switches core | und | 4 | $85,000 | $340,000 |
| 5 | Switches distribución | und | 15 | $12,000 | $180,000 |
| 6 | Sistema VoIP completo | lote | 1 | $95,000 | $95,000 |
| 7 | Enlaces de respaldo | und | 3 | $25,000 | $75,000 |
| 8 | ODF y conectividad | lote | 1 | $120,000 | $120,000 |
| 9 | Instalación y empalmes | km | 205 | $2,800 | $574,000 |
| 10 | Pruebas y certificación | lote | 1 | $85,000 | $85,000 |
| 11 | Capacitación y documentación | lote | 1 | $45,000 | $45,000 |
| 12 | Contingencias (5%) | lote | 1 | $224,525 | $224,525 |
| | | | | **TOTAL** | **$3,685,025** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Validar diseño de red con especialistas
- [ ] Solicitar cotizaciones de integradores certificados
- [ ] Coordinar con diseño de canalizaciones
- [ ] Obtener permisos de operadores de telecomunicaciones
- [ ] Definir cronograma de instalación por tramos
- [ ] Establecer acuerdos de soporte técnico

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Telecomunicaciones | Especificaciones técnicas iniciales |

---

**Elaborado por:** Ingeniero de Telecomunicaciones  
**Revisado por:** Coordinador Técnico  
**Aprobado por:** Gerente de Proyecto  

**Fecha de elaboración:** 21/10/2025  
**Próxima revisión:** 30/11/2025