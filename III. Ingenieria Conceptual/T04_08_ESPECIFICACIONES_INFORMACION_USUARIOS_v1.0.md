# T04_08: ESPECIFICACIONES TÉCNICAS - SISTEMA DE INFORMACIÓN A USUARIOS
## Proyecto APP Nuevo Contrato Vial

**Fecha:** 21/10/2025  
**Sistema:** Sistema de Información a Usuarios  
**Responsable:** Ingeniero de Sistemas ITS  
**Versión:** 1.0  
**Referencia T01:** T01_08_FICHA_SISTEMA_INFORMACION_USUARIOS_v1.0.md  
**Referencia T03:** T03_08_ARQUITECTURA_INFORMACION_USUARIOS_v1.0.md  

---

## 📋 **CONTROL DE CAMBIOS**

| Versión | Fecha | Cambios | Autor |
|:--------|:------|:--------|:------|
| 1.0 | 21/10/2025 | Creación inicial | Ingeniero de Sistemas ITS |

---

## 1. IDENTIFICACIÓN Y ALCANCE

### 1.1 Identificación del Sistema

| Campo | Valor |
|:------|:------|
| **Nombre del sistema** | Sistema de Información a Usuarios |
| **Categoría** | ITS - Información y Comunicación |
| **Código interno** | T04-08-v1.0 |
| **Cantidad total** | 45 postes SOS + sistemas complementarios |
| **CAPEX estimado** | USD $1,680,000 |
| **Documentos base** | T01_08, T02_08, T03_08, Validación Contractual |

### 1.2 Alcance de las Especificaciones

**Este documento especifica:**
- ✅ Postes SOS de emergencia
- ✅ Sistemas de comunicación de voz
- ✅ Señalización informativa estática
- ✅ Sistemas de audio para túneles
- ✅ Aplicaciones móviles y web

**Este documento NO especifica:**
- ❌ Paneles LED de mensaje variable (ver T04_04)
- ❌ Centro de atención telefónica (ver T04_11)
- ❌ Sistemas de peaje (ver T04_01)

---

## 2. MARCO NORMATIVO Y CONTRACTUAL

### 2.1 Referencias Contractuales

| Documento | Sección | Requisito Clave |
|:----------|:--------|:----------------|
| **Apéndice Técnico 1** | 8.1.2 | Postes SOS cada 2 km |
| **Apéndice Técnico 2** | 6.2.1 | Comunicación bidireccional |
| **Apéndice Técnico 3** | 7.1.3 | Información en tiempo real |

### 2.2 Normativa Aplicable

#### Normativa Nacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **Manual de Señalización INVIAS** | Señalización vial | Diseño de señales |
| **Ley 1581/2012** | Protección de datos personales | Manejo de información |
| **RETIE** | Instalaciones eléctricas | Equipos eléctricos |

#### Normativa Internacional

| Norma | Título | Aplicación |
|:------|:-------|:-----------|
| **ISO 3864** | Graphical symbols - Safety signs | Señalización |
| **ITU-T P.862** | Perceptual evaluation of speech quality | Calidad de voz |
| **WCAG 2.1** | Web Content Accessibility Guidelines | Accesibilidad web |#
## 2.3 Certificaciones Requeridas

| Certificación | Organismo | Obligatoria | Aplicación |
|:--------------|:----------|:------------|:-----------|
| **Homologación CRC** | CRC Colombia | ✅ Sí | Equipos de telecomunicaciones |
| **Certificación de accesibilidad** | ICONTEC | ⏳ Opcional | Interfaces de usuario |
| **Certificación ISO 27001** | Organismo certificador | ✅ Sí | Seguridad de información |

---

## 3. ESPECIFICACIONES TÉCNICAS GENERALES

### 3.1 Clasificación de Componentes

#### 3.1.1 Postes SOS (Sistema Principal)

**Cantidad:** 45 unidades  
**Ubicación:** Cada 2 km en promedio  
**Función:** Comunicación de emergencia bidireccional

#### 3.1.2 Señalización Informativa

**Cantidad:** 180 señales  
**Tipos:** Informativas, preventivas, reglamentarias  
**Material:** Lámina reflectiva grado diamante

#### 3.1.3 Sistemas Digitales

**Componentes:** App móvil, portal web, API  
**Usuarios:** Público general, operadores, autoridades

### 3.2 Características Ambientales

