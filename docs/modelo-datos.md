# 📊 Modelo de Datos - Acompañamiento Adultos Mayores

## 📌 Descripción General

Este documento define la estructura de la base de datos para la aplicación de acompañamiento de adultos mayores. Incluye todas las entidades, relaciones, atributos y restricciones.

---

## 🗄️ Entidades y Atributos

### **1. ADULTO_MAYOR**
Representa a la persona mayor que usa la aplicación.

```
ADULTO_MAYOR
├── id (UUID) [PRIMARY KEY]
├── nombre (VARCHAR 100) [REQUIRED]
├── apellido (VARCHAR 100) [REQUIRED]
├── edad (INT) [REQUIRED, >= 65]
├── email (VARCHAR 120) [UNIQUE, NULLABLE]
├── telefono (VARCHAR 20) [REQUIRED]
├── genero (ENUM: M, F, Otro) [REQUIRED]
├── nivel_tecnologia (ENUM: basico, intermedio, avanzado) [DEFAULT: basico]
├── direccion (VARCHAR 255) [NULLABLE]
├── ciudad (VARCHAR 100) [NULLABLE]
├── pais (VARCHAR 100) [NULLABLE]
├── foto_perfil (VARCHAR 500) [NULLABLE]
├── estado (ENUM: activo, inactivo, suspendido) [DEFAULT: activo]
├── fecha_registro (TIMESTAMP) [DEFAULT: NOW()]
├── ultima_actividad (TIMESTAMP) [NULLABLE]
├── notas_medicas (TEXT) [NULLABLE]
├── alergias (TEXT) [NULLABLE]
└── condiciones_medicas (TEXT) [NULLABLE]
```

---

### **2. FAMILIAR**
Representa a los familiares o cuidadores del adulto mayor.

```
FAMILIAR
├── id (UUID) [PRIMARY KEY]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR]
├── nombre (VARCHAR 100) [REQUIRED]
├── apellido (VARCHAR 100) [REQUIRED]
├── relacion (ENUM: hijo, hija, nieto, nieta, hermano, hermana, sobrino, otro) [REQUIRED]
├── email (VARCHAR 120) [UNIQUE, REQUIRED]
├── telefono (VARCHAR 20) [REQUIRED]
├── direccion (VARCHAR 255) [NULLABLE]
├── ciudad (VARCHAR 100) [NULLABLE]
├── pais (VARCHAR 100) [NULLABLE]
├── foto_perfil (VARCHAR 500) [NULLABLE]
├── permisos (JSONB) [DEFAULT: {ver_estado: true}]
│   ├── ver_estado (BOOLEAN)
│   ├── enviar_mensajes (BOOLEAN)
│   ├── cargar_medicinas (BOOLEAN)
│   ├── cargar_turnos (BOOLEAN)
│   ├── recibir_alertas (BOOLEAN)
│   └── ver_historial (BOOLEAN)
├── estado (ENUM: activo, inactivo, bloqueado) [DEFAULT: activo]
├── fecha_registro (TIMESTAMP) [DEFAULT: NOW()]
└── es_contacto_emergencia (BOOLEAN) [DEFAULT: false]
```

---

### **3. MEDICINAS**
Registro de medicinas que toma el adulto mayor.

```
MEDICINAS
├── id (UUID) [PRIMARY KEY]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR]
├── familiar_id (UUID) [FOREIGN KEY → FAMILIAR, REQUIRED]
├── nombre (VARCHAR 150) [REQUIRED]
├── dosis (VARCHAR 100) [REQUIRED]
│   └── Ejemplo: "1 comprimido", "10ml", "2 capsulas"
├── unidad (ENUM: comprimido, capsula, ml, gota, otro) [REQUIRED]
├── cantidad (INT) [REQUIRED]
├── horarios (JSONB) [REQUIRED]
│   └── Ejemplo: ["08:00", "14:00", "20:00"]
├── frecuencia (ENUM: diaria, interdiaria, semanal, cada_X_dias) [REQUIRED]
├── dias_semana (ARRAY[INT]) [NULLABLE]
│   └── 0=Lunes, 1=Martes, ..., 6=Domingo
├── fecha_inicio (DATE) [REQUIRED]
├── fecha_fin (DATE) [NULLABLE]
├── indicaciones_especiales (TEXT) [NULLABLE]
├── efectos_secundarios (TEXT) [NULLABLE]
├── cargada_por (UUID) [FOREIGN KEY → FAMILIAR]
├── activa (BOOLEAN) [DEFAULT: true]
├── fecha_registro (TIMESTAMP) [DEFAULT: NOW()]
└── ultima_actualizacion (TIMESTAMP) [ON UPDATE: NOW()]
```

