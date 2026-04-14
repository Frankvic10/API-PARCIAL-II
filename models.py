from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Tabla de asociación muchos-a-muchos entre Usuario y Rol
usuario_rol = Table('usuario_rol', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id')),
    Column('rol_id', Integer, ForeignKey('roles.id'))
)

# Tabla de asociación muchos-a-muchos entre Rol y Permiso
rol_permiso = Table('rol_permiso', Base.metadata,
    Column('rol_id', Integer, ForeignKey('roles.id')),
    Column('permiso_id', Integer, ForeignKey('permisos.id'))
)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    roles = relationship("Rol", secondary=usuario_rol, back_populates="usuarios")

class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    
    usuarios = relationship("Usuario", secondary=usuario_rol, back_populates="roles")
    permisos = relationship("Permiso", secondary=rol_permiso, back_populates="roles")

class Permiso(Base):
    __tablename__ = "permisos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    
    roles = relationship("Rol", secondary=rol_permiso, back_populates="permisos")

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    año = Column(Integer)
