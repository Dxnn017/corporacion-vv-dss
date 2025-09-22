import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import {
  Wrench,
  Zap,
  Cpu,
  Snowflake,
  Settings,
  Battery,
  Building,
  TrendingUp,
  TrendingDown,
  DollarSign,
  Users,
  Target,
} from "lucide-react"
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
  LineChart,
  Line,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
} from "recharts"

// Mock data para áreas de servicio
const serviceAreasData = [
  {
    id: "metal-mecanica",
    name: "Metal Mecánica",
    icon: Wrench,
    revenue: 680000,
    projects: 18,
    efficiency: 92,
    satisfaction: 94,
    utilization: 87,
    growth: 15.2,
    team: 12,
    avgProjectDuration: 45,
    profitMargin: 28.5,
    color: "#003DA5",
    description: "Servicios especializados en metalurgia y mecánica industrial",
    keyMetrics: {
      completedProjects: 156,
      onTimeDelivery: 94,
      budgetCompliance: 96,
      clientRetention: 89,
    },
    topClients: ["ABB", "Siemens", "Hyundai"],
    challenges: ["Escasez de materiales especializados", "Capacitación técnica continua"],
    opportunities: ["Expansión a nuevos sectores", "Automatización de procesos"],
  },
  {
    id: "electricidad",
    name: "Electricidad",
    icon: Zap,
    revenue: 540000,
    projects: 22,
    efficiency: 89,
    satisfaction: 96,
    utilization: 91,
    growth: 12.8,
    team: 15,
    avgProjectDuration: 30,
    profitMargin: 32.1,
    color: "#FFCC00",
    description: "Instalaciones eléctricas industriales y sistemas de control",
    keyMetrics: {
      completedProjects: 198,
      onTimeDelivery: 96,
      budgetCompliance: 94,
      clientRetention: 92,
    },
    topClients: ["Schneider Electric", "ABB", "INDECO"],
    challenges: ["Normativas cambiantes", "Seguridad en instalaciones"],
    opportunities: ["Energías renovables", "Smart grids"],
  },
  {
    id: "automatizacion",
    name: "Automatización",
    icon: Cpu,
    revenue: 720000,
    projects: 14,
    efficiency: 95,
    satisfaction: 98,
    utilization: 85,
    growth: 22.5,
    team: 8,
    avgProjectDuration: 60,
    profitMargin: 35.8,
    color: "#0066CC",
    description: "Sistemas de automatización industrial y control de procesos",
    keyMetrics: {
      completedProjects: 87,
      onTimeDelivery: 98,
      budgetCompliance: 97,
      clientRetention: 95,
    },
    topClients: ["ABB", "Siemens", "Schneider Electric"],
    challenges: ["Tecnología en constante evolución", "Integración de sistemas legacy"],
    opportunities: ["IoT Industrial", "Inteligencia Artificial"],
  },
  {
    id: "refrigeracion",
    name: "Refrigeración",
    icon: Snowflake,
    revenue: 380000,
    projects: 12,
    efficiency: 88,
    satisfaction: 91,
    utilization: 82,
    growth: 8.3,
    team: 6,
    avgProjectDuration: 35,
    profitMargin: 26.4,
    color: "#87CEEB",
    description: "Sistemas de refrigeración industrial y comercial",
    keyMetrics: {
      completedProjects: 124,
      onTimeDelivery: 91,
      budgetCompliance: 93,
      clientRetention: 87,
    },
    topClients: ["Hyundai", "Miguelez", "Otros"],
    challenges: ["Refrigerantes ecológicos", "Eficiencia energética"],
    opportunities: ["Refrigeración sostenible", "Sistemas inteligentes"],
  },
  {
    id: "sistemas-energia",
    name: "Sistemas de Energía",
    icon: Battery,
    revenue: 420000,
    projects: 8,
    efficiency: 91,
    satisfaction: 93,
    utilization: 79,
    growth: 18.7,
    team: 5,
    avgProjectDuration: 50,
    profitMargin: 30.2,
    color: "#FFD700",
    description: "Sistemas de generación y distribución de energía",
    keyMetrics: {
      completedProjects: 65,
      onTimeDelivery: 93,
      budgetCompliance: 95,
      clientRetention: 91,
    },
    topClients: ["Siemens", "ABB", "Schneider Electric"],
    challenges: ["Transición energética", "Almacenamiento de energía"],
    opportunities: ["Energía solar", "Sistemas híbridos"],
  },
  {
    id: "obras-civiles",
    name: "Obras Civiles",
    icon: Building,
    revenue: 310000,
    projects: 6,
    efficiency: 85,
    satisfaction: 89,
    utilization: 88,
    growth: 5.2,
    team: 10,
    avgProjectDuration: 90,
    profitMargin: 22.8,
    color: "#4A90E2",
    description: "Construcción de infraestructura industrial",
    keyMetrics: {
      completedProjects: 45,
      onTimeDelivery: 89,
      budgetCompliance: 91,
      clientRetention: 85,
    },
    topClients: ["INDECO", "Hyundai", "Otros"],
    challenges: ["Permisos y regulaciones", "Condiciones climáticas"],
    opportunities: ["Construcción sostenible", "Prefabricación"],
  },
  {
    id: "mantenimiento",
    name: "Mantenimiento Preventivo",
    icon: Settings,
    revenue: 290000,
    projects: 24,
    efficiency: 93,
    satisfaction: 95,
    utilization: 94,
    growth: 10.1,
    team: 8,
    avgProjectDuration: 15,
    profitMargin: 38.5,
    color: "#32CD32",
    description: "Mantenimiento preventivo y correctivo de equipos industriales",
    keyMetrics: {
      completedProjects: 312,
      onTimeDelivery: 95,
      budgetCompliance: 98,
      clientRetention: 96,
    },
    topClients: ["Siemens", "ABB", "Schneider Electric"],
    challenges: ["Programación de paradas", "Repuestos especializados"],
    opportunities: ["Mantenimiento predictivo", "Digitalización"],
  },
]