| Parámetro | Especificación Mínima | Referencia |
|:----------|:---------------------|:-----------|
| **Temperatura operación** | -20°C a +70°C | IEC 60068 |
| **Humedad relativa** | 0-95% sin condensación | IEC 60068 |
| **Protección IP** | IP65 mínimo | IEC 60529 |
| **Resistencia a viento** | 150 km/h | AASHTO |
| **Resistencia UV** | Sin degradación 10 años | ASTM G154 |

### 3.3 Requisitos de Comunicación

| Parámetro | Especificación | Protocolo |
|:----------|:---------------|:----------|
| **Comunicación de voz** | Full-duplex, cancelación eco | SIP/VoIP |
| **Calidad de audio** | MOS >4.0 | ITU-T P.862 |
| **Tiempo de establecimiento** | <3 segundos | - |
| **Disponibilidad** | ≥99% | SLA |

---

## 4. ESPECIFICACIONES POR COMPONENTE

### 4.1 Postes SOS de Emergencia

#### 4.1.1 Descripción General

Postes de comunicación de emergencia para permitir a los usuarios solicitar ayuda directamente al CCO en caso de accidentes, averías o emergencias médicas.

#### 4.1.2 Especificaciones Técnicas

**Estructura Principal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Altura total** | 2.5 metros | Medición física |
| **Material** | Acero inoxidable AISI 304 | Certificado material |
| **Espesor pared** | 3 mm mínimo | Inspección ultrasónica |
| **Acabado** | Pulido satinado | Inspección visual |
| **Base** | Concreto armado 60x60x80 cm | Planos estructurales |
| **Anclaje** | 4 pernos M16 acero inoxidable | Inspección física |

**Panel Frontal:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Dimensiones** | 40 x 60 cm | Medición física |
| **Material** | Aluminio anodizado | Certificado material |
| **Color** | Amarillo RAL 1023 | Comparación visual |
| **Botón SOS** | Diámetro 10 cm, rojo | Inspección visual |
| **Micrófono** | Omnidireccional, cancelación ruido | Prueba acústica |
| **Altavoz** | 10W, respuesta 300-3400 Hz | Prueba acústica |

#### 4.1.3 Sistema de Comunicación

**Especificaciones de Audio:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Micrófono** | Sensibilidad -40 dBV/Pa | Medición acústica |
| **Altavoz** | SPL 85 dB @ 1m | Medición acústica |
| **Cancelación de eco** | >40 dB | Medición acústica |
| **Supresión de ruido** | >20 dB | Medición acústica |
| **Ancho de banda** | 300-3400 Hz | Analizador de espectro |

**Procesamiento Digital:**
- Procesador: ARM Cortex-A9 o superior
- Memoria: 1 GB RAM, 8 GB almacenamiento
- Códecs: G.711, G.729, G.722
- Protocolos: SIP 2.0, RTP/RTCP
- Interfaces: Ethernet, 4G/LTE

#### 4.1.4 Características Adicionales

**Iluminación:**
- LED perimetral azul (identificación nocturna)
- LED rojo intermitente (llamada activa)
- Sensor crepuscular automático
- Consumo: 5W máximo

**Alimentación:**
- Tensión: 12V DC
- Consumo standby: 8W
- Consumo activo: 25W
- Respaldo: Batería 12V 7Ah (4 horas)

**Seguridad:**
- Cerradura triangular universal
- Protección anti-vandálica
- Registro de eventos
- Cámara de seguridad integrada (opcional)

#### 4.1.5 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **GAI-Tronics** - Modelo: Commander Smart
2. **Federal Signal** - Modelo: Informer
3. **R.R. Donnelley** - Modelo: Emergency Phone
4. **O equivalente** que cumpla especificaciones

### 4.2 Señalización Informativa

#### 4.2.1 Descripción General

Sistema de señalización vial estática para información, orientación y seguridad de los usuarios de la autopista.

#### 4.2.2 Especificaciones Técnicas

**Señales Informativas Principales:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Dimensiones** | 2.4 x 1.2 m | Medición física |
| **Sustrato** | Lámina de aluminio 3 mm | Inspección técnica |
| **Reflectivo** | Grado diamante (DG3) | Certificado fabricante |
| **Coeficiente reflectivo** | >250 cd/lx/m² (blanco) | Medición fotométrica |
| **Vida útil** | 10 años mínimo | Certificado fabricante |

