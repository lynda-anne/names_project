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
# print('INSPECT NAMES')
# print(len(df))
# print(df[0].head)
# print(df[0].info())

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
# print('CONCATENTATED NAMES DATAFRAME')
# print(names.info())

names2 = names.copy()
total_births_by_year = names2.groupby('Year')['Count'].transform('sum')
names2['pct_name']= (names2['Count']/total_births_by_year)* 100
print('NAMES DATAFRAME WITH PCT NAME ADDED')
# print(names2.tail())
# print(names2.shape)

#create dataframe with female names
female = names2['Sex'] == 'F'
names_f= names2[female]
print('FEMALE NAME DATAFRAME')
# print(names_f.tail())

fnames_year= names_f.set_index('Year')
print(fnames_year.tail())

fnames_2000_2016= fnames_year.loc[2000:2016]
del fnames_2000_2016['Sex']
del fnames_2000_2016['Count']
fnames_2000_2016.groupby('Name')
# print(fnames_2000_2016[100:130])
# print(fnames_2000_2016.info())

top= sum(fnames_2000_2016['pct_name'] >= 0.25 )
# print(top)

top= fnames_2000_2016['pct_name'] >= 0.25
top_fnames_21st_cent= fnames_2000_2016[top]
top_fnames_21st_cent= top_fnames_21st_cent.reset_index()
# print('TOP FEMALE NAME DATAFRAME')
# print(top_fnames_21st_cent.tail())
# print(top_fnames_21st_cent.shape)
# print(top_fnames_21st_cent.info())

fnames_2000_2016_tidy = top_fnames_21st_cent.pivot_table(values='pct_name', index=['Year'], columns=['Name'])
fnames_2000_2016_tidy = fnames_2000_2016_tidy.fillna(0)
fnames_2000_2016_tidy= fnames_2000_2016_tidy.reset_index()
## fnames_2000_2016_tidy= fnames_2000_2016_tidy.data_sort()
print(fnames_2000_2016_tidy.tail())
print(fnames_2000_2016_tidy.info())
# print(top_fnames_21st_cent.tail())
# print(top_fnames_21st_cent.info())
# print(top_fnames_21st_cent['Name'].drop_duplicates())

# print(fnames_2000_2016_tidy['Year'])
# print(fnames_2000_2016_tidy.iloc[:, 8 ])
    # colors=['red', 'blue', 'green', 'orange', 'yellow', 'lime', 'indigo', 'cyan', 'deeppink', 'peru', 'midnightblue', 'teal', 'gray' ]

def top_girls_names_1():
    colors=['red', 'blue', 'lime', 'deeppink']
    n=1
    for item in fnames_2000_2016_tidy :
        if n <= 4 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 1 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names1.pdf')
    plt.show()

def top_girls_names_2():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 5
    for item in fnames_2000_2016_tidy :
        if n <= 8 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 2 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names2.pdf')
    plt.show()

def top_girls_names_3():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 9
    for item in fnames_2000_2016_tidy :
        if n <= 12 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 3 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names3.pdf')
    plt.show()

def top_girls_names_4():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 13
    for item in fnames_2000_2016_tidy :
        if n <= 16 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 4 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names4.pdf')
    plt.show()

def top_girls_names_5():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 17
    for item in fnames_2000_2016_tidy :
        if n <= 20 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 5 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names5.pdf')
    plt.show()

def top_girls_names_6():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 21
    for item in fnames_2000_2016_tidy :
        if n <= 24 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 6 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names6.pdf')
    plt.show()

def top_girls_names_7():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 25
    for item in fnames_2000_2016_tidy :
        if n <= 28 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 7 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names7.pdf')
    plt.show()

def top_girls_names_8():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 29
    for item in fnames_2000_2016_tidy :
        if n <= 32 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 8 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names8.pdf')
    plt.show()

def top_girls_names_9():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 33
    for item in fnames_2000_2016_tidy :
        if n <= 36 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 9 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names9.pdf')
    plt.show()

def top_girls_names_10():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 37
    for item in fnames_2000_2016_tidy :
        if n <= 39 :
            x= fnames_2000_2016_tidy['Year']
            y = fnames_2000_2016_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)
    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 10 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_girls_names10.pdf')
    plt.show()

# top_girls_names_1()
# top_girls_names_2()
# top_girls_names_3()
# top_girls_names_4()
# top_girls_names_5()
# top_girls_names_6()
# top_girls_names_7()
# top_girls_names_8()
# top_girls_names_9()
# top_girls_names_10()


names= top_fnames_21st_cent['Name'].drop_duplicates()
# print(names)

fnames_year= fnames_year.reset_index()
fnames_year= fnames_year.set_index('Name')
tops= fnames_year.loc[names]

del tops['Sex']
del tops['Count']
# tops_group= tops.groupby('Name')

tops=tops.reset_index()


tops_group_tidy = tops.pivot_table(values='pct_name', index=['Year'], columns=['Name'])
tops_group_tidy = tops_group_tidy.fillna(0)
tops_group_tidy= tops_group_tidy.reset_index()

print(tops_group_tidy.info())
print(tops_group_tidy.head())

def tops_years1():
    colors=['red', 'blue', 'lime', 'deeppink']
    n=1
    for item in tops_group_tidy :
        if n <= 4 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 1 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names1.pdf')
    plt.show()

def tops_years2():
    colors=['red', 'blue', 'lime', 'deeppink']
    n=5
    for item in tops_group_tidy :
        if n <= 8 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 2 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names2.pdf')
    plt.show()

def tops_years3():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 9
    for item in tops_group_tidy :
        if n <= 12 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 3 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names3.pdf')
    plt.show()

def tops_years4():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 13
    for item in tops_group_tidy :
        if n <= 16 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 4 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names4.pdf')
    plt.show()

def tops_years5():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 17
    for item in tops_group_tidy :
        if n <= 20 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 5 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names5.pdf')
    plt.show()

def tops_years6():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 21
    for item in tops_group_tidy :
        if n <= 24 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 6 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names6.pdf')
    plt.show()

def tops_years7():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 25
    for item in tops_group_tidy :
        if n <= 28 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
    # plt.xticks(rotation='vertical')
    # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 7 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names7.pdf')
    plt.show()

def tops_years8():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 29
    for item in tops_group_tidy :
        if n <= 32 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
        # plt.xticks(rotation='vertical')
        # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 8 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names8.pdf')
    plt.show()


def tops_years9():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 32
    for item in tops_group_tidy :
        if n <= 35 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
        # plt.xticks(rotation='vertical')
        # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 9 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names9.pdf')
    plt.show()

def tops_years10():
    colors=['red', 'blue', 'lime', 'deeppink']
    n= 36
    for item in tops_group_tidy :
        if n <= 39 :
            x= tops_group_tidy['Year']
            y = tops_group_tidy.iloc[0:, n]
            plt.style.use('ggplot')
            plt.scatter(x, y)
            n= n + 1
        # plt.xticks(rotation='vertical')
        # plt.xlim(2009, 2018)

    plt.ylim(-0.05, 0.7)
    plt.subplots_adjust(left=0.1)
    plt.ylabel('Pecent of Names')
    plt.title('Top Girls Names Chart 10 of 10')
    plt.legend(loc='best', fontsize='xx-small', markerscale=0.7)
    plt.margins(0.2)
    plt.savefig('scatter_top_g_names10.pdf')
    plt.show()


tops_years1()
tops_years2()
tops_years3()
tops_years4()
tops_years5()
tops_years6()
tops_years7()
tops_years8()
tops_years9()
tops_years10()

# #______tops_years4()
# _________________________________________________________________________
# #
