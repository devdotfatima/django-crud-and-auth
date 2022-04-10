from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('noteslist/',views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>',views.NoteDetailView.as_view(), name='notes.detail'),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/new',views.NotesCreateView.as_view(),name='notes.new'),
    ]