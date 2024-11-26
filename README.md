# Web-Based Transportation Problem Solver
This website is developed to solve balanced transportation problems using two modern methods, namely the Supply Selection Method (SSM) and the Karagul-Sahin Approximation Method (KSAM). A transportation problem is a branch of operations research aimed at minimizing the total cost of distributing goods from supply points to demand points.

The goal of this project is to provide an efficient solution through a Python-based web interface. In testing, the SSM method proved to be more optimal compared to KSAM, resulting in an Initial Basic Feasible Solution (IBFS) with a lower distribution cost.

## ✨ Key Features
* **Balanced Transportation Problem Solution**: Optimizes the allocation of goods from sources to destinations.
* **Two Method Support**: Implements both SSM and KSAM for result comparison.
* **Data Validation**: The system automatically validates the balance between supply and demand.
* **Modern Interface**: Easy to use with a responsive web interface that provides solution table visualizations.

## 💻 System Requirements
To run this application, you will need:
- **Python**: Version 3.8 or higher
- **Django**: Version 4.2.16

## 🚀 Website Overview & How It Works
1. **Main Website Page**

    Users can choose which method they would like to use.
![Halaman Utama Website](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Login%20Page.png?raw=true)

2. **Transportation Problem Information Entry Page**

   Users can fill in the **Title**, **Number of Source**, **Number of Destination** and choose **Row Names**, and **Column Names** then click **Submit**
![Halaman Pengisian Informasi Permasalahan Transportasi](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Information%20Entry%20Page.png?raw=true)

3. **Transportation Problem Data Entry Page**

   Users can enter the transportation problem data they wish to solve.
![Halaman Pengisian Data Permasalahan Transportasi](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Data%20Entry%20Page.png?raw=true)
 
   Then click Validate to check if the inputted transportation problem is balanced. If balanced, a pop-up like this will appear:
![Halaman Pengisian Data Permasalahan Transportasi](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Balanced%20Data.png?raw=true)

   However, if the entered data is not balanced, a pop-up like this will appear:
![Halaman Pengisian Data Permasalahan Transportasi](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Unbalanced%20Data.png?raw=true)

4. **Data Ready to Solve View**
![Tampilan Data Siap untuk Di Solve](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Page%20to%20Solve.png?raw=true)

5. **IBFS Results or Final Solution Table View**
![Tampilan Hasil IBFS dari Permasalahan Transportasi atau Final Solution Table](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Final%20Solution%20Page.png?raw=true)



