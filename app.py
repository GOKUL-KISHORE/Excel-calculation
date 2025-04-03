from flask import Flask, render_template,request, url_for
#import Main_bg
import pandas as pd
import io
import openpyxl
import math
import seaborn as sns
import matplotlib.pyplot as plt
import string
import re
import warnings
from openpyxl import load_workbook
import random
import base64
import os

app = Flask(__name__) 

#TEXT_FILE = 'response_log.txt' 
#LOG_FILE = os.path.join(log_dir, 'response_log.txt')

log_dir = os.path.join(app.root_path, 'EXCEL_CAL_TEXT')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

LOG_FILE = os.path.join(log_dir, 'EXCEL_TEDOC.txt')
"""

try:
    with open(LOG_FILE, 'a') as f: 
        if os.path.getsize(LOG_FILE) == 0: 
            f.write("--- Application Log ---\n")  
except Exception as e:
    print(f"Error creating or accessing text file: {e}")

@app.route('/delete_text')
def delete_text():
    try:
        with open(TEXT_FILE, 'w') as f:  
            f.write("") 
        return render_template('index.html', message="Text file deleted.")
    except Exception as e:
        return render_template('index.html', error=f"Error deleting text file: {e}")
    """
@app.route('/', methods=['GET', 'POST'])
           
