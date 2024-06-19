from django.urls import path
from .views import (EventListCreate, EventRetrieveUpdateDestroy, event_list, event_detail, event_create, event_update,
                    event_delete)


urlpatterns = [
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name='event-detail'),

    path('', event_list, name='event-list'),
    path('events/<int:pk>/', event_detail, name='event-detail'),
    path('events/create/', event_create, name='event-create'),
    path('events/<int:pk>/update/', event_update, name='event-update'),
    path('events/<int:pk>/delete/', event_delete, name='event-delete'),
]

