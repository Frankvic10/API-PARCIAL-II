from fastapi import FastAPI
import models
from database import engine, SessionLocal

# Importando los Enrutadores (Routers)
from routers import usuarios, roles_permisos, vehiculos

# Crear todas las tablas en la base de datos de SQLite
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Vehículos y Roles",
    description="API para administrar usuarios, roles, permisos y vehículos con FastAPI.",
    version="1.0.0"
)

# Conectar rutas
app.include_router(usuarios.router)
app.include_router(roles_permisos.router_roles)
app.include_router(roles_permisos.router_permisos)
app.include_router(vehiculos.router)

# Añadir datos iniciales de prueba (Seed Data)
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    
    # Comprobar si ya existen permisos, de no ser así los añadimos a modo de semilla (seed).
    primer_permiso = db.query(models.Permiso).first()
    if primer_permiso is None:
        print("Inyectando datos de semilla a SQLite...")
        
        # 1. Crear los permisos solicitados
        p_leer = models.Permiso(nombre="PUNTUACIONES/LEER")
        p_crear = models.Permiso(nombre="PUNTUACIONES/CREAR")
        p_actualizar = models.Permiso(nombre="PUNTUACIONES/ACTUALIZAR")
        p_eliminar = models.Permiso(nombre="PUNTUACIONES/ELIMINAR")
        db.add_all([p_leer, p_crear, p_actualizar, p_eliminar])
        
        # 2. Crear los roles solicitados
        r_1 = models.Rol(nombre="Rol_1: Solo lectura", permisos=[p_leer])
        r_2 = models.Rol(nombre="Rol_2: Solo escritura", permisos=[p_leer, p_crear])
        r_3 = models.Rol(nombre="Rol_3: Actualizar y eliminar", permisos=[p_leer, p_actualizar, p_eliminar])
        db.add_all([r_1, r_2, r_3])
        
        # 3. Crear unos usuarios de prueba con sus roles
        u_1 = models.Usuario(nombre="Lector Perez", email="lector@test.com", roles=[r_1])
        u_2 = models.Usuario(nombre="Editor Gomez", email="editor@test.com", roles=[r_2])
        u_3 = models.Usuario(nombre="Admin Martinez", email="admin@test.com", roles=[r_3])
        db.add_all([u_1, u_2, u_3])
        
        # 4. Crear algunos vehículos de prueba
        v1 = models.Vehiculo(marca="Toyota", modelo="Corolla", año=2020)
        v2 = models.Vehiculo(marca="Honda", modelo="Civic", año=2021)
        db.add_all([v1, v2])

        db.commit()
        print("Datos iniciales insertados de manera exitosa.")
    else:
        print("La base de datos ya contenía información. Saltando paso de inyección.")
    
    db.close()

@app.get("/")
def read_root():
    return {
        "mensaje": "¡Hola! La API está funcionando correctamente.",
        "pista": "Ve a http://localhost:8000/docs para probar todos los endpoints interactivos."
    }
