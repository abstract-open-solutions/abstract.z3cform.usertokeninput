import zope.component
import zope.interface
import zope.schema

from z3c.form import interfaces
from z3c.form import widget

from collective.z3cform.widgets.token_input_widget import TokenInputWidget
from .interfaces import IUserTokenInputWidget


class UserTokenInputWidget(TokenInputWidget):
    zope.interface.implementsOnly(IUserTokenInputWidget)

    # js_template = """\
    # (function($) {
    #     $().ready(function() {
    #         $('#%(id)s').data('klass','%(klass)s');
    #         keywordTokenInputActivate('%(id)s', newValues, oldValues);
    #     });
    # })(jQuery);
    # """

    # def js(self):
    #     # $("#my-text-input").tokenInput("/url/to/your/script/");
    #     values = self.context.portal_catalog.uniqueValuesFor('Subject')
    #     old_values = self.context.Subject()
    #     tags = ""
    #     old_tags = ""
    #     index = 0
    #     for index, value in enumerate(values):
    #         tags += "{id: '%s', name: '%s'}" % (value.replace("'", "\\'"), value.replace("'", "\\'"))
    #         if index < len(values) - 1:
    #             tags += ", "
    #     old_index = 0
    #     #prepopulate
    #     for index, value in enumerate(old_values):
    #         old_tags += u"{id: '%s', name: '%s'}" % (value.replace("'", "\\'"), value.replace("'", "\\'"))
    #         if index < len(old_values) - 1:
    #             old_tags += ", "
    #     result = self.js_template % dict(id=self.id,
    #         klass=self.klass,
    #         newtags=unicode(tags, errors='ignore'),
    #         oldtags=old_tags)
    #     return result

    # def render(self):
    #     if self.mode == interfaces.DISPLAY_MODE:
    #         return self.display_template(self)
    #     else:
    #         return self.input_template(self)


@zope.interface.implementer(interfaces.IFieldWidget)
def UserTokenInputFieldWidget(field, request):
    """IFieldWidget factory for UserTokenInputWidget."""
    return widget.FieldWidget(field, UserTokenInputWidget(request))
