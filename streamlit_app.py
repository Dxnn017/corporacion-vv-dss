import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="V&V Corporación - DSS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Datos simulados para el DSS
@st.cache_data
def load_kpi_data():
    return {
        "revenue": 2850000,
        "activeProjects": 24,
        "clientSatisfaction": 94.2,
        "efficiency": 87.5,
        "monthlyGrowth": 12.3,
        "clients": 89,
        "newClients": 12
    }

@st.cache_data
def load_projects_data():
    return [
        {
            "id": "P001",
            "name": "Automatización Planta ABB",
            "client": "ABB",
            "status": "En Progreso",
            "progress": 75,
            "budget": 450000,
            "spent": 337500,
            "area": "Automatización",
            "location": "Lima Norte"
        },
        {
            "id": "P002",
            "name": "Mantenimiento Siemens Q1",
            "client": "Siemens",
            "status": "Completado",
            "progress": 100,
            "budget": 280000,
            "spent": 275000,
            "area": "Mantenimiento",
            "location": "Callao"
        },
        {
            "id": "P003",
            "name": "Instalación Eléctrica Schneider",
            "client": "Schneider Electric",
            "status": "En Progreso",
            "progress": 45,
            "budget": 320000,
            "spent": 144000,
            "area": "Electricidad",
            "location": "San Juan de Lurigancho"
        },
        {
            "id": "P004",
            "name": "Sistema Refrigeración Hyundai",
            "client": "Hyundai",
            "status": "Completado",
            "progress": 100,
            "budget": 280000,
            "spent": 275000,
            "area": "Refrigeración",
            "location": "Ate"
        }
    ]

@st.cache_data
def load_clients_data():
    return [
        {
            "name": "ABB",
            "tier": "Premium",
            "revenue": 850000,
            "projects": 8,
            "satisfaction": 96,
            "riskLevel": "Bajo"
        },
        {
            "name": "Siemens",
            "tier": "Premium",
            "revenue": 720000,
            "projects": 6,
            "satisfaction": 94,
            "riskLevel": "Bajo"
        },
        {
            "name": "Schneider Electric",
            "tier": "Gold",
            "revenue": 580000,
            "projects": 5,
            "satisfaction": 92,
            "riskLevel": "Bajo"
        },
        {
            "name": "Hyundai",
            "tier": "Gold",
            "revenue": 420000,
            "projects": 4,
            "satisfaction": 89,
            "riskLevel": "Medio"
        }
    ]

@st.cache_data
def load_service_areas_data():
    return [
        {
            "area": "Metal Mecánica",
            "revenue": 980000,
            "projects": 8,
            "efficiency": 92,
            "growth": 15.2,
            "team_size": 12
        },
        {
            "area": "Electricidad",
            "revenue": 850000,
            "projects": 7,
            "efficiency": 89,
            "growth": 18.7,
            "team_size": 10
        },
        {
            "area": "Automatización",
            "revenue": 750000,
            "projects": 6,
            "efficiency": 88,
            "growth": 22.1,
            "team_size": 8
        },
        {
            "area": "Refrigeración",
            "revenue": 620000,
            "projects": 5,
            "efficiency": 85,
            "growth": 8.3,
            "team_size": 6
        },
        {
            "area": "Mantenimiento",
            "revenue": 580000,
            "projects": 10,
            "efficiency": 91,
            "growth": 12.5,
            "team_size": 15
        },
        {
            "area": "Obras Civiles",
            "revenue": 520000,
            "projects": 4,
            "efficiency": 83,
            "growth": 5.8,
            "team_size": 18
        }
    ]

# Sidebar
st.sidebar.image("https://via.placeholder.com/200x80/003DA5/FFFFFF?text=V%26V+Corp", width=200)
st.sidebar.title("🏢 V&V Corporación Comercial S.A.C")
st.sidebar.markdown("---")

# Selector de módulos
st.sidebar.subheader("📊 Módulos de Análisis")
selected_module = st.sidebar.selectbox(
    "Seleccionar módulo:",
    ["Dashboard Principal", "Análisis de Proyectos", "Análisis de Clientes", "Áreas de Servicio", "Reportes Avanzados"]
)

# Header principal
st.markdown("""
<div style="background: linear-gradient(90deg, #003DA5 0%, #0066CC 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; text-align: center; margin: 0;">
        🏗️ V&V Corporación Comercial S.A.C
    </h1>
    <p style="color: #FFCC00; text-align: center; margin: 0.5rem 0 0 0; font-size: 1.1rem;">
        Sistema de Soporte a Decisiones - DSS Analytics
    </p>
</div>
""", unsafe_allow_html=True)

