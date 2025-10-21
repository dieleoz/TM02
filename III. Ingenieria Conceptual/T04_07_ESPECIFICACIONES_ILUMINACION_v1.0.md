# T04_07: ESPECIFICACIONES TÉCNICAS - SISTEMA DE ILUMINACIÓN
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Sistema de Iluminación  
**Responsable:** Ingeniero Eléctrico  
**Versión:** 1.0  
**Referencia T01:** T01_07_FICHA_SISTEMA_ILUMINACION_v1.0.md  
**Referencia T03:** T03_07_ARQUITECTURA_ILUMINACION_v1.0.md  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | 21/10/2025 | Creación inicial | Ingeniero Eléctrico |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | Sistema de Iluminación Vial |
| **Categoría** | Infraestructura Eléctrica |
| **Código interno** | T04-07-v1.0 |
| **Extensión total** | 85 km de autopista |
| **CAPEX estimado** | USD $3,400,000 |
| **Documentos base** | T01_07, T02_07, T03_07, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Luminarias LED para autopista
- ✅ Postes y estructuras de soporte
- ✅ Sistemas de control y automatización
- ✅ Redes eléctricas de distribución
- ✅ Sistemas de monitoreo y gestión

**Este documento NO especifica:**
- ❌ Subestaciones eléctricas principales (ver T05)
- ❌ Acometidas de media tensión (ver T05)
- ❌ Iluminación arquitectónica de edificios (ver T05)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 7.1.2 | Iluminación en puntos críticos |
| **Apéndice Técnico 2** | 5.2.1 | Eficiencia energética obligatoria |
| **Apéndice Técnico 3** | 6.1.3 | Control automático día/noche |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **RETIE** | Reglamento Técnico Instalaciones Eléctricas | Instalaciones eléctricas |
| **NTC 900** | Código Eléctrico Colombiano | Diseño eléctrico |
| **Manual INVIAS** | Especificaciones generales de construcción | Iluminación vial |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **CIE 115** | Lighting of Roads for Motor and Pedestrian Traffic | Diseño fotométrico |
| **IES RP-8** | Roadway Lighting | Niveles de iluminación |
| **EN 13201** | Road lighting | Clasificación y requisitos |##
# 2.3 Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **Certificación RETIE** | ONAC | ✅ Sí | Instalaciones eléctricas |
| **Certificación LM-79** | Laboratorio acreditado | ✅ Sí | Luminarias LED |
| **Certificación Energy Star** | EPA | ⏳ Opcional | Eficiencia energética |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Clasificación de Zonas de Iluminación

#### 3.1.1 Zona A - Calzada Principal

**Características:**
- Velocidad: 80-120 km/h
- Tráfico: Alto volumen
- Clase de iluminación: M2 (CIE 115)
- Luminancia promedio: 1.0 cd/m²

#### 3.1.2 Zona B - Intercambiadores y Rampas

**Características:**
- Velocidad: 40-80 km/h
- Tráfico: Medio volumen
- Clase de iluminación: M3 (CIE 115)
- Luminancia promedio: 0.75 cd/m²

#### 3.1.3 Zona C - Áreas de Servicio

**Características:**
- Velocidad: 20-40 km/h
- Tráfico: Bajo volumen
- Clase de iluminación: M4 (CIE 115)
- Luminancia promedio: 0.5 cd/m²

### 3.2 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura operación** | -10°C a +60°C | IEC 60598 |
| **Humedad relativa** | 0-95% sin condensación | IEC 60598 |
| **Protección IP** | IP66 mínimo | IEC 60529 |
| **Resistencia a viento** | 150 km/h | IEC 60598 |
| **Resistencia UV** | Sin degradación 25 años | ASTM G154 |

### 3.3 Requisitos Fotométricos

| Parámetro | Especificación | Norma |
|:----------|:---------------|:------|
| **Eficacia luminosa** | ≥130 lm/W | LM-79 |
| **Temperatura de color** | 4000K ±300K | LM-79 |
| **Índice de reproducción** | CRI ≥70 | LM-79 |
| **Vida útil** | L70 ≥100,000 horas | LM-80 |
| **Mantenimiento lumínico** | ≥90% a 50,000 horas | LM-80 |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Luminarias LED

#### 4.1.1 Descripción General

Luminarias LED de alta eficiencia para iluminación vial, con ópticas especializadas para distribución fotométrica optimizada según cada zona.

#### 4.1.2 Especificaciones Técnicas

