# T04: ESPECIFICACIONES TÉCNICAS - [NOMBRE DEL SISTEMA]
## Proyecto APP [NOMBRE_PROYECTO]

**Fecha:** [DD/MM/AAAA]  
**Sistema:** [Nombre del Sistema]  
**Responsable:** [Ingeniero Responsable]  
**Versión:** 1.0  
**Referencia T01:** [Código T01 relacionado]  
**Referencia T03:** [Código T03 relacionado]  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | [DD/MM/AAAA] | Creación inicial | [Nombre] |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | [Nombre completo] |
| **Categoría** | [ITS, Energía, Telecomunicaciones, etc.] |
| **Código interno** | [T04-XXX-v1.0] |
| **Cantidad total** | [X unidades] |
| **CAPEX estimado** | [USD $X,XXX,XXX] |
| **Documentos base** | T01, T02, T03, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Características técnicas mínimas
- ✅ Requisitos de desempeño
- ✅ Normativa y certificaciones
- ✅ Criterios de aceptación
- ✅ Procedimientos de prueba

**Este documento NO especifica:**
- ❌ Detalles de instalación (ver T05)
- ❌ Cronograma de obra
- ❌ Proveedores específicos (salvo referencia)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | [Sección] | [Requisito] |
| **Apéndice Técnico 2** | [Sección] | [Requisito] |
| **Apéndice Técnico 3** | [Sección] | [Requisito] |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **[Norma 1]** | [Título] | [Sección específica] |
| **[Norma 2]** | [Título] | [Sección específica] |

**Ejemplos:**
- **RETIE:** Reglamento Técnico de Instalaciones Eléctricas
- **Resolución 718/2018:** Radares y sistemas de detección
- **Resolución 546/2018:** Interoperabilidad de peajes (IP/REV)

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **ISO TC-204** | Intelligent Transport Systems | [Subsistemas ITS] |
| **ITU-T H.xxx** | Sistemas audiovisuales | [CCTV, PMV] |
| **IEEE 802.3** | Ethernet | [Telecomunicaciones] |

### 2.3 Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **[Certificación 1]** | [Organismo] | ✅ Sí / ⏳ Opcional | [Componente] |
| **[Certificación 2]** | [Organismo] | ✅ Sí / ⏳ Opcional | [Componente] |

**Ejemplos:**
- **ONAC:** Homologación metrológica (radares)
- **CE / FCC:** Compatibilidad electromagnética
- **IP65:** Protección contra ingreso de agua/polvo

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura de operación** | [-XX°C a +XX°C] | [Norma] |
| **Humedad relativa** | [0-95% sin condensación] | [Norma] |
| **Protección IP** | [IP65 mínimo] | IEC 60529 |
| **Resistencia a viento** | [XXX km/h] | [Norma] |
| **Altitud operación** | [0-XXXX msnm] | [Norma] |

**Condiciones específicas del proyecto:**
- Clima tropical húmedo
- Temperatura promedio: 27-32°C
- Humedad promedio: 70-85%
- Altitud: 0-500 msnm

### 3.2 Requisitos Eléctricos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Tensión nominal** | [120/208 VAC, 60 Hz] | RETIE |
| **Variación de tensión** | [±10%] | RETIE |
| **Factor de potencia** | [≥0.9] | RETIE |
| **Consumo máximo** | [XXX W] | - |
| **Respaldo UPS** | [X horas mínimo] | AT2 |

### 3.3 Requisitos de Comunicaciones

| Parámetro | Especificación | Protocolo |
|:----------|:---------------|:----------|
| **Medio físico** | [Fibra óptica monomodo] | - |
| **Velocidad** | [100 Mbps mínimo] | IEEE 802.3 |
| **Protocolo de red** | [TCP/IP] | - |
| **Protocolo aplicación** | [NTCIP, SNMP, etc.] | - |
| **Disponibilidad** | [≥99%] | AT2 |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 [Componente Principal 1]

