from django.shortcuts import render
from .ksam import *
from .ssm import *
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

def home_resultssm(request):
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
        matrix_supply = array_supply

        # Evaluasi string menggunakan eval() dan konversi ke np.array
        matrix_demand = np.array(eval(demand)).ravel()

        cost_matrix = matrix_cost

        # Supply dan demand
        supply = matrix_supply
        demand = matrix_demand
        print(type(demand))

        # Membuat matriks zero copy dengan ukuran yang sama seperti cost_matrix
        allocation = np.zeros_like(cost_matrix)

        # Mencari indeks biaya terkecil pertama di setiap kolom
        least_cost_indices = np.argmin(cost_matrix, axis=0)

        for j in range(cost_matrix.shape[1]):
            i = least_cost_indices[j]
            allocation[i, j] = demand[j]


        total_allocation_per_row = np.sum(allocation, axis=1)

        same_sup = (total_allocation_per_row==supply)
        total_all_col = np.sum(allocation,axis=0)
        excess = (total_allocation_per_row > supply)
        print("Iter: 1")
        print(allocation)

        iter = 1

        while np.any(excess):
            next_min_indices = []
            next_values = []
            for j in range(cost_matrix.shape[1]):
                sorted_indices = np.argsort(cost_matrix[:, j])
                for i in sorted_indices:
                    if i != least_cost_indices[j]:
                        if i in np.where(excess)[0]:
                            continue
                        else:
                            if total_allocation_per_row[i] == supply[i]:
                                next_values.append(float('inf'))
                                next_min_indices.append(None)
                                continue
                            else:
                                next_min_indices.append(i)
                                next_values.append(cost_matrix[i,j])
                                # print(cost_matrix[i,j])
                                    # print(cost_matrix[i,j])
                        break
                    
            sdiff=[]
            for j in range(cost_matrix.shape[1]):
                if next_min_indices[j] != None:
                    if j in np.where(same_sup)[0]:
                        # print("Berada di supply yang sama")
                        sdiff.append(float('inf'))
                    else:
                        if cost_matrix[least_cost_indices[j], j] and cost_matrix[next_min_indices[j], j] in np.where(same_sup)[0]:
                            sdiff.append(float('inf'))
                        else:
                            diff = abs(cost_matrix[least_cost_indices[j], j] - cost_matrix[next_min_indices[j], j])
                            sdiff.append(diff)
                else:
                    sdiff.append(float('inf'))  # Handling None as infinitely large differenc
            # sdiff = [abs(cost_matrix[least_cost_indices[j], j] - cost_matrix[next_min_indices[j], j]) for j in range(cost_matrix.shape[1] and cost_matrix[next_min_indices[j],j] != None)]
            min_sdiff = min(sdiff)
            # print(sdiff)
            # print("diff",min_sdiff)
            count_min_sdiff = sdiff.count(min_sdiff)
            
            
            if count_min_sdiff > 1:
                #print("1")
                min_sdiff_indices = [j for j, x in enumerate(sdiff) if x == min_sdiff]
                max_demand_col = max(min_sdiff_indices, key=lambda col: demand[col])
                chosen_index = least_cost_indices[max_demand_col]
                sec_chosen_index = next_min_indices[max_demand_col]
                # max_demand_col = max
            else:
                #print("1.2")
                # sec_chosen_index 
                # chosen_index = 0
                sec_chosen_index_2=0
                for j in range(cost_matrix.shape[1]):
                    # print(cost_matrix[j,j]s)
                    
                    if next_min_indices[j] != None:
                        if cost_matrix[least_cost_indices[j], j] and cost_matrix[next_min_indices[j], j] in np.where(same_sup)[0]:
                            continue
                        else:
                            diff2 = abs(cost_matrix[least_cost_indices[j], j] - cost_matrix[next_min_indices[j], j])
                        # print(cost_matrix[least_cost_indices[j],j])
                            # print(diff2==min_sdiff)
                            # print("diff2",diff2)
                            
                            if diff2 == min_sdiff:
                                # print(abs(cost_matrix[least_cost_indices[j], j]))
                                # print(abs(cost_matrix[next_min_indices[j], j]))
                                # Get the row indices for the least cost value
                                chosen_index = np.where(cost_matrix[:, j] == cost_matrix[least_cost_indices[j], j])[0].tolist()

                                # Get the row indices for the next min cost value
                                sec_chosen_index = np.where(cost_matrix[:, j] == cost_matrix[next_min_indices[j], j])[0].tolist()
                                #print("Sec", chosen_index)
                                chosen_index = int(chosen_index[0])
                                
                                #print("Sec", sec_chosen_index)
                                y=0
                                if len(sec_chosen_index)>1:
                                    for x in range(len(sec_chosen_index)):
                                        for y in range(y + 1, len(sec_chosen_index)):
                                            if supply[sec_chosen_index[x]] > supply[sec_chosen_index[y]]:
                                                sec_chosen_index_2 = sec_chosen_index[x]
                                                #print("total",total_allocation_per_row[sec_chosen_index_2])
                                                if total_allocation_per_row[sec_chosen_index[x]] == supply[sec_chosen_index[x]]:
                                                    #print("sudah penuh")
                                                    sec_chosen_index_2 = sec_chosen_index[y]
                                                    #print(sec_chosen_index_2)
                                                # if allocation[sec_chosen_index_2,j]==0:
                                                #     continue
                                                # sec_chosen_index_2 = sec_chosen_index[y]
                                            else:
                                                sec_chosen_index_2 = sec_chosen_index[y]
                                    sec_chosen_index = sec_chosen_index_2
                                else:
                                    sec_chosen_index = sec_chosen_index        
                                #print("Chosen index rows:", chosen_index)
                                #print("Sec Chosen index rows:", sec_chosen_index)
                                max_demand_col = j
                                #print("Max demand col rows:", max_demand_col)
                                # print(j)
                                
                                #print(cost_matrix[chosen_index,j])
                                # print(cost_matrix[least_cost_indices[choosen_index[0]],j])
                                # break
                            
            
            # print("chosen_index", chosen_index)
            # print(supply[sec_chosen_index])
            # print(cost_matrix[chosen_index])
            # print(cost_matrix[sec_chosen_index])
            if supply[chosen_index]==supply[sec_chosen_index]:
                if total_allocation_per_row[chosen_index] < supply[chosen_index]:
                    print("flc harus dipenuhi")
                else:
                    #print("oi?")
                    break
            else:
                ecount = 0
                for e in excess:
                    if e:
                        ecount+=1
                if ecount > 1:
                    if supply[chosen_index] > supply[sec_chosen_index]:
                        #print(cost_matrix[chosen_index,max_demand_col])
                        print(supply[chosen_index])
                    else:
                        #print("tidak ini?")
                        required_amount = supply[sec_chosen_index] - total_allocation_per_row[sec_chosen_index]
                        #print(required_amount)
                        allocation[sec_chosen_index,max_demand_col] = required_amount
                        allocation[chosen_index, max_demand_col] -= required_amount
                        
                else:
                    if supply[chosen_index] < supply[sec_chosen_index]:                
                        #Clear
                        lebih = total_allocation_per_row[chosen_index]
                        minus = lebih - supply[chosen_index]
                        allocation[chosen_index,max_demand_col] -= minus
                        allocation[sec_chosen_index,max_demand_col] += minus
                    else:
                        #Clear
                        required_amount = supply[sec_chosen_index] - total_allocation_per_row[sec_chosen_index]
                        allocation[chosen_index,max_demand_col] -= required_amount
                        allocation[sec_chosen_index,max_demand_col] += required_amount
                        
            total_allocation_per_row = np.sum(allocation, axis=1)
            total_all_col = np.sum(allocation, axis=0)
            same_sup = (total_allocation_per_row==supply)
            excess = (total_allocation_per_row > supply)
            iter += 1
            print("Iter: ", iter)
            print(allocation)
            if iter > 4:
                break

        total_cost = np.sum(cost_matrix * allocation)
        total_allocation_per_row = np.sum(allocation, axis=1)
        print("\n\nCost Mat: \n", cost_matrix)
        print("Alokasi: \n", allocation)
        print(f"Total biaya: {total_cost}")

        result_matrix = matrix_cost.copy()

        # Ubah tipe data result_matrix menjadi objek
        result_matrix = result_matrix.astype(object)

        # Iterasi dan ubah nilai jika ada alokasi (jalankan kembali kode yang sebelumnya error)
        for i in range(allocation.shape[0]):
            for j in range(allocation.shape[1]):
                if allocation[i, j] != 0:
                    result_matrix[i, j] = f"({allocation[i, j]:.0f}){cost_matrix[i, j]}"

        # Membuat DataFrame dari result_matrix
        df_result = pd.DataFrame(result_matrix)

        # Tambahkan kolom 'Supply'
        df_result['Supply'] = array_supply

        # Tambahkan elemen '0' pada akhir demand agar sesuai dengan jumlah kolom
        demand = np.append(matrix_demand, '')

        # Tambahkan baris 'Demand'
        df_result.loc['Demand'] = demand

        trans = Transportation(matrix_cost, matrix_supply, matrix_demand)
        trans.setup_table(minimize=True)
        KS = KaragulSahinApproximation(trans)
        allocation, wcd, wcs, min_cost = KS.solve(show_iter=True)
        df = trans.print_table(allocation)
        
        # Konversi DataFrame menjadi HTML
        html_table = df_result.to_html(classes='table table-striped text-center', index=True)

        context = {
            'title':title,
            'df': df,
            'html_table': html_table,
            'rownames':rownames,
            'columnames':columnames,
            # 'wcd':wcd,
            # 'wcs':wcs,
            'min_cost':total_cost,
        }
    else:
        context = {
            'title':'',
        }     
    return render(request, "resultssm.html", context)

# link ksam https://github.com/deyanarajib/transportation-problem/blob/main/karagul_sahin_approximation.py