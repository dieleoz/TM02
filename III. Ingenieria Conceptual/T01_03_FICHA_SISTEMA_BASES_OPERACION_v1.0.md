# T01: FICHA DE SISTEMA - BASES DE OPERACIÓN
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Bases de Operación  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Bases de Operación |
| **Categoría** | Emergencias y Atención a Usuarios |
| **Prioridad** | Crítica |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT2 (Sección 3.3.3.1.1, Tabla 2) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Centros operacionales estratégicamente ubicados para la atención inmediata de incidentes, accidentes y emergencias en el corredor vial, garantizando tiempos de respuesta óptimos y servicios de auxilio mecánico y médico 24/7/365.

### 2.2 Alcance del Sistema
- **Bases incluidas:**
  - Base de Operación Norte
  - Base de Operación Sur
  
- **Cobertura geográfica:** 272.1 km del corredor (cobertura completa)
- **Integración con:** CCO, Ambulancias TAM, Sistema de Información

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Obligaciones del Contrato
**Según AT2, Sección 3.3.3.1.1 - Bases de Operación:**
"Para efectuar el monitoreo de la vía y disponer la atención de incidentes, accidentes y emergencias, el Concesionario dispondrá de mínimo dos (2) Bases de Operaciones"

### 3.2 Equipamiento Obligatorio por Base
**Según AT2, Sección 3.3.3.1.1:**
- a) 1 Vehículo de vigilancia que recorrerá toda la longitud de la(s) vía(s) de forma ininterrumpida 24 horas al Día, 365 Días al año
- b) 1 Carrotaller
- c) 1 Grúa para movilizar vehículos Grandes
- d) 1 Grúa para movilizar vehículos pequeños
- e) 1 Ambulancia
- f) Personal capacitado en atención de emergencias y primeros auxilios

**Adicional:** "el Concesionario deberá contar como mínimo con una (1) Cama baja para todo el Proyecto"

### 3.3 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **NFPA 1936** | Equipos de rescate | Herramientas hidráulicas |
| **EN 13204** | Equipos de rescate | Estándares europeos |
| **Ministerio de Salud** | Ambulancias TAM | Dotación médica |
| **RETIE** | Instalaciones eléctricas | Infraestructura |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Base Norte** | 1 instalación | Km 50-80 (aprox) | Cobertura norte del corredor |
| **Base Sur** | 1 instalación | Km 180-220 (aprox) | Cobertura sur del corredor |
| **Vehículos vigilancia** | 2 unidades | 1 por base | Patrullaje 24/7/365 |
| **Carrotalleres** | 2 unidades | 1 por base | Auxilio mecánico |
| **Grúas grandes** | 2 unidades | 1 por base | Vehículos pesados |
| **Grúas pequeñas** | 2 unidades | 1 por base | Vehículos livianos |
| **Ambulancias TAM** | 2 unidades | 1 por base | Atención médica |
| **Cama baja** | 1 unidad | Base principal | Transporte especial |
| **Equipos rescate** | 2 juegos | 1 por base | Rescate vehicular |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Red IP/Radio | Ethernet/VHF | Coordinación operaciones |
| Ambulancias TAM | Radio | VHF/UHF | Emergencias médicas |
| Estaciones Peaje | Radio/IP | VHF/Ethernet | Incidentes en peajes |
| Paneles LED | Red IP | Ethernet | Información incidentes |
| Sistema Info Usuarios | Red IP | TCP/IP | Estado operacional |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Construcción bases** | 2 instalaciones | $300,000 | $600,000 |
| **Vehículos vigilancia** | 2 unidades | $45,000 | $90,000 |
| **Carrotalleres** | 2 unidades | $120,000 | $240,000 |
| **Grúas grandes** | 2 unidades | $180,000 | $360,000 |
| **Grúas pequeñas** | 2 unidades | $80,000 | $160,000 |
| **Ambulancias TAM** | 2 unidades | $150,000 | $300,000 |
| **Cama baja** | 1 unidad | $200,000 | $200,000 |
| **Equipos rescate** | 2 juegos | $50,000 | $100,000 |
| **Equipamiento base** | 2 bases | $75,000 | $150,000 |
| **TOTAL CAPEX** | | | **$2,200,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal operativo (24 personas) | $480,000 |
| Combustible vehículos | $120,000 |
| Mantenimiento vehículos | $180,000 |
| Mantenimiento equipos rescate | $30,000 |
| Seguros vehículos | $60,000 |
| Servicios públicos bases | $36,000 |
| Repuestos y consumibles | $48,000 |
| **TOTAL OPEX/año** | **$954,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Falla simultánea vehículos | Baja | Alto | Mantenimiento preventivo + respaldo |
| Accidente personal rescate | Media | Alto | Capacitación + EPP + seguros |
| Robo equipos costosos | Media | Medio | Seguridad bases + GPS tracking |
| Falta personal calificado | Media | Alto | Plan capacitación + contratos |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT2, Tabla 1:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **O4** | Tiempo de atención de incidentes | Según AT4 | Por evento |
| **O5** | Tiempo de atención de accidentes y emergencias | Según AT4 | Por evento |
| **O7** | Tiempo de atención de incidentes T | Según AT4 | Por evento |
| **O8** | Tiempo de atención de accidentes y emergencias T | Según AT4 | Por evento |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Definir ubicaciones óptimas de las bases
- [ ] Elaborar especificaciones técnicas vehículos (Template T04)
- [ ] Cotizar equipos de rescate certificados
- [ ] Diseñar plan de capacitación personal
- [ ] Validar tiempos de respuesta con simulaciones

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Ubicación bases para cobertura máxima 15 minutos cualquier punto
- Personal con certificaciones en rescate vehicular y primeros auxilios
- Equipos de rescate con certificación NFPA 1936/EN 13204
- Disponibilidad comunicaciones radio en todo el corredor

### 10.2 Dependencias
- Definición ubicaciones antes construcción
- Contratación personal calificado
- Certificación equipos rescate
- Coordinación con cuerpos de socorro locales

### 10.3 Restricciones
- Operación 24/7/365 sin interrupciones
- Tiempos respuesta según indicadores AT4
- Reemplazo equipos rescate cada 5 años
- Personal con certificaciones vigentes

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas