from core.schema import CategorySchema

from fkcommerce.core.models import Category

from . import inventory_category_api_blueprint

category_schema = CategorySchema(many=True)


@inventory_category_api_blueprint.route("/category", methods=["GET"])
def category():
    all_category = Category.query.all()
    return category_schema.dump(all_category)
