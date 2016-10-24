from django.contrib.auth.admin import UserAdmin


def roles(self):
    # short_name = unicode # function to get group name
    short_name = lambda x: x.name  # first letter of a group
    p = sorted([u"<a title='%s'>%s</a>" % (x, short_name(x))
                for x in self.groups.all()])
    if self.user_permissions.count():
        p += ['+']
    value = ', '.join(p)
    return value
roles.allow_tags = True
roles.short_description = u'Groups'

UserAdmin.list_display += (roles,)
