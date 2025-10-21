# T04_10: ESPECIFICACIONES TÉCNICAS - EQUIPOS DE EMERGENCIA Y RESCATE
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Equipos de Emergencia y Rescate  
**Responsable:** Ingeniero de Seguridad Vial  
**Versión:** 1.0  
**Referencia T01:** T01_10_FICHA_SISTEMA_EQUIPOS_EMERGENCIA_RESCATE_v1.0.md  
**Referencia T03:** T03_10_ARQUITECTURA_EQUIPOS_EMERGENCIA_RESCATE_v1.0.md  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | 21/10/2025 | Creación inicial | Ingeniero de Seguridad Vial |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | Equipos de Emergencia y Rescate |
| **Categoría** | Seguridad Vial y Emergencias |
| **Código interno** | T04-10-v1.0 |
| **Cantidad total** | 12 vehículos + equipos especializados |
| **CAPEX estimado** | USD $2,850,000 |
| **Documentos base** | T01_10, T02_10, T03_10, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Vehículos de emergencia y rescate
- ✅ Equipos de comunicación móvil
- ✅ Herramientas de rescate y primeros auxilios
- ✅ Sistemas de localización y seguimiento
- ✅ Equipos de protección personal

**Este documento NO especifica:**
- ❌ Bases de operación (ver T04_03)
- ❌ Personal y capacitación (ver procedimientos)
- ❌ Integración con entidades externas (ver T04_02)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 6.2.1 | Equipos de emergencia obligatorios |
| **Apéndice Técnico 2** | 4.3.2 | Tiempo de respuesta <15 minutos |
| **Apéndice Técnico 3** | 5.1.4 | Cobertura 100% del corredor |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **Resolución 3100/2019** | Vehículos de emergencia | Especificaciones técnicas |
| **NTC 1700** | Vehículos para transporte de heridos | Ambulancias |
| **RETIE** | Instalaciones eléctricas | Equipos eléctricos |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **EN 1789** | Medical vehicles and their equipment | Ambulancias |
| **NFPA 1901** | Standard for Automotive Fire Apparatus | Vehículos contra incendio |
| **ISO 3864** | Graphical symbols - Safety colours and safety signs | Señalización |### 
2.3 Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **Homologación vehicular** | RUNT | ✅ Sí | Todos los vehículos |
| **Certificación médica** | INVIMA | ✅ Sí | Equipos médicos |
| **Certificación contra incendio** | Bomberos | ✅ Sí | Equipos contra incendio |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Clasificación de Vehículos

#### 3.1.1 Vehículos Tipo A - Rescate Pesado

**Cantidad:** 4 unidades  
**Aplicación:** Rescate vehicular, accidentes mayores  
**Base vehicular:** Camión 4x2, GVWR >7,500 kg

#### 3.1.2 Vehículos Tipo B - Rescate Liviano

**Cantidad:** 4 unidades  
**Aplicación:** Primeros auxilios, rescate básico  
**Base vehicular:** Camioneta 4x4, GVWR 3,500-5,500 kg

#### 3.1.3 Vehículos Tipo C - Apoyo Logístico

**Cantidad:** 4 unidades  
**Aplicación:** Transporte de personal y equipos  
**Base vehicular:** Camioneta 4x2, GVWR <3,500 kg

### 3.2 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura operación** | -10°C a +50°C | - |
| **Humedad relativa** | 0-95% | - |
| **Altitud operación** | 0-2500 msnm | - |
| **Resistencia al agua** | IP65 equipos críticos | IEC 60529 |
| **Vibración** | Según ISO 16750-3 | ISO 16750 |

### 3.3 Requisitos de Comunicación

| Parámetro | Especificación | Protocolo |
|:----------|:---------------|:----------|
| **Radio VHF/UHF** | 25W potencia mínima | - |
| **Comunicación celular** | 4G/LTE con GPS | - |
| **Comunicación satelital** | Respaldo en zonas sin cobertura | - |
| **Integración CCO** | Tiempo real | TCP/IP |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Vehículos de Rescate Pesado (Tipo A)

#### 4.1.1 Descripción General

Vehículos especializados para rescate vehicular pesado, equipados con herramientas hidráulicas, sistemas de iluminación y equipos médicos avanzados.

