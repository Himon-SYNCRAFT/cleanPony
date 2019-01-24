def generate():
    from cleanPony.core import entities
    from cleanPony.generator import ActionGenerator

    for cls in entities.Entity.__subclasses__():
        generator = ActionGenerator(cls, force_rewrite=True)
        generator.generate_all()

if __name__ == '__main__':
    generate()
