from dataclasses import dataclass,field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Category:
      
    user_id: UUID 
    name: str
    category_id: UUID = field(default_factory=uuid4)
  
