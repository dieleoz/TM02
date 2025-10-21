# T03: ARQUITECTURA CONCEPTUAL - AMBULANCIAS TAM
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Ambulancias TAM (Traslado Asistencial Medicalizado)  
**Responsable:** Ingeniero Biomédico  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual del sistema de Ambulancias TAM que proporcionará atención médica prehospitalaria avanzada en el corredor, integrándose con bases de operación, CCO y centros de salud regionales.

### 1.2 Alcance
Arquitectura completa para 2 ambulancias TAM con equipamiento médico avanzado, personal especializado, sistemas de comunicación y protocolos de atención para cobertura de 272.1 km del corredor.

### 1.3 Referencias
- T01_05: Ficha de Sistema - Ambulancias TAM
- T02_05: Análisis de Requisitos - Ambulancias TAM
- AT2: Sección 3.3.3.1.4
- Resolución 2003/2014 MinSalud

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    ┌─────────────────────────────────────┐
                    │              CCO                    │
                    │  ┌─────────────────────────────┐    │
                    │  │   Sistema Gestión TAM       │    │
                    │  │   - Despacho ambulancias    │    │
                    │  │   - Seguimiento GPS         │    │
                    │  │   - Coordinación hospitales │    │
                    │  └─────────────────────────────┘    │
                    └─────────────┬───────────────────────┘
                                  │ Radio VHF/UHF + IP
                    ┌─────────────┴───────────────────────┐
                    │        Red Comunicaciones           │
                    │     (Radio + Celular 4G)           │
                    └─┬─────────────────────┬─────────────┘
                      │                     │
        ┌─────────────┴─────────┐    ┌─────┴─────────────┐
        │   Base Operación 1    │    │  Base Operación 2 │
        │   (Norte - km 90)     │    │  (Sur - km 180)   │
        │                       │    │                   │
        │  ┌─────────────────┐  │    │ ┌─────────────────┐│
        │  │ Ambulancia TAM-1│  │    │ │ Ambulancia TAM-2││
        │  │ - Equipo médico │  │    │ │ - Equipo médico ││
        │  │ - Personal 24/7 │  │    │ │ - Personal 24/7 ││
        │  │ - GPS/Radio     │  │    │ │ - GPS/Radio     ││
        │  └─────────────────┘  │    │ └─────────────────┘│
        └───────────────────────┘    └───────────────────┘
                      │                        │
        ┌─────────────┴─────────┐    ┌─────────┴─────────┐
        │  Centros Salud Norte  │    │ Centros Salud Sur │
        │  - Hospital Barranca  │    │ - Hospital Aguachica│
        │  - Clínica Sabana     │    │ - ESE Curumaní    │
        └───────────────────────┘    └───────────────────┘
```

**Descripción del diagrama:**
Sistema distribuido con 2 ambulancias TAM ubicadas estratégicamente en bases de operación, comunicación redundante (radio + celular), coordinación centralizada desde CCO y enlaces directos con centros de salud receptores.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Ambulancias Tipo TAM** | Atención médica avanzada | Vehículo 4x2, compartimento paciente | 2 unidades |
| **Monitor ECG/Desfibrilador** | Monitoreo cardíaco | 12 derivaciones, desfibrilación | 2 unidades |
| **Respirador Transporte** | Ventilación asistida | Modos IPPV/SIMV, batería 4h | 2 unidades |
| **Sistema Oxígeno** | Soporte respiratorio | 2 cilindros M, reguladores | 2 sistemas |
| **Bomba Infusión** | Medicación IV | Doble canal, alarmas | 2 unidades |
| **Equipo Inmovilización** | Trauma y rescate | Camilla, collarín, férulas | 2 juegos |
| **Sistema Comunicaciones** | Radio + GPS + Celular | VHF/UHF + 4G + GPS | 2 sistemas |
| **Personal Médico** | Atención especializada | Médico + Auxiliar + Conductor | 6 personas/turno |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Comunicaciones

- **Tipo de topología:** Estrella con redundancia
- **Protocolo principal:** Radio VHF/UHF + TCP/IP sobre 4G
- **Cobertura:** 100% del corredor con redundancia
- **Redundancia:** Sí - Radio + Celular + Satelital (emergencia)

### 3.2 Diagrama de Topología

```
                     CCO (Centro Control)
                    ┌─────────────────────┐
                    │  Radio Base VHF     │
                    │  + Sistema Despacho │
                    └──────────┬──────────┘
                               │ Radio VHF/UHF
                    ┌──────────┴──────────┐
                    │   Red Radio Troncal │
                    │   + Cobertura 4G    │
                    └─┬─────────┬─────────┘
                      │         │
            ┌─────────┴─┐   ┌───┴─────────┐
            │Base Norte │   │  Base Sur   │
            │Radio Rep. │   │ Radio Rep.  │
            └─┬─────────┘   └─┬───────────┘
              │               │
        ┌─────┴─────┐   ┌─────┴─────┐
        │TAM-1      │   │TAM-2      │
        │VHF+4G+GPS │   │VHF+4G+GPS │
        └───────────┘   └───────────┘
              │               │
        ┌─────┴─────┐   ┌─────┴─────┐
        │Hospitales │   │Hospitales │
        │Norte      │   │Sur        │
        └───────────┘   └───────────┘
