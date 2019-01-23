from pony.orm import Database, Required, Set, PrimaryKey
from typing import Any, Dict


db = Database()
Entity: Any = db.Entity


class ModelMixin:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def as_dict(self: Entity, related_objects=True) -> Dict:
        d = self.to_dict()

        if related_objects:
            for attr in self._attrs_:
                if attr.is_collection:
                    value = getattr(self, attr.name)
                    d[attr.name] = []

                    for item in value:
                        d[attr.name].append(ModelMixin.as_dict(item, related_objects=False))

                elif attr.is_relation:
                    d[attr.name] = ModelMixin.as_dict(attr)

        return d


class Product(Entity, ModelMixin):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    titles = Set('Title')


class Title(Entity, ModelMixin):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    product = Required(Product)
