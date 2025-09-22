import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Building2, TrendingUp, DollarSign, Star, Phone, Mail, MapPin, Users, BarChart3 } from "lucide-react"
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
  LineChart,
  Line,
  PieChart,
  Pie,
  Cell,
} from "recharts"

// Mock data para clientes
const clientsData = [
  {
    id: "C001",
    name: "ABB",
    industry: "Automatización Industrial",
    status: "Activo",
    tier: "Premium",
    totalRevenue: 1250000,
    projectsCount: 12,
    satisfaction: 96,
    lastProject: "2024-01-15",
    nextProject: "2024-04-01",
    contact: {
      email: "contacto@abb.com",
      phone: "+51 1 234-5678",
      address: "Av. Industrial 123, Lima",
    },
    services: ["Automatización", "Mantenimiento", "Electricidad"],
    riskLevel: "Bajo",
    paymentHistory: "Excelente",
    contractValue: 450000,
    renewalDate: "2024-12-31",
  },
  {
    id: "C002",
    name: "Siemens",
    industry: "Tecnología Industrial",
    status: "Activo",
    tier: "Premium",
    totalRevenue: 980000,
    projectsCount: 8,
    satisfaction: 94,
    lastProject: "2024-02-01",
    nextProject: "2024-04-15",
    contact: {
      email: "peru@siemens.com",
      phone: "+51 1 345-6789",
      address: "Av. Tecnológica 456, San Isidro",
    },
    services: ["Automatización", "Sistemas de Energía"],
    riskLevel: "Bajo",
    paymentHistory: "Excelente",
    contractValue: 380000,
    renewalDate: "2024-11-30",
  },
  {
    id: "C003",
    name: "Schneider Electric",
    industry: "Gestión de Energía",
    status: "Activo",
    tier: "Gold",
    totalRevenue: 750000,
    projectsCount: 6,
    satisfaction: 92,
    lastProject: "2024-01-20",
    nextProject: "2024-05-01",
    contact: {
      email: "info@schneider.pe",
      phone: "+51 1 456-7890",
      address: "Av. Energía 789, Miraflores",
    },
    services: ["Electricidad", "Automatización"],
    riskLevel: "Bajo",
    paymentHistory: "Bueno",
    contractValue: 320000,
    renewalDate: "2025-01-15",
  },
  {
    id: "C004",
    name: "Hyundai Heavy Industries",
    industry: "Industria Pesada",
    status: "Activo",
    tier: "Gold",
    totalRevenue: 620000,
    projectsCount: 5,
    satisfaction: 89,
    lastProject: "2023-11-01",
    nextProject: "2024-06-01",
    contact: {
      email: "contact@hyundai.pe",
      phone: "+51 1 567-8901",
      address: "Av. Industrial 321, Ate",
    },
    services: ["Refrigeración", "Metal Mecánica"],
    riskLevel: "Medio",
    paymentHistory: "Bueno",
    contractValue: 280000,
    renewalDate: "2024-10-30",
  },
  {
    id: "C005",
    name: "INDECO",
    industry: "Construcción",
    status: "Activo",
    tier: "Standard",
    totalRevenue: 450000,
    projectsCount: 4,
    satisfaction: 87,
    lastProject: "2024-01-20",
    nextProject: "2024-07-01",
    contact: {
      email: "proyectos@indeco.pe",
      phone: "+51 1 678-9012",
      address: "Av. Construcción 654, Villa El Salvador",
    },
    services: ["Obras Civiles", "Electricidad"],
    riskLevel: "Medio",
    paymentHistory: "Regular",
    contractValue: 520000,
    renewalDate: "2024-08-15",
  },
  {
    id: "C006",
    name: "Miguelez",
    industry: "Servicios Industriales",
    status: "Prospecto",
    tier: "Standard",
    totalRevenue: 0,
    projectsCount: 0,
    satisfaction: 0,
    lastProject: null,
    nextProject: "2024-05-15",
    contact: {
      email: "ventas@miguelez.pe",
      phone: "+51 1 789-0123",
      address: "Av. Servicios 987, San Juan de Lurigancho",
    },
    services: ["Mantenimiento"],
    riskLevel: "Alto",
    paymentHistory: "N/A",
    contractValue: 0,
    renewalDate: null,
  },
]