```

### 3.3 Distribución Física

**Ubicaciones principales:**
- **Base Norte (km 90):** TAM-1 + Personal turno A/B/C
- **Base Sur (km 180):** TAM-2 + Personal turno A/B/C
- **Cobertura:** Tiempo respuesta < 15 min en 90% del corredor

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo de Atención de Emergencia

```
1. [Llamada emergencia → CCO]
   ↓ Sistema despacho
2. [CCO despacha ambulancia más cercana]
   ↓ Radio VHF + GPS
3. [TAM se dirige al sitio]
   ↓ Comunicación continua
4. [Atención médica en sitio]
   ↓ Protocolos SVA
5. [Traslado con monitoreo]
   ↓ Comunicación hospital
6. [Entrega en centro salud]
   ↓ Reporte médico
7. [Regreso a base]
```

**Descripción del flujo:**
1. **Activación:** Llamada de emergencia recibida en CCO
2. **Despacho:** Sistema selecciona ambulancia más cercana disponible
3. **Respuesta:** TAM se dirige con comunicación continua CCO
4. **Atención:** Equipo médico proporciona soporte vital avanzado
5. **Traslado:** Paciente trasladado con monitoreo continuo
6. **Entrega:** Reporte médico completo al centro receptor
7. **Disponibilidad:** TAM regresa a base para próxima emergencia

### 4.2 Tipos de Datos

| Tipo de Dato | Formato | Volumen Estimado | Retención |
|:-------------|:--------|:-----------------|:----------|
| **Ubicación GPS** | NMEA | 50 MB/mes | 1 año |
| **Comunicaciones radio** | Audio digital | 2 GB/mes | 6 meses |
| **Reportes médicos** | PDF/Texto | 100 MB/mes | 10 años |
| **Estadísticas servicio** | CSV | 10 MB/mes | 5 años |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Ambulancias** | N+1 (2 para 1 requerida) | 2 ambulancias operativas | Disponibilidad 100% |
| **Personal médico** | 3 turnos por ambulancia | 18 personas total | Cobertura 24/7/365 |
| **Comunicaciones** | Triple redundancia | Radio+4G+Satelital | Comunicación crítica |
| **Equipos médicos** | Backup en bases | Equipos de respaldo | Continuidad servicio |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad:** 100% (una ambulancia siempre operativa)
- **Tiempo respuesta:** < 15 minutos en 90% de casos
- **MTBF equipos:** 2,000 horas
- **MTTR:** 2 horas para equipos críticos
- **Cobertura:** 100% del corredor

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Ambulancia individual** | Sí | Segunda ambulancia disponible |
| **Personal médico** | Sí | Personal de respaldo + turnos |
| **Comunicaciones** | No | Triple redundancia |
| **Equipos médicos** | Sí | Equipos backup en bases |

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- Ambulancias con sistemas antirrobo
- Equipos médicos asegurados en compartimento
- Personal con chalecos reflectivos y EPP
- Comunicación permanente con CCO
- Protocolos de seguridad en sitio

### 6.2 Seguridad Operacional

- Personal certificado en SVA/SVB
- Protocolos médicos estandarizados
- Equipos calibrados y certificados
- Medicamentos controlados con trazabilidad
- Auditorías médicas regulares

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| Resolución 2003/2014 | Atención prehospitalaria |
| NTC 3729 | Ambulancias terrestres |
| Ley 1562/2012 | Sistema riesgos laborales |
| INVIMA | Control medicamentos |

---

## 7. ARQUITECTURA DE EQUIPAMIENTO MÉDICO

### 7.1 Configuración por Ambulancia

```
┌─────────────────────────────────┐
│         COMPARTIMENTO           │
│                                 │
│  ┌─────────┐    ┌─────────────┐ │
│  │Monitor  │    │ Respirador  │ │
│  │ECG/Defib│    │ Transporte  │ │
│  └─────────┘    └─────────────┘ │
│                                 │
│  ┌─────────┐    ┌─────────────┐ │
│  │Sistema  │    │ Bomba       │ │
│  │Oxígeno  │    │ Infusión    │ │
│  └─────────┘    └─────────────┘ │
│                                 │
│  ┌─────────────────────────────┐ │
│  │    Equipo Inmovilización    │ │
│  │  + Medicamentos + Insumos   │ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

