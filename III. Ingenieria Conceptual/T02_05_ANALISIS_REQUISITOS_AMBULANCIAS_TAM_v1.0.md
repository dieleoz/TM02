# T02: ANÁLISIS DE REQUISITOS - AMBULANCIAS TAM
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Ambulancias TAM (Traslado Asistencial Medicalizado)  
**Responsable:** Ingeniero Biomédico  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para el sistema de Ambulancias TAM del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y normativa del Ministerio de Salud de Colombia.

### 1.2 Alcance
Análisis completo de requisitos para 2 ambulancias TAM con equipamiento médico avanzado, personal especializado y protocolos de atención prehospitalaria para 272.1 km del corredor.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **TAM** | Traslado Asistencial Medicalizado |
| **SVA** | Soporte Vital Avanzado |
| **SVB** | Soporte Vital Básico |
| **ECG** | Electrocardiograma |
| **DEA** | Desfibrilador Externo Automático |
| **IPS** | Institución Prestadora de Servicios de Salud |
| **SAMU** | Sistema de Atención Médica de Urgencias |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Atención Médica Prehospitalaria Avanzada

**ID:** RF-001  
**Descripción:** Las ambulancias deben proporcionar atención médica de soporte vital avanzado para pacientes críticos en el sitio del incidente  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.1.4  

**Criterios de Aceptación:**
- Capacidad de intubación endotraqueal
- Administración de medicamentos IV avanzados
- Monitoreo cardíaco continuo con ECG de 12 derivaciones
- Desfibrilación y cardioversión eléctrica
- Ventilación mecánica durante traslado

### 2.2 Traslado Seguro de Pacientes Críticos

**ID:** RF-002  
**Descripción:** Sistema debe garantizar traslado seguro y estable de pacientes críticos a centros de salud especializados  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.1.4  

**Criterios de Aceptación:**
- Estabilización hemodinámica durante traslado
- Monitoreo continuo de signos vitales
- Comunicación con centro receptor
- Inmovilización adecuada según tipo de trauma
- Ambiente estéril y controlado

### 2.3 Respuesta Rápida a Emergencias

**ID:** RF-003  
**Descripción:** El sistema debe garantizar tiempo de respuesta óptimo desde recepción de llamada hasta llegada al sitio  
**Prioridad:** Alta  
**Fuente:** AT4, Indicadores O5 y O8  

**Criterios de Aceptación:**
- Tiempo respuesta < 15 minutos en 90% de casos
- Disponibilidad 24/7/365
- Comunicación directa con CCO
- Localización GPS en tiempo real
- Activación automática por sensores

### 2.4 Coordinación con Centros de Salud

**ID:** RF-004  
**Descripción:** Las ambulancias deben coordinar efectivamente con centros de salud receptores para garantizar continuidad de atención  
**Prioridad:** Media  
**Fuente:** Resolución 2003/2014  

**Criterios de Aceptación:**
- Comunicación directa con urgencias
- Transmisión de datos vitales en tiempo real
- Confirmación de disponibilidad de camas
- Reporte médico completo al entregar paciente
- Seguimiento post-traslado

### 2.5 Gestión de Inventario Médico

**ID:** RF-005  
**Descripción:** Sistema debe mantener inventario completo y actualizado de medicamentos e insumos médicos  
**Prioridad:** Media  
**Fuente:** Ministerio de Salud  

**Criterios de Aceptación:**
- Control de vencimientos automático
- Reposición automática de insumos críticos
- Trazabilidad de medicamentos controlados
- Inventario mínimo garantizado
- Reportes de consumo mensuales

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad ambulancias | 100% | AT2, TAM01 |
| **RNF-002** | MTBF equipos médicos | 2,000 horas | Estándar médico |
| **RNF-003** | MTTR equipos críticos | 2 horas | AT2 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Tiempo respuesta emergencias | < 15 minutos | AT4, TAM02 |
| **RNF-005** | Velocidad máxima ambulancia | 120 km/h | NTC 3729 |
| **RNF-006** | Autonomía oxígeno | 4 horas mínimo | Estándar TAM |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Certificación personal médico | SVA 48h médicos, SVB 20h auxiliares | AT2 |
| **RNF-008** | Calibración equipos médicos | Cada 6 meses con certificado | Ministerio Salud |
| **RNF-009** | Medicamentos controlados | Custodia y trazabilidad completa | INVIMA |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Interface equipos médicos | Intuitiva para personal certificado | Estándar médico |
| **RNF-011** | Accesibilidad paciente | Rampa hidráulica, camilla regulable | NTC 3729 |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Mantenimiento vehículos | Cada 10,000 km o 6 meses | Fabricante |
| **RNF-013** | Calibración equipos | Certificada por laboratorio acreditado | Ministerio Salud |
| **RNF-014** | Repuestos críticos | Stock mínimo 30 días | AT2 |

