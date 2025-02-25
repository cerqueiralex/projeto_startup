from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, DECIMAL, ForeignKey

DATABASE_URL = "postgresql+asyncpg://postgres:minha_senha_secreta@postgres:5432/meu_ecommerce_db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Modelo Pedido
class Pedido(Base):
    __tablename__ = "pedido"
    id_pedido = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, nullable=False)
    valor_total = Column(DECIMAL(10,2), nullable=False)

# Criar tabelas no banco
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Inicializar FastAPI
app = FastAPI()

# Dependência para obter sessão do banco
async def get_db():
    async with SessionLocal() as session:
        yield session

# Modelo para recebimento de pedidos
class PedidoCreate(BaseModel):
    id_cliente: int
    valor_total: float

# Endpoint para criar pedidos
@app.post("/pedidos/")
async def criar_pedido(pedido: PedidoCreate, db: AsyncSession = Depends(get_db)):
    novo_pedido = Pedido(**pedido.dict())
    db.add(novo_pedido)
    await db.commit()
    await db.refresh(novo_pedido)
    return novo_pedido
