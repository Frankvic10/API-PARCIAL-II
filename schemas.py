from pydantic import BaseModel
from typing import List, Optional

# --- Permisos ---
class PermisoBase(BaseModel):
    nombre: str

class Permiso(PermisoBase):
    id: int
    class Config:
        from_attributes = True

# --- Roles ---
class RolBase(BaseModel):
    nombre: str

class Rol(RolBase):
    id: int
    class Config:
        from_attributes = True

class RolConPermisos(Rol):
    permisos: List[Permiso] = []

# --- Usuarios ---
class UsuarioBase(BaseModel):
    nombre: str
    email: str

class Usuario(UsuarioBase):
    id: int
    class Config:
        from_attributes = True

class UsuarioConRoles(Usuario):
    roles: List[Rol] = []

# --- Vehículos ---
class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    año: int

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    año: Optional[int] = None

class Vehiculo(VehiculoBase):
    id: int
    class Config:
        from_attributes = True
