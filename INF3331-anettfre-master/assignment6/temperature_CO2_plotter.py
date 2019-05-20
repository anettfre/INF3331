import pandas as pd
import matplotlib.pyplot as plt
import sys

'''
Liker denne løsningen, her er det mye bra. Jeg gjorde ting litt annerledes ved at jeg
tok inn input til funksjonenen fra kommandolinjen, men det er jo bare personlig preferanse.
Det gjør det litt enklere å teste flere løsninger, man slipper å endre på det som er hardkodet.
'''

def plot_co2(time_range=None, y_axis=None):
    """Plots the co2 from co2.csv with optional changes.


    Arguments:
        - time_range: Time from and to for the plot.
        - y_axis: min and max for y axis.
    """
    co2_read = pd.read_csv('co2.csv', sep=',')

    if time_range != None:
        start_year = abs(time_range[0]-co2_read["Year"].loc[0])
        end_year = abs(time_range[1]-co2_read["Year"].loc[0])
        co2_read = co2_read.loc[start_year:end_year]
        co2_read.plot(x='Year', y='Carbon', ylim=y_axis)

    else:
        co2_read.plot(x='Year', y='Carbon', ylim=y_axis)
    plt.savefig('static/co2.jpg')
    plt.show()


def plot_temperature(month="May", time_range=None, y_axis=None):
    """Plots the temperature from temperature.csv with optional changes.
    If no month is given as input January is selected.

    Arguments:
        -month: Month to use in the plot.
        -time_range: Time from and to for the plot.
        -y_axis: min and max for y axis.
    """
    temp_read = pd.read_csv('temperature.csv', sep=',')
    if time_range != None:
        start_year = abs(time_range[0]-temp_read["Year"].loc[0])
        end_year = abs(time_range[1]-temp_read["Year"].loc[0])
        temp_read = temp_read[[month, "Year"]].loc[start_year:end_year]
        temp_read.plot(x='Year', y='Carbon', ylim=y_axis)
    else:
        temp_read.plot(x='Year', y=month, ylim=y_axis)
    plt.savefig('static/temperature.jpg')
    plt.show()

if __name__ == '__main__':
    plot_co2()
    plot_temperature()
