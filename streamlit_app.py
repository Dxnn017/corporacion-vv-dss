import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="V&V Corporación - Analytics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuración de URLs
def get_base_url():
    """Detecta automáticamente la URL base del dashboard"""
    # Intenta obtener la URL desde variables de entorno
    if 'DASHBOARD_URL' in os.environ:
        return os.environ['DASHBOARD_URL']
    
    # URLs de prueba (cambiar por tu URL real cuando despliegues)
    production_urls = [
        "https://corporacion-vv-dss.vercel.app",  # Cambiar por tu URL de Vercel
        "https://vv-dss-dashboard.vercel.app",    # URL alternativa
    ]
    
    # En desarrollo local
    local_urls = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]
    
    # Probar URLs en orden de prioridad
    for url in production_urls + local_urls:
        try:
            response = requests.get(f"{url}/api/data?type=kpis", timeout=5)
            if response.status_code == 200:
                return url
        except:
            continue
    
    return None

BASE_URL = get_base_url()
API_URL = f"{BASE_URL}/api/data" if BASE_URL else None

def show_connection_status():
    """Muestra el estado de conexión con el dashboard"""
    if BASE_URL:
        st.success(f"✅ Conectado al dashboard: {BASE_URL}")
        return True
    else:
        st.error("❌ No se pudo conectar al dashboard. Verifica que esté desplegado.")
        st.info("💡 Asegúrate de que tu dashboard Next.js esté desplegado en Vercel y actualiza la URL en el código.")
        return False

# Funciones para conectar con el dashboard
@st.cache_data(ttl=300)  # Cache por 5 minutos
def fetch_dashboard_data(data_type):
    """Obtiene datos del dashboard Next.js"""
    if not API_URL:
        return None
        
    try:
        response = requests.get(f"{API_URL}?type={data_type}", timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error obteniendo datos: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error de conexión: {str(e)}")
        return None

def get_fallback_data(data_type):
    """Datos de respaldo cuando no hay conexión con el API"""
    fallback_data = {
        "kpis": {
            "revenue": 2850000,
            "activeProjects": 24,
            "clientSatisfaction": 94.2,
            "efficiency": 87.5,
            "monthlyGrowth": 12.3,
            "timestamp": datetime.now().isoformat(),
        },
        "projects": [
            {
                "id": "P001",
                "name": "Modernización Sistema Eléctrico ABB",
                "client": "ABB",
                "status": "En Progreso",
                "progress": 75,
                "budget": 450000,
                "spent": 337500,
                "area": "Electricidad",
            }
        ],
        "clients": [
            {
                "id": "C001",
                "name": "ABB",
                "tier": "Premium",
                "revenue": 850000,
                "projects": 8,
                "satisfaction": 96,
                "riskLevel": "Bajo",
            }
        ],
        "service-areas": [
            {
                "area": "Electricidad",
                "revenue": 980000,
                "projects": 8,
                "efficiency": 92,
                "growth": 15.2,
            }
        ]
    }
    return fallback_data.get(data_type, {})


# Dashboard Principal
if selected_module == "Dashboard Principal":
    st.header("📈 Dashboard Ejecutivo")
    
    is_connected = show_connection_status()
    
    # Obtener KPIs del dashboard
    kpis = fetch_dashboard_data("kpis")
    if not kpis and not is_connected:
        st.warning("⚠️ Usando datos de demostración (sin conexión al dashboard)")
        kpis = get_fallback_data("kpis")
    
    if kpis:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Ingresos Totales", 
                f"S/ {kpis['revenue']:,.0f}",
                f"{kpis['monthlyGrowth']:.1f}%"
            )
        
        with col2:
            st.metric(
                "Proyectos Activos", 
                kpis['activeProjects'],
                "2 nuevos"
            )
        
        with col3:
            st.metric(
                "Satisfacción Cliente", 
                f"{kpis['clientSatisfaction']:.1f}%",
                "1.2%"
            )
        
        with col4:
            st.metric(
                "Eficiencia Operativa", 
                f"{kpis['efficiency']:.1f}%",
                "3.5%"
            )

# Análisis de Proyectos
elif selected_module == "Análisis de Proyectos":
    st.header("🏗️ Análisis Detallado de Proyectos")
    
    show_connection_status()
    
    projects = fetch_dashboard_data("projects")
    if not projects:
        projects = get_fallback_data("projects")
    
    if projects:
        df_projects = pd.DataFrame(projects)
        
        # Gráfico de progreso de proyectos
        fig = px.bar(
            df_projects, 
            x='name', 
            y='progress',
            color='status',
            title="Progreso de Proyectos Activos",
            color_discrete_map={
                'En Progreso': '#3b82f6',
                'Completado': '#10b981',
                'Pendiente': '#f59e0b'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabla detallada
        st.subheader("Detalles de Proyectos")
        st.dataframe(df_projects, use_container_width=True)

# Análisis de Clientes
elif selected_module == "Análisis de Clientes":
    st.header("👥 Análisis de Clientes")
    
    show_connection_status()
    
    clients = fetch_dashboard_data("clients")
    if not clients:
        clients = get_fallback_data("clients")
    
    if clients:
        df_clients = pd.DataFrame(clients)
        
        # Gráfico de ingresos por cliente
        fig = px.pie(
            df_clients, 
            values='revenue', 
            names='name',
            title="Distribución de Ingresos por Cliente"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Análisis de satisfacción
        fig2 = px.scatter(
            df_clients,
            x='projects',
            y='satisfaction',
            size='revenue',
            color='tier',
            hover_name='name',
            title="Satisfacción vs Número de Proyectos"
        )
        st.plotly_chart(fig2, use_container_width=True)

# Áreas de Servicio
elif selected_module == "Áreas de Servicio":
    st.header("⚙️ Rendimiento por Áreas de Servicio")
    
    show_connection_status()
    
    service_areas = fetch_dashboard_data("service-areas")
    if not service_areas:
        service_areas = get_fallback_data("service-areas")
    
    if service_areas:
        df_areas = pd.DataFrame(service_areas)
        
        # Gráfico comparativo
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Ingresos (Miles S/)',
            x=df_areas['area'],
            y=df_areas['revenue'] / 1000,
            yaxis='y',
            offsetgroup=1
        ))
        
        fig.add_trace(go.Bar(
            name='Eficiencia (%)',
            x=df_areas['area'],
            y=df_areas['efficiency'],
            yaxis='y2',
            offsetgroup=2
        ))
        
        fig.update_layout(
            title='Rendimiento por Área de Servicio',
            xaxis=dict(title='Área de Servicio'),
            yaxis=dict(title='Ingresos (Miles S/)', side='left'),
            yaxis2=dict(title='Eficiencia (%)', side='right', overlaying='y'),
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Configuración
elif selected_module == "Configuración":
    st.header("⚙️ Configuración de Integración")
    
    st.subheader("Estado de Conexión")
    show_connection_status()
    
    if BASE_URL:
        st.info(f"Dashboard URL: {BASE_URL}")
    
    st.subheader("Instrucciones de Configuración")
    st.markdown("""
    ### Para conectar con tu dashboard desplegado:
    
    1. **Despliega tu dashboard Next.js** en Vercel
    2. **Copia la URL** de tu deployment (ej: `https://tu-app.vercel.app`)
    3. **Actualiza la URL** en el código de Streamlit:
       ```python
       production_urls = [
           "https://corporacion-vv-dss.streamlit.app",  # Tu URL aquí
       ]