**Luminaria Tipo A - Calzada Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Potencia** | 150W ±5% | Medición eléctrica |
| **Flujo luminoso** | 19,500 lm mínimo | Medición LM-79 |
| **Eficacia luminosa** | 130 lm/W mínimo | Cálculo LM-79 |
| **Distribución fotométrica** | Tipo II Medium | Gonofotómetro |
| **Temperatura de color** | 4000K ±300K | Espectrofotómetro |
| **Factor de potencia** | ≥0.95 | Medición eléctrica |

**Luminaria Tipo B - Intercambiadores:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Potencia** | 100W ±5% | Medición eléctrica |
| **Flujo luminoso** | 13,000 lm mínimo | Medición LM-79 |
| **Eficacia luminosa** | 130 lm/W mínimo | Cálculo LM-79 |
| **Distribución fotométrica** | Tipo III Medium | Gonofotómetro |
| **Temperatura de color** | 4000K ±300K | Espectrofotómetro |
| **Factor de potencia** | ≥0.95 | Medición eléctrica |

**Luminaria Tipo C - Áreas de Servicio:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Potencia** | 60W ±5% | Medición eléctrica |
| **Flujo luminoso** | 7,800 lm mínimo | Medición LM-79 |
| **Eficacia luminosa** | 130 lm/W mínimo | Cálculo LM-79 |
| **Distribución fotométrica** | Tipo V | Gonofotómetro |
| **Temperatura de color** | 4000K ±300K | Espectrofotómetro |
| **Factor de potencia** | ≥0.95 | Medición eléctrica |

#### 4.1.3 Características Constructivas

**Carcasa y Disipación:**
- Material: Aleación de aluminio fundido
- Acabado: Pintura poliéster termoestable
- Color: Gris RAL 7035
- Disipación: Aletas de refrigeración integradas
- Temperatura de unión LED: <85°C

**Óptica:**
- Material: Vidrio templado o PMMA
- Espesor: 4 mm mínimo
- Transmitancia: >92%
- Tratamiento: Anti-reflectivo
- Sellado: Silicona estructural

**Driver LED:**
- Tipo: Fuente conmutada
- Eficiencia: >90%
- THD: <20%
- Protección: Sobretensión, cortocircuito
- Dimming: 0-10V o DALI

#### 4.1.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Philips** - Modelo: RoadFocus Gen2
2. **GE Current** - Modelo: Evolve LED
3. **Cree** - Modelo: XSP Series
4. **O equivalente** que cumpla especificaciones

### 4.2 Postes y Estructuras

#### 4.2.1 Descripción General

Postes metálicos para soporte de luminarias, diseñados para resistir cargas de viento y sísmicas según normativa local.

#### 4.2.2 Especificaciones Técnicas

