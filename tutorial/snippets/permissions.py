from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of the object to edit it
	"""

	def has_object_permission(self, request, view, obj):
		#READ permissions are allowed to any requests
		#GET, HEAD and OPTIONS  requests will always be allowed
		if request.method in permissions.SAFE_METHODS:
			return True

		#Write permissions are only allowed to the owner of the snippet
		return request.user == obj.owner