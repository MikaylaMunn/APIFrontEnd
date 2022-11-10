from django.urls import path
from squaring.views import SquareView, HelloWorldView

urlpatterns = [
    # These names come from views.py and match the class names
    # Good practice to give names but not needed currently
    # putting brackets here, it's stating its a variable whatever they put in, number has to match the SquareView in views
    path('<int:number>', SquareView.as_view(), name='number'),
    # Runs the first path it sees that matches
    path('home', HelloWorldView.as_view(), name="home"),
]