**Señales Preventivas y Reglamentarias:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Dimensiones** | 75 x 75 cm | Medición física |
| **Sustrato** | Lámina de aluminio 2 mm | Inspección técnica |
| **Reflectivo** | Grado ingeniería (EG) | Certificado fabricante |
| **Coeficiente reflectivo** | >70 cd/lx/m² (blanco) | Medición fotométrica |
| **Vida útil** | 7 años mínimo | Certificado fabricante |

#### 4.2.3 Estructuras de Soporte

**Pórticos de Señalización:**
- Material: Acero galvanizado ASTM A572
- Altura libre: 5.5 metros mínimo
- Carga de viento: 150 km/h
- Cimentación: Concreto f'c=28 MPa

**Postes Laterales:**
- Material: Acero galvanizado
- Altura: 2.5-4.0 metros
- Diámetro: 89-114 mm
- Base: Concreto 40x40x60 cm

#### 4.2.4 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **3M** - Modelo: Diamond Grade DG³
2. **Avery Dennison** - Modelo: T-11500 Series
3. **Orafol** - Modelo: ORALITE 5900 Series
4. **O equivalente** que cumpla especificaciones

### 4.3 Aplicación Móvil y Portal Web

#### 4.3.1 Descripción General

Plataforma digital para proporcionar información en tiempo real sobre el estado de la autopista, servicios disponibles y asistencia al usuario.

#### 4.3.2 Especificaciones Funcionales

**Aplicación Móvil:**
| Función | Especificación Mínima | Método de Verificación |
|:--------|:---------------------|:-----------------------|
| **Plataformas** | iOS 12+, Android 8+ | Prueba de compatibilidad |
| **Idiomas** | Español, inglés | Prueba funcional |
| **Tiempo de carga** | <3 segundos | Medición de rendimiento |
| **Tamaño descarga** | <50 MB | Inspección técnica |
| **Actualizaciones** | OTA automáticas | Prueba funcional |

**Funcionalidades Principales:**
- Información de tráfico en tiempo real
- Estado de peajes y tarifas
- Ubicación de servicios (gasolineras, restaurantes)
- Reportes de incidentes
- Asistencia vial y emergencias
- Navegación GPS integrada

**Portal Web:**
| Función | Especificación Mínima | Método de Verificación |
|:--------|:---------------------|:-----------------------|
| **Compatibilidad** | Chrome, Firefox, Safari, Edge | Prueba cross-browser |
| **Responsive** | Móvil, tablet, desktop | Prueba de adaptabilidad |
| **Accesibilidad** | WCAG 2.1 AA | Auditoría de accesibilidad |
| **Tiempo de carga** | <2 segundos | Medición de rendimiento |
| **Disponibilidad** | 99.5% | Monitoreo continuo |

#### 4.3.3 Arquitectura Técnica

**Backend:**
- Lenguaje: Java/Python/Node.js
- Base de datos: PostgreSQL/MySQL
- API: RESTful + GraphQL
- Autenticación: OAuth 2.0
- Hosting: Cloud (AWS/Azure/GCP)

**Frontend:**
- Framework: React/Angular/Vue.js
- Mobile: React Native/Flutter
- CDN: CloudFlare/AWS CloudFront
- Analytics: Google Analytics
- Monitoreo: New Relic/DataDog

#### 4.3.4 Integración de Datos

**Fuentes de Información:**
| Sistema | Tipo de Datos | Frecuencia |
|:--------|:--------------|:-----------|
| **CCO** | Estado de tráfico, incidentes | Tiempo real |
| **Peajes** | Tarifas, tiempos de espera | Cada minuto |
| **Meteorología** | Condiciones climáticas | Cada 15 minutos |
| **Servicios** | Disponibilidad, precios | Cada hora |

### 4.4 Sistema de Audio para Túneles

#### 4.4.1 Descripción General

Sistema de audio para comunicación de emergencia y difusión de información en túneles y pasos deprimidos.

#### 4.4.2 Especificaciones Técnicas

**Altavoces:**
| Parámetro | Especificación Mínima | Método de Verificación |
|:----------|:---------------------|:-----------------------|
| **Potencia** | 30W RMS | Medición eléctrica |
| **Respuesta frecuencia** | 200-8000 Hz | Analizador de espectro |
| **SPL máximo** | 110 dB @ 1m | Medición acústica |
| **Protección IP** | IP65 | Certificado fabricante |
| **Material** | Acero inoxidable | Inspección visual |

**Sistema de Control:**
- Amplificadores: Clase D, >90% eficiencia
- Procesamiento: DSP integrado
- Zonas: Mínimo 4 zonas independientes
- Protocolos: Dante, AES67
- Respaldo: Fuente redundante

#### 4.4.3 Fabricantes de Referencia

**Fabricantes aceptables:**
1. **Bosch** - Modelo: PRAESENSA
2. **TOA** - Modelo: VX-2000 Series
3. **Yamaha** - Modelo: VXL Series
4. **O equivalente** que cumpla especificaciones

---

## 5. INTEGRACIÓN Y COMPATIBILIDAD

### 5.1 Integración con CCO

| Aspecto | Requisito | Verificación |
|:--------|:----------|:-------------|
| **Llamadas SOS** | Enrutamiento automático | Prueba de conectividad |
| **Localización** | GPS automático | Verificación de coordenadas |
| **Grabación** | 100% llamadas | Auditoría de registros |
| **Estadísticas** | Reportes automáticos | Validación de datos |

### 5.2 Integración con Otros Sistemas

| Sistema | Tipo de Interfaz | Datos Intercambiados |
|:--------|:-----------------|:---------------------|
| **Cámaras CCTV** | TCP/IP | Activación por llamada SOS |
| **Paneles LED** | TCP/IP | Mensajes de información |
| **Sistema de Peajes** | API REST | Tarifas, estados |
| **Meteorología** | API REST | Condiciones climáticas |

---

## 6. REQUISITOS DE INSTALACIÓN

### 6.1 Ubicación de Postes SOS

| Criterio | Especificación | Norma |
|:---------|:---------------|:------|
| **Separación** | 2 km máximo | AT1 |
| **Ubicación** | Berma derecha | Manual INVIAS |
| **Distancia de calzada** | 3 metros mínimo | Manual INVIAS |
| **Visibilidad** | 200 metros mínimo | Manual INVIAS |

### 6.2 Instalaciones Eléctricas

| Parámetro | Especificación |
|:----------|:---------------|
| **Alimentación** | 120V AC monofásica |
| **Protección** | Breaker 15A + DPS |
| **Canalización** | PVC 2" subterráneo |
| **Tierras** | <25 Ω resistencia |

### 6.3 Comunicaciones

| Parámetro | Especificación |
|:----------|:---------------|
| **Medio principal** | Fibra óptica |
| **Respaldo** | 4G/LTE |
| **Latencia** | <100 ms |
| **Ancho de banda** | 1 Mbps por poste |

---

## 7. PRUEBAS Y CRITERIOS DE ACEPTACIÓN

### 7.1 Pruebas de Comunicación

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Calidad de voz** | Verificar inteligibilidad | MOS >4.0 |
| **Tiempo de respuesta** | Verificar conexión | <3 segundos |
| **Cancelación de eco** | Verificar audio | >40 dB supresión |
| **Cobertura** | Verificar alcance | 100% postes funcionales |

### 7.2 Pruebas de Aplicaciones

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Rendimiento** | Verificar velocidad | <3 seg carga inicial |
| **Usabilidad** | Verificar experiencia | 90% tareas completadas |
| **Compatibilidad** | Verificar dispositivos | 100% plataformas soportadas |
| **Seguridad** | Verificar protección | Sin vulnerabilidades críticas |

### 7.3 Pruebas de Integración

| Prueba | Objetivo | Criterio de Aceptación |
|:-------|:---------|:-----------------------|
| **Integración CCO** | Verificar conectividad | 100% llamadas enrutadas |
| **Datos en tiempo real** | Verificar actualización | <30 segundos latencia |
| **Respaldo 4G** | Verificar contingencia | Conmutación automática |
| **Grabación** | Verificar almacenamiento | 100% llamadas grabadas |

---

## 8. DOCUMENTACIÓN REQUERIDA

### 8.1 Documentos Técnicos

| Documento | Descripción | Idioma | Cantidad |
|:----------|:------------|:-------|:---------|
| **Manual de usuario** | Guía para usuarios finales | Español | 10 copias + digital |
| **Manual de operación** | Procedimientos CCO | Español | 5 copias + digital |
| **Manual técnico** | Instalación y mantenimiento | Español | 3 copias + digital |
| **Código fuente** | Aplicaciones desarrolladas | - | Digital completo |
| **Documentación API** | Interfaces de programación | Español/Inglés | Digital |