# Dashboard Principal
if selected_module == "Dashboard Principal":
    st.header("📈 Dashboard Ejecutivo")
    
    # Cargar datos
    kpis = load_kpi_data()
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💰 Ingresos Mensuales", 
            f"S/ {kpis['revenue']:,.0f}",
            f"+{kpis['monthlyGrowth']:.1f}%"
        )
    
    with col2:
        st.metric(
            "📁 Proyectos Activos", 
            kpis['activeProjects'],
            "+2 nuevos"
        )
    
    with col3:
        st.metric(
            "😊 Satisfacción Cliente", 
            f"{kpis['clientSatisfaction']:.1f}%",
            "+1.2%"
        )
    
    with col4:
        st.metric(
            "⚡ Eficiencia Operativa", 
            f"{kpis['efficiency']:.1f}%",
            "+3.5%"
        )
    
    st.markdown("---")
    
    # Gráficos de resumen
    col1, col2 = st.columns(2)
    
    with col1:
        # Ingresos por área de servicio
        areas_data = load_service_areas_data()
        df_areas = pd.DataFrame(areas_data)
        
        fig_pie = px.pie(
            df_areas, 
            values='revenue', 
            names='area',
            title="📊 Distribución de Ingresos por Área de Servicio",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Evolución mensual (datos simulados)
        monthly_data = pd.DataFrame({
            'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            'Ingresos': [2200000, 2350000, 2180000, 2450000, 2680000, 2850000],
            'Proyectos': [18, 20, 19, 22, 25, 24]
        })
        
        fig_line = px.line(
            monthly_data, 
            x='Mes', 
            y='Ingresos',
            title="📈 Evolución de Ingresos Mensuales",
            markers=True
        )
        fig_line.update_traces(line_color='#003DA5')
        st.plotly_chart(fig_line, use_container_width=True)

# Análisis de Proyectos
elif selected_module == "Análisis de Proyectos":
    st.header("🏗️ Análisis Detallado de Proyectos")
    
    projects = load_projects_data()
    df_projects = pd.DataFrame(projects)
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.selectbox("Estado:", ["Todos"] + list(df_projects['status'].unique()))
    with col2:
        area_filter = st.selectbox("Área:", ["Todas"] + list(df_projects['area'].unique()))
    with col3:
        client_filter = st.selectbox("Cliente:", ["Todos"] + list(df_projects['client'].unique()))
    
    # Aplicar filtros
    filtered_df = df_projects.copy()
    if status_filter != "Todos":
        filtered_df = filtered_df[filtered_df['status'] == status_filter]
    if area_filter != "Todas":
        filtered_df = filtered_df[filtered_df['area'] == area_filter]
    if client_filter != "Todos":
        filtered_df = filtered_df[filtered_df['client'] == client_filter]
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        # Progreso de proyectos
        fig_bar = px.bar(
            filtered_df, 
            x='name', 
            y='progress',
            color='status',
            title="📊 Progreso de Proyectos",
            color_discrete_map={
                'En Progreso': '#FFCC00',
                'Completado': '#28a745',
                'Pendiente': '#dc3545'
            }
        )
        fig_bar.update_xaxis(tickangle=45)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Utilización de presupuesto
        filtered_df['budget_utilization'] = (filtered_df['spent'] / filtered_df['budget']) * 100
        
        fig_scatter = px.scatter(
            filtered_df,
            x='budget',
            y='spent',
            size='progress',
            color='area',
            hover_name='name',
            title="💰 Presupuesto vs Gasto Real",
            labels={'budget': 'Presupuesto (S/)', 'spent': 'Gastado (S/)'}
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Tabla detallada
    st.subheader("📋 Detalles de Proyectos")
    st.dataframe(filtered_df, use_container_width=True)

# Análisis de Clientes
elif selected_module == "Análisis de Clientes":
    st.header("👥 Análisis de Clientes")
    
    clients = load_clients_data()
    df_clients = pd.DataFrame(clients)
    
    # Métricas de clientes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👥 Total Clientes", len(df_clients))
    with col2:
        premium_clients = len(df_clients[df_clients['tier'] == 'Premium'])
        st.metric("⭐ Clientes Premium", premium_clients)
    with col3:
        avg_satisfaction = df_clients['satisfaction'].mean()
        st.metric("😊 Satisfacción Promedio", f"{avg_satisfaction:.1f}%")
    with col4:
        total_revenue = df_clients['revenue'].sum()
        st.metric("💰 Ingresos Totales", f"S/ {total_revenue:,.0f}")
    
    # Gráficos de análisis
    col1, col2 = st.columns(2)
    
    with col1:
        # Ingresos por cliente
        fig_bar = px.bar(
            df_clients.sort_values('revenue', ascending=True),
            x='revenue',
            y='name',
            orientation='h',
            color='tier',
            title="💰 Ingresos por Cliente",
            color_discrete_map={
                'Premium': '#003DA5',
                'Gold': '#FFCC00',
                'Standard': '#0066CC'
            }
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Satisfacción vs Proyectos
        fig_scatter = px.scatter(
            df_clients,
            x='projects',
            y='satisfaction',
            size='revenue',
            color='tier',
            hover_name='name',
            title="📊 Satisfacción vs Número de Proyectos",
            labels={'projects': 'Número de Proyectos', 'satisfaction': 'Satisfacción (%)'}
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Tabla de clientes
    st.subheader("📋 Cartera de Clientes")
    st.dataframe(df_clients, use_container_width=True)

# Áreas de Servicio
elif selected_module == "Áreas de Servicio":
    st.header("⚙️ Rendimiento por Áreas de Servicio")
    
    areas_data = load_service_areas_data()
    df_areas = pd.DataFrame(areas_data)
    
    # Métricas por área
    col1, col2 = st.columns(2)
    
    with col1:
        # Ingresos y eficiencia
        fig_bar = go.Figure()
        
        fig_bar.add_trace(go.Bar(
            name='Ingresos (Miles S/)',
            x=df_areas['area'],
            y=df_areas['revenue'] / 1000,
            yaxis='y',
            offsetgroup=1,
            marker_color='#003DA5'
        ))
        
        fig_bar.add_trace(go.Bar(
            name='Eficiencia (%)',
            x=df_areas['area'],
            y=df_areas['efficiency'],
            yaxis='y2',
            offsetgroup=2,
            marker_color='#FFCC00'
        ))
        
        fig_bar.update_layout(
            title='💼 Ingresos vs Eficiencia por Área',
            xaxis=dict(title='Área de Servicio', tickangle=45),
            yaxis=dict(title='Ingresos (Miles S/)', side='left'),
            yaxis2=dict(title='Eficiencia (%)', side='right', overlaying='y'),
            barmode='group'
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Crecimiento por área
        fig_growth = px.bar(
            df_areas.sort_values('growth', ascending=True),
            x='growth',
            y='area',
            orientation='h',
            title="📈 Crecimiento por Área de Servicio (%)",
            color='growth',
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig_growth, use_container_width=True)
    
    # Análisis detallado
    st.subheader("📊 Análisis Multidimensional")
    
    fig_bubble = px.scatter(
        df_areas,
        x='projects',
        y='efficiency',
        size='revenue',
        color='growth',
        hover_name='area',
        title="🎯 Proyectos vs Eficiencia (Tamaño = Ingresos, Color = Crecimiento)",
        labels={
            'projects': 'Número de Proyectos',
            'efficiency': 'Eficiencia (%)',
            'growth': 'Crecimiento (%)'
        },
        color_continuous_scale='RdYlGn'
    )
    st.plotly_chart(fig_bubble, use_container_width=True)
    
    # Tabla detallada
    st.subheader("📋 Detalles por Área de Servicio")
    st.dataframe(df_areas, use_container_width=True)

# Reportes Avanzados
elif selected_module == "Reportes Avanzados":
    st.header("📊 Reportes y Análisis Avanzados")
    
    # Análisis comparativo
    st.subheader("🔍 Análisis Comparativo Integral")
    
    # Cargar todos los datos
    kpis = load_kpi_data()
    projects = load_projects_data()
    clients = load_clients_data()
    areas = load_service_areas_data()
    
    # Crear dashboard comparativo
    col1, col2 = st.columns(2)
    
    with col1:
        # Rendimiento por cliente vs área
        df_projects = pd.DataFrame(projects)
        client_area_summary = df_projects.groupby(['client', 'area']).agg({
            'budget': 'sum',
            'spent': 'sum',
            'progress': 'mean'
        }).reset_index()
        
        fig_heatmap = px.density_heatmap(
            client_area_summary,
            x='area',
            y='client',
            z='progress',
            title="🎯 Mapa de Calor: Progreso por Cliente y Área"
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with col2:
        # Análisis de rentabilidad
        df_areas = pd.DataFrame(areas)
        df_areas['roi'] = (df_areas['revenue'] / df_areas['team_size']) / 1000
        
        fig_roi = px.bar(
            df_areas.sort_values('roi', ascending=True),
            x='roi',
            y='area',
            orientation='h',
            title="💎 ROI por Área (Ingresos/Empleado en Miles)",
            color='roi',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_roi, use_container_width=True)
    
    # Resumen ejecutivo
    st.subheader("📈 Resumen Ejecutivo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"""
        **💰 Situación Financiera**
        - Ingresos: S/ {kpis['revenue']:,.0f}
        - Crecimiento: +{kpis['monthlyGrowth']:.1f}%
        - Proyectos activos: {kpis['activeProjects']}
        """)
    
    with col2:
        best_area = max(areas, key=lambda x: x['growth'])
        st.success(f"""
        **🚀 Área de Mayor Crecimiento**
        - {best_area['area']}: +{best_area['growth']:.1f}%
        - Ingresos: S/ {best_area['revenue']:,.0f}
        - Eficiencia: {best_area['efficiency']}%
        """)
    
    with col3:
        best_client = max(clients, key=lambda x: x['revenue'])
        st.warning(f"""
        **⭐ Cliente Principal**
        - {best_client['name']} ({best_client['tier']})
        - Ingresos: S/ {best_client['revenue']:,.0f}
        - Satisfacción: {best_client['satisfaction']}%
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>V&V Corporación Comercial S.A.C - Sistema Integrado de Análisis</p>
    <p>📞 972 257 767 | 📍 Calle Manuel Ubalde N° 1125 - A. PJ. El Porvenir</p>
</div>
""", unsafe_allow_html=True)
