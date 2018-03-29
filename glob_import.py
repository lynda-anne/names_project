import pandas as pd
import math
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

#this imports all the data into one list with no marking for where the years start and st
path = 'yob*.csv'
files = glob.glob(path)

df= []
for file in files :
    df.append(pd.read_csv(file, index_col= None, header=None))

#Inspect loaded files
#print(len(df))
#print(df[0].head)
#print(df[0].info())

# Add column names
i=0
n = 1880
for item in df :
    df[i].columns =  ['Name', 'Sex', 'Count']
    #print(df[i].info())
    df[i]['Year']= n
    i= i  + 1
    n= n + 1

print(df[0].head())
print(df[-1].tail())

#Concatenate the list of dataframes into one dataframe
names= pd.concat(df)
print(names.info())
#print(names[100000:])

#_______________________________________________________________________________
# Initial Exploratory data review
# plt.scatter(x=names.Year, y=names.Count)
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Frequency and Number of Names')
# plt.savefig('by_year_scatter.pdf')
# plt.show()
#
# names= names.set_index('Sex')
# plt.scatter(x=names.loc['F'].Year, y=names.loc['F'].Count)
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Frequency and Number of Girls Names')
# plt.savefig('female_by_year_scatter.pdf')
# plt.show()
#
# plt.scatter(x=names.loc['M'].Year, y=names.loc['M'].Count)
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Frequency and Number of Boys Names')
# plt.savefig('male_by_year_scatter.pdf')
# plt.show()
#_______________________________________________________________________________
#calculate proportion of count for each name
names2 = names.copy()
total_births_by_year = names2.groupby('Year')['Count'].transform('sum')
#print(total_births_by_year)
names2['prop_births']= names2['Count']/total_births_by_year
print(names2)
print(names2.shape)

#create dataframe with female names
names_f = names2['Sex'] == 'F'
names_f= names2[names_f]
print(names_f.tail())
#Select top 5 female names for each year
top5_f= names_f.groupby('Year').head()
print(top5_f)
top5_female= top5_f.reset_index()
del top5_female['index']
del top5_female['Sex']
print(top5_female.info())
del top5_female['Count']
top5_fnames= top5_female.set_index('Name')
print(top5_fnames.head())

# #Pivot the dataframe to make years columns
top5_fnames_tidy = top5_fnames.pivot_table(values='prop_births', index=['Name'], columns=['Year'])
top5_fnames_tidy = top5_fnames_tidy.fillna(0)
print(top5_fnames_tidy.head())
print(top5_fnames_tidy.tail())
print(top5_fnames_tidy.info())

top5_fnames_tidy= top5_fnames_tidy.reset_index()
print(top5_fnames_tidy.info())
print(top5_fnames_tidy.head())
print('&&&&&&&&&&&&&&&&&&')
print(top5_fnames_tidy.shape)

top5_fnames_tidy= top5_fnames_tidy.set_index('Name')
df=[]
n= 0
for item in top5_fnames_tidy :
    if n <= 45 :
        top5f_by_year= top5_fnames_tidy.iloc[n]
        df.append(top5f_by_year)
        n = n + 1
top5_fnames= pd.concat(df, axis=1)
top5_fnames= top5_fnames.reset_index()
print(top5_fnames.info())
print(top5_fnames.head())
print(top5_fnames.shape)

#Plots for top 5 girls names over the years
n=1
for item in top5_fnames :
    if n <= 9 :
        x= top5_fnames['Year']
        y = top5_fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_girls_names1.pdf')
plt.show()

n=10
for item in top5_fnames :
    if n <= 19:
        x= top5_fnames['Year']
        y = top5_fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_girls_names2.pdf')
plt.show()

n=20
for item in top5_fnames :
    if n <= 29:
        x= top5_fnames['Year']
        y = top5_fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_girls_names3.pdf')
plt.show()

n=30
for item in top5_fnames :
    if n <= 39:
        x= top5_fnames['Year']
        y = top5_fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_girls_names4.pdf')
plt.show()

n=40
for item in top5_fnames :
    if n <= 46:
        x= top5_fnames['Year']
        y = top5_fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_girls_names5.pdf')
plt.show()

#_______________________________________________________________________________
#find top 5 boys names for each year
names_m = names2['Sex'] == 'M'
names_m= names2[names_m]
print(names_m.tail())
#Select top 5 male names for each year
top5_m= names_m.groupby('Year').head()
print(top5_m)
top5_male= top5_m.reset_index()
del top5_male['index']
del top5_male['Sex']
print(top5_male.info())
del top5_male['Count']
top5_mnames= top5_male.set_index('Name')
print(top5_mnames.head())

