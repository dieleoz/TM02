# T04_01: ESPECIFICACIONES TÉCNICAS - ESTACIONES DE PEAJE
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Estaciones de Peaje  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  
**Referencia T01:** T01_01_FICHA_SISTEMA_ESTACIONES_PEAJE_v1.0.md  
**Referencia T03:** T03_01_ARQUITECTURA_ESTACIONES_PEAJE_v1.0.md  

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
| **Nombre del sistema** | Estaciones de Peaje Electrónico |
| **Categoría** | ITS - Sistemas de Recaudo |
| **Código interno** | T04-01-v1.0 |
| **Cantidad total** | 8 estaciones principales + 4 auxiliares |
| **CAPEX estimado** | USD $2,400,000 |
| **Documentos base** | T01_01, T02_01, T03_01, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Equipos de detección vehicular (lazos, cámaras)
- ✅ Sistemas de clasificación automática
- ✅ Equipos de cobro electrónico (TAG/RFID)
- ✅ Barreras automáticas y señalización
- ✅ Sistemas de respaldo y contingencia

**Este documento NO especifica:**
- ❌ Obras civiles de casetas (ver T05)
- ❌ Integración con bancos (ver T04_14)
- ❌ Software de gestión central (ver T04_02)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 3.2.1 | Sistema de peaje electrónico obligatorio |
| **Apéndice Técnico 2** | 4.1.3 | Interoperabilidad nacional (IP/REV) |
| **Apéndice Técnico 3** | 2.4.2 | Disponibilidad mínima 99.5% |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **Resolución 546/2018** | Interoperabilidad de peajes IP/REV | Protocolo de comunicación |
| **RETIE** | Reglamento Técnico Instalaciones Eléctricas | Instalaciones eléctricas |
| **Decreto 1079/2015** | Sector Transporte | Operación de peajes |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **ISO 14906** | Electronic Fee Collection | Sistemas DSRC |
| **ISO 12813** | Electronic Fee Collection | Arquitectura de sistemas |
| **IEEE 802.11p** | Wireless Access Vehicular Environments | Comunicación V2I |
### 2.3 Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **Homologación IP/REV** | ANI Colombia | ✅ Sí | Equipos DSRC |
| **Certificación CE** | Organismo Notificado | ✅ Sí | Equipos electrónicos |
| **Certificación FCC** | FCC | ⏳ Opcional | Equipos de radiofrecuencia |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura de operación** | -10°C a +60°C | IEC 60068 |
| **Humedad relativa** | 0-95% sin condensación | IEC 60068 |
| **Protección IP** | IP65 mínimo | IEC 60529 |
| **Resistencia a viento** | 150 km/h | AASHTO |
| **Altitud operación** | 0-2500 msnm | - |

**Condiciones específicas del proyecto:**
- Clima tropical húmedo
- Temperatura promedio: 27-32°C
- Humedad promedio: 70-85%
- Exposición directa al sol y lluvia

### 3.2 Requisitos Eléctricos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Tensión nominal** | 120/208 VAC, 60 Hz | RETIE |
| **Variación de tensión** | ±10% | RETIE |
| **Factor de potencia** | ≥0.9 | RETIE |
| **Consumo máximo por carril** | 2.5 kW | - |
| **Respaldo UPS** | 4 horas mínimo | AT2 |

### 3.3 Requisitos de Comunicaciones

| Parámetro | Especificación | Protocolo |
|:----------|:---------------|:----------|
| **Medio físico** | Fibra óptica monomodo | - |
| **Velocidad** | 1 Gbps mínimo | IEEE 802.3 |
| **Protocolo de red** | TCP/IP | - |
| **Protocolo aplicación** | IP/REV, NTCIP | Resolución 546/2018 |
| **Disponibilidad** | ≥99.5% | AT2 |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Sistema de Detección Vehicular

#### 4.1.1 Descripción General

Sistema de detección automática de vehículos mediante lazos inductivos y sensores de respaldo para garantizar la detección del 100% de los vehículos que ingresan al carril de peaje.

#### 4.1.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Tasa de detección** | ≥99.9% | Prueba estadística 1000 vehículos |
| **Tiempo de respuesta** | <100 ms | Prueba con osciloscopio |
| **Velocidad de detección** | 5-120 km/h | Prueba con vehículos |
| **Sensibilidad** | Motocicletas >150 kg | Prueba con motocicleta |
| **Inmunidad electromagnética** | Clase A según EN 50121 | Ensayo EMC |

#### 4.1.3 Componentes del Sistema

**Lazos Inductivos Principales:**
- 2 lazos por carril (entrada y salida)
- Cable detector 14 AWG, resistente a cortes
- Profundidad de instalación: 5-8 cm
- Sellado con material elastomérico

**Sensores de Respaldo:**
- Sensores ultrasónicos o microondas
- Alcance: 0.5-8 metros
- Precisión: ±2 cm
- Inmunidad a condiciones climáticas

