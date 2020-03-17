from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . models import Daily
from  .seializers import DailySerializer
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django_pandas.io import read_frame


# Create your views here.


def daily_visualize(request):
    qs = Daily.objects.all()
    df = read_frame(qs)

    # import pdb;pdb.set_trace()

    plot_div = plot([Scatter(x=df.date, y=df.binn,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div', show_link=False)
    return render(request, "index.html", context={'plot_div': plot_div})




def plotly_visualize(request):
    data = Daily.objects.all()
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div', show_link=False)
    return render(request, "index.html", context={'plot_div': plot_div})






    