from django.urls import path
from .views import (
    event_list_create_view,
    event_detail_view,
    upcoming_events_view,
    events_by_category_view
)

urlpatterns = [
    path('events/', event_list_create_view, name='event-list-create'),
    path('events/<int:pk>/', event_detail_view, name='event-detail'),
    path('events/upcoming/', upcoming_events_view, name='upcoming-events'),
    path('events/category/<str:categoryName>/', events_by_category_view, name='events-by-category'),
]
