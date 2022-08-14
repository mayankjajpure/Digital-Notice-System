from django.contrib import admin
from home.models import Category,Posts,notice,Feedback

# # comfiguring category admin
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('title','description',)
#     search_fields=('title',)

# class PostAdmin(admin.ModelAdmin):
#     list_display=('title',)
#     search_fields=('title',)
#     list_filter=('cat',)

admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(notice)
admin.site.register(Feedback)



# admin.site.register(CategoryAdmin,PostAdmin)