#### 4.1.1 Descripción General

[Descripción funcional del componente]

#### 4.1.2 Especificaciones Técnicas

| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **[Parámetro 1]** | [Valor mínimo] | [Ensayo/Inspección] |
| **[Parámetro 2]** | [Valor mínimo] | [Ensayo/Inspección] |
| **[Parámetro 3]** | [Valor mínimo] | [Ensayo/Inspección] |

**Ejemplo para Poste SOS:**
| Parámetro | Especificación Mínima | Verificación |
|:----------|:---------------------|:-------------|
| **Altura total** | 2.5 m | Inspección física |
| **Ancho botón SOS** | Mín. 10 cm | Inspección física |
| **Tiempo respuesta** | <3 segundos | Prueba funcional |
| **Audio bidireccional** | Full-duplex, 20-20kHz | Prueba acústica |

#### 4.1.3 Materiales y Construcción

| Elemento | Material | Acabado | Norma |
|:---------|:---------|:--------|:------|
| **[Elemento 1]** | [Material] | [Acabado] | [Norma] |
| **[Elemento 2]** | [Material] | [Acabado] | [Norma] |

**Ejemplo:**
| Elemento | Material | Acabado | Norma |
|:---------|:---------|:--------|:------|
| **Carcasa** | Acero inoxidable AISI 304 | Pulido | ASTM A240 |
| **Puerta frontal** | Aluminio anodizado | Gris RAL 7035 | - |

#### 4.1.4 Dimensiones y Pesos

| Dimensión | Valor | Tolerancia |
|:----------|:------|:-----------|
| **Alto** | [X.XX m] | [±X%] |
| **Ancho** | [X.XX m] | [±X%] |
| **Profundidad** | [X.XX m] | [±X%] |
| **Peso total** | [XXX kg] | [±X%] |

#### 4.1.5 Fabricantes de Referencia

**Fabricantes aceptables (sin orden de preferencia):**
1. **[Fabricante 1]** - Modelo: [Modelo de referencia]
2. **[Fabricante 2]** - Modelo: [Modelo de referencia]
3. **[Fabricante 3]** - Modelo: [Modelo de referencia]
4. **O equivalente** que cumpla especificaciones

> **Nota:** La lista es referencial. El contratista puede proponer alternativas que cumplan o superen las especificaciones.

### 4.2 [Componente Auxiliar 1]

[Repetir estructura 4.1 para cada componente]

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con Sistema Central

| Aspecto | Requisito | Verificación |
|:--------|:----------|:-------------|
| **Conexión a CCO** | [Protocolo, velocidad] | Prueba de conectividad |
| **Tiempo de respuesta** | [<X segundos] | Prueba de latencia |
| **Disponibilidad** | [≥99%] | Monitoreo 30 días |

### 5.2 Interfaz con Otros Sistemas

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **[Sistema 1]** | [Protocolo] | [Descripción] |
| **[Sistema 2]** | [Protocolo] | [Descripción] |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Obras Civiles Requeridas

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Cimentación** | [Tipo, dimensiones] | [Norma] |
| **Canalizaciones** | [Tipo, diámetro, profundidad] | [Norma] |
| **Tierras** | [Resistencia <X Ω] | RETIE |

### 6.2 Acometidas Eléctricas

| Parámetro | Especificación |
|:----------|:---------------|
| **Tensión** | [120/208 VAC, 60 Hz] |
| **Corriente máxima** | [XX A] |
| **Calibre conductor** | [AWGXX] |
| **Protección** | [Breaker XX A + DPS] |

### 6.3 Conectividad

| Parámetro | Especificación |
|:----------|:---------------|
| **Medio** | [Fibra óptica SM 9/125 μm] |
| **Conectores** | [SC/APC] |
| **ODF más cercano** | [<XXX m] |
| **Atenuación máxima** | [<X dB] |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas en Fábrica (FAT)

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **[Prueba 1]** | [Objetivo] | [Criterio] |
| **[Prueba 2]** | [Objetivo] | [Criterio] |