# #Pivot the dataframe to make years columns
top5_mnames_tidy = top5_mnames.pivot_table(values='prop_births', index=['Name'], columns=['Year'])
top5_mnames_tidy = top5_mnames_tidy.fillna(0)
print(top5_mnames_tidy.head())
print(top5_mnames_tidy.tail())
print(top5_mnames_tidy.info())

top5_mnames_tidy= top5_mnames_tidy.reset_index()
print(top5_mnames_tidy.info())
print(top5_mnames_tidy.head())
print('&&&&&&&&&&&&&&&&&&')
print(top5_mnames_tidy.shape)
#_____________________________________________________________________
#create 'tidy' dataframe for boys names
top5_mnames_tidy= top5_mnames_tidy.set_index('Name')
df=[]
n= 0
for item in top5_mnames_tidy :
    if n <= 24 :
        top5m_by_year= top5_mnames_tidy.iloc[n]
        df.append(top5m_by_year)
        #(top5f_by_year)
        n = n + 1
top5_mnames= pd.concat(df, axis=1)
top5_mnames= top5_mnames.reset_index()
print(top5_mnames.info())
print(top5_mnames.head())
print(top5_mnames.shape)

#Plot the % change of use of top 5 boys names
n=1
for item in top5_mnames :
    if n <= 5 :
        x= top5_mnames['Year']
        y = top5_mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_boyss_names1.pdf')
plt.show()

n=6
for item in top5_mnames :
    if n <= 10:
        x= top5_mnames['Year']
        y = top5_mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Boyss Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_boyss_names2.pdf')
plt.show()

n=11
for item in top5_mnames :
    if n <= 20:
        x= top5_mnames['Year']
        y = top5_mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_boys_names3.pdf')
plt.show()

n=21
for item in top5_mnames :
    if n <= 25:
        x= top5_mnames['Year']
        y = top5_mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.ylim(-0.005, 0.05)
plt.subplots_adjust(left=0.2)
plt.ylabel('Proportion of Names')
plt.title('Top 5 Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_top5_boys_names4.pdf')
plt.show()

#_______________________________________________________________________________
#Create dataframe with only female names
female = names['Sex'] == 'F'
fnames= names[female]
del fnames['Sex']
print('fnames info')
print(fnames.info())
#create a list frequent female names
dupf= names_f.groupby('Name').sum()
print('dup_f info')
print(dupf.info())
freq_f = dupf['Count'] >= 20000
common_f= dupf[freq_f]
print(common_f[250:260])
print(common_f.info())
common_f= common_f.reset_index()
common_fnames= common_f['Name']
freq_fnames= common_fnames.tolist()
print(freq_fnames[700:750])

#set fnames index to Name and pull out the common names
print(fnames.info())
fnames=fnames.set_index('Name')
common_f= fnames.loc[common_fnames]
common_df= common_f.reset_index()
print(common_df.head())
print(common_df.info())
#
# #Pivot the dataframe to make years columns
fnames_tidy = common_df.pivot_table(values='Count', index=['Name'], columns=['Year'])
fnames_tidy = fnames_tidy.fillna(0)
print(fnames_tidy.head())
print(fnames_tidy.info())
#
fnames_tidy['Total']= fnames_tidy.sum(axis=1)
print(fnames_tidy.head())
fnames_tidy= fnames_tidy.sort_values(by= 'Total', ascending= False)
print(fnames_tidy[0:9])

#Select very popular female names
top10_fnames= fnames_tidy[0:9]
top10_fnames= top10_fnames.reset_index()
print(top10_fnames.info())
#
# #Extra plot Scatter plot of most popular girls names
# i=1880
# for item in top10_fnames :
#     if i <= 2010 :
#         x= top10_fnames['Name']
#         y= top10_fnames[i]
#         plt.scatter(x, y, label= i)
#         i= i + 10
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.2)
# plt.ylabel('Count')
# plt.title('Top 10 Girls Names')
# plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
# plt.margins(0.1)
# plt.savefig('scatter_top10_girls_names.pdf')
# plt.show()

