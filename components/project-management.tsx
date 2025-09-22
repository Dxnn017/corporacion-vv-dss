import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Calendar, Clock, User, MapPin, AlertCircle, CheckCircle, Play, Pause } from "lucide-react"

// Mock data para proyectos
const projectsData = [
  {
    id: "P001",
    name: "Automatización Planta ABB",
    client: "ABB",
    status: "En Progreso",
    priority: "Alta",
    progress: 75,
    startDate: "2024-01-15",
    endDate: "2024-03-30",
    budget: 450000,
    spent: 337500,
    team: ["Carlos Mendoza", "Ana García", "Luis Torres"],
    area: "Automatización",
    location: "Lima Norte",
    description: "Implementación de sistema de automatización industrial para optimizar procesos de producción",
  },
  {
    id: "P002",
    name: "Mantenimiento Siemens Q1",
    client: "Siemens",
    status: "Planificado",
    priority: "Media",
    progress: 0,
    startDate: "2024-04-01",
    endDate: "2024-04-15",
    budget: 180000,
    spent: 0,
    team: ["Roberto Silva", "María López"],
    area: "Mantenimiento Preventivo",
    location: "Callao",
    description: "Mantenimiento preventivo trimestral de equipos industriales",
  },
  {
    id: "P003",
    name: "Instalación Eléctrica Schneider",
    client: "Schneider Electric",
    status: "En Progreso",
    priority: "Alta",
    progress: 45,
    startDate: "2024-02-01",
    endDate: "2024-05-15",
    budget: 320000,
    spent: 144000,
    team: ["Pedro Ramírez", "Carmen Vega", "José Herrera"],
    area: "Electricidad",
    location: "San Juan de Lurigancho",
    description: "Instalación completa de sistema eléctrico industrial con tableros de control",
  },
  {
    id: "P004",
    name: "Sistema Refrigeración Hyundai",
    client: "Hyundai",
    status: "Completado",
    priority: "Media",
    progress: 100,
    startDate: "2023-11-01",
    endDate: "2024-01-30",
    budget: 280000,
    spent: 275000,
    team: ["Fernando Castro", "Lucía Morales"],
    area: "Refrigeración",
    location: "Ate",
    description: "Implementación de sistema de refrigeración industrial para almacenes",
  },
  {
    id: "P005",
    name: "Obras Civiles INDECO",
    client: "INDECO",
    status: "En Progreso",
    priority: "Baja",
    progress: 30,
    startDate: "2024-01-20",
    endDate: "2024-06-30",
    budget: 520000,
    spent: 156000,
    team: ["Miguel Ángel", "Rosa Delgado", "Andrés Vásquez", "Elena Ruiz"],
    area: "Obras Civiles",
    location: "Villa El Salvador",
    description: "Construcción de infraestructura industrial y obras complementarias",
  },
]

const getStatusColor = (status: string) => {
  switch (status) {
    case "Completado":
      return "bg-green-100 text-green-800 border-green-200"
    case "En Progreso":
      return "bg-blue-100 text-blue-800 border-blue-200"
    case "Planificado":
      return "bg-yellow-100 text-yellow-800 border-yellow-200"
    case "Pausado":
      return "bg-red-100 text-red-800 border-red-200"
    default:
      return "bg-gray-100 text-gray-800 border-gray-200"
  }
}

const getPriorityColor = (priority: string) => {
  switch (priority) {
    case "Alta":
      return "bg-red-100 text-red-800 border-red-200"
    case "Media":
      return "bg-yellow-100 text-yellow-800 border-yellow-200"
    case "Baja":
      return "bg-green-100 text-green-800 border-green-200"
    default:
      return "bg-gray-100 text-gray-800 border-gray-200"
  }
}

const getStatusIcon = (status: string) => {
  switch (status) {
    case "Completado":
      return <CheckCircle className="h-4 w-4 text-green-600" />
    case "En Progreso":
      return <Play className="h-4 w-4 text-blue-600" />
    case "Planificado":
      return <Clock className="h-4 w-4 text-yellow-600" />
    case "Pausado":
      return <Pause className="h-4 w-4 text-red-600" />
    default:
      return <AlertCircle className="h-4 w-4 text-gray-600" />
  }
}