### 7.2 Especificaciones Técnicas Críticas

| Equipo | Especificación | Autonomía | Certificación |
|:-------|:---------------|:----------|:--------------|
| **Monitor ECG** | 12 derivaciones, desfibrilador | 4 horas | FDA/CE |
| **Respirador** | IPPV/SIMV, alarmas | 4 horas | ISO 13485 |
| **Sistema O2** | 2 cilindros M, 680L c/u | 4 horas | INVIMA |
| **Bomba infusión** | Doble canal, 0.1-999 ml/h | 8 horas | FDA/CE |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | IF-001 | Radio VHF/UHF | Alta | Despacho, ubicación, estado |
| **Bases Operación** | IF-002 | Radio/Presencial | Alta | Personal, equipos, logística |
| **Centros Salud** | IF-003 | Radio/Teléfono | Alta | Información paciente, ETA |
| **Sistema Info Usuarios** | IF-004 | TCP/IP | Media | Estado servicios médicos |
| **Red Telecomunicaciones** | IF-005 | 4G/Satelital | Alta | Comunicaciones backup |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Ambulancias TAM** | 2 | 2 | 3 | Bases para 3 |
| **Personal médico** | 18 | 18 | 27 | Estructura escalable |
| **Emergencias/mes** | 50 | 80 | 120 | Capacidad 150 |
| **Tiempo respuesta** | <15 min | <12 min | <10 min | Optimización continua |

### 9.2 Estrategia de Crecimiento

El sistema permite agregar una tercera ambulancia en base central (km 135) sin cambios arquitectónicos mayores. Requiere únicamente:
- Ampliación de una base existente
- Personal médico adicional (9 personas)
- Equipos médicos estándar
- Integración al sistema de comunicaciones

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Vehículo** | Ambulancia Tipo TAM | NTC 3729 | Normativa colombiana |
| **Comunicaciones** | Radio VHF/UHF | Digital | Cobertura y confiabilidad |
| **GPS** | Sistema navegación | Tiempo real | Seguimiento y despacho |
| **Equipos médicos** | Certificados FDA/CE | Actuales | Calidad y confiabilidad |

### 10.2 Interoperabilidad

- **Con sistemas salud:** Protocolos estándar MinSalud
- **Con otros concesionarios:** Radio en frecuencias comunes
- **Con autoridades:** Integración Policía/Bomberos

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Ambulancias Básicas

**Descripción:** Ambulancias tipo TBS (Transporte Básico de Salud)

**Ventajas:**
- Menor costo inicial
- Personal menos especializado
- Mantenimiento más simple

**Desventajas:**
- No cumple requisitos contractuales
- Limitaciones atención crítica
- Mayor mortalidad

**Costo estimado:** $200,000

### 11.2 Alternativa 2: Ambulancias TAM ⭐ **RECOMENDADA**

**Descripción:** Ambulancias con soporte vital avanzado según AT2

**Ventajas:**
- Cumple requisitos contractuales
- Atención médica avanzada
- Personal especializado
- Mejor pronóstico pacientes

**Desventajas:**
- Mayor costo inicial
- Personal más especializado
- Mantenimiento complejo

**Costo estimado:** $466,000

**Justificación de selección:** Cumplimiento contractual obligatorio y mejor atención médica para usuarios del corredor.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Contratación personal médico | 3 meses | Certificaciones vigentes |
| **Fase 2** | Adquisición ambulancias y equipos | 4 meses | Especificaciones aprobadas |
| **Fase 3** | Capacitación personal | 2 meses | Personal contratado |
| **Fase 4** | Instalación equipos comunicaciones | 1 mes | Bases operativas |
| **Fase 5** | Pruebas y certificación | 1 mes | Todo instalado |
| **Fase 6** | Puesta en operación | 1 mes | Pruebas aprobadas |

### 12.2 Hitos Críticos

- **H1:** Personal médico contratado y certificado - Mes 3
- **H2:** Primera ambulancia operativa - Mes 8
- **H3:** Sistema completo 24/7 - Mes 12

---

## 13. PRÓXIMOS PASOS

- [ ] Establecer convenios con centros de salud regionales
- [ ] Iniciar proceso contratación personal médico certificado
- [ ] Desarrollar especificaciones técnicas ambulancias (T04)
- [ ] Definir protocolos médicos específicos del corredor
- [ ] Estimar costos detallados equipos médicos
- [ ] Crear plan capacitación continua personal

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Biomédico | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Biomédico