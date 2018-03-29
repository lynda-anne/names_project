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
print('INSPECT NAMES')
print(len(df))
print(df[0].head)
print(df[0].info())

# Add column names
i=0
n = 1880
for item in df :
    df[i].columns =  ['Name', 'Sex', 'Count']
    #print(df[i].info())
    df[i]['Year']= n
    i= i  + 1
    n= n + 1

#Concatenate the list of dataframes into one dataframe
names= pd.concat(df)
print('CONCATENTATED NAMES DATAFRAME')
print(names.info())

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
names2['prop_births']= names2['Count']/total_births_by_year
print('NAMES DATAFRAME WITH PROP BIRTHS ADDED')
print(names2.tail())
print(names2.shape)
#_______________________________________________________________________________
#create dataframe with female names
female = names2['Sex'] == 'F'
names_f= names2[female]
print('FEMALE NAME DATAFRAME')
print(names_f.tail())
#Select top 5 female names for each year
top5_f= names_f.groupby('Year').head()
top5_female= top5_f.reset_index()
del top5_female['index']
del top5_female['Sex']
del top5_female['Count']
top5_fnames= top5_female.set_index('Name')
print('TOP 5 FEMALE NAMES')
print(top5_fnames.head())

# #Pivot the dataframe to make years columns
top5_fnames_tidy = top5_fnames.pivot_table(values='prop_births', index=['Name'], columns=['Year'])
top5_fnames_tidy = top5_fnames_tidy.fillna(0)

top5_fnames_tidy= top5_fnames_tidy.reset_index()

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
#Create dataframe with males names
names_m = names2['Sex'] == 'M'
names_m= names2[names_m]
print('MALE NAME DATAFRAME')
print(names_m.tail())
#Select top 5 male names for each year
top5_m= names_m.groupby('Year').head()
top5_male= top5_m.reset_index()
del top5_male['index']
del top5_male['Sex']
del top5_male['Count']
top5_mnames= top5_male.set_index('Name')
print('TOP 5 MALE NAMES')
print(top5_male.head())
# #Pivot the dataframe to make years columns
top5_mnames_tidy = top5_mnames.pivot_table(values='prop_births', index=['Name'], columns=['Year'])
top5_mnames_tidy = top5_mnames_tidy.fillna(0)
top5_mnames_tidy= top5_mnames_tidy.reset_index()
print('TOP 5 MALE NAMES, PIVOTED')
print(top5_mnames_tidy.head())
print(top5_mnames_tidy.tail())
print(top5_mnames_tidy.info())
#_____________________________________________________________________
#create 'tidy' dataframe for boys names
top5_mnames_tidy= top5_mnames_tidy.set_index('Name')
df=[]
n= 0
for item in top5_mnames_tidy :
    if n <= 24 :
        top5m_by_year= top5_mnames_tidy.iloc[n]
        df.append(top5m_by_year)
        n = n + 1
top5_mnames= pd.concat(df, axis=1)
top5_mnames= top5_mnames.reset_index()

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
plt.title('Top 5 Boys Names')
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
#Review dataframe with only female names
print('REVIEW OF FEMALE NAME DATAFRAME')
print(names_f.info())
print(names_f.head())
#create a list frequent female names
dupf= names_f.groupby('Name').sum()
freq_f = dupf['prop_births'] >= 0.1
common_f= dupf[freq_f]
common_f= common_f.reset_index()
common_fnames= common_f['Name']
freq_fnames= common_fnames.tolist()

#set fnames index to Name and pull out the common names
fnames= names_f.set_index('Name')
common_girls= fnames.loc[freq_fnames]
common_df= common_girls.reset_index()
print('COMMON FEMALE NAMES')
print(common_df.head())
print(common_df.info())
#
# #Pivot the dataframe to make years columns
fnames_tidy = common_df.pivot_table(values='prop_births', index=['Name'], columns=['Year'])
fnames_tidy = fnames_tidy.fillna(0)
print('COMMON FEMALE NAMES, PIVOTED')
print(fnames_tidy.head())
print(fnames_tidy.info())
fnames_tidy['Total']= fnames_tidy.sum(axis=1)
fnames_tidy= fnames_tidy.sort_values(by= 'Total', ascending= False)