def process_data():
    if request.method == 'POST':
        excel_file = request.files['excel_file']
        temperature= request.form['temperature']
        if excel_file.filename == '':
            return "No file selected"
   
        try:
            file=pd.read_excel(io.BytesIO(excel_file.read()))
            df = pd.DataFrame(file)
            temp=0
            temp=temperature
            #print(f"Temperature: {temperature}")
            #print("DataFrame:")
            #print(df)
            df = pd.DataFrame(file)
            column_names = df.columns
            num_lists = len(column_names)
            input_string=None
            column_to_print_A=0
            column_to_print_B=1
            if len(column_names) == 0 or len(column_names) == 2 or len(column_names) == 3:
                
                #column_to_print_A=0
                #column_to_print_B=1
                 
                search_word = "Test Temperature"
                rows_index = 0
                col_index=[]   
                for row_index, row in file.iterrows():
                    for col_name, cell_value in row.items():
                        if isinstance(cell_value, str):
                            if search_word.lower() in cell_value.lower():
                                    rows_index=row_index
                                    col_index.append((col_name))
                result_col=0
                for col in col_index:
                    input_string = str(col)
                    parts = input_string.split(':')
                    if len(parts) == 2:
                        number_string = parts[1]
                        integer_value = int(number_string)
                        result=integer_value+1
                        result_col=result
                if 0 <= rows_index < len(df) and 0 <= result_col < len(df.columns):
                    cell_value = df.iloc[rows_index,result_col]
                    temp=cell_value
                      
            else:
                
                search_word = "Test Temperature"
                results = []
                temin=[]   
                for row_index, row in file.iterrows():
                    for col_name, cell_value in row.items():
                        if isinstance(cell_value, str):
                            if search_word.lower() in cell_value.lower():
                                results.append((row_index))
                 
                for r in results:
                    row = file.iloc[r]
                    value_list = row.to_list()
                    for value in value_list:
                        temin.append(value)
                
                temperature=0
                for tem in temin:
                    if tem == temp:
                        return temp
                        break
                    else:
                        for result in results:
                            res=result + 1
                            if res == temp:
                                return temp
                                break
                                
                
                search_value=int(temp)
                
                for row_number in results:
                    if 0 <= row_number < len(file):
                        row = file.iloc[row_number]
                        for column_name, cell_value in row.items():
                            if isinstance(cell_value, str):
                                if search_value == cell_value:                              
                                    input_string = column_name
                                    break
                                else:
                                    if isinstance(search_value, str) and search_value.lower() == cell_value.lower():
                                            
                                        input_string = column_name
                                        break
                                      
                            elif isinstance(cell_value, (int, float)):
                                if search_value == cell_value:
                                       
                                    input_string = column_name
                                    break
                                        
                                
                input_string = str(input_string)
                parts = input_string.split(':')
                if len(parts) == 2:
                    number_string = parts[1]
                    integer_value = int(number_string)
                    column_to_print_A=integer_value-1
                    column_to_print_B=integer_value

                
            # A column


            def print_excel_columnA(df,column_number,sheet=None):
                column_name = df.columns[column_number]
                column_values = []
                for value in df[column_name]:
                    if not isinstance(value, float) or not math.isnan(value):
                        k.append(value)
                 
                es=["Engineering","Strain"]
                es1=[item.lower() if isinstance(item, str) else item for item in es]
                
                
                for item in k:
                    if isinstance(item, str):
                        words = re.findall(r'\b\w+\b',item.lower())
                        sp.append(words)
                    else:
                        string_value = str(item)
                        sp.append(string_value)
                        
                               
                ind=0
                for i in es1:
                    for j in sp:
                        for m in j:
                            if m==i and len(sp)>= 1 :
                                ind = sp.index(j)
                                
               
                ix.append(ind)
                if ind != 0:          
                    for i in range(ind + 1,len(k),1):
                        if isinstance(k[i], str):
                            mm=i
                            break
                        else:
                            mm=len(k)
                    
                    for i in range(mm):
                        if ind < i:
                            if isinstance(k[i], float):
                                a.append(k[i])
                            elif isinstance(k[i], int):
                                a.append(k[i])
                            else:
                                continue
                else:
                    for i in range(ind + 1,len(k),1):
                        if isinstance(k[i], str):
                            mm=i
                            break
                        else:
                            mm=len(k)
                    
                    for i in range(mm):
                        if isinstance(k[i], float):
                            a.append(k[i])
                        elif isinstance(k[i], int):
                            a.append(k[i])
                        else:
                            continue
                     
                    
            #column_to_print_A = "A"
            k=[]
            sp=[]
            a=[]
            ix=[]
            print_excel_columnA(df,column_to_print_A)

             
            #B column

            def print_excel_column(df,column_number,sheet=None):
                column_name = df.columns[column_number]
                column_values = []
                for value in df[column_name]:
                    if not isinstance(value, float) or not math.isnan(value):
                        l.append(value)
                 
                es=["Engineering","Stress"]
                es1=[item.lower() if isinstance(item, str) else item for item in es]
                
                for i in l:
                    if isinstance(i, str):
                        words = re.findall(r'\b\w+\b',i.lower())
                        sp2.append(words)
                    else:
                        string_value = str(i)
                        sp2.append(string_value)
                  
                
                ind=0
                for i in es1:
                    for j in sp2:
                        for m in j:
                            if m==i and len(sp2)>= 1 :
                                ind = sp2.index(j)
                                
                
                if ind != 0:           
                    for i in range(ind + 1,len(l),1):
                        if isinstance(l[i], str):
                            mm=i
                            break
                        else:
                            mm=len(l)
                    for i in range(mm):
                        if ind < i:
                            if isinstance(l[i], float):
                                b.append(l[i])
                            elif isinstance(l[i], int):
                                b.append(l[i])
                            else:
                                False
                  
                else:
                    for i in range(ind + 1,len(l),1):
                        if isinstance(l[i], str):
                            mm=i
                            break
                        else:
                            mm=len(l)
                     
                    for i in range(mm):
                        if isinstance(l[i], float):
                            b.append(l[i])
                        elif isinstance(l[i], int):
                            b.append(l[i])
                        else:
                            continue
                         
            #column_to_print_B= "B"
            l=[]
            b=[]
            e=[]
            sp2=[]
            print_excel_column(df,column_to_print_B)

            # STRAIN UNIT CONVERSION

            k1=0
            for i in sp:
                for j in i:
                    if j=="µm":
                        ix = i.index(j)
                        if i[ix + 1] =="m":
                            k1=1
                            break
                    elif j=="nm" :
                        ix = i.index(j)
                        if i[ix + 1] =="m":
                            k1=4
                            break

                                   
            k3=[]           
            if k1==1:
                for item in a:
                    k3.append(item * 0.000001)
            elif k1==4:
                for item in a:
                    k3.append(item /1000000.0)
            else:
                for item in a:
                    k3.append(item)
                                                       

            # STRESS UNIT CONVERSION

            k2=0
            for i in sp2:
                for j in i:
                    if j=="pa":
                        k2=1
                        break
                    elif j=="kpa" :
                        k2=2
                        break
                    elif j== "gpa":
                        k2=3
                        break
                    elif j== "mpa":
                        k2=4
                        break
                    elif j=="psi" :
                        k2=5
                        break
                    elif j=="ksi" :
                        k2=6
                        break
                      

            k4=[]               

            if k2==1:
                for item in b:
                    k4.append(item / 1000000.0)
            elif k2==2:
                for item in b:
                    k4.append(item / 1000.0)
            elif k2==3:
                for item in b:
                    k4.append(item * 1000.0)
            elif k2==4:
                for item in b:
                    k4.append(item)
            elif k2==5:
                for item in b:
                    k4.append(item * 0.00689476)
            elif k2==6:
                for item in b:
                    k4.append(item * 6.89476)
            else:
                for item in b:
                    k4.append(item)


            # LOG VALUE A


            c=[]
            d=[]

            for i in range(0,len(k3),1):
                c.append(k3[i])
                
            for i in c:
                if i >= 0:
                    natural_log = math.log(1+i)
                    d.append(natural_log)
                else:
                    natural_log= -math.log(abs(1+i))
                    d.append(natural_log)
                     
              
            for i in range(0,len(k4),1):
                e.append(k4[i])
                
            # CALCULATE USING THIS FORMULA L1*(1+L2)(STRESS)

            g = []
            for x in c:
                f = 1+float(x)
                g.append(f)

            result_list=[]
            for i in range(len(g)):
                result_list.append(g[i]*e[i])
                

            # CALCULATE USING THIS FORMULA d-(result_list / D) (STRAIN)


            z=[]
            for i in range(0,len(e),1):
                if c[i]==0 or e[i]==0:
                    z.append(0)
                else:
                    lk=e[i] / c[i]
                    z.append(lk)

            #READ THE CONSTANT VALUE OF EXCEL FILE

            def constant_value(search_word, sheet_name=0):
                global cv
                cv=0
                result_row=[]
                result_column=[]
                for row_index, row in file.iterrows():
                     for col_name, cell_value in row.items():
                          if isinstance(cell_value, str):
                               if search_word.lower() in cell_value.lower():
                                    result_row.append((row_index))
                                    result_column.append((col_name))
                                    
                
                str2=0
                str3=0
                result_col=[]
                for col in result_column:
                    input_string = str(col)
                    parts = input_string.split(':')
                    if len(parts) == 2:
                         number_string = parts[1]
                         integer_value = int(number_string)
                         result=integer_value
                         result_col.append(result)
                         
                result_rows=[]       
                for row in result_row:
                    rows=int(row)+1
                    result_rows.append(rows)
                    
                for rows in result_row:
                    for col in result_col:
                        if 0 <= rows < len(df) and 0 <= col < len(df.columns):
                            cell_value = df.iloc[rows,col]
                            str2=cell_value
                            
                for rows in result_rows:
                    for col in result_col:
                        if 0 <= rows < len(df) and 0 <= col < len(df.columns):
                            cell_value = df.iloc[rows,col]
                            if pd.isna(cell_value) or cell_value == "":
                                rows=rows+1
                                if 0 <= rows < len(df) and 0 <= col < len(df.columns):
                                    cell_value = df.iloc[rows,col]
                                    str3=cell_value
                            else:
                                str3=cell_value
                                
                str4=[] 
                k=str2.split()
                for item in k:
                    if isinstance(item, str):
                        words = re.findall(r'\b\w+\b',item.lower())
                        str4.append(words)
                    else:  
                        string_value = str(item)
                        str4.append(string_value)

                k2=0
                
                for i in str4:
                    for j in i:
                        if j=="pa":
                            k2=1
                            break
                        elif j=="kpa" :
                            k2=2
                            break
                        elif j== "gpa":
                            k2=3
                            break
                        elif j== "mpa":
                            k2=4
                            break
                        elif j=="psi" :
                            k2=5
                            break
                        elif j=="ksi" :
                            k2=6
                            break
                      
                            

                if k2==1:
                    str5=str3 / 1000000.0
                elif k2==2:
                    str5=str3 / 1000.0
                elif k2==3:    
                    str5=str3 * 1000.0
                elif k2==4:
                    str5=str3
                elif k2==5:
                    str5=str3 * 0.00689476
                elif k2==6:     
                    str5=str3 * 6.89476
                else:     
                    str5=str3
               
                cv=round(str5)
                

            str5=0
            #cv=0
            search_phrase ="Young's (Tensile) Modulus"
            constant_value(search_phrase)

           
            c_v=[]
            for i in range(len(z)):
                if float (cv) < float (z[i]):
                    c_v.append(z[i])
                    
            if len(c_v)!=0:
                con = min(c_v)
                con_i=0
            else:
                if len(c_v)==0 or len(c_v)==1:
                    con =cv
                    con_i=1
                      
            h = []
            for x in result_list :
                m = float(x) / con
                h.append(m)

            n = []
            for i in range(min(len(d), len(h))):
                n.append(d[i] - h[i])

            # CALCULATE USING THIS FORMULA (result_list - (n* con))

            o = []
            for x in n :
                
                p = float(x) * con
                o.append(p)


            q = []
            for i in range(min(len(result_list),len(o))):
                q.append(result_list[i] - o[i])


            # X AND Y Conversion

            if con_i==0:
                ind = z.index(con)
            else:
                if con_i==1:
                    con=max(q)
                    ind = q.index(con)

            y=[]
            y.append(q[ind])  
            for j in range(1,len(result_list),1):
                result_list[j] = abs(result_list[j])
                if ind +1 < j:
                    y.append(result_list[j])
                 
                 
            x=[]
            x.append(0)
            for i in range(1,len(n),1):
                n[i] = abs(n[i])
                if ind + 1 < i:
                    x.append(n[i])

            result_index_y=[]
            ka=1
            #print(x,len(x))
            #print(y,len(y))
            if len(y)<=10:
                 
                y.clear()
                y.append(q[ind])
                for i in range(len(result_list)):
                    if y[0] < result_list[i]:
                        result_index_y.append(result_list.index(result_list[i]))
                        y.append(result_list[i])
                 
                x.clear()
                x.append(0)
                for i in range(len(n)):
                    for j in result_index_y:
                        if i==j:
                            x.append(n[i])
                                
                                 
                if len(result_index_y)==0:
                    inx = len(result_list) // 2
                    y.clear()
                    y.append(q[inx])
                    for i in range(len(result_list)):
                        if y[0] < result_list[i]:
                            result_index_y.append(result_list.index(result_list[i]))
                            y.append(result_list[i])
                                
                    x.clear()
                    x.append(0)
                    for i in range(len(n)):
                        for j in result_index_y:
                            if i==j:
                                x.append(n[i])
                      
                 
                del x[1]
                del y[1]
                start_point = x[0]
                end_point = x[1]
                total_range = end_point - start_point
                increment = total_range / 7
                x_1 = start_point + increment
                x_2 = start_point + 2 * increment
                x_3 = start_point + 3 * increment
                x_4 = start_point + 4 * increment
                x_5 = start_point + 5 * increment
                x_6 = start_point + 6 * increment
                random_values_x1 = [random.uniform(x_1, x_2)]
                random_values_x2 = [random.uniform(x_3, x_4)]
                random_values_x3 = [random.uniform(x_5, x_6)]
                x[1 :1]=random_values_x1
                x[2 :2]=random_values_x2
                x[3 :3]=random_values_x3

                 

                start_pointy = y[0]
                end_pointy = y[1]
                total_rangey = end_pointy - start_pointy
                incrementy = total_rangey / 7
                y_1 = start_pointy + incrementy
                y_2 = start_pointy + 2 * incrementy
                y_3 = start_pointy + 3 * incrementy
                y_4 = start_pointy + 4 * incrementy
                y_5 = start_pointy + 5 * incrementy
                y_6 = start_pointy + 6 * incrementy
                random_values_y1 = [random.uniform(y_1, y_2)]
                random_values_y2 = [random.uniform(y_3, y_4)]
                random_values_y3 = [random.uniform(y_5, y_6)]
                y[1 :1]=random_values_y1
                y[2 :2]=random_values_y2
                y[3 :3]=random_values_y3
                 

            yy=[]
            xx=[]
            len_value = len(x)
            if len_value <= 50 and len_value > 0:
                ka =len_value//len_value
            elif len_value >= 50 and len_value < 200 :
                ka =len_value//35
            elif len_value >= 200 and len_value < 600 :
                ka =len_value//35
            elif len_value >= 600 and len_value < 1000 :
                ka =len_value//35
            elif len_value >= 1000 :
                ka =len_value//35

            if len(y)<=10:
                st=6
                for i in range(0,6,1):
                    xx.append(x[i])
                for j in range(0,6,1):
                    yy.append(y[j])
            else:
                st=0
                 
            for i in range(st,len(x),ka):
                x[i] = abs(x[i])
                xx.append(x[i])
                 
            for j in range(st,len(y),ka):
                y[i] = abs(y[i])
                yy.append(y[j])
            #print(xx,len(xx))
            #print(yy,len(yy))
            result_index_x=[]
            yyy=[]
            xxx=[]
            yyy.append(yy[0])

            for i in range(1,len(yy),1):
                if yy[0]<yy[i]:
                    result_index_x.append(yy.index(yy[i]))
                    yyy.append(yy[i])
                                
                      
            xxx.append(0)
            for i in range(1,len(xx),1):
                for j in result_index_x:
                    if i==j:
                        xxx.append(xx[i])
                        
            #yyy = sorted(yyy)
            xxx = sorted(xxx)
                          
            new_temp=[]
            for i in range(len(x)):
                i=temp
                new_temp.append(i)

            # OUTPUT FORMATION

            #1      
            def find_phrase_in_excel1(df,search_phrase, sheet_name=0):
                result_row =[]
                result_column =[]
                for search in search_phrase:
                    for row_index, row in df.iterrows():
                        for col_name, cell_value in row.items():
                            if isinstance(cell_value, str):         
                                if cell_value == search:
                                    result_row.append((row_index))
                                    result_column.append((col_name))

                            elif cell_value == search: 
                                result_row.append((row_index))
                                result_column.append((col_name))
                                
                
                for col in result_column:
                    input_string = str(col)
                    parts = input_string.split(':')
                    if len(parts) == 2:
                        number_string = parts[1]
                        integer_value = int(number_string)
                        result_col=integer_value +1
                         
                for row in result_row:         
                    if 0 <= row < len(df) and 0 <= result_col < len(df.columns):
                        cell_value = df.iloc[row, result_col]
                        str1.append(cell_value)
                
                str1.append("Matcen_QS_RT")         
                string_list = [str(x) for x in str1]
                joined_string = "_".join(string_list)
                
                #print(" *  MATERIAL, NAME = ",joined_string)
                
            str1=[]
            search_phrase =["Industry Standard or Ford Engineering Material Specification","Material Type"]
            find_phrase_in_excel1(df, search_phrase)
            
            #str1.append("Matcen_QS_RT")         
            string_list = [str(x) for x in str1]
            joined_string = "_".join(string_list)
            #print(joined_string)
            #2

            def find_phrase_in_excel2(df,search_word, sheet_name=0):
              
                result_row=[]
                result_column=[]
                for word in search_word:
                    for row_index, row in file.iterrows():
                        for col_name, cell_value in row.items():
                            if isinstance(cell_value, str):
                                if word.lower() in cell_value.lower():
                                    result_row.append((row_index))
                                    result_column.append((col_name))
                                    
               
                result_col=[]
                for col in result_column:
                    input_string = str(col)
                    parts = input_string.split(':')
                    if len(parts) == 2:
                        number_string = parts[1]
                        integer_value = int(number_string)
                        result=integer_value
                        result_col.append(result)
                         
                result_rows=[]       
                for row in result_row:
                    rows=int(row)+1
                    result_rows.append(rows)
                    
                for rows in result_row:
                    for col in result_col:
                        if 0 <= rows < len(df) and 0 <= col < len(df.columns):
                            cell_value = df.iloc[rows,col]
                            str2.append(cell_value)
                            
                for rows in result_rows:
                    for col in result_col:
                        if 0 <= rows < len(df) and 0 <= col < len(df.columns):
                            cell_value = df.iloc[rows,col]
                            if pd.isna(cell_value) or cell_value == "":
                                rows=rows+1
                                if 0 <= rows < len(df) and 0 <= col < len(df.columns):
                                    cell_value = df.iloc[rows,col]
                                    str3.append(cell_value)
                            else:
                                str3.append(cell_value)
                  
                #print(" * ",str2[0]," = ",str3[0])
                #print(" * ",str2[1]," = ",str3[1])
                #print(" *  PLASTIC , HARDENING = ISOTROPIC")
                
            str2=[]
            str3=[]              
            search_phrase =["DENSITY","Poisson's Ratio"]
            find_phrase_in_excel2(df,search_phrase)
            
            
            #PLOT GRAPH

    
            data = list(zip(xxx,yyy,new_temp))

            df = pd.DataFrame(data, columns=["X-AXIS", "Y-AXIS", "TEMPERATURE"])  
            response_data = df.to_string()
            #print (df)
            with open(LOG_FILE, 'w') as f:
                f.write(f" *  MATERIAL, NAME = {joined_string}\n")
                f.write(f" * {str2[0]} = {str3[0]}\n")
                f.write(f" * {str2[1]} = {str3[1]}\n")
                f.write(" *  PLASTIC , HARDENING = ISOTROPIC \n")
                f.write(response_data)
                    
              
                    

            return render_template("output.html",output=joined_string,output1=str2[0],output2=str3[0],output3=str2[1],output4=str3[1],dataframe=df.to_html())
        except Exception as e:
            return f"An error occurred: {str(e)}"
            
    return render_template('index.html')  
    

if __name__ == '__main__':
    app.run(debug=True)