---

### **4. TURNOS_MEDICOS**
Registro de turnos/citas médicas del adulto mayor.

```
TURNOS_MEDICOS
├── id (UUID) [PRIMARY KEY]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR]
├── familiar_id (UUID) [FOREIGN KEY → FAMILIAR]
├── tipo_especialidad (ENUM: cardiologia, neurologia, oftalmologia, dentista, medico_general, otro) [REQUIRED]
├── nombre_medico (VARCHAR 150) [NULLABLE]
├── nombre_centro (VARCHAR 150) [REQUIRED]
├── direccion (VARCHAR 255) [REQUIRED]
├── telefono_centro (VARCHAR 20) [NULLABLE]
├── fecha (DATE) [REQUIRED]
├── hora (TIME) [REQUIRED]
├── duracion_estimada_minutos (INT) [DEFAULT: 30]
├── motivo (TEXT) [REQUIRED]
├── notas_importantes (TEXT) [NULLABLE]
├── requiere_acompanante (BOOLEAN) [DEFAULT: false]
├── confirmado (BOOLEAN) [DEFAULT: false]
├── asistio (BOOLEAN) [NULLABLE]
├── diagnostico_resultados (TEXT) [NULLABLE]
├── proxima_cita_sugerida (DATE) [NULLABLE]
├── cargado_por (UUID) [FOREIGN KEY → FAMILIAR]
├── recordatorio_enviado (BOOLEAN) [DEFAULT: false]
├── fecha_registro (TIMESTAMP) [DEFAULT: NOW()]
└── ultima_actualizacion (TIMESTAMP) [ON UPDATE: NOW()]
```

---

### **5. CHECK_IN** (Charlas/Interacciones Diarias)
Registro de las charlas diarias y preguntas.

```
CHECK_IN
├── id (UUID) [PRIMARY KEY]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR]
├── tipo_pregunta (ENUM: estado_animo, actividades, salud, tiempo, ejercicio, adivinanza, compras, otro) [REQUIRED]
├── pregunta (TEXT) [REQUIRED]
│   └── Ejemplo: "¿Cómo amaneciste hoy?", "¿Qué ejercicio hiciste?"
├── respuesta (TEXT) [NULLABLE]
├── respondido (BOOLEAN) [DEFAULT: false]
├── timestamp_creacion (TIMESTAMP) [DEFAULT: NOW()]
├── timestamp_respuesta (TIMESTAMP) [NULLABLE]
├── tiempo_respuesta_minutos (INT) [NULLABLE]
├── calidad_respuesta (ENUM: completa, parcial, vaga, sin_respuesta) [NULLABLE]
├── necesita_seguimiento (BOOLEAN) [DEFAULT: false]
├── notas_seguimiento (TEXT) [NULLABLE]
├── activo (BOOLEAN) [DEFAULT: true]
└── enviado_por_sistema (BOOLEAN) [DEFAULT: true]
```

---

### **6. ALERTAS**
Sistema de alertas y notificaciones.

```
ALERTAS
├── id (UUID) [PRIMARY KEY]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR]
├── tipo (ENUM: no_responde, medicina_olvidada, turno_proximo, emergencia, mensaje_familiar, otra) [REQUIRED]
├── severidad (ENUM: baja, media, alta, critica) [DEFAULT: media]
├── titulo (VARCHAR 200) [REQUIRED]
├── descripcion (TEXT) [REQUIRED]
├── relacionado_con (VARCHAR 50) [NULLABLE]
│   └── Ejemplo: "medicina_123", "turno_456", "checkin_789"
├── intento_numero (INT) [DEFAULT: 1]
│   └── Tracking de reintentos (1er intento, 2do intento, notificar familiar)
├── familia_notificados (ARRAY[UUID]) [NULLABLE]
│   └── IDs de familiares que recibieron la alerta
├── estado (ENUM: pendiente, enviada, resuelta, ignorada) [DEFAULT: pendiente]
├── fecha_creacion (TIMESTAMP) [DEFAULT: NOW()]
├── fecha_resolucion (TIMESTAMP) [NULLABLE]
├── resuelto_por (UUID) [NULLABLE]
│   └── ID del familiar o admin que cerró la alerta
├── notas_resolucion (TEXT) [NULLABLE]
└── activa (BOOLEAN) [DEFAULT: true]
```

---

### **7. MENSAJES** (Chat Familiar)
Comunicación bidireccional entre adulto mayor y familiares.

