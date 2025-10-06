from django.urls import path

from .views import all_tasks_view, edit_task, delete_task, view_task, edit_task_feature, edit_feature_full, new_task, more

app_name = 'app'

urlpatterns = [
    path('', all_tasks_view, name='all'),
    path('<int:id>/edit/', edit_task, name='edit'),
    path('<int:id>/edit/edit_feature/<int:num>/', edit_task_feature, name='edit_feature'),
    path('<int:id>/edit/edit_feature/<int:num>/full_edit/', edit_feature_full, name = 'full'),
    path('<int:id>/delete/', delete_task, name='delete'),
    path('create/', new_task, name='new'),
    path('<int:id>/more/', more, name='more')
]