#### 4.1.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Kapsch TrafficCom** - Modelo: ETC-D1
2. **TransCore** - Modelo: TC-30
3. **SICK** - Modelo: LMS511
4. **O equivalente** que cumpla especificaciones

### 4.2 Sistema de Clasificación Vehicular

#### 4.2.1 Descripción General

Sistema automático de clasificación vehicular según categorías tarifarias definidas en el contrato, utilizando sensores de altura, longitud y número de ejes.

#### 4.2.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Precisión clasificación** | ≥98% | Prueba 1000 vehículos conocidos |
| **Categorías soportadas** | Mín. 8 categorías | Configuración software |
| **Velocidad clasificación** | 5-80 km/h | Prueba dinámica |
| **Detección de ejes** | ≥99% precisión | Prueba con vehículos multi-eje |
| **Medición de altura** | ±5 cm precisión | Calibración con patrón |

#### 4.2.3 Tecnologías de Clasificación

**Sensores de Altura:**
- Tecnología: Láser o ultrasonido
- Rango: 0.5-4.5 metros
- Resolución: 1 cm
- Múltiples puntos de medición

**Sensores de Longitud:**
- Integrado con lazos inductivos
- Precisión: ±10 cm
- Rango: 2-25 metros

**Contadores de Ejes:**
- Sensores piezoeléctricos o neumáticos
- Sensibilidad: 500 kg por eje
- Velocidad: 5-120 km/h

### 4.3 Sistema DSRC (Dedicated Short Range Communications)

#### 4.3.1 Descripción General

Sistema de comunicación de corto alcance para lectura automática de TAGs vehiculares, cumpliendo con estándares IP/REV para interoperabilidad nacional.

#### 4.3.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Frecuencia operación** | 5.8 GHz (IP/REV) | Analizador de espectro |
| **Alcance de lectura** | 2-8 metros | Prueba de campo |
| **Tiempo de transacción** | <200 ms | Medición temporal |
| **Tasa de lectura exitosa** | ≥99.5% | Prueba estadística |
| **Potencia transmisión** | Según Resolución 546/2018 | Medición RF |

#### 4.3.3 Componentes DSRC

**Antena DSRC:**
- Polarización circular
- Ganancia: 6-9 dBi
- Patrón de radiación: Sectorial
- Protección IP65

**Unidad de Roadside (RSU):**
- Procesador ARM o equivalente
- Memoria: 512 MB RAM mínimo
- Interfaces: Ethernet, RS-232/485
- Certificación IP/REV obligatoria

### 4.4 Barreras Automáticas

#### 4.4.1 Descripción General

Barreras automáticas de alta velocidad para control de acceso vehicular, con sistemas de seguridad anti-colisión y operación en modo manual de contingencia.

#### 4.4.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Tiempo de apertura** | <1.5 segundos | Cronometraje |
| **Tiempo de cierre** | <2.0 segundos | Cronometraje |
| **Longitud de brazo** | 4-6 metros | Inspección física |
| **Ciclos de operación** | >2,000,000 ciclos | Certificado fabricante |
| **Fuerza de ruptura** | <15 kg | Prueba de seguridad |

#### 4.4.3 Características de Seguridad

**Sistema Anti-Colisión:**
- Sensores de presencia vehicular
- Detección de obstáculos
- Reversión automática
- Brazo frangible o articulado

**Operación Manual:**
- Liberación manual de emergencia
- Operación con llave
- Indicadores luminosos de estado
- Batería de respaldo 24V

#### 4.4.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **CAME** - Modelo: GARD 6500
2. **FAAC** - Modelo: 640
3. **BFT** - Modelo: MOOVI 60
4. **O equivalente** que cumpla especificaciones

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con Sistema Central

| Aspecto | Requisito | Verificación |
|:--------|:----------|:-------------|
| **Conexión a CCO** | TCP/IP sobre fibra óptica | Prueba de conectividad |
| **Tiempo de respuesta** | <500 ms | Prueba de latencia |
| **Disponibilidad** | ≥99.5% | Monitoreo 30 días |
| **Protocolo de datos** | IP/REV + propietario | Validación de mensajes |

### 5.2 Interfaz con Otros Sistemas

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **Sistema Financiero** | TCP/IP seguro | Transacciones, saldos |
| **Sistema de Videovigilancia** | Red IP | Eventos, alarmas |
| **Sistema de Pesaje** | RS-485/Ethernet | Datos de peso por eje |
| **Sistema de Información** | TCP/IP | Estados de carriles, tarifas |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Obras Civiles Requeridas

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Canalización lazos** | Ranuras 5x40 cm, sellado elastomérico | AASHTO |
| **Cimentación barreras** | Concreto 3000 PSI, 80x80x120 cm | ACI 318 |
| **Ductos comunicaciones** | PVC 4", profundidad 80 cm | RETIE |
| **Tierras eléctricas** | Resistencia <10 Ω | RETIE |