**Poste Tipo A - Calzada Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Altura** | 12 metros | Medición física |
| **Material** | Acero galvanizado ASTM A572 Gr. 50 | Certificado material |
| **Espesor pared** | 6 mm mínimo | Inspección ultrasónica |
| **Diámetro base** | 219 mm (8") | Medición física |
| **Diámetro tope** | 114 mm (4.5") | Medición física |
| **Carga de viento** | 150 km/h | Cálculo estructural |

**Poste Tipo B - Intercambiadores:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Altura** | 10 metros | Medición física |
| **Material** | Acero galvanizado ASTM A572 Gr. 50 | Certificado material |
| **Espesor pared** | 5 mm mínimo | Inspección ultrasónica |
| **Diámetro base** | 168 mm (6.5") | Medición física |
| **Diámetro tope** | 89 mm (3.5") | Medición física |
| **Carga de viento** | 150 km/h | Cálculo estructural |

#### 4.2.3 Características Constructivas

**Galvanizado:**
- Proceso: Inmersión en caliente
- Espesor: 85 μm mínimo
- Norma: ASTM A123
- Acabado: Liso, sin goteo

**Accesorios:**
- Puerta de inspección: 200x300 mm
- Cerradura: Triangular universal
- Puesta a tierra: Terminal de cobre
- Base: Placa de anclaje con pernos

#### 4.2.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Valmont** - Modelo: Lighting Poles
2. **Hapco** - Modelo: Steel Lighting Poles
3. **Union Metal** - Modelo: Decorative Poles
4. **O equivalente** que cumpla especificaciones

### 4.3 Sistema de Control y Automatización

#### 4.3.1 Descripción General

Sistema inteligente de control para encendido/apagado automático, regulación de intensidad y monitoreo remoto de la iluminación.

#### 4.3.2 Especificaciones Técnicas

**Controlador Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Puntos de control** | 500 luminarias | Configuración software |
| **Protocolos** | DALI, 0-10V, relé | Prueba de comunicación |
| **Interfaces** | Ethernet, RS-485, WiFi | Inspección técnica |
| **Memoria** | 32 GB almacenamiento | Inspección técnica |
| **Respaldo** | Batería 8 horas | Prueba de autonomía |

**Funcionalidades:**
- Encendido/apagado por horario
- Regulación por sensor de luz
- Detección de fallas automática
- Programación de escenarios
- Reportes de consumo energético
- Integración con CCO

#### 4.3.3 Sensores y Detectores

**Sensor Crepuscular:**
- Rango: 1-100,000 lux
- Precisión: ±5%
- Histéresis: Configurable
- Protección: IP65
- Comunicación: 4-20 mA

**Detector de Presencia:**
- Tecnología: Microondas
- Alcance: 15 metros
- Ángulo: 360°
- Sensibilidad: Ajustable
- Retardo: 1-30 minutos

#### 4.3.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Schneider Electric** - Modelo: EcoStruxure
2. **Siemens** - Modelo: LOGO! 8
3. **ABB** - Modelo: System pro E power
4. **O equivalente** que cumpla especificaciones

### 4.4 Red Eléctrica de Distribución

#### 4.4.1 Descripción General

Red eléctrica subterránea para alimentación de luminarias, con transformadores de distribución y sistemas de protección.

#### 4.4.2 Especificaciones Técnicas

**Cable Subterráneo:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Tensión nominal** | 600V | Certificado fabricante |
| **Conductor** | Cobre, temple suave | Inspección física |
| **Aislamiento** | XLPE | Certificado fabricante |
| **Cubierta** | PVC negro | Inspección visual |
| **Calibres** | AWG 12, 10, 8, 6 | Medición física |
| **Temperatura** | 90°C continua | Certificado fabricante |

**Transformadores de Distribución:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Potencia** | 25, 37.5, 50 kVA | Placa de características |
| **Tensión primaria** | 13.2 kV | Placa de características |
| **Tensión secundaria** | 208/120V | Medición eléctrica |
| **Conexión** | Delta-Estrella | Diagrama vectorial |
| **Impedancia** | 4% ±0.5% | Ensayo de cortocircuito |
| **Pérdidas** | Según NTC 819 | Ensayo de pérdidas |

#### 4.4.3 Canalizaciones

**Ductos Subterráneos:**
- Material: PVC rígido
- Diámetros: 4", 6", 8"
- Profundidad: 80 cm mínimo
- Separación: 30 cm entre ductos
- Cámaras: Cada 100 metros

**Cajas de Conexión:**
- Material: Polímero o concreto
- Dimensiones: 60x60x60 cm mínimo
- Tapa: Hierro fundido clase D400
- Drenaje: Sistema de evacuación
- Acceso: Tapa con cerradura

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con CCO

| Aspecto | Requisito | Verificación |
|:--------|:----------|:-------------|
| **Monitoreo remoto** | Estado de cada luminaria | Interface SCADA |
| **Control remoto** | Encendido/apagado por zonas | Comandos TCP/IP |
| **Alarmas** | Fallas automáticas | Notificaciones tiempo real |
| **Reportes** | Consumo energético | Base de datos |

### 5.2 Integración con Otros Sistemas

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **Sistema Eléctrico** | Medidores inteligentes | Consumo, demanda |
| **Cámaras CCTV** | Sincronización | Activación por movimiento |
| **Paneles LED** | Red eléctrica | Alimentación compartida |
| **Postes SOS** | Red eléctrica | Alimentación de emergencia |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Cimentaciones

| Elemento | Especificación | Norma |
|:---------|:---------------|:------|
| **Concreto** | f'c = 21 MPa (3000 PSI) | ACI 318 |
| **Acero de refuerzo** | fy = 420 MPa (60 ksi) | ASTM A615 |
| **Profundidad** | 1.8 metros mínimo | Cálculo estructural |
| **Dimensiones base** | 1.2 x 1.2 x 1.8 m | Planos estructurales |

### 6.2 Instalación Eléctrica

| Parámetro | Especificación |
|:----------|:---------------|
| **Acometida** | 13.2 kV trifásica |
| **Transformación** | 13.2 kV / 208-120V |
| **Distribución** | 208/120V trifásica |
| **Protección** | Fusibles + DPS |
| **Tierras** | <25 Ω por poste |

### 6.3 Pruebas de Instalación

| Prueba | Objetivo | Criterio |
|:-------|:---------|:---------|
| **Resistencia de aislamiento** | Verificar aislamiento | >1 MΩ |
| **Continuidad** | Verificar conexiones | <1 Ω |
| **Puesta a tierra** | Verificar seguridad | <25 Ω |
| **Fotometría** | Verificar iluminación | Según CIE 115 |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas Fotométricas

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Luminancia promedio** | Verificar nivel de iluminación | Según clase CIE |
| **Uniformidad general** | Verificar distribución | Uo ≥ 0.4 |
| **Uniformidad longitudinal** | Verificar continuidad | Ul ≥ 0.5 |
| **Deslumbramiento** | Verificar confort visual | TI ≤ 15% |

### 7.2 Pruebas Eléctricas

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Consumo de potencia** | Verificar eficiencia | ±5% valor nominal |
| **Factor de potencia** | Verificar calidad | ≥0.95 |
| **THD corriente** | Verificar distorsión | <20% |
| **Temperatura de operación** | Verificar disipación | <85°C unión LED |

### 7.3 Pruebas de Sistema

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Control automático** | Verificar automatización | 100% funcional |
| **Comunicación** | Verificar conectividad | Sin pérdida de datos |
| **Respaldo de energía** | Verificar UPS | 8 horas autonomía |
| **Detección de fallas** | Verificar diagnóstico | 100% fallas detectadas |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos Técnicos

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Cálculos fotométricos** | Simulación DIALux o similar | Español | 3 copias + digital |
| **Planos de instalación** | Ubicación y detalles | - | Digital (DWG + PDF) |
| **Manual de operación** | Sistema de control | Español | 5 copias + digital |
| **Manual de mantenimiento** | Procedimientos preventivos | Español | 3 copias + digital |
| **Certificados LM-79/LM-80** | Ensayos fotométricos | - | Digital |

### 8.2 Software y Licencias

| Software | Descripción | Licencias | Vigencia |
|:---------|:------------|:----------|:---------|
| **Sistema de control** | Software de gestión | 5 usuarios | Perpetua |
| **Software de monitoreo** | Interface SCADA | 3 usuarios | 5 años |
| **Actualizaciones** | Firmware luminarias | Incluidas | 5 años |

### 8.3 Garantías

| Elemento | Garantía Mínima | Observaciones |
|:---------|:----------------|:--------------|
| **Luminarias LED** | 60 meses | L70 garantizado |
| **Postes metálicos** | 120 meses | Contra corrosión |
| **Sistema de control** | 36 meses | Hardware y software |
| **Instalación** | 24 meses | Mano de obra |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza de luminarias** | Semestral | Contratista |
| **Inspección visual postes** | Trimestral | Contratista |
| **Medición fotométrica** | Anual | Especialista |
| **Revisión conexiones** | Anual | Electricista |
| **Actualización software** | Según disponibilidad | Fabricante |

### 9.2 Mantenimiento Correctivo

| Falla | Tiempo de Respuesta | Tiempo de Reparación |
|:------|:-------------------|:---------------------|
| **Luminaria apagada** | 4 horas | 8 horas |
| **Poste dañado** | 8 horas | 48 horas |
| **Falla de comunicación** | 2 horas | 4 horas |
| **Falla de control** | 1 hora | 2 horas |

### 9.3 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **Luminarias completas** | 5% del total | 30 días |
| **Drivers LED** | 10% del total | 15 días |
| **Sensores crepusculares** | 10 unidades | 10 días |
| **Controladores** | 2 unidades | 20 días |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Luminaria LED 150W Tipo A | und | 680 | $850 | $578,000 |
| 2 | Luminaria LED 100W Tipo B | und | 240 | $650 | $156,000 |
| 3 | Luminaria LED 60W Tipo C | und | 180 | $450 | $81,000 |
| 4 | Poste 12m galvanizado Tipo A | und | 680 | $1,200 | $816,000 |
| 5 | Poste 10m galvanizado Tipo B | und | 420 | $950 | $399,000 |
| 6 | Sistema de control y automatización | lote | 1 | $180,000 | $180,000 |
| 7 | Red eléctrica subterránea | km | 85 | $12,500 | $1,062,500 |
| 8 | Transformadores de distribución | und | 25 | $8,500 | $212,500 |
| 9 | Instalación y puesta en marcha | lote | 1 | $420,000 | $420,000 |
| 10 | Contingencias (5%) | lote | 1 | $195,250 | $195,250 |
| | | | | **TOTAL** | **$4,100,250** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Realizar cálculos fotométricos detallados por zona
- [ ] Solicitar cotizaciones de fabricantes LED
- [ ] Coordinar con diseño eléctrico de subestaciones
- [ ] Validar ubicaciones con topografía del proyecto
- [ ] Establecer cronograma de instalación por tramos
- [ ] Definir procedimientos de mantenimiento

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Eléctrico | Especificaciones técnicas iniciales |

---

**Elaborado por:** Ingeniero Eléctrico  
**Revisado por:** Coordinador Técnico  
**Aprobado por:** Gerente de Proyecto  

**Fecha de elaboración:** 21/10/2025  
**Próxima revisión:** 30/11/2025