#### 4.1.2 Especificaciones del Chasis

**Chasis Base:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Configuración** | 4x2, cabina simple | Inspección visual |
| **Motor** | Diésel, 250 HP mínimo | Ficha técnica |
| **Transmisión** | Manual 6 velocidades o automática | Inspección técnica |
| **GVWR** | 12,000 kg mínimo | Certificado fabricante |
| **Distancia entre ejes** | 4,500-5,500 mm | Medición física |
| **Capacidad de carga** | 5,000 kg mínimo | Certificado fabricante |

#### 4.1.3 Carrocería y Compartimentos

**Diseño de Carrocería:**
- Material: Aluminio estructural
- Compartimentos: Mínimo 8 compartimentos
- Acceso: Puertas enrollables con cerraduras
- Iluminación: LED interior y exterior
- Ventilación: Forzada con filtros

**Distribución de Compartimentos:**
| Compartimento | Dimensiones Mín. | Contenido |
|:--------------|:-----------------|:----------|
| **Herramientas hidráulicas** | 1.2 x 0.8 x 0.6 m | Separador, expansor, cortador |
| **Equipos médicos** | 1.0 x 0.8 x 0.5 m | Desfibrilador, oxígeno, camilla |
| **Herramientas manuales** | 0.8 x 0.6 x 0.4 m | Llaves, destornilladores, martillos |
| **Equipos eléctricos** | 0.6 x 0.6 x 0.4 m | Generador, extensiones, lámparas |

#### 4.1.4 Equipos Especializados

**Sistema Hidráulico de Rescate:**
| Equipo | Especificación Mínima | Método de Verificación |
|:-------|:---------------------|:-----------------------|
| **Separador hidráulico** | 32 ton fuerza, apertura 80 cm | Prueba de carga |
| **Cortador hidráulico** | Corte columna A, fuerza 100 ton | Prueba de corte |
| **Cilindros de extensión** | 10 ton, carrera 150 cm | Prueba de extensión |
| **Bomba hidráulica** | Eléctrica + manual, 700 bar | Prueba de presión |
| **Mangueras** | 15 m longitud, 700 bar | Prueba de presión |

**Equipos Médicos:**
| Equipo | Especificación Mínima | Certificación |
|:-------|:---------------------|:--------------|
| **Desfibrilador** | Semiautomático, bifásico | INVIMA |
| **Equipo de oxígeno** | 2 cilindros, reguladores | INVIMA |
| **Camilla rígida** | Fibra de carbono, inmovilización | INVIMA |
| **Kit de vía aérea** | Intubación, mascarillas | INVIMA |
| **Monitor de signos** | FC, PA, SpO2, temperatura | INVIMA |

#### 4.1.5 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Rosenbauer** - Modelo: RT Industrial
2. **Ferrara** - Modelo: Heavy Rescue
3. **Pierce** - Modelo: Velocity Heavy Rescue
4. **O equivalente** que cumpla especificaciones

### 4.2 Vehículos de Rescate Liviano (Tipo B)

#### 4.2.1 Descripción General

Vehículos ágiles para respuesta rápida, primeros auxilios y rescate básico en accidentes menores.

#### 4.2.2 Especificaciones del Vehículo

**Vehículo Base:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Configuración** | 4x4, doble cabina | Inspección visual |
| **Motor** | Diésel, 180 HP mínimo | Ficha técnica |
| **Capacidad de carga** | 1,500 kg | Certificado fabricante |
| **Tanque combustible** | 80 litros mínimo | Inspección técnica |
| **Autonomía** | 600 km mínimo | Cálculo técnico |

#### 4.2.3 Equipamiento Médico

**Kit de Primeros Auxilios Avanzado:**
- Desfibrilador portátil
- Oxígeno portátil (2 horas)
- Camilla plegable
- Inmovilizadores cervicales
- Kit de trauma
- Medicamentos básicos

#### 4.2.4 Herramientas de Rescate

**Herramientas Básicas:**
- Cortador de cinturones
- Rompe vidrios
- Linterna LED de alta potencia
- Extintor PQS 10 lb
- Kit de señalización
- Herramientas manuales básicas

### 4.3 Sistema de Comunicaciones Móvil

