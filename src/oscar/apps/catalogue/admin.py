from django.contrib import admin
from oscar.core.loading import get_model
from treebeard.admin import TreeAdmin

AttributeOptionGroup = get_model('catalogue', 'AttributeOptionGroup')
Category = get_model('catalogue', 'Category')
Option = get_model('catalogue', 'Option')
Product = get_model('catalogue', 'Product')
Attribute = get_model('catalogue', 'Attribute')
AttributeValue = get_model('catalogue', 'AttributeValue')
ProductVariantAttributeValue = get_model('catalogue', 'ProductVariantAttributeValue')
ProductCategory = get_model('catalogue', 'ProductCategory')
ProductClass = get_model('catalogue', 'ProductClass')
ProductImage = get_model('catalogue', 'ProductImage')
ProductRecommendation = get_model('catalogue', 'ProductRecommendation')


class ProductRecommendationInline(admin.TabularInline):
    model = ProductRecommendation
    fk_name = 'primary'


class CategoryInline(admin.TabularInline):
    model = ProductCategory
    extra = 1


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 2


class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'requires_shipping', 'track_stock')


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_filter = ['is_discountable']
    inlines = [CategoryInline, ProductRecommendationInline]
    prepopulated_fields = {"slug": ("title",)}

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return (
            qs
            .select_related('parent')
            .prefetch_related(
                'variants'))


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'upc', 'get_product_class', 'structure',
                    'attribute_summary', 'date_created')
    list_filter = ['structure', 'is_discountable']
    search_fields = ['upc', 'title']
    inlines = [AttributeInline]

    def get_queryset(self, request):
        qs = super(ProductVariantAdmin, self).get_queryset(request)
        return (
            qs
            .select_related('parent')
            .prefetch_related(
                'attribute_values',
                'attribute_values__attribute'))


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type')
    prepopulated_fields = {"code": ("name", )}


class OptionAdmin(admin.ModelAdmin):
    pass


class ProductVariantAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product_variant', 'attribute', 'attribute_value')


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue


class AttributeOptionGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'option_summary')
    inlines = [AttributeValueInline, ]


class CategoryAdmin(TreeAdmin):
    pass


admin.site.register(ProductClass, ProductClassAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute, AttributeAdmin)
# admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(ProductVariantAttributeValue, ProductVariantAttributeValueAdmin)
admin.site.register(AttributeOptionGroup, AttributeOptionGroupAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(ProductImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductCategory)