#Select very popular female names
top10_fnames= fnames_tidy[0:9]
top10_fnames= top10_fnames.reset_index()

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
plt.ylabel('Proportion of Names')
plt.title('Top 10 Traditional Girls Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('bar_top10_traditional_girls_names.pdf')
plt.show()

# #Calulate % change of name popularity top 10 girls names
del top10_fnames['Total']
top10_fnames= top10_fnames.set_index('Name')
top10_fnames_chg = top10_fnames.apply('pct_change', axis=1)*100
pd.set_option('use_inf_as_na', True)
top10_fnames_chg= top10_fnames_chg.replace(np.inf, 0)
top10_fnames_chg= top10_fnames_chg.fillna(0)
del top10_fnames_chg[1880]
top10_fnames_chg = top10_fnames_chg.reset_index()
print('TOP 10 COMMON FEMALE NAMES')
print(top10_fnames.head())

#Create dataframe of the top 10 Traditional girls names
top10_fnames_chg= top10_fnames_chg.set_index('Name')
df=[]
n= 0
for item in top10_fnames_chg :
    if n <= 8 :
        f_by_year= top10_fnames_chg.iloc[n]
        df.append(f_by_year)
        n = n + 1
fnames= pd.concat(df, axis=1)
fnames= fnames.reset_index()

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
#review dataframe with males names
print('REVIEW OF MALE NAMES DATAFRAME')
print(names_m.info())
print(names_m.head())
#create a list frequent male names
dupm= names_m.groupby('Name').sum()
freq_m = dupm['prop_births'] >= 0.1
common_m= dupm[freq_m]
common_m= common_m.reset_index()
common_mnames= common_m['Name']
freq_mnames= common_mnames.tolist()

#set names_m index to Name and pull out the common names
names_m= names_m.set_index('Name')
common_boys= names_m.loc[freq_mnames]
common_dm= common_boys.reset_index()
print('COMMON MALE NAMES')
print(common_dm.head())
print(common_dm.info())
#
# #Pivot the dataframe to make years columns
mnames_tidy = common_dm.pivot_table(values='prop_births', index=['Name'], columns=['Year'])
mnames_tidy = mnames_tidy.fillna(0)
print('COMMON MALE NAMES, PIVOTED')
print(mnames_tidy.head())
print(mnames_tidy.info())
#
mnames_tidy['Total']= mnames_tidy.sum(axis=1)
mnames_tidy= mnames_tidy.sort_values(by= 'Total', ascending= False)

#Select very popular male names
top10_mnames= mnames_tidy[0:9]
top10_mnames= top10_mnames.reset_index()

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
plt.ylabel('Proportion of Names')
plt.title('Top 10 Traditional Boys Names')
plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
plt.margins(0.1)
plt.savefig('bar_top10_traditional_boys_names.pdf')
plt.show()

# #Calulate % change of name popularity top 10 girls names
del top10_mnames['Total']
top10_mnames= top10_mnames.set_index('Name')
top10_mnames_chg = top10_mnames.apply('pct_change', axis=1)*100
pd.set_option('use_inf_as_na', True)
top10_mnames_chg= top10_mnames_chg.replace(np.inf, 0)
top10_mnames_chg= top10_mnames_chg.fillna(0)
del top10_mnames_chg[1880]
top10_mnames_chg = top10_mnames_chg.reset_index()
print(top10_mnames_chg.info())
print(top10_mnames_chg.head())

#Create dataframe of the top 10 Traditional boys names
top10_mnames_chg= top10_mnames_chg.set_index('Name')
dm=[]
n= 0
for item in top10_mnames_chg :
    if n <= 8 :
        m_by_year= top10_mnames_chg.iloc[n]
        dm.append(m_by_year)
        n = n + 1
mnames= pd.concat(dm, axis=1)
mnames= mnames.reset_index()

#plot %Change of top 10 Traditional boys names
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
plt.savefig('scatter_traditional_boys_names3.pdf')
plt.show()

#_______________________________________________________________________________

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
