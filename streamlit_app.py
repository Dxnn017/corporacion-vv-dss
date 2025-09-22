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
        st.markdown("""
        <div style="background: linear-gradient(135deg, #28a745, #20c997); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">💰 Ingresos Mensuales</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">S/ 2,850,000</h2>
            <p style="margin: 0; color: #d4edda;">+12.3% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #007bff, #0056b3); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">📁 Proyectos Activos</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">24</h2>
            <p style="margin: 0; color: #cce7ff;">+2 nuevos ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffc107, #e0a800); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">😊 Satisfacción Cliente</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">94.2%</h2>
            <p style="margin: 0; color: #fff3cd;">+1.2% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #dc3545, #c82333); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">⚡ Eficiencia Operativa</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">87.5%</h2>
            <p style="margin: 0; color: #f8d7da;">+3.5% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
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
            color_discrete_sequence=['#003DA5', '#0066CC', '#FFCC00', '#FF6B35', '#28a745', '#6f42c1'],
            hole=0.4  # Donut chart
        )
        fig_pie.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Ingresos: S/ %{value:,.0f}<br>Porcentaje: %{percent}<extra></extra>'
        )
        fig_pie.update_layout(
            showlegend=True,
            legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.01),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Evolución mensual (datos simulados)
        monthly_data = pd.DataFrame({
            'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            'Ingresos': [2200000, 2350000, 2180000, 2450000, 2680000, 2850000],
            'Proyectos': [18, 20, 19, 22, 25, 24]
        })
        
        fig_line = go.Figure()
        
        # Add area chart for revenue
        fig_line.add_trace(go.Scatter(
            x=monthly_data['Mes'],
            y=monthly_data['Ingresos'],
            mode='lines+markers',
            name='Ingresos',
            line=dict(color='#003DA5', width=3),
            marker=dict(size=8, color='#FFCC00', line=dict(width=2, color='#003DA5')),
            fill='tonexty',
            fillcolor='rgba(0, 61, 165, 0.1)',
            hovertemplate='<b>%{x}</b><br>Ingresos: S/ %{y:,.0f}<extra></extra>'
        ))
        
        fig_line.update_layout(
            title="📈 Evolución de Ingresos Mensuales",
            xaxis_title="Mes",
            yaxis_title="Ingresos (S/)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified',
            showlegend=False
        )
        
        # Add grid
        fig_line.update_xaxis(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
        fig_line.update_yaxis(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
        
        st.plotly_chart(fig_line, use_container_width=True)
    
    # Métricas Adicionales
    st.markdown("### 📊 Métricas Adicionales")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Project completion rate
        projects = load_projects_data()
        completed = len([p for p in projects if p['status'] == 'Completado'])
        completion_rate = (completed / len(projects)) * 100
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = completion_rate,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Tasa de Completación"},
            delta = {'reference': 80},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#003DA5"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col2:
        # Client distribution by tier
        clients = load_clients_data()
        df_clients = pd.DataFrame(clients)
        tier_counts = df_clients['tier'].value_counts()
        
        fig_donut = px.pie(
            values=tier_counts.values,
            names=tier_counts.index,
            title="Distribución de Clientes por Tier",
            color_discrete_map={
                'Premium': '#003DA5',
                'Gold': '#FFCC00',
                'Standard': '#0066CC'
            },
            hole=0.6
        )
        fig_donut.update_layout(height=300)
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col3:
        # Team efficiency by area
        df_areas['efficiency_score'] = df_areas['efficiency']
        
        fig_bar_eff = px.bar(
            df_areas.sort_values('efficiency', ascending=True),
            x='efficiency',
            y='area',
            orientation='h',
            title="Eficiencia por Área",
            color='efficiency',
            color_continuous_scale='RdYlGn',
            text='efficiency'
        )
        fig_bar_eff.update_traces(texttemplate='%{text}%', textposition='inside')
        fig_bar_eff.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_bar_eff, use_container_width=True)

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
            title="📊 Progreso de Proyectos (%)",
            color_discrete_map={
                'En Progreso': '#FFCC00',
                'Completado': '#28a745',
                'Pendiente': '#dc3545'
            },
            text='progress'
        )
        fig_bar.update_traces(texttemplate='%{text}%', textposition='outside')
        fig_bar.update_layout(
            xaxis_tickangle=-45,
            yaxis_title="Progreso (%)",
            xaxis_title="Proyecto",
            showlegend=True,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        fig_bar.update_yaxis(range=[0, 110])
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
            labels={'budget': 'Presupuesto (S/)', 'spent': 'Gastado (S/)'},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        # Add diagonal line for perfect budget utilization
        max_budget = filtered_df['budget'].max()
        fig_scatter.add_shape(
            type="line",
            x0=0, y0=0, x1=max_budget, y1=max_budget,
            line=dict(color="red", width=2, dash="dash"),
        )
        fig_scatter.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
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