const revenueByClientData = clientsData
  .filter((client) => client.totalRevenue > 0)
  .map((client) => ({
    name: client.name,
    revenue: client.totalRevenue,
    projects: client.projectsCount,
  }))
  .sort((a, b) => b.revenue - a.revenue)

const clientTierData = [
  { name: "Premium", value: clientsData.filter((c) => c.tier === "Premium").length, color: "#003DA5" },
  { name: "Gold", value: clientsData.filter((c) => c.tier === "Gold").length, color: "#FFCC00" },
  { name: "Standard", value: clientsData.filter((c) => c.tier === "Standard").length, color: "#0066CC" },
]

const satisfactionTrendData = [
  { month: "Ene", satisfaction: 91 },
  { month: "Feb", satisfaction: 93 },
  { month: "Mar", satisfaction: 92 },
  { month: "Apr", satisfaction: 94 },
  { month: "May", satisfaction: 93 },
  { month: "Jun", satisfaction: 95 },
]

const getTierColor = (tier: string) => {
  switch (tier) {
    case "Premium":
      return "bg-purple-100 text-purple-800 border-purple-200"
    case "Gold":
      return "bg-yellow-100 text-yellow-800 border-yellow-200"
    case "Standard":
      return "bg-blue-100 text-blue-800 border-blue-200"
    default:
      return "bg-gray-100 text-gray-800 border-gray-200"
  }
}

const getStatusColor = (status: string) => {
  switch (status) {
    case "Activo":
      return "bg-green-100 text-green-800 border-green-200"
    case "Prospecto":
      return "bg-yellow-100 text-yellow-800 border-yellow-200"
    case "Inactivo":
      return "bg-red-100 text-red-800 border-red-200"
    default:
      return "bg-gray-100 text-gray-800 border-gray-200"
  }
}

const getRiskColor = (risk: string) => {
  switch (risk) {
    case "Bajo":
      return "bg-green-100 text-green-800 border-green-200"
    case "Medio":
      return "bg-yellow-100 text-yellow-800 border-yellow-200"
    case "Alto":
      return "bg-red-100 text-red-800 border-red-200"
    default:
      return "bg-gray-100 text-gray-800 border-gray-200"
  }
}

