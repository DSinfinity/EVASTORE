import pandas as pd

from datetime import *
import os

def convert(filename):
    #print(os.getcwd())
    #print(filename)
    #os.chdir(r"C:\Users\Rafid_S\Documents\EVASTORE\Input Folder")
    os.chdir("/home/pi/EVASTORE/Input Folder")
    print(os.getcwd())
    #os.chdir(filename)
    df = pd.read_excel(str(filename))
    #df=df.drop(df.columns[[0,1,2]],axis = 1)

    df_out = pd.DataFrame(columns=["Record Type","Level 1 Account Code","Level 2 Account Code","Level 3 Account Code","Open?","Separate Invoice?","Account Description","Contract Expire","Date","PO Number","Salesman Code","Mail Attention","Mail Addr Line 1","Mail Addr Line 2","Mail Addr Line 3","Mail Addr Phone","Mail Addr Fax","Mail Addr Route","Pickup Contact","Pickup Addr Line 1","Pickup Addr Line 2","Pickup Addr Line 3","Pickup Addr Phone","Pickup Addr Fax"])

    #df_out[["Level 1 Account Code", "Account Description","Mail Addr Line 1", "Mail Addr Line 2"]] = df[["O'Neil Account Number","Account Name", "Address Line 1", "Address Line 2"]]
    df_out[[ "Account Description","Mail Addr Line 1", "Mail Addr Line 2"]] = df[["Account Name", "Address Line 1", "Address Line 2"]]
    #df_out["Mail Addr Line 3"] = df["Address Line 3"]+", "+df["Region"]+", "+df["Postcode"]
    df_out["Mail Addr Line 3"] = df[["Address Line 3", "Region", "Postcode"]].fillna('').astype(str).agg(', '.join, axis=1)
    df_out["Mail Addr Line 3"] = df_out["Mail Addr Line 3"].str.strip(", ,")
    df_out["Mail Addr Line 3"] = df_out["Mail Addr Line 3"].str.replace(", ,",",")
    df_out["Record Type"]= "AC"
    df_out["Open?"]= "YES"
    df_out["Separate Invoice?"]= "YES"
    df_out[["Pickup Addr Line 1","Pickup Addr Line 2","Pickup Addr Line 3"]] = df_out[["Mail Addr Line 1","Mail Addr Line 2","Mail Addr Line 3"]]
    df_out["Mail Addr Phone"] = df["Main Phone"]

    for values in df["O'Neil Account Number"]:
        if isinstance(values,str) is not True:
            
            next
        else:
            if "/" not in values:
                #df_out["Level 1 Account Code"] = values
                df_out.iloc[df[df["O'Neil Account Number"]== values].index.values[0],1] = values
                #print(df_out.iloc[df[df["O'Neil Account Number"]== values].index.values[0],1])
            else:
                x = values.split("/")
                for i in range (len(x)):
                    #print (df[df["O'Neil Account Number"]== values].index.values[0])
                    df_out.iloc[df[df["O'Neil Account Number"]== values].index.values[0],i+1] = x[i]

    df_out["Level 1 Account Code"] =  df_out["Level 1 Account Code"].combine_first(df["Account Number"])        
    #print(df_out.head(5))
    outfile_name= "oneilImportFile_"+ datetime.now().strftime("%d-%m-%Y")+".csv"
    global outputpath
    #outputpath = 'C:/Users/Rafid_S/Documents/EVASTORE/Output Folder/'+outfile_name
    outputpath = "/home/pi/EVASTORE/Output Folder/"+outfile_name
    df_out.to_csv(outputpath, index = False)
    #C:\Users\Rafid_S\Downloadsprint ("File Saved at C:/Users/Rafid_S/Documents/EVASTORE/Output Folder/"+outfile_name)
#convert(input("File dir: "))
#print(df_out.head(2))