### 6.2 Acometidas Eléctricas

| Parámetro | Especificación |
|:----------|:---------------|
| **Tensión por carril** | 120/208 VAC, 60 Hz |
| **Corriente máxima** | 15 A por carril |
| **Calibre conductor** | AWG 12 mínimo |
| **Protección** | Breaker 20 A + DPS Clase II |

### 6.3 Conectividad

| Parámetro | Especificación |
|:----------|:---------------|
| **Medio principal** | Fibra óptica SM 9/125 μm |
| **Conectores** | SC/APC |
| **Respaldo** | Cable UTP Cat 6A |
| **Atenuación máxima** | <3 dB total |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas en Fábrica (FAT)

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Inspección visual** | Verificar acabados y etiquetado | Sin defectos visibles |
| **Prueba eléctrica** | Verificar consumo y aislamiento | Dentro de especificación ±5% |
| **Prueba funcional** | Verificar todas las funciones | 100% funciones operativas |
| **Prueba de comunicación** | Verificar protocolos | Mensajes IP/REV correctos |

### 7.2 Pruebas en Sitio (SAT)

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Prueba de detección** | Verificar tasa de detección | ≥99.9% en 1000 vehículos |
| **Prueba de clasificación** | Verificar precisión | ≥98% en muestra representativa |
| **Prueba de transacciones** | Verificar cobro electrónico | ≥99.5% transacciones exitosas |
| **Prueba de integración** | Verificar comunicación CCO | Latencia <500 ms |
| **Prueba de contingencia** | Verificar modo manual | Operación 100% funcional |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos del Fabricante

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Ficha técnica** | Especificaciones detalladas | Español | 3 copias + digital |
| **Manual de instalación** | Procedimiento paso a paso | Español | 2 copias + digital |
| **Manual de operación** | Guía de usuario | Español | 5 copias + digital |
| **Manual de mantenimiento** | Procedimientos preventivos/correctivos | Español | 3 copias + digital |
| **Planos de instalación** | Dimensiones, conexiones | - | Digital (DWG + PDF) |
| **Software de configuración** | Herramientas de setup | - | Licencias incluidas |

### 8.2 Certificados Requeridos

| Certificado | Emisor | Vigencia |
|:------------|:-------|:---------|
| **Homologación IP/REV** | ANI Colombia | Vigente |
| **Certificado CE** | Organismo Notificado | Vigente |
| **Certificado de calidad ISO 9001** | Organismo certificador | Vigente |
| **Certificado de origen** | Fabricante | - |

### 8.3 Garantías

| Elemento | Garantía Mínima | Observaciones |
|:---------|:----------------|:--------------|
| **Equipos electrónicos** | 36 meses | Desde puesta en servicio |
| **Barreras mecánicas** | 24 meses | Desde puesta en servicio |
| **Software** | 36 meses | Actualizaciones incluidas |
| **Lazos inductivos** | 60 meses | Contra defectos de fabricación |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza de equipos** | Mensual | Contratista |
| **Verificación funcional** | Semanal | Contratista |
| **Calibración de sensores** | Trimestral | Fabricante autorizado |
| **Actualización de software** | Según disponibilidad | Fabricante |
| **Prueba de respaldo UPS** | Mensual | Contratista |

### 9.2 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **Antenas DSRC** | 2 unidades | 15 días |
| **Controladores de barrera** | 2 unidades | 30 días |
| **Sensores de clasificación** | 4 unidades | 20 días |
| **Módulos de comunicación** | 2 unidades | 15 días |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Sistema DSRC completo | und | 24 | $8,500 | $204,000 |
| 2 | Sistema de clasificación | und | 24 | $12,000 | $288,000 |
| 3 | Barrera automática | und | 24 | $3,500 | $84,000 |
| 4 | Sistema de detección | und | 24 | $2,800 | $67,200 |
| 5 | Equipos de comunicación | und | 12 | $4,200 | $50,400 |
| 6 | UPS y respaldo eléctrico | und | 12 | $3,800 | $45,600 |
| 7 | Software y licencias | lote | 1 | $180,000 | $180,000 |
| 8 | Instalación y puesta en marcha | lote | 1 | $320,000 | $320,000 |
| 9 | Capacitación y documentación | lote | 1 | $45,000 | $45,000 |
| 10 | Contingencias (5%) | lote | 1 | $65,700 | $65,700 |
| | | | | **TOTAL** | **$1,349,900** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Validar especificaciones con fabricantes especializados
- [ ] Solicitar cotizaciones formales de al menos 3 proveedores
- [ ] Desarrollar protocolos de prueba detallados
- [ ] Crear cronograma de suministro e instalación
- [ ] Obtener pre-aprobación de homologación IP/REV
- [ ] Coordinar con diseño de obras civiles

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