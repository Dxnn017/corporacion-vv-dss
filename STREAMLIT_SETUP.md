# Configuración de Integración Streamlit

## Pasos para conectar tu Dashboard DSS con Streamlit

### 1. Configurar el archivo Streamlit

El archivo `streamlit_app.py` ya está configurado para conectarse con tu dashboard Next.js.

**Importante**: Cambia la variable `BASE_URL` en el archivo por tu URL real de producción:

\`\`\`python
BASE_URL = "https://tu-dashboard-url.vercel.app"  # Cambiar por tu URL real
\`\`\`

### 2. Instalar dependencias

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Ejecutar localmente

\`\`\`bash
streamlit run streamlit_app.py
\`\`\`

### 4. Desplegar en Streamlit Cloud

1. Sube tu repositorio a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Configura el archivo principal como `streamlit_app.py`
5. Despliega

### 5. Configurar variables de entorno (opcional)

Si necesitas configuraciones adicionales, crea un archivo `.streamlit/secrets.toml`:

\`\`\`toml
[connections]
dashboard_url = "https://tu-dashboard-url.vercel.app"
api_key = "tu-api-key-si-es-necesaria"
\`\`\`

### 6. Funcionalidades disponibles

- **Conexión bidireccional**: El Streamlit puede leer y enviar datos al dashboard
- **Cache inteligente**: Los datos se cachean por 5 minutos para mejor rendimiento
- **Visualizaciones avanzadas**: Gráficos interactivos con Plotly
- **Módulos especializados**: Análisis de proyectos, clientes y áreas de servicio

### 7. Endpoints API disponibles

- `GET /api/data?type=kpis` - Obtener KPIs
- `GET /api/data?type=projects` - Obtener proyectos
- `GET /api/data?type=clients` - Obtener clientes
- `GET /api/data?type=service-areas` - Obtener áreas de servicio
- `POST /api/data` - Enviar datos al dashboard

### 8. Personalización

Puedes personalizar los colores y branding editando las secciones de CSS en el archivo Streamlit para que coincidan exactamente con tu identidad corporativa.
