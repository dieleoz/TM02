# T02: ANÁLISIS DE REQUISITOS - ESTACIONES DE PEAJE
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Estaciones de Peaje  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para las 3 estaciones de peaje del proyecto, incluyendo la reubicación obligatoria de La Gómez y la modernización de Morrison y Pailitas.

### 1.2 Alcance
Cubre todos los requisitos para el diseño, implementación y operación de las estaciones de peaje, incluyendo sistemas de recaudación, control de acceso, TAG/DSRC, vigilancia y integración con el CCO.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **TAG** | Transponder de Identificación Automática |
| **DSRC** | Dedicated Short Range Communications |
| **OBU** | On Board Unit (Unidad de Abordo) |
| **RSU** | Road Side Unit (Unidad de Carretera) |
| **AVI** | Automatic Vehicle Identification |
| **ALPR** | Automatic License Plate Recognition |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Recaudación de Peajes

**ID:** RF-001  
**Descripción:** Las estaciones deben recaudar peajes según tarifas oficiales ANI  
**Prioridad:** Alta  
**Fuente:** AT1, Tabla 2; AT2, Sección 2.1.g  

**Criterios de Aceptación:**
- Cobro manual en efectivo y tarjetas
- Cobro automático con TAG/DSRC
- Aplicación tarifas diferenciadas por categoría vehicular
- Registro completo de todas las transacciones
- Emisión de recibos/facturas

### 2.2 Control de Acceso Vehicular

**ID:** RF-002  
**Descripción:** Control de paso de vehículos con barreras automáticas  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 2.1.g  

**Criterios de Aceptación:**
- Barreras automáticas por carril
- Detección automática de vehículos
- Control manual de emergencia
- Registro de todos los accesos
- Integración con sistema recaudación

### 2.3 Identificación Automática de Vehículos

**ID:** RF-003  
**Descripción:** Identificación automática mediante TAG y reconocimiento de placas  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 2.1.o  

**Criterios de Aceptación:**
- Lectura TAG/DSRC a velocidad operacional
- Reconocimiento automático de placas (ALPR)
- Clasificación automática de vehículos
- Base de datos de vehículos autorizados
- Manejo de excepciones y violaciones

### 2.4 Vigilancia y Seguridad

**ID:** RF-004  
**Descripción:** Sistema integral de vigilancia para seguridad y evidencia  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 2.1.g  

**Criterios de Aceptación:**
- Cámaras CCTV en todos los carriles
- Grabación continua 24/7
- Transmisión en vivo al CCO
- Almacenamiento mínimo 30 días
- Calidad de imagen para identificación

### 2.5 Integración con CCO

**ID:** RF-005  
**Descripción:** Comunicación permanente con Centro de Control de Operación  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Transmisión datos recaudación en tiempo real
- Envío automático de alarmas y eventos
- Control remoto desde CCO
- Respaldo de datos centralizado
- Monitoreo estado operacional

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad sistema recaudación | 99% mensual | AT4 |
| **RNF-002** | MTBF equipos críticos | 8,760 horas | Buenas prácticas |
| **RNF-003** | MTTR reparaciones | 2 horas | AT4 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Tiempo transacción manual | < 30 segundos | AT4 |
| **RNF-005** | Tiempo transacción TAG | < 5 segundos | AT4 |
| **RNF-006** | Capacidad procesamiento | 1,000 veh/hora/carril | Estimado |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Seguridad recaudación | Bóvedas, cámaras, alarmas | AT2 |
| **RNF-008** | Cifrado transacciones | Encriptación datos financieros | Buenas prácticas |
| **RNF-009** | Backup transacciones | Respaldo cada 15 minutos | AT2 |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Interfaz operador | Intuitiva, capacitación < 16 horas | AT2 |
| **RNF-011** | Señalización usuarios | Clara y visible día/noche | Manual Señalización |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Mantenimiento preventivo | Acceso fácil a equipos | Buenas prácticas |
| **RNF-013** | Diagnóstico remoto | Monitoreo desde CCO | AT2 |
| **RNF-014** | Repuestos críticos | Stock mínimo 6 meses | AT2 |

### 3.6 Requisitos Ambientales

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Operación climática | -5°C a +50°C, 95% humedad | Condiciones locales |
| **RNF-016** | Protección IP | IP65 mínimo equipos exteriores | Buenas prácticas |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con CCO

**ID:** RI-001  
**Sistemas:** Estaciones Peaje ↔ CCO  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP, HTTPS  
**Datos Intercambiados:** Recaudación, alarmas, video, estado operacional  
**Frecuencia:** Tiempo real

### 4.2 Interface con Sistema TAG Nacional

**ID:** RI-002  
**Sistemas:** Estaciones Peaje ↔ Sistema TAG Nacional  
**Tipo:** Red de Datos  
**Protocolo:** DSRC, TCP/IP  
**Datos Intercambiados:** Validación TAG, saldos, listas negras  
**Frecuencia:** Por transacción

### 4.3 Interface con Bancos

**ID:** RI-003  
**Sistemas:** Estaciones Peaje ↔ Entidades Financieras  
**Tipo:** Red de Datos  
**Protocolo:** HTTPS, ISO 8583  
**Datos Intercambiados:** Transacciones tarjetas, autorizaciones  
**Frecuencia:** Por transacción