### 3.6 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Capacidad crecimiento | +1 ambulancia sin cambios mayores | Buenas prácticas |
| **RNF-016** | Equipos intercambiables | Compatibilidad entre ambulancias | Buenas prácticas |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con CCO

**ID:** RI-001  
**Sistemas:** Ambulancias TAM ↔ CCO  
**Tipo:** Radio y Red de Datos  
**Protocolo:** VHF/UHF + TCP/IP  
**Datos Intercambiados:** Ubicación GPS, estado, emergencias, comunicación voz  
**Frecuencia:** Tiempo real

### 4.2 Interface con Bases de Operación

**ID:** RI-002  
**Sistemas:** Ambulancias TAM ↔ Bases Operación  
**Tipo:** Radio  
**Protocolo:** VHF/UHF  
**Datos Intercambiados:** Coordinación operaciones, estado ambulancias  
**Frecuencia:** Continua durante servicio

### 4.3 Interface con Centros de Salud

**ID:** RI-003  
**Sistemas:** Ambulancias TAM ↔ Hospitales/Clínicas  
**Tipo:** Radio y Celular  
**Protocolo:** VHF + GSM/4G  
**Datos Intercambiados:** Datos paciente, signos vitales, ETA  
**Frecuencia:** Durante traslado

### 4.4 Interface con Sistema de Información

**ID:** RI-004  
**Sistemas:** Ambulancias TAM ↔ Sistema Info Usuarios  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP  
**Datos Intercambiados:** Estado servicios médicos, disponibilidad  
**Frecuencia:** Cada 5 minutos

### 4.5 Interface con Equipos Médicos

**ID:** RI-005  
**Sistemas:** Personal Médico ↔ Equipos TAM  
**Tipo:** Física y Digital  
**Protocolo:** Interfaces estándar médicas  
**Datos Intercambiados:** Signos vitales, parámetros ventilación  
**Frecuencia:** Continua durante atención

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Atención médica SVA | AT2, 3.3.3.1.4 | Equipos médicos | Alta |
| RF-002 | Funcional | Traslado seguro pacientes | AT2, 3.3.3.1.4 | Ambulancia completa | Alta |
| RF-003 | Funcional | Respuesta rápida < 15 min | AT4, TAM02 | Sistema completo | Alta |
| RF-004 | Funcional | Coordinación centros salud | Resolución 2003/2014 | Comunicaciones | Media |
| RF-005 | Funcional | Gestión inventario médico | Ministerio Salud | Sistema logístico | Media |
| RNF-001 | No Funcional | Disponibilidad 100% | AT2, TAM01 | Sistema completo | Alta |
| RNF-004 | No Funcional | Tiempo respuesta < 15 min | AT4, TAM02 | Operaciones | Alta |
| RNF-007 | No Funcional | Certificación personal | AT2 | Personal médico | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Personal con certificaciones vigentes | Limitación contratación | AT2, Contractual |
| **REST-002** | Equipos con certificación médica | Selección fabricantes específicos | Ministerio Salud |
| **REST-003** | Servicio 24/7/365 sin interrupciones | Redundancia personal y equipos | AT2, Contractual |
| **REST-004** | Cumplimiento protocolos ministerio | Procedimientos estandarizados | Legal |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Personal médico disponible en región | Alto (no hay servicio) | Estudio mercado laboral |
| **SUP-002** | Centros salud con capacidad adecuada | Medio (traslados largos) | Convenios con IPS |
| **SUP-003** | Comunicaciones radio estables | Alto (coordinación deficiente) | Pruebas cobertura |
| **SUP-004** | Suministro medicamentos garantizado | Medio (limitación atención) | Contratos proveedores |

