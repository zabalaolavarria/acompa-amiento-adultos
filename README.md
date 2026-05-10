# 🏥 Acompañamiento para Adultos Mayores

Una aplicación móvil y web diseñada para acompañar a personas mayores de 65 años, ofreciendo charlas diarias, recordatorios de medicinas, seguimiento de salud, y conexión directa con sus familiares.

---

## 📋 Visión del Proyecto

Muchos adultos mayores viven solos y carecen de una red diaria de apoyo. Esta app busca:
- **Reducir la soledad** mediante charlas cortas y diarias
- **Monitorear su bienestar** a través de check-ins regulares
- **Prevenir emergencias** con alertas a familiares ante ausencia de respuesta
- **Facilitar la comunicación** entre el adulto mayor y su familia
- **Recordar tareas importantes** (medicinas, turnos médicos, actividades)

---

## ✨ Funcionalidades Principales

### 1️⃣ **Charlas Diarias**
- Preguntas abiertas y cortas cada 4 horas
- Temas variados:
  - "¿Cómo amaneciste hoy?"
  - "¿Qué tiempo hace donde estás?"
  - "¿Qué actividades tienes planeadas?"
  - Adivinanzas o preguntas para pensar
  - Ejercicios simples (estiramientos, respiración, etc.)
  - Propuestas de compras o tareas

### 2️⃣ **Sistema de Alertas**
- Check-in cada 4 horas
- Si no responde:
  - **1er intento:** Recordatorio suave (insistir)
  - **2do intento:** Recordatorio más urgente
  - **3er intento:** Notificación a familiares registrados
- Los familiares reciben alerta + información de contacto del adulto mayor

### 3️⃣ **Gestión de Medicinas y Turnos**
- Los familiares cargan medicinas, horarios y turnos médicos
- Recordatorios automáticos al adulto mayor
- Historial de cumplimiento (si tomó la medicina, asistió al turno)

### 4️⃣ **Comunicación Familiar**
- Los familiares pueden ver el estado del adulto mayor
- Mensajes bidireccionales entre familiares y adulto mayor
- Notificaciones en tiempo real

### 5️⃣ **Historial y Reportes**
- Registro de charlas y respuestas
- Estadísticas de bienestar (ánimo, actividad, salud)
- Acceso controlado según permisos (solo familiares autorizados)

---

## 👥 Usuarios del Sistema

### **Adulto Mayor (AM)**
- Interfaz simple y amigable
- Fuente grande, colores contrastados
- Navegación intuitiva (pocos botones)
- Notificaciones frecuentes

### **Familiar**
- Panel de control para ver estado del AM
- Cargar medicinas, turnos, contactos
- Recibir alertas y mensajes
- Comunicación directa con el AM

### **Administrador** (futuro)
- Gestión de usuarios
- Reportes generales
- Análisis de datos

---

## 🛠 Stack Tecnológico (Propuesta)

| Capa | Tecnología |
|------|-----------|
| **Frontend Móvil** | React Native / Flutter |
| **Frontend Web** | React / Vue.js |
| **Backend** | Node.js (Express) / Python (Django/FastAPI) |
| **Base de Datos** | PostgreSQL / Firebase |
| **Autenticación** | Firebase Auth / JWT |
| **Notificaciones** | Firebase Cloud Messaging (FCM) |
| **Hosting** | AWS / Google Cloud / Heroku |

---

## 📁 Estructura del Proyecto

```
acompa-amiento-adultos/
├── docs/                    # Documentación
│   ├── arquitectura.md
│   ├── casos-uso.md
│   └── bd-esquema.md
├── backend/                 # API Rest
│   ├── src/
│   ├── tests/
│   └── requirements.txt
├── frontend-mobile/         # App Móvil (React Native/Flutter)
│   ├── src/
│   └── package.json
├── frontend-web/            # Web (React/Vue)
│   ├── src/
│   └── package.json
├── README.md
└── .gitignore
```

---

## 🚀 Roadmap (Fases)

### **Fase 1: MVP (Mínimo Viable)**
- [ ] Autenticación (adulto mayor + familiar)
- [ ] Check-in cada 4 horas (preguntas abiertas)
- [ ] Sistema de alertas (2 intentos + notificar familiar)
- [ ] Cargar medicinas y recordatorios básicos
- [ ] Chat simple entre familiar y adulto

### **Fase 2: Mejoras**
- [ ] Ejercicios con videos/descripciones
- [ ] Adivinanzas y juegos de memoria
- [ ] Historial detallado
- [ ] Reportes semanales/mensuales

### **Fase 3: Expansión**
- [ ] Integración con servicios de emergencia
- [ ] IA para análisis de bienestar
- [ ] Comunidad (conectar abuelos entre sí)
- [ ] Videollamadas con familiares

---

## 🔐 Consideraciones de Privacidad y Seguridad

- Encriptación de datos sensibles
- Consentimiento informado del adulto mayor
- Permisos explícitos para familiares
- Cumplimiento de RGPD / LGPD (según jurisdicción)
- No compartir datos sin autorización

---

## 🤝 Cómo Contribuir

Este proyecto está en fase inicial. Si deseas colaborar:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m "Descripción"`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📝 Licencia

Por definir

---

## 📧 Contacto

**Responsable del proyecto:** [zabalaolavarria](https://github.com/zabalaolavarria)

---

**Última actualización:** Mayo 2026