### 4.4 Interface con ANI

**ID:** RI-004  
**Sistemas:** Estaciones Peaje ↔ Sistemas ANI  
**Tipo:** VPN/Web  
**Protocolo:** HTTPS, XML  
**Datos Intercambiados:** Reportes recaudación, estadísticas  
**Frecuencia:** Diaria

### 4.5 Interface con Sistema Información Usuarios

**ID:** RI-005  
**Sistemas:** Estaciones Peaje ↔ Sistema Web  
**Tipo:** API REST  
**Protocolo:** HTTPS, JSON  
**Datos Intercambiados:** Tarifas, estado operacional  
**Frecuencia:** Cada hora

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Recaudación peajes | AT1 Tabla 2, AT2 2.1.g | Sistema recaudación | Alta |
| RF-002 | Funcional | Control acceso | AT2 Sección 2.1.g | Barreras, detectores | Alta |
| RF-003 | Funcional | Identificación automática | AT2 Sección 2.1.o | TAG/DSRC, ALPR | Alta |
| RF-004 | Funcional | Vigilancia | AT2 Sección 2.1.g | CCTV, grabación | Alta |
| RF-005 | Funcional | Integración CCO | AT2 Sección 3.1.7 | Comunicaciones | Alta |
| RNF-001 | No Funcional | Disponibilidad 99% | AT4 | Todos los sistemas | Alta |
| RNF-004 | No Funcional | Tiempo transacción | AT4 | Sistema recaudación | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Reubicación La Gómez obligatoria | Construcción nueva estación | AT1 Tabla 49 |
| **REST-002** | Interoperabilidad TAG nacional | Equipos certificados requeridos | AT2 |
| **REST-003** | Tarifas según resolución ANI | Sistema debe ser configurable | Contractual |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Comunicaciones estables con CCO | Operación aislada | Validar mes 2 |
| **SUP-002** | Personal operativo disponible | Servicio deficiente | Validar mes 1 |
| **SUP-003** | Certificación equipos TAG | No interoperabilidad | Validar fabricantes |

---

## 7. CASOS DE USO

### 7.1 Transacción TAG Exitosa

**ID:** CU-001  
**Actor:** Usuario con TAG  
**Descripción:** Paso exitoso por peaje con TAG  
**Precondiciones:** Vehículo con TAG válido, saldo suficiente  
**Flujo Normal:**
1. Vehículo se aproxima a carril TAG
2. Detector de lazo activa lectura
3. RSU lee TAG del vehículo
4. Sistema valida TAG y saldo
5. Clasifica vehículo automáticamente
6. Calcula tarifa correspondiente
7. Debita saldo del TAG
8. Abre barrera automáticamente
9. Registra transacción completa
10. Vehículo pasa y barrera se cierra

**Postcondiciones:** Transacción registrada, saldo actualizado  
**Flujos Alternativos:** Si TAG inválido, dirigir a carril manual

### 7.2 Manejo de Violación

**ID:** CU-002  
**Actor:** Sistema automático  
**Descripción:** Detección y manejo de violación de peaje  
**Precondiciones:** Sistema ALPR operativo, cámaras funcionando  
**Flujo Normal:**
1. Detector identifica vehículo sin pago
2. Sistema ALPR captura placa
3. Cámaras graban evidencia
4. Genera alarma automática
5. Notifica a operador y CCO
6. Registra violación en base datos
7. Inicia proceso administrativo
8. Envía información a autoridades

**Postcondiciones:** Violación documentada y reportada

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Recaudación 100% de vehículos que transitan
- [ ] Tiempo transacción manual < 30 segundos
- [ ] Tiempo transacción TAG < 5 segundos
- [ ] Exactitud recaudación 99.9%
- [ ] Detección violaciones 95%

### 8.2 Criterios de Performance

- [ ] Disponibilidad ≥ 99% mensual
- [ ] Capacidad 1,000 vehículos/hora/carril
- [ ] Lectura TAG exitosa 98%
- [ ] Reconocimiento placas 95%

### 8.3 Criterios de Calidad

- [ ] Equipos TAG certificados por ANI
- [ ] Cumplir normativa financiera
- [ ] Personal certificado en operación
- [ ] Procedimientos aprobados por ANI

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| Telecomunicaciones | Comunicación con CCO y bancos | Alta | ⏳ Pendiente |
| Energía Eléctrica | Suministro estable 24/7 | Alta | ⏳ Pendiente |
| Construcción estaciones | Infraestructura civil completada | Alta | ⏳ Pendiente |
| Certificación TAG | Equipos homologados ANI | Alta | ⏳ Pendiente |
| Personal operativo | Contratado y capacitado | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual estaciones (T03)
- [ ] Definir ubicación exacta La Gómez reubicada
- [ ] Validar requisitos con ANI
- [ ] Elaborar especificaciones técnicas equipos (T04)
- [ ] Tramitar certificaciones TAG
- [ ] Diseñar procedimientos operacionales

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Sistemas | Análisis inicial requisitos estaciones peaje |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas