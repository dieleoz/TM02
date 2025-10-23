# T02 - ANÁLISIS DE REQUISITOS UF3: RÍO SOGAMOSO - EL JUNCAL

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Código**: STC-APP4G-UF3-T02
- **Fecha**: 2024-10-23
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_UF3_RIO_SOGAMOSO_EL_JUNCAL.md

## 🎯 OBJETIVO DEL ANÁLISIS
Definir requisitos técnicos, normativos y operacionales para el mejoramiento de 77.2 km de calzada existente, incluyendo la reubicación del Peaje La Gómez y la construcción del Intercambio San Martín Norte.

---

## 📋 ANÁLISIS DE REQUISITOS POR SISTEMA

### **1. SISTEMA VIAL PRINCIPAL - MEJORAMIENTO 77.2 KM**

#### **Requisitos Técnicos**
- **R-UF3-V01**: Velocidad de diseño ≥ 80 km/h (categoría primaria)
- **R-UF3-V02**: Ancho de calzada: 7.30 m (2 carriles de 3.65 m)
- **R-UF3-V03**: Bermas: 1.80 m a cada lado
- **R-UF3-V04**: Capacidad: ≥ 1,500 veh/h/carril (Nivel de Servicio C)
- **R-UF3-V05**: Estructura pavimento: Diseño para 20 años, tráfico pesado
- **R-UF3-V06**: Índice de rugosidad ≤ 2.5 m/km al final de construcción

#### **Requisitos Geométricos**
- **R-UF3-G01**: Pendiente máxima: 6% (terreno ondulado)
- **R-UF3-G02**: Radio mínimo horizontal: 230 m (V=80 km/h)
- **R-UF3-G03**: Distancia visibilidad parada: ≥ 130 m
- **R-UF3-G04**: Distancia visibilidad adelantamiento: ≥ 540 m (30% longitud)
- **R-UF3-G05**: Peralte máximo: 8%

#### **Requisitos de Calidad**
- **R-UF3-C01**: Regularidad superficial IRI ≤ 2.0 m/km
- **R-UF3-C02**: Resistencia al deslizamiento ≥ 0.45 (coef. fricción)
- **R-UF3-C03**: Drenabilidad: evacuación agua superficial < 2 min
- **R-UF3-C04**: Durabilidad: vida útil ≥ 20 años sin mantenimiento mayor

### **2. SISTEMA PEAJE - REUBICACIÓN LA GÓMEZ**

#### **Requisitos Operacionales**
- **R-UF3-P01**: Capacidad: 6 casetas (4 operativas + 2 reserva)
- **R-UF3-P02**: Tiempo servicio: ≤ 15 segundos por vehículo
- **R-UF3-P03**: Colas máximas: ≤ 50 m en hora pico
- **R-UF3-P04**: Disponibilidad: 99.5% anual (máximo 44 horas fuera servicio)
- **R-UF3-P05**: Transición sin pérdida ingresos durante reubicación

#### **Requisitos Tecnológicos**
- **R-UF3-T01**: Sistema recaudo electrónico (TAG + manual)
- **R-UF3-T02**: Integración con sistema central concesionario
- **R-UF3-T03**: Cámaras seguridad y control acceso
- **R-UF3-T04**: Sistema pesaje dinámico (WIM)
- **R-UF3-T05**: Comunicaciones redundantes (fibra óptica + radio)

#### **Requisitos de Infraestructura**
- **R-UF3-I01**: Edificio administración: 200 m²
- **R-UF3-I02**: Área total: 2.5 hectáreas
- **R-UF3-I03**: Carriles aproximación: 150 m antes de casetas
- **R-UF3-I04**: Carriles salida: 100 m después de casetas
- **R-UF3-I05**: Facilidades usuarios: baños, cafetería, parqueadero

### **3. SISTEMA INTERCAMBIO SAN MARTÍN NORTE**

#### **Requisitos Funcionales**
- **R-UF3-IN01**: Tipo: Diamante modificado (4 movimientos)
- **R-UF3-IN02**: Capacidad rampas: 800 veh/h cada una
- **R-UF3-IN03**: Velocidad rampas: 60 km/h
- **R-UF3-IN04**: Radio mínimo rampas: 120 m
- **R-UF3-IN05**: Pendiente máxima rampas: 5%

#### **Requisitos Estructurales**
- **R-UF3-ES01**: Puente principal: luz ≥ 30 m (cruce vía principal)
- **R-UF3-ES02**: Carga viva: HL-93 + sobrecarga peatonal
- **R-UF3-ES03**: Vida útil: 75 años
- **R-UF3-ES04**: Sismo: NSR-10 zona de amenaza intermedia
- **R-UF3-ES05**: Gálibo vertical: 5.50 m mínimo

