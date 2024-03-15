from core import ma


class CategorySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "slug")