#### 4.3.1 Descripción General

Sistema integrado de comunicaciones para coordinación con CCO, entidades de emergencia y otros vehículos del sistema.

#### 4.3.2 Especificaciones Técnicas

**Radio Móvil VHF/UHF:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Potencia** | 25W VHF, 25W UHF | Medición RF |
| **Canales** | 128 canales mínimo | Configuración |
| **Sensibilidad** | -116 dBm @ 12 dB SINAD | Medición RF |
| **Selectividad** | 70 dB @ ±25 kHz | Medición RF |
| **Ciclo de trabajo** | 100% continuo | Prueba térmica |

**Sistema de Localización GPS:**
- Precisión: <3 metros
- Actualización: Cada 10 segundos
- Transmisión: Tiempo real al CCO
- Respaldo: Memoria interna 30 días
- Geofencing: Alertas automáticas

#### 4.3.3 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Motorola** - Modelo: XTL5000
2. **Kenwood** - Modelo: NX-800
3. **Icom** - Modelo: IC-F8101
4. **O equivalente** que cumpla especificaciones

### 4.4 Equipos de Protección Personal

#### 4.4.1 Descripción General

Equipos de protección individual para el personal de rescate, cumpliendo con estándares internacionales de seguridad.

#### 4.4.2 Especificaciones por Tipo

**Cascos de Rescate:**
| Parámetro | Especificación Mínima | Norma |
|:----------|:---------------------|:------|
| **Material** | ABS o policarbonato | EN 397 |
| **Resistencia impacto** | 5 J mínimo | EN 397 |
| **Resistencia eléctrica** | 1000V AC | EN 397 |
| **Linterna integrada** | LED, 3 horas autonomía | - |
| **Sistema de sujeción** | 4 puntos, ajustable | EN 397 |

**Trajes de Rescate:**
- Material: Nomex o equivalente
- Resistencia al fuego: Nivel 2
- Reflectivos: Clase 2 ANSI
- Impermeabilidad: 10,000 mm
- Transpirabilidad: 5,000 g/m²/24h

**Guantes de Rescate:**
- Material: Cuero + Kevlar
- Resistencia corte: Nivel 4
- Resistencia punción: Nivel 3
- Agarre húmedo: Nivel 4
- Destreza: Nivel 4

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con CCO

| Aspecto | Requisito | Verificación |
|:--------|:----------|:-------------|
| **Localización GPS** | Tiempo real, <10 seg actualización | Prueba de conectividad |
| **Estado del vehículo** | Disponible/En servicio/Fuera servicio | Interface software |
| **Comunicación de voz** | Calidad digital | Prueba de audio |
| **Datos de emergencia** | Tipo, ubicación, recursos | Protocolo de datos |

### 5.2 Integración con Otros Sistemas

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **Postes SOS** | Radio VHF | Llamadas de emergencia |
| **Cámaras CCTV** | TCP/IP | Verificación visual incidentes |
| **Paneles LED** | TCP/IP | Información de desvíos |
| **Entidades Externas** | Radio/Celular | Coordinación de respuesta |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Equipamiento de Vehículos

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Instalación eléctrica** | 12V/24V, fusibles automáticos | SAE J1128 |
| **Antenas** | VHF/UHF/GPS/Celular | - |
| **Sirenas y luces** | LED, múltiples patrones | SAE J845 |
| **Anclajes de equipos** | Resistencia 10G | - |

### 6.2 Homologación Vehicular

| Documento | Descripción | Entidad |
|:----------|:------------|:--------|
| **CDA inicial** | Revisión técnico-mecánica | CDA autorizado |
| **Registro RUNT** | Inscripción vehicular | RUNT |
| **Póliza SOAT** | Seguro obligatorio | Aseguradora |
| **Revisión de gases** | Emisiones contaminantes | CDA autorizado |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas de Vehículos

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Prueba de carga** | Verificar capacidad | 100% carga nominal |
| **Prueba de autonomía** | Verificar combustible | >600 km sin reabastecimiento |
| **Prueba de tracción** | Verificar 4x4 | Pendiente 30% con carga |
| **Prueba de frenado** | Verificar seguridad | Distancia según norma |