#### **Requisitos Integración Urbana**
- **R-UF3-IU01**: Conexión con red vial urbana San Martín
- **R-UF3-IU02**: Accesos peatonales y ciclistas
- **R-UF3-IU03**: Integración paisajística
- **R-UF3-IU04**: Minimizar afectación predial urbana
- **R-UF3-IU05**: Coordinación con POT municipal

### **4. SISTEMA DRENAJE - MEJORAMIENTO INTEGRAL**

#### **Requisitos Hidrológicos**
- **R-UF3-H01**: Período retorno: 25 años (drenaje menor)
- **R-UF3-H02**: Período retorno: 100 años (drenaje mayor)
- **R-UF3-H03**: Tiempo concentración ≤ 10 minutos
- **R-UF3-H04**: Coeficiente escorrentía según uso del suelo
- **R-UF3-H05**: Evaluación cambio climático (+20% precipitación)

#### **Requisitos Técnicos**
- **R-UF3-DT01**: Alcantarillas: diámetro mínimo 0.90 m
- **R-UF3-DT02**: Cunetas: capacidad según intensidad lluvia
- **R-UF3-DT03**: Filtros subdrenaje: k ≥ 1x10⁻³ m/s
- **R-UF3-DT04**: Pendiente mínima: 0.5%
- **R-UF3-DT05**: Materiales: vida útil ≥ 50 años

---

## ⚠️ ANÁLISIS DE RIESGOS POR REQUISITO

### **RIESGOS CRÍTICOS**
- **RC-UF3-01**: Reubicación peaje sin pérdida ingresos
  - *Impacto*: Alto (financiero)
  - *Probabilidad*: Media
  - *Mitigación*: Plan detallado transición operativa

- **RC-UF3-02**: Estado actual calzada puede requerir reconstrucción
  - *Impacto*: Muy Alto (costos y cronograma)
  - *Probabilidad*: Media
  - *Mitigación*: Diagnóstico detallado inmediato

- **RC-UF3-03**: Interferencias servicios públicos en intercambio
  - *Impacto*: Alto (cronograma)
  - *Probabilidad*: Alta
  - *Mitigación*: Levantamiento detallado redes existentes

### **RIESGOS MODERADOS**
- **RM-UF3-01**: Coordinación con tráfico durante mejoramiento
- **RM-UF3-02**: Gestión predial para intercambio
- **RM-UF3-03**: Condiciones geotécnicas variables en 77.2 km

---

## 📊 MATRIZ DE TRAZABILIDAD

| Requisito | Origen Contractual | Sistema | Prioridad | Verificación |
|-----------|-------------------|---------|-----------|--------------|
| R-UF3-V01 | Anexo Técnico 2.1 | Vial | Alta | Diseño geométrico |
| R-UF3-P01 | Anexo Técnico 3.2 | Peaje | Crítica | Simulación tráfico |
| R-UF3-IN01 | Anexo Técnico 4.1 | Intercambio | Alta | Análisis capacidad |
| R-UF3-H01 | Norma INVIAS | Drenaje | Alta | Estudio hidrológico |

---

## 🎯 CRITERIOS DE ACEPTACIÓN

### **Técnicos**
- ✅ Todos los requisitos R-UF3-* validados por especialistas
- ✅ Diseños aprobados por interventoría
- ✅ Cumplimiento normativa INVIAS vigente
- ✅ Integración exitosa con UF adyacentes

### **Operacionales**
- ✅ Peaje reubicado sin pérdida ingresos
- ✅ Intercambio operativo según capacidad diseño
- ✅ Nivel servicio vial ≥ C en operación
- ✅ Disponibilidad sistemas ≥ 99%

### **Contractuales**
- ✅ Cumplimiento especificaciones técnicas
- ✅ Entrega en cronograma acordado
- ✅ Presupuesto dentro de límites aprobados
- ✅ Calidad según estándares contractuales

---

## 📅 CRONOGRAMA DE VALIDACIÓN

- **Semana 1**: Diagnóstico estado actual calzada
- **Semana 2**: Validación requisitos técnicos con especialistas
- **Semana 3**: Aprobación diseños conceptuales
- **Semana 4**: Integración con cronograma general proyecto

---

## ✅ ESTADO Y PRÓXIMOS PASOS

### **Completado**
- [x] Identificación requisitos por sistema
- [x] Análisis de riesgos preliminar
- [x] Matriz de trazabilidad inicial

### **Pendiente**
- [ ] Validación con contratos reales
- [ ] Diagnóstico estado actual calzada
- [ ] Diseños conceptuales peaje e intercambio
- [ ] Integración con análisis T03 (Arquitectura)

---
**Próximo paso**: T03 - Arquitectura de Sistemas UF3