import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Badge } from "@/components/ui/badge"
import { TrendingUp, DollarSign, Users, FolderOpen, Wrench, Calendar, AlertTriangle } from "lucide-react"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer, PieChart, Pie, Cell } from "recharts"

// Mock data para el dashboard
const kpiData = {
  revenue: { current: 2450000, previous: 2180000, target: 2800000 },
  projects: { active: 24, completed: 156, pending: 8 },
  clients: { total: 89, active: 67, new: 12 },
  satisfaction: 94.2,
  efficiency: 87.5,
}

const serviceAreasData = [
  { name: "Metal Mecánica", value: 28, color: "#003DA5" },
  { name: "Electricidad", value: 22, color: "#FFCC00" },
  { name: "Automatización", value: 18, color: "#0066CC" },
  { name: "Refrigeración", value: 15, color: "#FFD700" },
  { name: "Obras Civiles", value: 10, color: "#4A90E2" },
  { name: "Otros", value: 7, color: "#87CEEB" },
]

const monthlyRevenueData = [
  { month: "Ene", revenue: 180000, projects: 18 },
  { month: "Feb", revenue: 220000, projects: 22 },
  { month: "Mar", revenue: 195000, projects: 19 },
  { month: "Apr", revenue: 240000, projects: 25 },
  { month: "May", revenue: 280000, projects: 28 },
  { month: "Jun", revenue: 245000, projects: 24 },
]

const topClientsData = [
  { name: "ABB", projects: 8, revenue: 450000 },
  { name: "Siemens", projects: 6, revenue: 380000 },
  { name: "Schneider Electric", projects: 5, revenue: 320000 },
  { name: "Hyundai", projects: 4, revenue: 280000 },
]

export function KPIOverview() {
  const revenueGrowth = (
    ((kpiData.revenue.current - kpiData.revenue.previous) / kpiData.revenue.previous) *
    100
  ).toFixed(1)
  const targetProgress = ((kpiData.revenue.current / kpiData.revenue.target) * 100).toFixed(1)

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-foreground">Dashboard Ejecutivo</h1>
          <p className="text-muted-foreground">Sistema de Soporte a Decisiones - V&V Corporación Comercial S.A.C</p>
        </div>
        <Badge variant="secondary" className="bg-secondary text-secondary-foreground">
          Actualizado: {new Date().toLocaleDateString("es-ES")}
        </Badge>
      </div>

      {/* KPIs Principales */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Ingresos Mensuales</CardTitle>
            <DollarSign className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">S/ {kpiData.revenue.current.toLocaleString()}</div>
            <div className="flex items-center gap-1 text-xs">
              <TrendingUp className="h-3 w-3 text-green-500" />
              <span className="text-green-500">+{revenueGrowth}%</span>
              <span className="text-muted-foreground">vs mes anterior</span>
            </div>
            <Progress value={Number.parseFloat(targetProgress)} className="mt-2" />
            <p className="text-xs text-muted-foreground mt-1">{targetProgress}% de la meta mensual</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Proyectos Activos</CardTitle>
            <FolderOpen className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{kpiData.projects.active}</div>
            <div className="text-xs text-muted-foreground">
              {kpiData.projects.completed} completados | {kpiData.projects.pending} pendientes
            </div>
            <div className="flex gap-2 mt-2">
              <Badge variant="outline" className="text-xs">
                Completados: {kpiData.projects.completed}
              </Badge>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Clientes</CardTitle>
            <Users className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{kpiData.clients.total}</div>
            <div className="text-xs text-muted-foreground">
              {kpiData.clients.active} activos | {kpiData.clients.new} nuevos este mes
            </div>
            <div className="flex gap-2 mt-2">
              <Badge variant="secondary" className="text-xs">
                +{kpiData.clients.new} nuevos
              </Badge>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Satisfacción Cliente</CardTitle>
            <TrendingUp className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{kpiData.satisfaction}%</div>
            <div className="text-xs text-muted-foreground">Eficiencia operativa: {kpiData.efficiency}%</div>
            <Progress value={kpiData.satisfaction} className="mt-2" />
          </CardContent>
        </Card>
      </div>

      {/* Gráficos y Análisis */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Ingresos por Mes */}
        <Card>
          <CardHeader>
            <CardTitle>Evolución de Ingresos</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={monthlyRevenueData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="month" />
                <YAxis />
                <Bar dataKey="revenue" fill="hsl(var(--primary))" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Distribución por Áreas de Servicio */}
        <Card>
          <CardHeader>
            <CardTitle>Distribución por Áreas de Servicio</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={serviceAreasData}
                  cx="50%"
                  cy="50%"
                  outerRadius={100}
                  dataKey="value"
                  label={({ name, value }) => `${name}: ${value}%`}
                >
                  {serviceAreasData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
              </PieChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>

      {/* Principales Clientes y Alertas */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Principales Clientes</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {topClientsData.map((client, index) => (
                <div key={client.name} className="flex items-center justify-between p-3 border rounded-lg">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-primary/10 rounded-full flex items-center justify-center text-primary font-semibold text-sm">
                      {index + 1}
                    </div>
                    <div>
                      <p className="font-medium">{client.name}</p>
                      <p className="text-sm text-muted-foreground">{client.projects} proyectos</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="font-semibold">S/ {client.revenue.toLocaleString()}</p>
                    <p className="text-sm text-muted-foreground">ingresos</p>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <AlertTriangle className="h-5 w-5 text-yellow-500" />
              Alertas y Notificaciones
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              <div className="flex items-start gap-3 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                <Calendar className="h-4 w-4 text-yellow-600 mt-0.5" />
                <div>
                  <p className="text-sm font-medium">Proyecto ABB - Fase 2</p>
                  <p className="text-xs text-muted-foreground">Vence en 3 días</p>
                </div>
              </div>

              <div className="flex items-start gap-3 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                <Wrench className="h-4 w-4 text-blue-600 mt-0.5" />
                <div>
                  <p className="text-sm font-medium">Mantenimiento Preventivo</p>
                  <p className="text-xs text-muted-foreground">Siemens - Programado para mañana</p>
                </div>
              </div>

              <div className="flex items-start gap-3 p-3 bg-green-50 border border-green-200 rounded-lg">
                <Users className="h-4 w-4 text-green-600 mt-0.5" />
                <div>
                  <p className="text-sm font-medium">Nuevo Cliente</p>
                  <p className="text-xs text-muted-foreground">Schneider Electric - Reunión programada</p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