# #Bar plot of most popluar girls names
i=1880
for item in top10_fnames :
    if i <= 2010 :
        # print(over_1mf['Name'])
        # print(over_1mf[i])
        x= top10_fnames['Name']
        y= top10_fnames[i]
        plt.bar(x, y, label= i)
        i= i + 10
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('Count')
plt.title('Top 10 Traditional Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('bar_top10_traditional_girls_names.pdf')
plt.show()

# #Calulate % change of name popularity top 10 girls names
del top10_fnames['Total']
top10_fnames= top10_fnames.set_index('Name')
print(top10_fnames.head())
top10_fnames_chg = top10_fnames.apply('pct_change', axis=1)*100
pd.set_option('use_inf_as_na', True)
top10_fnames_chg= top10_fnames_chg.replace(np.inf, 0)
top10_fnames_chg= top10_fnames_chg.fillna(0)
del top10_fnames_chg[1880]
# print(top10_fnames_chg.info())
# print(top10_fnames_chg.head())
top10_fnames_chg = top10_fnames_chg.reset_index()
print(top10_fnames_chg.info())
print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(top10_fnames_chg.head())
#plot above spilt out by early and late periods
# i=1890
# for item in top10_fnames_chg :
#     if i <= 1939 :
#         # print(over_1mf['Name'])
#         # print(over_1mf[i])
#         x= top10_fnames_chg['Name']
#         y= top10_fnames_chg[i]
#         plt.scatter(x, y, label= i)
#         i= i + 10
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.2)
# plt.ylabel('Count')
# plt.title('% Change of Top 10 Girls Names 1890-1939')
# plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
# plt.margins(0.1)
# plt.savefig('bar_pctchg_top10_girls_names_early.pdf')
# plt.show()
#
# i=1940
# for item in top10_fnames_chg :
#     if i <= 2016 :
#         # print(over_1mf['Name'])
#         # print(over_1mf[i])
#         x= top10_fnames_chg['Name']
#         y= top10_fnames_chg[i]
#         plt.scatter(x, y, label= i)
#         i= i + 10
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.2)
# plt.ylabel('% Change')
# plt.title('% Change of Top 10 Girls Names 1940-2016')
# plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
# plt.margins(0.1)
# plt.savefig('scatter_pctchg_top10_girls_names_late.pdf')
# plt.show()

# fhigh_var = top10_fnames_chg['Max'] > 50
# var_f_high = top10_fnames_chg[fhigh_var]
# del var_f_high['Max']
# var_f_high= var_f_high.set_index('Name')
# print(var_f_high)
# print(var_f_high.info())

#Create dataframe of the top 10 Traditional girls names
top10_fnames_chg= top10_fnames_chg.set_index('Name')
df=[]
n= 0
for item in top10_fnames_chg :
    if n <= 8 :
        f_by_year= top10_fnames_chg.iloc[n]
        df.append(f_by_year)
        print(f_by_year)
        n = n + 1
fnames= pd.concat(df, axis=1)
fnames= fnames.reset_index()
print(names.info())
print(fnames.head())

#plot %Change of top 10 Traditional girls names
n=1
for item in fnames :
    if n <= 3 :
        x= fnames['Year']
        y = fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('% Change')
plt.title('% Change Traditional Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_traditional_girls_names1.pdf')
plt.show()

n=4
for item in fnames :
    if n <= 6 :
        x= fnames['Year']
        y = fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('% Change')
plt.title('% Change Traditional Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_traditional_girls_names2.pdf')
plt.show()

n=7
for item in fnames :
    if n <= 9 :
        x= fnames['Year']
        y = fnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('% Change')
plt.title('% Change Traditional Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_traditional_girls_names3.pdf')
plt.show()
#___________________________________________________________________________________
#male names
male = names['Sex'] == 'M'
mnames= names[male]
del mnames['Sex']
print('mnames info')
print(mnames.info())
#create a list frequent female names
dupm= mnames.groupby('Name').sum()
print('dupm info')
print(dupm.info())
freq_m = dupm['Count'] >= 20000
common_m= dupm[freq_m]
print(common_m[250:260])
print(common_m.info())
common_m= common_m.reset_index()
common_mnames= common_m['Name']
freq_mnames= common_mnames.tolist()
print(freq_mnames[700:750])

#set fnames index to Name and pull out the common names
print(mnames.info())
mnames=mnames.set_index('Name')
common_m= mnames.loc[common_mnames]
common_dm= common_m.reset_index()
print(common_dm.head())
print(common_dm.info())
#
# #Pivot the dataframe to make years columns
mnames_tidy = common_dm.pivot_table(values='Count', index=['Name'], columns=['Year'])
mnames_tidy = mnames_tidy.fillna(0)
print(mnames_tidy.head())
print(mnames_tidy.info())
#
mnames_tidy['Total']= mnames_tidy.sum(axis=1)
print(mnames_tidy.head())
mnames_tidy= mnames_tidy.sort_values(by= 'Total', ascending= False)
print(mnames_tidy[0:9])