```
MENSAJES
├── id (UUID) [PRIMARY KEY]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR]
├── remitente_id (UUID) [REQUIRED]
│   └── Puede ser adulto_mayor_id o familiar_id
├── remitente_tipo (ENUM: adulto_mayor, familiar) [REQUIRED]
├── destinatario_id (UUID) [REQUIRED]
│   └── Puede ser adulto_mayor_id o familiar_id
├── destinatario_tipo (ENUM: adulto_mayor, familiar) [REQUIRED]
├── contenido (TEXT) [REQUIRED]
├── tipo_contenido (ENUM: texto, foto, audio, video, archivo) [DEFAULT: texto]
├── url_archivo (VARCHAR 500) [NULLABLE]
├── leido (BOOLEAN) [DEFAULT: false]
├── timestamp_creacion (TIMESTAMP) [DEFAULT: NOW()]
├── timestamp_lectura (TIMESTAMP) [NULLABLE]
├── editado (BOOLEAN) [DEFAULT: false]
├── timestamp_edicion (TIMESTAMP) [NULLABLE]
├── borrado_por_remitente (BOOLEAN) [DEFAULT: false]
├── borrado_por_destinatario (BOOLEAN) [DEFAULT: false]
└── reaccion (VARCHAR 10) [NULLABLE]
    └── Emoji: 👍 ❤️ 😂 etc.
```

---

### **8. USUARIO** (Autenticación)
Tabla de usuarios para login (incluye adultos mayores y familiares).

```
USUARIO
├── id (UUID) [PRIMARY KEY]
├── email (VARCHAR 120) [UNIQUE, REQUIRED]
├── password_hash (VARCHAR 255) [REQUIRED]
├── tipo (ENUM: adulto_mayor, familiar, admin) [REQUIRED]
├── adulto_mayor_id (UUID) [FOREIGN KEY → ADULTO_MAYOR, NULLABLE]
├── familiar_id (UUID) [FOREIGN KEY → FAMILIAR, NULLABLE]
├── activo (BOOLEAN) [DEFAULT: true]
├── email_verificado (BOOLEAN) [DEFAULT: false]
├── telefono_verificado (BOOLEAN) [DEFAULT: false]
├── dos_factor_activado (BOOLEAN) [DEFAULT: false]
├── ultimo_login (TIMESTAMP) [NULLABLE]
├── fecha_registro (TIMESTAMP) [DEFAULT: NOW()]
├── ultima_actualizacion (TIMESTAMP) [ON UPDATE: NOW()]
└── intentos_fallidos_login (INT) [DEFAULT: 0]
```

---

## 📈 Relaciones (ER Diagram)

```
ADULTO_MAYOR (1) ──── (N) FAMILIAR
ADULTO_MAYOR (1) ──── (N) MEDICINAS
ADULTO_MAYOR (1) ──── (N) TURNOS_MEDICOS
ADULTO_MAYOR (1) ──── (N) CHECK_IN
ADULTO_MAYOR (1) ──── (N) ALERTAS
ADULTO_MAYOR (1) ──── (N) MENSAJES (como destinatario o remitente)

FAMILIAR (1) ──── (N) MEDICINAS (cargador)
FAMILIAR (1) ──── (N) TURNOS_MEDICOS (cargador)
FAMILIAR (1) ──── (N) ALERTAS (notificado)
FAMILIAR (1) ──── (N) MENSAJES (como remitente o destinatario)

USUARIO (1) ──── (1) ADULTO_MAYOR (opcional)
USUARIO (1) ──── (1) FAMILIAR (opcional)
```

---

## 🔑 Índices Recomendados

Para optimizar queries frecuentes:

```sql
-- Búsqueda por adulto mayor
CREATE INDEX idx_medicinas_am ON MEDICINAS(adulto_mayor_id);
CREATE INDEX idx_turnos_am ON TURNOS_MEDICOS(adulto_mayor_id);
CREATE INDEX idx_checkin_am ON CHECK_IN(adulto_mayor_id);
CREATE INDEX idx_alertas_am ON ALERTAS(adulto_mayor_id);
CREATE INDEX idx_mensajes_am ON MENSAJES(adulto_mayor_id);

-- Búsqueda por familiar
CREATE INDEX idx_familiar_am ON FAMILIAR(adulto_mayor_id);
CREATE INDEX idx_medicinas_familiar ON MEDICINAS(cargada_por);

-- Búsquedas por estado
CREATE INDEX idx_alertas_estado ON ALERTAS(estado);
CREATE INDEX idx_adulto_estado ON ADULTO_MAYOR(estado);
CREATE INDEX idx_familiar_estado ON FAMILIAR(estado);
CREATE INDEX idx_usuario_email ON USUARIO(email);

-- Búsquedas por timestamp
CREATE INDEX idx_checkin_fecha ON CHECK_IN(timestamp_creacion);
CREATE INDEX idx_alertas_fecha ON ALERTAS(fecha_creacion);
CREATE INDEX idx_mensajes_fecha ON MENSAJES(timestamp_creacion);

-- Búsquedas complejas
CREATE INDEX idx_medicinas_activas ON MEDICINAS(adulto_mayor_id, activa);
CREATE INDEX idx_turnos_proximos ON TURNOS_MEDICOS(adulto_mayor_id, fecha);
CREATE INDEX idx_alertas_pendientes ON ALERTAS(adulto_mayor_id, estado);
```

---

## 🔄 Flujos Principales de Datos

### **Flujo 1: Check-In (Charla Diaria)**
```
1. Sistema genera CHECK_IN automático cada 4h
2. Notifica al ADULTO_MAYOR
3. ADULTO_MAYOR responde (guarda respuesta)
4. Si no responde en X tiempo:
   - 1er intento: Recordatorio suave
   - 2do intento: Recordatorio más urgente
   - 3er intento: Crea ALERTA y notifica FAMILIARES
```

### **Flujo 2: Medicinas**
```
1. FAMILIAR carga MEDICINA con horarios
2. Sistema recuerda al ADULTO_MAYOR en cada horario
3. ADULTO_MAYOR marca como "tomada"
4. Si no marca en X minutos:
   - Crea ALERTA tipo "medicina_olvidada"
   - Notifica al FAMILIAR cargador
```

### **Flujo 3: Turnos Médicos**
```
1. FAMILIAR carga TURNO_MEDICO
2. Sistema envía recordatorios:
   - 7 días antes
   - 1 día antes
   - 2 horas antes
3. Después del turno: pregunta si asistió
4. Permite registrar diagnóstico/resultados
```

### **Flujo 4: Comunicación Familiar**
```
1. FAMILIAR envía MENSAJE al ADULTO_MAYOR
2. ADULTO_MAYOR recibe notificación
3. ADULTO_MAYOR o FAMILIAR leen el mensaje
4. Se marca como leído y se registra timestamp
```

---

## 🔐 Restricciones y Reglas de Negocio

| Regla | Descripción |
|-------|-------------|
| **R1** | Un ADULTO_MAYOR debe tener al menos 1 FAMILIAR asociado |
| **R2** | Un FAMILIAR no puede cargar MEDICINAS para adultos mayores que no estén asociados |
| **R3** | Las MEDICINAS con fecha_fin < HOY deben marcarse como inactivas |
| **R4** | Los TURNOS_MEDICOS pasados no pueden editarse (solo lectura) |
| **R5** | Las ALERTAS críticas deben notificar a ALL FAMILIARES con permiso `recibir_alertas` |
| **R6** | Un CHECK_IN sin respuesta > 4h genera ALERTA automática |
| **R7** | Los MENSAJES borrados lógicamente no deben ser visibles en chat |
| **R8** | El email y teléfono deben ser únicos por USUARIO |
| **R9** | Permisos de FAMILIAR se validan antes de cada operación |
| **R10** | Auditoría: todos los cambios deben registrarse con timestamp y usuario |

---

## 📱 Estados y Enumeraciones

### **Estados de ADULTO_MAYOR**
- `activo`: Usando la aplicación normalmente
- `inactivo`: No ha usado en 30+ días
- `suspendido`: Cuenta suspendida por admin

### **Estados de ALERTA**
- `pendiente`: Alerta creada, no enviada
- `enviada`: Notificación enviada a familiares
- `resuelta`: Problema solucionado
- `ignorada`: Alerta descartada

### **Severidad de ALERTA**
- `baja`: Información general
- `media`: Acción recomendada (ej: medicina olvidada)
- `alta`: Requiere atención pronta (ej: no responde)
- `critica`: Emergencia (ej: alerta manual de AM)

---

## 🎯 Próximos Pasos

1. ✅ Validar modelo con stakeholders
2. ⏳ Crear script de creación de BD (SQL)
3. ⏳ Definir ORM (Sequelize, TypeORM, SQLAlchemy)
4. ⏳ Crear migraciones de BD
5. ⏳ Documentar endpoints de API

---

**Última actualización:** Mayo 2026
