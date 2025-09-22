import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json


# Configuración de la página
st.set_page_config(
    page_title="V&V Corporación - Analytics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# URL base de tu dashboard Next.js (cambiar por tu URL de producción)
BASE_URL = "https://tu-dashboard-url.vercel.app"  # Cambiar por tu URL real
API_URL = f"{BASE_URL}/api/data"

# Funciones para conectar con el dashboard
@st.cache_data(ttl=300)  # Cache por 5 minutos
def fetch_dashboard_data(data_type):
    """Obtiene datos del dashboard Next.js"""
    try:
        response = requests.get(f"{API_URL}?type={data_type}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error obteniendo datos: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error de conexión: {str(e)}")
        return None

def send_data_to_dashboard(data_type, payload):
    """Envía datos al dashboard Next.js"""
    try:
        response = requests.post(API_URL, json={
            "type": data_type,
            "payload": payload
        })
        return response.status_code == 200
    except Exception as e:
        st.error(f"Error enviando datos: {str(e)}")
        return False

# Header con branding de V&V
st.markdown("""
<div style="background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%); padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; margin: 0; text-align: center;">
        🏗️ V&V Corporación Comercial S.A.C
    </h1>
    <p style="color: #fbbf24; margin: 0; text-align: center; font-size: 1.1rem;">
        Sistema de Análisis Avanzado - Streamlit Integration
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar para navegación
st.sidebar.title("📊 Módulos de Análisis")
selected_module = st.sidebar.selectbox(
    "Seleccionar módulo:",
    ["Dashboard Principal", "Análisis de Proyectos", "Análisis de Clientes", "Áreas de Servicio", "Configuración"]
)

# Dashboard Principal
if selected_module == "Dashboard Principal":
    st.header("📈 Dashboard Ejecutivo")
    
    # Obtener KPIs del dashboard
    kpis = fetch_dashboard_data("kpis")
    
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
    
    projects = fetch_dashboard_data("projects")
    
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
    
    clients = fetch_dashboard_data("clients")
    
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
    
    service_areas = fetch_dashboard_data("service-areas")
    
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
    
    st.subheader("Conexión con Dashboard")
    
    # Test de conexión
    if st.button("Probar Conexión"):
        test_data = fetch_dashboard_data("kpis")
        if test_data:
            st.success("✅ Conexión exitosa con el dashboard")
            st.json(test_data)
        else:
            st.error("❌ Error de conexión")
    
    st.subheader("Enviar Datos de Prueba")
    
    # Formulario para enviar datos
    with st.form("send_data_form"):
        data_type = st.selectbox("Tipo de datos:", ["analytics", "feedback", "alerts"])
        data_content = st.text_area("Contenido (JSON):", '{"test": "data"}')
        
        if st.form_submit_button("Enviar Datos"):
            try:
                payload = json.loads(data_content)
                if send_data_to_dashboard(data_type, payload):
                    st.success("✅ Datos enviados correctamente")
                else:
                    st.error("❌ Error enviando datos")
            except json.JSONDecodeError:
                st.error("❌ Formato JSON inválido")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 1rem;">
    <p>V&V Corporación Comercial S.A.C - Sistema Integrado de Análisis</p>
    <p>📞 972 257 767 | 📍 Calle Manuel Ubalde N° 1125 - A. PJ. El Porvenir</p>
</div>
""", unsafe_allow_html=True)