### 7.2 Pruebas de Equipos

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Equipos hidráulicos** | Verificar fuerza | 100% especificación |
| **Equipos médicos** | Verificar funcionamiento | Calibración vigente |
| **Comunicaciones** | Verificar alcance | Cobertura 100% corredor |
| **Iluminación** | Verificar potencia | Según especificación |

### 7.3 Pruebas de Integración

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Comunicación CCO** | Verificar conectividad | 100% disponibilidad |
| **Localización GPS** | Verificar precisión | <3 metros error |
| **Tiempo de respuesta** | Verificar operación | <15 minutos promedio |
| **Coordinación** | Verificar procedimientos | 100% protocolos |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos Técnicos

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Ficha técnica vehículos** | Especificaciones completas | Español | 3 copias + digital |
| **Manual de operación** | Guía de uso equipos | Español | 5 copias + digital |
| **Manual de mantenimiento** | Procedimientos preventivos | Español | 3 copias + digital |
| **Protocolos de emergencia** | Procedimientos operativos | Español | 10 copias + digital |
| **Planos de instalación** | Distribución de equipos | - | Digital (DWG + PDF) |

### 8.2 Certificados Requeridos

| Certificado | Emisor | Vigencia |
|:------------|:-------|:---------|
| **Homologación RUNT** | RUNT | Vigente |
| **Certificación INVIMA** | INVIMA | Vigente |
| **Certificado de origen** | Fabricante | - |
| **Garantía de equipos** | Fabricante | 24-60 meses |

### 8.3 Capacitación

| Programa | Duración | Participantes | Certificación |
|:---------|:---------|:--------------|:--------------|
| **Operación de equipos** | 40 horas | Personal operativo | Fabricante |
| **Primeros auxilios** | 20 horas | Todo el personal | Cruz Roja |
| **Rescate vehicular** | 60 horas | Personal especializado | Bomberos |
| **Comunicaciones** | 16 horas | Todo el personal | Interno |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Revisión general vehículo** | Mensual | Contratista |
| **Mantenimiento motor** | Según fabricante | Taller autorizado |
| **Calibración equipos médicos** | Semestral | Técnico certificado |
| **Prueba equipos hidráulicos** | Trimestral | Técnico especializado |
| **Actualización comunicaciones** | Según disponibilidad | Fabricante |

### 9.2 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **Filtros motor** | 24 unidades | 7 días |
| **Baterías vehículo** | 12 unidades | 3 días |
| **Mangueras hidráulicas** | 6 juegos | 15 días |
| **Electrodos desfibrilador** | 24 pares | 5 días |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Vehículo rescate pesado Tipo A | und | 4 | $180,000 | $720,000 |
| 2 | Vehículo rescate liviano Tipo B | und | 4 | $85,000 | $340,000 |
| 3 | Vehículo apoyo logístico Tipo C | und | 4 | $45,000 | $180,000 |
| 4 | Equipos hidráulicos de rescate | lote | 4 | $35,000 | $140,000 |
| 5 | Equipos médicos avanzados | lote | 8 | $25,000 | $200,000 |
| 6 | Sistema comunicaciones móvil | lote | 12 | $8,500 | $102,000 |
| 7 | Equipos protección personal | lote | 1 | $45,000 | $45,000 |
| 8 | Herramientas y accesorios | lote | 1 | $85,000 | $85,000 |
| 9 | Capacitación y certificación | lote | 1 | $65,000 | $65,000 |
| 10 | Contingencias (5%) | lote | 1 | $95,850 | $95,850 |
| | | | | **TOTAL** | **$1,972,850** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Validar especificaciones con cuerpos de bomberos
- [ ] Solicitar cotizaciones de fabricantes especializados
- [ ] Coordinar con bases de operación para almacenamiento
- [ ] Establecer protocolos de operación con entidades
- [ ] Planificar programa de capacitación del personal
- [ ] Definir cronograma de entrega escalonada

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Seguridad Vial | Especificaciones técnicas iniciales |

---

**Elaborado por:** Ingeniero de Seguridad Vial  
**Revisado por:** Coordinador Técnico  
**Aprobado por:** Gerente de Proyecto  

**Fecha de elaboración:** 21/10/2025  
**Próxima revisión:** 30/11/2025