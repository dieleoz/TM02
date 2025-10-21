# T01: FICHA DE SISTEMA - AMBULANCIAS TAM
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Ambulancias TAM (Traslado Asistencial Medicalizado)  
**Responsable:** Ingeniero Biomédico  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Ambulancias TAM (Traslado Asistencial Medicalizado) |
| **Categoría** | Emergencias Médicas |
| **Prioridad** | Alta |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT2 (Sección 3.3.3.1.4, Dotación TAM) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema de atención médica prehospitalaria especializada para atender emergencias médicas en el corredor vial, con capacidad de soporte vital avanzado y traslado de pacientes críticos a centros de salud especializados.

### 2.2 Alcance del Sistema
- **Ambulancias incluidas:**
  - Mínimo 2 ambulancias TAM (1 por Base de Operación)
  - Equipamiento médico completo
  - Personal especializado
  
- **Cobertura geográfica:** 272.1 km del corredor completo
- **Integración con:** Bases de Operación, CCO, Centros de Salud

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Obligaciones del Contrato
**Según AT2, Sección 3.3.3.1.4:**
"Para proporcionar los servicios de atención médica, el Concesionario dispondrá de ambulancias propias o subcontratadas, en la cantidad y ubicación señalada en el numeral 3.3.3.1.1 de este Apéndice, que deberán contar con los medios para atender heridos del máximo nivel de gravedad"

### 3.2 Especificaciones de Personal
**Según AT2:**
"conformado en cada ambulancia por las siguientes personas:
• Un (1) médico general con entrenamiento certificado en soporte vital avanzado de mínimo 48 horas
• Un (1) auxiliar de enfermería o de urgencias médicas o tecnólogo o técnico en atención prehospitalaria con entrenamiento en soporte vital básico de mínimo 20 horas
• Un (1) conductor con mínimo 40 horas de capacitación en primeros auxilios"

### 3.3 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **Ministerio de Salud** | Dotación ambulancias TAM | Equipamiento médico |
| **Resolución 2003/2014** | Atención prehospitalaria | Personal y procedimientos |
| **NTC 3729** | Ambulancias terrestres | Especificaciones vehículo |

---

## 4. COMPONENTES PRINCIPALES

### 4.1 Vehículos y Equipamiento

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Ambulancias Tipo TAM** | 2 unidades | 1 por Base Operación | Atención médica avanzada |
| **Sistema oxígeno** | 2 sistemas | Por ambulancia | Soporte respiratorio |
| **Monitor ECG/Desfibrilador** | 2 unidades | Por ambulancia | Monitoreo cardíaco |
| **Respirador transporte** | 2 unidades | Por ambulancia | Ventilación asistida |
| **Bomba infusión** | 2 unidades | Por ambulancia | Medicación IV |
| **Equipo inmovilización** | 2 juegos | Por ambulancia | Trauma y rescate |

### 4.2 Personal Especializado

| Personal | Cantidad | Certificación Requerida | Función |
|:---------|:---------|:----------------------|:--------|
| **Médicos generales** | 6 personas | Soporte vital avanzado 48h | Atención médica |
| **Auxiliares enfermería** | 6 personas | Soporte vital básico 20h | Asistencia médica |
| **Conductores** | 6 personas | Primeros auxilios 40h | Conducción especializada |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Radio/IP | VHF/Ethernet | Emergencias, ubicación, estado |
| Bases de Operación | Radio | VHF/UHF | Coordinación operaciones |
| Centros de Salud | Radio/Teléfono | VHF/Celular | Información pacientes |
| Sistema Info Usuarios | Red IP | TCP/IP | Estado servicios médicos |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Ambulancias TAM** | 2 unidades | $150,000 | $300,000 |
| **Sistema oxígeno completo** | 2 sistemas | $8,000 | $16,000 |
| **Monitor ECG/Desfibrilador** | 2 unidades | $25,000 | $50,000 |
| **Respirador transporte** | 2 unidades | $15,000 | $30,000 |
| **Bomba infusión** | 2 unidades | $5,000 | $10,000 |
| **Equipo inmovilización** | 2 juegos | $3,000 | $6,000 |
| **Medicamentos e insumos** | Inicial | $8,000 | $8,000 |
| **Sistemas comunicación** | 2 sistemas | $5,000 | $10,000 |
| **Capacitación personal** | 18 personas | $2,000 | $36,000 |
| **TOTAL CAPEX** | | | **$466,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal médico (18 personas) | $432,000 |
| Combustible ambulancias | $24,000 |
| Mantenimiento vehículos | $36,000 |
| Medicamentos e insumos | $48,000 |
| Calibración equipos médicos | $12,000 |
| Seguros ambulancias | $18,000 |
| Capacitación continua | $24,000 |
| **TOTAL OPEX/año** | **$594,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Falta personal médico calificado | Media | Alto | Contratos con IPS + incentivos |
| Falla equipos médicos críticos | Baja | Alto | Mantenimiento preventivo + respaldo |
| Vencimiento medicamentos | Media | Medio | Control inventario + rotación |
| Accidente ambulancia | Baja | Alto | Capacitación + mantenimiento |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT2, Tabla 1:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **O5** | Tiempo de atención de accidentes y emergencias | Según AT4 | Por evento |
| **O8** | Tiempo de atención de accidentes y emergencias T | Según AT4 | Por evento |
| **TAM01** | Disponibilidad ambulancias | 100% | Continua |
| **TAM02** | Tiempo respuesta emergencias | < 15 minutos | Por evento |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Definir protocolos atención médica específicos
- [ ] Elaborar especificaciones técnicas ambulancias (Template T04)
- [ ] Cotizar ambulancias y equipos médicos
- [ ] Diseñar plan capacitación personal médico
- [ ] Establecer convenios con centros de salud

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Personal médico disponible en la región
- Centros de salud receptores con capacidad adecuada
- Equipos médicos con certificación vigente
- Comunicaciones radio disponibles en todo el corredor

### 10.2 Dependencias
- Contratación personal médico calificado
- Certificación equipos médicos
- Convenios con centros de salud
- Disponibilidad comunicaciones radio

### 10.3 Restricciones
- Servicio 24/7/365 sin interrupciones
- Personal con certificaciones vigentes
- Equipos médicos calibrados y certificados
- Cumplimiento protocolos Ministerio de Salud

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Biomédico