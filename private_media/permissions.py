
class DefaultPrivatePermissions(object):

    def has_read_permission(self, request, path):
        """Return True if the user is a staff member or superuser."""
        user = request.user

        return user.is_authenticated() \
            and (user.is_superuser or user.is_staff)
