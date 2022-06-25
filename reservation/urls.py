from django.urls import path
from .views import (
    display_reservation_form,
    load_durations,
    DurationListView,
    reservation_done,
)

urlpatterns = [
    path('', display_reservation_form, name='reservations'),
    path('', DurationListView.as_view(), name='duration_changelist'),
    path('<int:machineID>', display_reservation_form),
    path('done', reservation_done, name='reservation_done'),

    path('ajax/load-durations/', load_durations, name='ajax_load_durations'),

]