#Select very popular female names
top10_mnames= mnames_tidy[0:9]
top10_mnames= top10_mnames.reset_index()
print(top10_mnames.info())
#
# #Extra plot Scatter plot of most popular boys names
# i=1880
# for item in top10_fnames :
#     if i <= 2010 :
#         x= top10_fnames['Name']
#         y= top10_fnames[i]
#         plt.scatter(x, y, label= i)
#         i= i + 10
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.2)
# plt.ylabel('Count')
# plt.title('Top 10 Girls Names')
# plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
# plt.margins(0.1)
# plt.savefig('scatter_top10_girls_names.pdf')
# plt.show()

# #Bar plot of most popluar boys names
i=1880
for item in top10_mnames :
    if i <= 2010 :
        # print(over_1mf['Name'])
        # print(over_1mf[i])
        x= top10_mnames['Name']
        y= top10_mnames[i]
        plt.bar(x, y, label= i)
        i= i + 10
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('Count')
plt.title('Top 10 Traditional Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('bar_top10_traditional_boys_names.pdf')
plt.show()

# #Calulate % change of name popularity top 10 boys names
del top10_mnames['Total']
top10_mnames= top10_mnames.set_index('Name')
print(top10_mnames.head())
top10_mnames_chg = top10_mnames.apply('pct_change', axis=1)*100
pd.set_option('use_inf_as_na', True)
top10_mnames_chg= top10_mnames_chg.replace(np.inf, 0)
top10_mnames_chg= top10_mnames_chg.fillna(0)
del top10_mnames_chg[1880]
print(top10_mnames_chg.info())
print(top10_mnames_chg.head())
top10_mnames_chg = top10_mnames_chg.reset_index()
print(top10_mnames_chg.info())

#extra plots that split the above data into early and late periods
# i=1890
# for item in top10_fnames_chg :
#     if i <= 1939 :
#         # print(over_1mf['Name'])
#         # print(over_1mf[i])
#         x= top10_fnames_chg['Name']
#         y= top10_fnames_chg[i]
#         plt.scatter(x, y, label= i)
#         i= i + 10
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.2)
# plt.ylabel('Count')
# plt.title('% Change of Top 10 Girls Names 1890-1939')
# plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
# plt.margins(0.1)
# plt.savefig('bar_pctchg_top10_girls_names_early.pdf')
# plt.show()
#
# i=1940
# for item in top10_fnames_chg :
#     if i <= 2016 :
#         # print(over_1mf['Name'])
#         # print(over_1mf[i])
#         x= top10_fnames_chg['Name']
#         y= top10_fnames_chg[i]
#         plt.scatter(x, y, label= i)
#         i= i + 10
# plt.xticks(rotation='vertical')
# plt.subplots_adjust(bottom=0.2)
# plt.ylabel('% Change')
# plt.title('% Change of Top 10 Girls Names 1940-2016')
# plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
# plt.margins(0.1)
# plt.savefig('scatter_pctchg_top10_girls_names_late.pdf')
# plt.show()

# fhigh_var = top10_fnames_chg['Max'] > 50
# var_f_high = top10_fnames_chg[fhigh_var]
# del var_f_high['Max']
# var_f_high= var_f_high.set_index('Name')
# print(var_f_high)
# print(var_f_high.info())

#create DataFrame with top 10 Traditional boys names
top10_mnames_chg= top10_mnames_chg.set_index('Name')
dm=[]
n= 0
for item in top10_mnames_chg :
    if n <= 8 :
        m_by_year= top10_mnames_chg.iloc[n]
        dm.append(m_by_year)
        print(m_by_year)
        n = n + 1
mnames= pd.concat(dm, axis=1)
mnames= mnames.reset_index()
print(mnames.info())
print(mnames.head())

#Plot the % change of use of top 10 Traditional boys names
n=1
for item in mnames :
    if n <= 3 :
        x= mnames['Year']
        y = mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('% Change')
plt.title('% Change Traditional Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_traditional_boys_names1.pdf')
plt.show()

n=4
for item in mnames :
    if n <= 6 :
        x= mnames['Year']
        y = mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('% Change')
plt.title('% Change Traditional Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_traditional_boys_names2.pdf')
plt.show()

n=7
for item in mnames :
    if n <= 9 :
        x= mnames['Year']
        y = mnames.iloc[0:, n]
        plt.scatter(x, y)
        n= n + 1
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.2)
plt.ylabel('% Change')
plt.title('% Change Traditional Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('scatter_traditional_boyss_names3.pdf')
plt.show()


#___________________________________________________________________________________
#source= ColumnDataSource(fnames_pctchange)
# plot=figure()
#plot.vbar(y='Mary' top='top', width= 0.5, source=source, legend='Counts')

# plot.legend.location='top_right'
# hover = HoverTool(tooltips=[('Name', '@Name')])
# plot = figure(tools=[hover, 'pan'])
# plot.add_tools(hover)
# output_file('hover.html')
#show(plot)