**Ejemplo:**
| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Inspección visual** | Verificar acabados | Sin defectos visibles |
| **Prueba eléctrica** | Verificar consumo | Dentro de especificación ±5% |
| **Prueba funcional** | Verificar operación | 100% funciones operativas |

### 7.2 Pruebas en Sitio (SAT)

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **[Prueba 1]** | [Objetivo] | [Criterio] |
| **[Prueba 2]** | [Objetivo] | [Criterio] |

**Ejemplo:**
| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Prueba de conectividad** | Verificar comunicación con CCO | Respuesta <3 seg |
| **Prueba de audio** | Verificar calidad de voz | Inteligibilidad >90% |
| **Prueba de autonomía** | Verificar respaldo UPS | >2 horas continuidad |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos del Fabricante

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Ficha técnica** | Especificaciones detalladas | Español | 3 copias + digital |
| **Manual de instalación** | Procedimiento paso a paso | Español | 2 copias + digital |
| **Manual de operación** | Guía de usuario | Español | 3 copias + digital |
| **Manual de mantenimiento** | Procedimientos preventivos/correctivos | Español | 2 copias + digital |
| **Planos de taller** | Dimensiones, conexiones | - | Digital (DWG + PDF) |

### 8.2 Certificados Requeridos

| Certificado | Emisor | Vigencia |
|:------------|:-------|:---------|
| **[Certificado 1]** | [Organismo] | [X años] |
| **[Certificado 2]** | [Organismo] | [X años] |

**Ejemplo:**
| Certificado | Emisor | Vigencia |
|:------------|:-------|:---------|
| **Certificado de origen** | Fabricante | - |
| **Certificado de calidad ISO 9001** | Organismo certificador | Vigente |
| **Homologación ONAC** | ONAC Colombia | Vigente |

### 8.3 Garantías

| Elemento | Garantía Mínima | Observaciones |
|:---------|:----------------|:--------------|
| **Equipos electrónicos** | [24 meses] | Desde puesta en servicio |
| **Componentes mecánicos** | [12 meses] | Desde puesta en servicio |
| **Software** | [24 meses] | Actualizaciones incluidas |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **[Actividad 1]** | [Mensual/Trimestral/Anual] | [Contratista/Fabricante] |
| **[Actividad 2]** | [Mensual/Trimestral/Anual] | [Contratista/Fabricante] |

**Ejemplo:**
| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza externa** | Mensual | Contratista |
| **Verificación funcional** | Trimestral | Contratista |
| **Calibración** | Anual | Fabricante autorizado |

### 9.2 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **[Componente 1]** | [X unidades] | [XX días] |
| **[Componente 2]** | [X unidades] | [XX días] |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | [Descripción] | [und/m/kg] | [X] | $[X,XXX] | $[XX,XXX] |
| 2 | [Descripción] | [und/m/kg] | [X] | $[X,XXX] | $[XX,XXX] |
| | | | | **TOTAL** | **$X,XXX,XXX** |

---

## 11. PRÓXIMOS PASOS

- [ ] Validar especificaciones con fabricantes/proveedores
- [ ] Solicitar cotizaciones formales
- [ ] Desarrollar protocolos de prueba detallados
- [ ] Crear cronograma de suministro e instalación
- [ ] Obtener aprobación de stakeholders

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | [DD/MM/AAAA] | [Ingeniero] | Especificaciones técnicas iniciales |

---

**Elaborado por:** [Nombre]  
**Revisado por:** [Nombre]  
**Aprobado por:** [Nombre]  

**Fecha de elaboración:** [DD/MM/AAAA]  
**Fecha de revisión:** [DD/MM/AAAA]  
**Fecha de aprobación:** [DD/MM/AAAA]