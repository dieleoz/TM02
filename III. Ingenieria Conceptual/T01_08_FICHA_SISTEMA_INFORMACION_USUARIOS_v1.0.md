# T01: FICHA DE SISTEMA - SISTEMA DE INFORMACIÓN A USUARIOS
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Sistema de Información a Usuarios  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Sistema de Información a Usuarios |
| **Categoría** | ITS - Comunicaciones y Servicios |
| **Prioridad** | Alta |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT2 (Sección 3.3.3.2 - Información a Usuarios) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema integral de comunicación que mantiene informados a los usuarios del corredor vial sobre condiciones de tráfico, incidentes, trabajos en la vía, tarifas de peaje y servicios disponibles, a través de múltiples canales de comunicación.

### 2.2 Alcance del Sistema
- **Componentes incluidos:**
  - Página Web institucional
  - Boletín trimestral impreso
  - Emisora de radio FM
  - Paneles LED (ya incluidos en T01_04)
  
- **Cobertura geográfica:** 272.1 km del corredor completo
- **Integración con:** CCO, Paneles LED, Bases de Operación

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Página Web (Obligatoria)
**Según AT2, Sección 3.3.3.2.1:**
"El Concesionario deberá mantener una página web con información actualizada sobre el estado de la vía, incidentes, trabajos programados, tarifas vigentes y servicios disponibles. La información deberá actualizarse en tiempo real y estar disponible 24 horas al día, 7 días a la semana"

**Actualización:** "La información deberá actualizarse máximo cada hora"

### 3.2 Boletín Trimestral (Obligatorio)
**Según AT2, Sección 3.3.3.2.2:**
"El Concesionario deberá elaborar y distribuir gratuitamente un boletín trimestral con información sobre el proyecto, avances de obra, servicios disponibles y noticias de interés para los usuarios"

### 3.3 Emisora de Radio (Obligatoria)
**Según AT2, Sección 3.3.3.2.3:**
"El Concesionario deberá contar con una emisora de radio que transmita información sobre el estado de la vía, incidentes y servicios disponibles. La información deberá transmitirse mínimo 4 veces por hora y tener cobertura en toda la extensión de la vía"

### 3.4 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **MinTIC** | Regulación telecomunicaciones | Emisora de radio |
| **ANTV** | Autoridad Nacional TV | Licencias radiodifusión |
| **Ley 1341/2009** | TIC en Colombia | Marco regulatorio |
| **ISO 27001** | Seguridad información | Protección datos web |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Página Web** | 1 plataforma | Hosting cloud | Información 24/7 |
| **Servidores web** | 2 servidores | Data center | Hosting redundante |
| **Aplicación móvil** | 1 app | Stores | Información móvil |
| **Emisora FM** | 1 estación | Por definir | Radio información |
| **Equipos transmisión** | 3 repetidoras | Cobertura total | Señal radio |
| **Estudio radio** | 1 instalación | CCO o independiente | Producción contenido |
| **Boletín trimestral** | 4 ediciones/año | Distribución regional | Información impresa |
| **Sistema gestión contenido** | 1 plataforma | CCO | Administración info |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Red IP | Ethernet/API | Estado vía, incidentes, tráfico |
| Paneles LED | Red IP | TCP/IP | Mensajes coordinados |
| Estaciones Peaje | Red IP | API REST | Tarifas, estado operacional |
| Bases de Operación | Red IP/Radio | Ethernet/VHF | Información emergencias |
| Sistema Atención Cliente | Red IP | API | Consultas y reclamos |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Desarrollo página web** | 1 plataforma | $80,000 | $80,000 |
| **Desarrollo app móvil** | 1 aplicación | $60,000 | $60,000 |
| **Servidores web** | 2 servidores | $15,000 | $30,000 |
| **Licencia emisora FM** | 1 licencia | $50,000 | $50,000 |
| **Equipos transmisión radio** | 3 repetidoras | $40,000 | $120,000 |
| **Estudio de radio** | 1 instalación | $80,000 | $80,000 |
| **Sistema gestión contenido** | 1 plataforma | $40,000 | $40,000 |
| **Equipos producción** | 1 lote | $30,000 | $30,000 |
| **Instalación y configuración** | 1 proyecto | $60,000 | $60,000 |
| **TOTAL CAPEX** | | | **$550,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal comunicaciones (4 personas) | $120,000 |
| Hosting y servicios web | $24,000 |
| Licencias software | $18,000 |
| Producción boletín trimestral | $32,000 |
| Operación emisora radio | $48,000 |
| Mantenimiento equipos | $36,000 |
| Servicios internet y comunicaciones | $24,000 |
| **TOTAL OPEX/año** | **$302,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Caída página web | Media | Alto | Servidores redundantes + CDN |
| Pérdida licencia radio | Baja | Alto | Cumplimiento normativo + respaldos |
| Ciberataques | Media | Alto | Seguridad multicapa + respaldos |
| Falta personal especializado | Media | Medio | Contratos + capacitación |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT2:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **SIU01** | Disponibilidad página web | 99% mensual | Continua |
| **SIU02** | Actualización información | < 1 hora | Por evento |
| **SIU03** | Cobertura emisora radio | 100% corredor | Mensual |
| **SIU04** | Frecuencia transmisión radio | 4 veces/hora mínimo | Continua |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Tramitar licencia emisora FM ante MinTIC
- [ ] Elaborar especificaciones técnicas plataformas (Template T04)
- [ ] Cotizar equipos transmisión radio
- [ ] Diseñar arquitectura web y móvil
- [ ] Definir ubicación óptima emisora radio

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Disponibilidad frecuencia FM en la región
- Cobertura 3G/4G para aplicación móvil
- Personal especializado en comunicaciones disponible
- Integración API con sistemas existentes

### 10.2 Dependencias
- Aprobación licencia emisora por MinTIC
- Disponibilidad internet banda ancha
- Integración con CCO para datos tiempo real
- Coordinación con autoridades locales

### 10.3 Restricciones
- Cumplimiento normativa MinTIC para radio
- Actualización web máximo cada hora
- Transmisión radio mínimo 4 veces/hora
- Distribución gratuita boletín trimestral

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas