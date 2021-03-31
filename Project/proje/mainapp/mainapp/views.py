from django.shortcuts import render,HttpResponse
import matplotlib.pyplot as plt
from io import StringIO
import os

def index(request):
    return render(request, 'index.html')

def readd():
    
    dizim = []

    mydir = 'C:/Users/jsquadjy/Desktop/karataca2/proje/mainapp/logs'

    myfile = 'project_logs.log'
    training_images_labels_path = os.path.join(mydir, myfile)

    # Okuma
    f = open(training_images_labels_path, "r")
    yazi = f.readlines()

    for i in yazi:
        old_value = i.strip('\n')
        new_value = old_value.split(',')
        dizim.append(new_value)

    for i in range(len(dizim)):
        a = float(dizim[i][1])
        a = "{:.2f}".format(a)
        b = float(dizim[i][2])
        b = "{:.2f}".format(b)
        dizim[i][1] = float(a)
        dizim[i][2] = float(b)

    get = []
    clock_get = []
    c_get = 0
    post = []
    clock_post = []
    c_post = 0
    put = []
    clock_put = []
    c_put = 0
    delete = []
    clock_delete = []
    c_delete = 0

    for i in range(len(dizim)):
        if(dizim[i][0] == 'GET'):
            get.append(dizim[i][1])
            clock_get.append(dizim[i][3])
            c_get = c_get + 1
        elif(dizim[i][0] == 'POST'):
            post.append(dizim[i][1])
            clock_post.append(dizim[i][3])
            c_post = c_post + 1
        elif(dizim[i][0] == 'PUT'):
            put.append(dizim[i][1])
            clock_put.append(dizim[i][3])
            c_put = c_put + 1
        else:
            delete.append(dizim[i][1])
            clock_delete.append(dizim[i][3])
            c_delete = c_delete + 1

    return (get, clock_get, post, clock_post, put, clock_put, delete, clock_delete)

def return_graph():

    (get, clock_get, post, clock_post, put,
     clock_put, delete, clock_delete) = readd()

    


    fig = plt.figure()
    plt.plot(clock_get, get, label="line 1")

    plt.plot(clock_post, post, label="line 2")

    plt.plot(clock_put, put, label="line 3")

    plt.plot(clock_delete, delete, label="line 4")
    
    plt.xlabel('x - axis')
    
    plt.ylabel('y - axis')
    
    plt.title('Two lines on same graph!')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def goster(request):

    
    
    context = {"graph": return_graph()}
    return render(request, 'dashboard.html',context)


