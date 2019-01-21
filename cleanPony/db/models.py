from pony.orm import Database, Required, Set, PrimaryKey


db = Database()
Entity = db.Entity


class ModelMixin(object):
    def __init__(self, *args, **kwargs):
        pass

    def as_dict(self, related_objects=True):
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
