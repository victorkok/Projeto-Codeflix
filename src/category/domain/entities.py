from datetime import datetime
from dataclasses import dataclass , field
from typing import Optional
import uuid


#entidade - conjunto de atributos + entidades + objetos de valores | identificação + operaçoes

# lapis - propriedades - color - Objeto de valor

#mede,quantificar ou descrever no dominio
#ele precisa modelar um todo conceitual com informações relacionadas,se uma unica unidade

# ter que ser imutavel -> objeto de valor

@dataclass(kw_only=True, frozen=True) #init,repr, eq dataclass
class Category:

    id: uuid.UUID = field(
        default_factory=lambda: uuid.uuid4()
    )
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    )