### 8.2 Capacitación

| Programa | Duración | Participantes | Modalidad |
|:---------|:---------|:--------------|:----------|
| **Operación CCO** | 16 horas | Operadores | Presencial |
| **Mantenimiento** | 24 horas | Técnicos | Presencial |
| **Administración sistema** | 32 horas | Administradores | Presencial + Virtual |

### 8.3 Garantías

| Elemento | Garantía Mínima | Observaciones |
|:---------|:----------------|:--------------|
| **Postes SOS** | 60 meses | Hardware completo |
| **Señalización** | 84 meses | Reflectividad garantizada |
| **Software** | 36 meses | Actualizaciones incluidas |
| **Aplicaciones móviles** | 36 meses | Soporte técnico incluido |

---

## 9. MANTENIMIENTO

### 9.1 Mantenimiento Preventivo

| Actividad | Frecuencia | Responsable |
|:----------|:-----------|:------------|
| **Limpieza postes SOS** | Mensual | Contratista |
| **Prueba de comunicación** | Semanal | Contratista |
| **Actualización software** | Según disponibilidad | Desarrollador |
| **Inspección señalización** | Trimestral | Contratista |
| **Medición reflectividad** | Anual | Especialista |

### 9.2 Monitoreo Automático

| Parámetro | Frecuencia | Acción |
|:----------|:-----------|:-------|
| **Estado postes SOS** | Continuo | Alarma automática |
| **Calidad de voz** | Por llamada | Log de calidad |
| **Disponibilidad app** | Continuo | Notificación fallas |
| **Tiempo de respuesta** | Continuo | Dashboard en tiempo real |

### 9.3 Repuestos Críticos

| Componente | Cantidad Mínima | Plazo de Entrega |
|:-----------|:----------------|:-----------------|
| **Módulos de comunicación** | 5 unidades | 15 días |
| **Botones SOS** | 10 unidades | 7 días |
| **Altavoces** | 10 unidades | 10 días |
| **Señales reflectivas** | 20 unidades | 30 días |

---

## 10. PRESUPUESTO Y CANTIDADES

### 10.1 Resumen de Cantidades

| Ítem | Descripción | Unidad | Cantidad | Precio Unit. (USD) | Total (USD) |
|:-----|:------------|:-------|:---------|:-------------------|:------------|
| 1 | Poste SOS completo | und | 45 | $12,500 | $562,500 |
| 2 | Señalización informativa | und | 180 | $850 | $153,000 |
| 3 | Estructuras de soporte | und | 60 | $2,200 | $132,000 |
| 4 | Sistema de audio túneles | lote | 1 | $85,000 | $85,000 |
| 5 | Aplicación móvil | desarrollo | 1 | $120,000 | $120,000 |
| 6 | Portal web | desarrollo | 1 | $95,000 | $95,000 |
| 7 | Integración y APIs | desarrollo | 1 | $75,000 | $75,000 |
| 8 | Instalación y configuración | lote | 1 | $180,000 | $180,000 |
| 9 | Capacitación y documentación | lote | 1 | $45,000 | $45,000 |
| 10 | Contingencias (5%) | lote | 1 | $67,375 | $67,375 |
| | | | | **TOTAL** | **$1,514,875** |

**Nota:** Precios estimados basados en cotizaciones de mercado 2025. Sujeto a actualización con cotizaciones formales.

---

## 11. PRÓXIMOS PASOS

- [ ] Validar ubicaciones de postes SOS con topografía
- [ ] Solicitar cotizaciones de fabricantes especializados
- [ ] Definir especificaciones detalladas de aplicaciones
- [ ] Coordinar con diseño de señalización vial
- [ ] Establecer acuerdos con proveedores de conectividad
- [ ] Planificar cronograma de desarrollo de software

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Sistemas ITS | Especificaciones técnicas iniciales |

---

**Elaborado por:** Ingeniero de Sistemas ITS  
**Revisado por:** Coordinador Técnico  
**Aprobado por:** Gerente de Proyecto  

**Fecha de elaboración:** 21/10/2025  
**Próxima revisión:** 30/11/2025