---

## 7. CASOS DE USO

### 7.1 Atención de Emergencia Cardíaca

**ID:** CU-001  
**Actor:** Equipo Médico TAM  
**Descripción:** Atender paciente con infarto agudo de miocardio en vía  
**Precondiciones:** Ambulancia disponible, personal certificado  
**Flujo Normal:**
1. CCO recibe llamada de emergencia cardíaca
2. Despacha ambulancia TAM más cercana
3. Equipo llega al sitio en < 15 minutos
4. Médico evalúa paciente y confirma IAM
5. Inicia protocolo SVA: ECG 12 derivaciones, vía IV, medicamentos
6. Contacta centro cardíaco receptor
7. Traslada con monitoreo continuo
8. Entrega paciente con reporte completo

**Postcondiciones:** Paciente estabilizado en centro especializado  
**Flujos Alternativos:** Si paro cardíaco, inicia RCP avanzado inmediatamente

### 7.2 Trauma Múltiple por Accidente

**ID:** CU-002  
**Actor:** Equipo Médico TAM  
**Descripción:** Atender víctimas de accidente de tránsito con trauma múltiple  
**Precondiciones:** Ambulancia operativa, equipos de inmovilización  
**Flujo Normal:**
1. Activación por sensores automáticos o llamada
2. Despacho inmediato con información preliminar
3. Evaluación primaria en sitio (ABCDE)
4. Inmovilización cervical y corporal
5. Control hemorragias y vías aéreas
6. Comunicación con trauma center
7. Traslado con soporte vital continuo
8. Entrega con Glasgow y signos vitales

**Postcondiciones:** Paciente en trauma center para cirugía  
**Flujos Alternativos:** Si múltiples víctimas, solicita segunda ambulancia

### 7.3 Mantenimiento Preventivo Equipos

**ID:** CU-003  
**Actor:** Técnico Biomédico  
**Descripción:** Realizar mantenimiento preventivo de equipos médicos  
**Precondiciones:** Ambulancia fuera de servicio, técnico certificado  
**Flujo Normal:**
1. Programa mantenimiento según cronograma
2. Retira ambulancia de servicio operativo
3. Ejecuta checklist de mantenimiento
4. Calibra equipos según especificaciones
5. Actualiza registros de mantenimiento
6. Certifica equipos operativos
7. Devuelve ambulancia a servicio

**Postcondiciones:** Ambulancia certificada para servicio  
**Flujos Alternativos:** Si falla detectada, programa reparación

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Ambulancias equipadas según listado Ministerio de Salud
- [ ] Personal médico con certificaciones SVA/SVB vigentes
- [ ] Tiempo respuesta < 15 minutos en 90% de emergencias
- [ ] Comunicación efectiva con centros de salud
- [ ] Inventario médico completo y actualizado

### 8.2 Criterios de Performance

- [ ] Disponibilidad 100% (una ambulancia siempre operativa)
- [ ] MTBF equipos médicos ≥ 2,000 horas
- [ ] Autonomía oxígeno ≥ 4 horas
- [ ] Velocidad máxima 120 km/h en condiciones seguras

### 8.3 Criterios de Calidad

- [ ] Certificación NTC 3729 para ambulancias
- [ ] Equipos médicos con registro INVIMA
- [ ] Personal con certificados vigentes
- [ ] Protocolos según Resolución 2003/2014

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Personal Médico Certificado** | Contratación previa a operación | Alta | ⏳ Pendiente |
| **Centros de Salud Receptores** | Convenios operativos | Alta | ⏳ Pendiente |
| **Sistema Comunicaciones** | Debe estar operativo | Alta | ⏳ Pendiente |
| **Bases de Operación** | Estacionamiento y mantenimiento | Alta | ⏳ Pendiente |
| **Suministro Medicamentos** | Contratos con distribuidores | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Definir protocolos médicos específicos del corredor
- [ ] Validar requisitos con médicos especialistas
- [ ] Establecer convenios con centros de salud regionales
- [ ] Elaborar especificaciones técnicas ambulancias (T04)
- [ ] Iniciar proceso de contratación personal médico

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Biomédico | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Biomédico