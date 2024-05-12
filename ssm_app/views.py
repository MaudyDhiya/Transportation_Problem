from django.shortcuts import render
from .ksam import *

# Create your views here.
def home_beranda(request):
    return render(request, "layouts.html")
def home_ssm(request):
    return render(request, "ssm.html")
def home_ksam(request):
    return render(request, "ksam.html")
# handling submit ssm
def home_submitssm(request):
    list_row=[]
    if request.method=="POST":
        title=request.POST.get('title') #memanggil input title
        
        nos=request.POST.get('nos') #memanggil input nos

        nod=request.POST.get('nod') #memanggil input nod

        rownames=request.POST.get('rownames')
        columnames=request.POST.get('columnames') 
        #ini logika untuk rownames
        if rownames=='2':
            rownames=''
        elif rownames=='1':
            rownames='Source'
        elif rownames=='4':
            rownames=request.POST.get('input_lainnya')
        
        #ini logika untuk columnames
        if columnames=='2':
            columnames=''
        elif columnames=='1':
            columnames='Destination'
        elif columnames=='4':
            columnames=request.POST.get('input_lainnya2')

        context = {
            'title':title,
            'nos':nos,
            'nod':nod,
            'rownames':rownames,
            'columnames':columnames,
    
        }
    else:
        context = {
            'title':'',
        }    
    return render(request, "submitssm.html", context)
# handling submit ksam
def home_submitksam(request):
    if request.method=="POST":
        title=request.POST.get('title') #memanggil input title
        
        nos=request.POST.get('nos') #memanggil input nos

        nod=request.POST.get('nod') #memanggil input nod

        rownames=request.POST.get('rownames')
        columnames=request.POST.get('columnames') 
        #ini logika untuk rownames
        if rownames=='2':
            rownames=''
        elif rownames=='1':
            rownames='Source'
        elif rownames=='4':
            rownames=request.POST.get('input_lainnya')

        #ini logika untuk columnames
        if columnames=='2':
            columnames=''
        elif columnames=='1':
            columnames='Destination'
        elif columnames=='4':
            columnames=request.POST.get('input_lainnya2')
        

        context = {
            'title':title,
            'nos':nos,
            'nod':nod,
            'rownames':rownames,
            'columnames':columnames,
        }
    else:
        context = {
            'title':'',
        }    
    return render(request, "submitksam.html", context)

def home_resultksam(request):
    if request.method=="POST":
        rownames=request.POST.get('rownames') #memanggil input nama baris
        columnames=request.POST.get('columnames') #memanggil input nama kolom
        title=request.POST.get('title') #memanggil input title
        cost=request.POST.get('cost') #memanggil input cost
        supply=request.POST.get('supply') #memanggil input supply
        demand=request.POST.get('demand') #memanggil input demand

        print (cost)
        print (supply)
        print (demand)

        # Evaluasi string menggunakan eval() dan konversi ke np.array
        matrix_cost = np.array(eval(cost))

        # Evaluasi string menggunakan eval() dan konversi ke np.array
        array_supply = np.array(eval(supply))

        # Reshape array ke bentuk [[3,3,3]]
        matrix_supply = array_supply.reshape(1, -1)

        # Evaluasi string menggunakan eval() dan konversi ke np.array
        matrix_demand = np.array(eval(demand))

        # cost = np.array([[73,  40, 9, 79, 20],
        #         [62, 93, 96, 8, 13],
        #         [96, 65, 80, 50, 65],
        #         [57, 58, 29, 12, 87],
        #         [56, 23, 87, 18, 12],])
        # supply = np.array([8, 7, 9, 3, 5])
        # demand = np.array([6, 8, 10, 4, 4])
        
        trans = Transportation(matrix_cost, matrix_supply, matrix_demand)
        trans.setup_table(minimize=True)
        KS = KaragulSahinApproximation(trans)
        allocation, wcd, wcs, min_cost = KS.solve(show_iter=True)
        df = trans.print_table(allocation)
        
        # Konversi DataFrame menjadi HTML
        html_table = df.to_html(classes='table table-striped text-center', index=True)

        context = {
            'title':title,
            'df': df,
            'html_table': html_table,
            'rownames':rownames,
            'columnames':columnames,
            'wcd':wcd,
            'wcs':wcs,
            'min_cost':min_cost,
        }
    else:
        context = {
            'title':'',
        }     
    return render(request, "resultksam.html", context)

#TO DO: 
#Membuat logika metode SSM
#Membuat logika metode KSAM

# link ksam https://github.com/deyanarajib/transportation-problem/blob/main/karagul_sahin_approximation.py