export function ClientAnalysis() {
  const activeClients = clientsData.filter((c) => c.status === "Activo")
  const prospects = clientsData.filter((c) => c.status === "Prospecto")
  const totalRevenue = clientsData.reduce((sum, client) => sum + client.totalRevenue, 0)
  const avgSatisfaction =
    clientsData.filter((c) => c.satisfaction > 0).reduce((sum, client) => sum + client.satisfaction, 0) /
    clientsData.filter((c) => c.satisfaction > 0).length

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-foreground">Análisis de Clientes</h1>
          <p className="text-muted-foreground">Gestión y análisis de la cartera de clientes</p>
        </div>
        <Button className="bg-primary text-primary-foreground">Nuevo Cliente</Button>
      </div>

      {/* Métricas Principales */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Users className="h-5 w-5 text-blue-600" />
              <div>
                <p className="text-2xl font-bold">{activeClients.length}</p>
                <p className="text-sm text-muted-foreground">Clientes Activos</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Building2 className="h-5 w-5 text-yellow-600" />
              <div>
                <p className="text-2xl font-bold">{prospects.length}</p>
                <p className="text-sm text-muted-foreground">Prospectos</p>
              </div>
            </div>
          </CardContent>
        </Card>

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
              <Star className="h-5 w-5 text-purple-600" />
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
            <CardTitle>Ingresos por Cliente</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={revenueByClientData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Bar dataKey="revenue" fill="hsl(var(--primary))" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Distribución por Tier</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={clientTierData}
                  cx="50%"
                  cy="50%"
                  outerRadius={100}
                  dataKey="value"
                  label={({ name, value }) => `${name}: ${value}`}
                >
                  {clientTierData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
              </PieChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Evolución de Satisfacción</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={satisfactionTrendData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis domain={[80, 100]} />
              <Line type="monotone" dataKey="satisfaction" stroke="hsl(var(--primary))" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Lista de Clientes */}
      <Tabs defaultValue="active" className="space-y-4">
        <TabsList>
          <TabsTrigger value="active">Activos ({activeClients.length})</TabsTrigger>
          <TabsTrigger value="prospects">Prospectos ({prospects.length})</TabsTrigger>
          <TabsTrigger value="all">Todos ({clientsData.length})</TabsTrigger>
        </TabsList>

        <TabsContent value="active" className="space-y-4">
          <div className="grid gap-4">
            {activeClients.map((client) => (
              <ClientCard key={client.id} client={client} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="prospects" className="space-y-4">
          <div className="grid gap-4">
            {prospects.map((client) => (
              <ClientCard key={client.id} client={client} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="all" className="space-y-4">
          <div className="grid gap-4">
            {clientsData.map((client) => (
              <ClientCard key={client.id} client={client} />
            ))}
          </div>
        </TabsContent>
      </Tabs>
    </div>
  )
}

function ClientCard({ client }: { client: (typeof clientsData)[0] }) {
  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <Building2 className="h-5 w-5 text-primary" />
              <CardTitle className="text-lg">{client.name}</CardTitle>
            </div>
            <p className="text-sm text-muted-foreground">{client.industry}</p>
          </div>
          <div className="flex gap-2">
            <Badge className={getTierColor(client.tier)}>{client.tier}</Badge>
            <Badge className={getStatusColor(client.status)}>{client.status}</Badge>
          </div>
        </div>
      </CardHeader>

      <CardContent className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm">
              <DollarSign className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Ingresos:</span>
              <span>S/ {client.totalRevenue.toLocaleString()}</span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <BarChart3 className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Proyectos:</span>
              <span>{client.projectsCount}</span>
            </div>
          </div>

          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm">
              <Star className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Satisfacción:</span>
              <span>{client.satisfaction > 0 ? `${client.satisfaction}%` : "N/A"}</span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <TrendingUp className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Riesgo:</span>
              <Badge className={getRiskColor(client.riskLevel)} variant="outline">
                {client.riskLevel}
              </Badge>
            </div>
          </div>

          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm">
              <Phone className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Teléfono:</span>
              <span className="text-xs">{client.contact.phone}</span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <Mail className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Email:</span>
              <span className="text-xs">{client.contact.email}</span>
            </div>
          </div>
        </div>

        <div className="space-y-2">
          <div className="flex items-center gap-2 text-sm">
            <MapPin className="h-4 w-4 text-muted-foreground" />
            <span className="font-medium">Dirección:</span>
            <span className="text-sm">{client.contact.address}</span>
          </div>
        </div>

        <div className="space-y-2">
          <span className="text-sm font-medium">Servicios:</span>
          <div className="flex gap-2 flex-wrap">
            {client.services.map((service, index) => (
              <Badge key={index} variant="outline" className="text-xs">
                {service}
              </Badge>
            ))}
          </div>
        </div>

        {client.status === "Activo" && client.satisfaction > 0 && (
          <div className="space-y-2">
            <div className="flex justify-between text-sm">
              <span>Nivel de Satisfacción</span>
              <span>{client.satisfaction}%</span>
            </div>
            <Progress value={client.satisfaction} />
          </div>
        )}

        <div className="flex items-center justify-between pt-2 border-t">
          <div className="text-sm text-muted-foreground">
            {client.lastProject ? (
              <>Último proyecto: {new Date(client.lastProject).toLocaleDateString("es-ES")}</>
            ) : (
              "Sin proyectos previos"
            )}
          </div>
          {client.nextProject && (
            <div className="text-sm text-muted-foreground">
              Próximo: {new Date(client.nextProject).toLocaleDateString("es-ES")}
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
