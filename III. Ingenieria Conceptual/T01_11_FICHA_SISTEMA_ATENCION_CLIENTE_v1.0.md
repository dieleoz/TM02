# T01: FICHA DE SISTEMA - SISTEMA DE ATENCIÓN AL CLIENTE
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Sistema de Atención al Cliente  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Sistema de Atención al Cliente |
| **Categoría** | Servicios al Usuario - CRM |
| **Prioridad** | Alta |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT2 (Sección 3.3.3.3 - Atención al Cliente) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema integral de atención y servicio al cliente que proporciona múltiples canales de comunicación para recibir consultas, quejas, reclamos y sugerencias de los usuarios del corredor vial, garantizando respuesta oportuna y seguimiento adecuado.

### 2.2 Alcance del Sistema
- **Canales incluidos:**
  - Servicio telefónico gratuito 24/7
  - Libros de registro físicos
  - Correo electrónico
  - Sistema fax
  - Portal web integrado
  
- **Cobertura geográfica:** Atención a usuarios de todo el corredor
- **Integración con:** CCO, Sistema Web, Estaciones de Peaje

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Servicio Telefónico Gratuito
**Según AT2, Sección 3.3.3.3:**
"El Concesionario deberá contar con un servicio telefónico gratuito para atención al cliente las 24 horas del día, los 7 días de la semana"

### 3.2 Libros de Registro
**Según AT2, Sección 3.3.3.3:**
"Los libros de registro deberán estar disponibles permanentemente en el Centro de Control de Operación para que los usuarios puedan consignar sus observaciones, quejas y reclamos"

### 3.3 Canales Digitales
**Según AT2, Sección 3.3.3.3:**
"El Concesionario deberá contar con sistemas de correo electrónico y fax para recepción de comunicaciones de usuarios"

### 3.4 Sistema Web Integrado
**Según AT2, Sección 3.3.3.3:**
"Sistema web integrado para gestión de peajes y trámites relacionados con el proyecto"

### 3.5 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **Ley 1581/2012** | Protección datos personales | Manejo información |
| **Decreto 1377/2013** | Habeas data | Tratamiento datos |
| **SIC** | Superintendencia Industria y Comercio | Atención consumidor |
| **ISO 27001** | Seguridad información | Protección datos |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Call Center** | 1 centro | CCO o independiente | Atención telefónica 24/7 |
| **Puestos atención** | 6 puestos | Call center | Operadores telefónicos |
| **Sistema telefónico** | 1 sistema | Call center | PBX y líneas |
| **Libros registro** | 5 libros | CCO y peajes | Registro físico |
| **Sistema CRM** | 1 plataforma | Servidores | Gestión casos |
| **Portal web** | 1 plataforma | Cloud | Atención digital |
| **Sistema email** | 1 plataforma | Servidores | Correo electrónico |
| **Sistema fax** | 2 equipos | CCO y call center | Recepción fax |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Red IP | Ethernet | Casos, reportes, estadísticas |
| Sistema Web | API | REST/JSON | Casos web, consultas |
| Estaciones Peaje | Red IP | TCP/IP | Consultas tarifas, reclamos |
| Base de Datos | SQL | Database | Información usuarios |
| Sistema Info Usuarios | API | REST | Información actualizada |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Montaje call center** | 1 centro | $80,000 | $80,000 |
| **Puestos trabajo** | 6 puestos | $8,000 | $48,000 |
| **Sistema telefónico PBX** | 1 sistema | $25,000 | $25,000 |
| **Líneas telefónicas** | 10 líneas | $500 | $5,000 |
| **Sistema CRM** | 1 licencia | $40,000 | $40,000 |
| **Portal web atención** | 1 desarrollo | $30,000 | $30,000 |
| **Sistema email corporativo** | 1 plataforma | $15,000 | $15,000 |
| **Equipos fax** | 2 equipos | $1,000 | $2,000 |
| **Mobiliario y equipos** | 1 lote | $25,000 | $25,000 |
| **TOTAL CAPEX** | | | **$270,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal call center (18 operadores) | $216,000 |
| Supervisor atención cliente | $36,000 |
| Líneas telefónicas | $12,000 |
| Licencias CRM | $24,000 |
| Hosting portal web | $6,000 |
| Mantenimiento equipos | $18,000 |
| Servicios internet | $12,000 |
| **TOTAL OPEX/año** | **$324,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Caída sistema telefónico | Media | Alto | Redundancia líneas + respaldo |
| Sobrecarga llamadas | Media | Alto | Dimensionamiento adecuado + escalabilidad |
| Pérdida información | Baja | Alto | Respaldos + seguridad datos |
| Personal no capacitado | Media | Medio | Capacitación continua + protocolos |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT2:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **AC01** | Disponibilidad servicio telefónico | 99% | Continua |
| **AC02** | Tiempo respuesta llamadas | < 30 segundos | Por llamada |
| **AC03** | Tiempo resolución casos | < 48 horas | Por caso |
| **AC04** | Satisfacción cliente | > 85% | Mensual |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Diseñar procesos atención al cliente
- [ ] Elaborar especificaciones técnicas CRM (Template T04)
- [ ] Cotizar sistemas telefónicos y CRM
- [ ] Desarrollar protocolos atención
- [ ] Capacitar personal en atención al cliente

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Volumen estimado 500 llamadas/día
- Personal bilingüe (español/inglés) disponible
- Integración CRM con sistemas existentes
- Cumplimiento normativa protección datos

### 10.2 Dependencias
- Disponibilidad líneas telefónicas en la región
- Personal capacitado en atención al cliente
- Integración con sistemas CCO y web
- Cumplimiento normativa SIC

### 10.3 Restricciones
- Servicio 24/7/365 obligatorio
- Línea gratuita para usuarios
- Libros registro físicos en CCO
- Cumplimiento Ley 1581/2012 protección datos

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas