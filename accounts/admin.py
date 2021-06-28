from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "title", 'city', 'country')
	search_fields = ("title", "content", 'city', 'country')
	class Meta:
		model = UserProfile

	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('user')
		return queryset


#Register Post Admin
admin.site.register(UserProfile, UserProfileAdmin)
