from models import PopupMixin
import datetime

class PopupMixin(object):
    popup_name = None
    view_once = False

    def get_context_data(self, *args, **kwargs):
        context = super(PopupMixin, self).get_context_data(*args, **kwargs)
        if self.popup_name and self.request.user.is_authenticated():
            # retrieve a record of the popup
            popup, created = PopupRecord.objects.get_or_create(
                    popup_name=self.popup_name,
                    user=self.request.user,
                    )
            # Initialize status to show and override if needed
            status = "show"
            if not created:
                if self.view_once or popup.closed_at:
                    status = "hide"
            context.update(
                    { self.popup_name : status }
                    )
        return context