export function ProjectManagement() {
  const activeProjects = projectsData.filter((p) => p.status === "En Progreso")
  const completedProjects = projectsData.filter((p) => p.status === "Completado")
  const plannedProjects = projectsData.filter((p) => p.status === "Planificado")

  const totalBudget = projectsData.reduce((sum, project) => sum + project.budget, 0)
  const totalSpent = projectsData.reduce((sum, project) => sum + project.spent, 0)
  const budgetUtilization = ((totalSpent / totalBudget) * 100).toFixed(1)

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-foreground">Gestión de Proyectos</h1>
          <p className="text-muted-foreground">Control y seguimiento de proyectos activos</p>
        </div>
        <Button className="bg-primary text-primary-foreground">Nuevo Proyecto</Button>
      </div>

      {/* Resumen de Proyectos */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Play className="h-5 w-5 text-blue-600" />
              <div>
                <p className="text-2xl font-bold">{activeProjects.length}</p>
                <p className="text-sm text-muted-foreground">En Progreso</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <CheckCircle className="h-5 w-5 text-green-600" />
              <div>
                <p className="text-2xl font-bold">{completedProjects.length}</p>
                <p className="text-sm text-muted-foreground">Completados</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Clock className="h-5 w-5 text-yellow-600" />
              <div>
                <p className="text-2xl font-bold">{plannedProjects.length}</p>
                <p className="text-sm text-muted-foreground">Planificados</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div>
              <p className="text-2xl font-bold">{budgetUtilization}%</p>
              <p className="text-sm text-muted-foreground">Utilización Presupuesto</p>
              <Progress value={Number.parseFloat(budgetUtilization)} className="mt-2" />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Tabs de Proyectos */}
      <Tabs defaultValue="active" className="space-y-4">
        <TabsList>
          <TabsTrigger value="active">Activos ({activeProjects.length})</TabsTrigger>
          <TabsTrigger value="planned">Planificados ({plannedProjects.length})</TabsTrigger>
          <TabsTrigger value="completed">Completados ({completedProjects.length})</TabsTrigger>
          <TabsTrigger value="all">Todos ({projectsData.length})</TabsTrigger>
        </TabsList>

        <TabsContent value="active" className="space-y-4">
          <div className="grid gap-4">
            {activeProjects.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="planned" className="space-y-4">
          <div className="grid gap-4">
            {plannedProjects.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="completed" className="space-y-4">
          <div className="grid gap-4">
            {completedProjects.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        </TabsContent>

        <TabsContent value="all" className="space-y-4">
          <div className="grid gap-4">
            {projectsData.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        </TabsContent>
      </Tabs>
    </div>
  )
}

function ProjectCard({ project }: { project: (typeof projectsData)[0] }) {
  const budgetUtilization = ((project.spent / project.budget) * 100).toFixed(1)
  const daysRemaining = Math.ceil((new Date(project.endDate).getTime() - new Date().getTime()) / (1000 * 60 * 60 * 24))

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              {getStatusIcon(project.status)}
              <CardTitle className="text-lg">{project.name}</CardTitle>
            </div>
            <p className="text-sm text-muted-foreground">{project.description}</p>
          </div>
          <div className="flex gap-2">
            <Badge className={getPriorityColor(project.priority)}>{project.priority}</Badge>
            <Badge className={getStatusColor(project.status)}>{project.status}</Badge>
          </div>
        </div>
      </CardHeader>

      <CardContent className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm">
              <User className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Cliente:</span>
              <span>{project.client}</span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <MapPin className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Ubicación:</span>
              <span>{project.location}</span>
            </div>
          </div>

          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm">
              <Calendar className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Inicio:</span>
              <span>{new Date(project.startDate).toLocaleDateString("es-ES")}</span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <Calendar className="h-4 w-4 text-muted-foreground" />
              <span className="font-medium">Fin:</span>
              <span>{new Date(project.endDate).toLocaleDateString("es-ES")}</span>
            </div>
          </div>

          <div className="space-y-2">
            <div className="text-sm">
              <span className="font-medium">Presupuesto:</span>
              <span className="ml-2">S/ {project.budget.toLocaleString()}</span>
            </div>
            <div className="text-sm">
              <span className="font-medium">Gastado:</span>
              <span className="ml-2">S/ {project.spent.toLocaleString()}</span>
            </div>
          </div>
        </div>

        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>Progreso del Proyecto</span>
            <span>{project.progress}%</span>
          </div>
          <Progress value={project.progress} />
        </div>

        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>Utilización Presupuesto</span>
            <span>{budgetUtilization}%</span>
          </div>
          <Progress value={Number.parseFloat(budgetUtilization)} />
        </div>

        <div className="flex items-center justify-between pt-2 border-t">
          <div className="flex items-center gap-2">
            <span className="text-sm font-medium">Equipo:</span>
            <div className="flex gap-1">
              {project.team.slice(0, 3).map((member, index) => (
                <Badge key={index} variant="outline" className="text-xs">
                  {member.split(" ")[0]}
                </Badge>
              ))}
              {project.team.length > 3 && (
                <Badge variant="outline" className="text-xs">
                  +{project.team.length - 3}
                </Badge>
              )}
            </div>
          </div>

          {project.status !== "Completado" && (
            <div className="text-sm text-muted-foreground">
              {daysRemaining > 0 ? `${daysRemaining} días restantes` : "Vencido"}
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
