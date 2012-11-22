import json
import zope.component
import zope.interface
import zope.schema

from z3c.form import interfaces
from z3c.form import widget
from Products.CMFCore.utils import getToolByName

from collective.z3cform.widgets.token_input_widget import TokenInputWidget
from .interfaces import IUserTokenInputWidget


class UserTokenInputWidget(TokenInputWidget):
    zope.interface.implementsOnly(IUserTokenInputWidget)

    js_template = """\
    (function($) {
        $().ready(function() {
            $("#%(id)s").tokenInput(
              "%(path)s",
              {theme: "facebook",
               preventDuplicates: true,
               prePopulate: %(values)s,
               tokenDelimiter: "\\n"
              }
            );
        });
    })(jQuery);
    """

    def widget_values(self):
        pm = getToolByName(self.context, 'portal_membership')
        values = getattr(self.context, self.field.getName(), [])
        results = []
        if not values:
            # try to get them from widget setup
            # you can set this on updateWidgets call
            values = getattr(self, 'value', [])
        if not values:
            # try to get them from request
            values = self.request.get(self.field.getName(), [])
        for user_id in values:
            usr = pm.getMemberById(user_id)
            if not usr:
                continue
            results.append({
                    'id': user_id,
                    'name': usr.getProperty('fullname') or user_id
            })

        return json.dumps(results)

    def js(self):
        pt = self.context.restrictedTraverse('plone_portal_state')
        view_url = "%s/users_search" % pt.portal_url()

        return self.js_template % dict(
            id=self.id,
            path=view_url,
            values=self.widget_values()
        )


@zope.interface.implementer(interfaces.IFieldWidget)
def UserTokenInputFieldWidget(field, request):
    """IFieldWidget factory for UserTokenInputWidget."""
    return widget.FieldWidget(field, UserTokenInputWidget(request))