const monthlyPerformanceData = [
  { month: "Ene", metalMecanica: 85, electricidad: 88, automatizacion: 92, refrigeracion: 82 },
  { month: "Feb", metalMecanica: 87, electricidad: 90, automatizacion: 94, refrigeracion: 85 },
  { month: "Mar", metalMecanica: 89, electricidad: 89, automatizacion: 93, refrigeracion: 87 },
  { month: "Apr", metalMecanica: 91, electricidad: 91, automatizacion: 95, refrigeracion: 88 },
  { month: "May", metalMecanica: 92, electricidad: 93, automatizacion: 96, refrigeracion: 89 },
  { month: "Jun", metalMecanica: 94, electricidad: 95, automatizacion: 98, refrigeracion: 91 },
]

const radarData = serviceAreasData.map((area) => ({
  area: area.name,
  efficiency: area.efficiency,
  satisfaction: area.satisfaction,
  utilization: area.utilization,
  profitability: area.profitMargin,
}))

export function ServiceAreasPerformance() {
  const totalRevenue = serviceAreasData.reduce((sum, area) => sum + area.revenue, 0)
  const totalProjects = serviceAreasData.reduce((sum, area) => sum + area.projects, 0)
  const avgEfficiency = serviceAreasData.reduce((sum, area) => sum + area.efficiency, 0) / serviceAreasData.length
  const avgSatisfaction = serviceAreasData.reduce((sum, area) => sum + area.satisfaction, 0) / serviceAreasData.length

  const topPerformingAreas = [...serviceAreasData].sort((a, b) => b.efficiency - a.efficiency).slice(0, 3)

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-foreground">Rendimiento por Áreas de Servicio</h1>
          <p className="text-muted-foreground">Análisis de performance y métricas por especialidad técnica</p>
        </div>
        <Badge variant="secondary" className="bg-secondary text-secondary-foreground">
          {serviceAreasData.length} Áreas Activas
        </Badge>
      </div>

      {/* Métricas Generales */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <DollarSign className="h-5 w-5 text-green-600" />
              <div>
                <p className="text-2xl font-bold">S/ {totalRevenue.toLocaleString()}</p>
                <p className="text-sm text-muted-foreground">Ingresos Totales</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Target className="h-5 w-5 text-blue-600" />
              <div>
                <p className="text-2xl font-bold">{totalProjects}</p>
                <p className="text-sm text-muted-foreground">Proyectos Activos</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <TrendingUp className="h-5 w-5 text-purple-600" />
              <div>
                <p className="text-2xl font-bold">{avgEfficiency.toFixed(1)}%</p>
                <p className="text-sm text-muted-foreground">Eficiencia Promedio</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Users className="h-5 w-5 text-orange-600" />
              <div>
                <p className="text-2xl font-bold">{avgSatisfaction.toFixed(1)}%</p>
                <p className="text-sm text-muted-foreground">Satisfacción Promedio</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Gráficos de Análisis */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Ingresos por Área de Servicio</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={serviceAreasData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
                <YAxis />
                <Bar dataKey="revenue" fill="hsl(var(--primary))" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Análisis Multidimensional</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <RadarChart data={radarData.slice(0, 4)}>
                <PolarGrid />
                <PolarAngleAxis dataKey="area" />
                <PolarRadiusAxis angle={90} domain={[0, 100]} />
                <Radar
                  name="Eficiencia"
                  dataKey="efficiency"
                  stroke="hsl(var(--primary))"
                  fill="hsl(var(--primary))"
                  fillOpacity={0.1}
                />
                <Radar
                  name="Satisfacción"
                  dataKey="satisfaction"
                  stroke="hsl(var(--secondary))"
                  fill="hsl(var(--secondary))"
                  fillOpacity={0.1}
                />
              </RadarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Evolución de Performance Mensual</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={monthlyPerformanceData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis domain={[75, 100]} />
              <Line type="monotone" dataKey="automatizacion" stroke="#0066CC" strokeWidth={2} name="Automatización" />
              <Line type="monotone" dataKey="electricidad" stroke="#FFCC00" strokeWidth={2} name="Electricidad" />
              <Line type="monotone" dataKey="metalMecanica" stroke="#003DA5" strokeWidth={2} name="Metal Mecánica" />
              <Line type="monotone" dataKey="refrigeracion" stroke="#87CEEB" strokeWidth={2} name="Refrigeración" />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Áreas de Servicio Detalladas */}
      <Tabs defaultValue="overview" className="space-y-4">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="overview">Resumen</TabsTrigger>
          <TabsTrigger value="performance">Performance</TabsTrigger>
          <TabsTrigger value="analysis">Análisis</TabsTrigger>
          <TabsTrigger value="opportunities">Oportunidades</TabsTrigger>
        </TabsList>

        <TabsContent value="overview" className="space-y-4">
          <div className="grid gap-4">
            {serviceAreasData.map((area) => (
              <ServiceAreaCard key={area.id} area={area} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="performance" className="space-y-4">
          <div className="grid gap-4">
            {topPerformingAreas.map((area, index) => (
              <Card key={area.id} className="border-l-4" style={{ borderLeftColor: area.color }}>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="p-2 rounded-lg" style={{ backgroundColor: `${area.color}20` }}>
                        <area.icon className="h-5 w-5" style={{ color: area.color }} />
                      </div>
                      <div>
                        <CardTitle className="text-lg">{area.name}</CardTitle>
                        <p className="text-sm text-muted-foreground">Posición #{index + 1} en eficiencia</p>
                      </div>
                    </div>
                    <Badge className="bg-green-100 text-green-800 border-green-200">Top Performer</Badge>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="text-center">
                      <p className="text-2xl font-bold">{area.efficiency}%</p>
                      <p className="text-sm text-muted-foreground">Eficiencia</p>
                    </div>
                    <div className="text-center">
                      <p className="text-2xl font-bold">{area.satisfaction}%</p>
                      <p className="text-sm text-muted-foreground">Satisfacción</p>
                    </div>
                    <div className="text-center">
                      <p className="text-2xl font-bold">{area.utilization}%</p>
                      <p className="text-sm text-muted-foreground">Utilización</p>
                    </div>
                    <div className="text-center">
                      <p className="text-2xl font-bold">{area.profitMargin.toFixed(1)}%</p>
                      <p className="text-sm text-muted-foreground">Margen</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="analysis" className="space-y-4">
          <div className="grid gap-6">
            {serviceAreasData.map((area) => (
              <Card key={area.id}>
                <CardHeader>
                  <div className="flex items-center gap-3">
                    <area.icon className="h-6 w-6 text-primary" />
                    <CardTitle>{area.name} - Análisis Detallado</CardTitle>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div>
                      <p className="text-sm font-medium">Proyectos Completados</p>
                      <p className="text-2xl font-bold">{area.keyMetrics.completedProjects}</p>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Entrega a Tiempo</p>
                      <p className="text-2xl font-bold">{area.keyMetrics.onTimeDelivery}%</p>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Cumplimiento Presupuesto</p>
                      <p className="text-2xl font-bold">{area.keyMetrics.budgetCompliance}%</p>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Retención Clientes</p>
                      <p className="text-2xl font-bold">{area.keyMetrics.clientRetention}%</p>
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <p className="text-sm font-medium mb-2">Principales Clientes</p>
                      <div className="flex gap-2 flex-wrap">
                        {area.topClients.map((client, index) => (
                          <Badge key={index} variant="outline">
                            {client}
                          </Badge>
                        ))}
                      </div>
                    </div>
                    <div>
                      <p className="text-sm font-medium mb-2">Desafíos Principales</p>
                      <ul className="text-sm text-muted-foreground space-y-1">
                        {area.challenges.map((challenge, index) => (
                          <li key={index}>• {challenge}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="opportunities" className="space-y-4">
          <div className="grid gap-4">
            {serviceAreasData.map((area) => (
              <Card key={area.id} className="hover:shadow-md transition-shadow">
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <area.icon className="h-5 w-5 text-primary" />
                      <CardTitle className="text-lg">{area.name}</CardTitle>
                    </div>
                    <div className="flex items-center gap-2">
                      {area.growth > 15 ? (
                        <TrendingUp className="h-4 w-4 text-green-500" />
                      ) : (
                        <TrendingDown className="h-4 w-4 text-yellow-500" />
                      )}
                      <span className="text-sm font-medium">+{area.growth}% crecimiento</span>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <p className="text-sm text-muted-foreground">{area.description}</p>
                    <div>
                      <p className="text-sm font-medium mb-2">Oportunidades de Crecimiento</p>
                      <ul className="text-sm space-y-1">
                        {area.opportunities.map((opportunity, index) => (
                          <li key={index} className="flex items-center gap-2">
                            <div className="w-2 h-2 bg-primary rounded-full"></div>
                            {opportunity}
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>
      </Tabs>
    </div>
  )
}

function ServiceAreaCard({ area }: { area: (typeof serviceAreasData)[0] }) {
  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="flex items-center gap-3">
            <div className="p-3 rounded-lg" style={{ backgroundColor: `${area.color}20` }}>
              <area.icon className="h-6 w-6" style={{ color: area.color }} />
            </div>
            <div>
              <CardTitle className="text-lg">{area.name}</CardTitle>
              <p className="text-sm text-muted-foreground">{area.description}</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            {area.growth > 15 ? (
              <TrendingUp className="h-4 w-4 text-green-500" />
            ) : (
              <TrendingDown className="h-4 w-4 text-yellow-500" />
            )}
            <span className="text-sm font-medium">+{area.growth}%</span>
          </div>
        </div>
      </CardHeader>

      <CardContent className="space-y-4">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="text-center">
            <p className="text-2xl font-bold">S/ {area.revenue.toLocaleString()}</p>
            <p className="text-sm text-muted-foreground">Ingresos</p>
          </div>
          <div className="text-center">
            <p className="text-2xl font-bold">{area.projects}</p>
            <p className="text-sm text-muted-foreground">Proyectos</p>
          </div>
          <div className="text-center">
            <p className="text-2xl font-bold">{area.team}</p>
            <p className="text-sm text-muted-foreground">Equipo</p>
          </div>
          <div className="text-center">
            <p className="text-2xl font-bold">{area.avgProjectDuration}d</p>
            <p className="text-sm text-muted-foreground">Duración Prom.</p>
          </div>
        </div>

        <div className="space-y-3">
          <div className="space-y-2">
            <div className="flex justify-between text-sm">
              <span>Eficiencia</span>
              <span>{area.efficiency}%</span>
            </div>
            <Progress value={area.efficiency} />
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-sm">
              <span>Satisfacción Cliente</span>
              <span>{area.satisfaction}%</span>
            </div>
            <Progress value={area.satisfaction} />
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-sm">
              <span>Utilización Recursos</span>
              <span>{area.utilization}%</span>
            </div>
            <Progress value={area.utilization} />
          </div>
        </div>

        <div className="flex items-center justify-between pt-2 border-t">
          <div className="text-sm">
            <span className="font-medium">Margen:</span>
            <span className="ml-1">{area.profitMargin.toFixed(1)}%</span>
          </div>
          <Badge variant="outline" style={{ borderColor: area.color, color: area.color }}>
            {area.topClients[0]}
          </Badge>
        </div>
      </CardContent>
    </Card>
  )
}
