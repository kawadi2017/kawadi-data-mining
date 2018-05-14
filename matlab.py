import matplotlib.pyplot as plt
import csv,json,random
from random import randint
from datetime import datetime
import pandas as pd


class Waste:
    def __init__(
        self,address,sourceId,sourceLat,sourceLon,sourceStatus,sourceType,distance,duration,timeStamp,sourceWeight,amount):
        self.address=address
        self.sourceId=sourceId
        self.lat=sourceLat
        self.lon=sourceLon
        self.sourceStatus=sourceStatus
        self.sourceType=sourceType
        self.distance=distance
        self.duration=duration
        self.timeStamp=timeStamp
        self.sourceWeight=sourceWeight
        self.amount=amount

class DataMining:
    slices=[]

    def randomData(self):
        districts=[]
        wasteContainer=[]
        status=['completed','Ongoing','NotStarted'] #labels on the chart
        types=['school','office','home','hospital','park','restaurant','college','university','lakeside','private hostel','government offices','factory','temples']
        with open('./nepal_districts.csv','r',encoding='utf-8') as file:
            reader=csv.DictReader(file)
            for row in reader:
                districts.append(row)

        print(districts[randint(0,74)]['District'])
        for index in range(0,100000):
            year = randint(2000,2019)
            month=randint(1,12)
            days=randint(1,28)
            date=datetime(year,month,days).strftime('%Y-%m-%d')


            each =Waste(
                districts[randint(0,74)]['District'],
                index,None,None,status[randint(0,2)],
                types[randint(0,len(types)-1)],
                randint(20,12000),
                randint(1,1000),
                year,
                randint(1,20),
                randint(200,400)
                )
            wasteContainer.append(each)

        wasteContainerJsonString=json.dumps([ob.__dict__ for ob in wasteContainer])
        wasteContainer=json.loads(wasteContainerJsonString)

        # convert to csv in the format
        with open('./wastes.csv','w') as file:
            writer=csv.writer(file)
            #write each row
            writer.writerow(wasteContainer[0].keys())#get the headers
            for eachwaste in wasteContainer:
                writer.writerow(eachwaste.values())#prints the value as per the header

        counter=pd.read_csv('./wastes.csv')
        print(counter['sourceStatus'].value_counts())
        slices=counter['sourceStatus'].value_counts()
        self.slices=slices
        print(counter['sourceType'].value_counts())

            
        
    def piechart(self):
        activities=['completed','ongoing','no started'] #labels on the chart
        colors=['r','g','b'] #color range for each
        plt.pie(self.slices,labels=activities,colors=colors,startangle=90,shadow=False,explode=(0,0,0.0),radius=1.5,autopct='%0.3f%%')
        #activity[0] starts from 90 and goes anticlockwise
        #shadow is just the highlights accross the borders
        #radius of the pie
        #autopct is auto percentage with5 decimal places to display
        plt.legend()
        plt.show()


    def linePltAmountSum(self):
        data=pd.read_csv('./wastes.csv')
        fig, ax = plt.subplots(figsize=(15,7))
        ax.set_xlabel('Date')
        ax.set_ylabel('Amounts')
        data.groupby(['timeStamp','sourceType']).sum()['amount'].unstack().plot(ax=ax)
        plt.show()

    def linePltDurationSum(self):
        data=pd.read_csv('./wastes.csv')
        fig, ax = plt.subplots(figsize=(15,7))
        ax.set_xlabel('Date')
        ax.set_ylabel('Total duration in the years')
        data.groupby(['timeStamp','sourceType']).sum()['duration'].unstack().plot(ax=ax)
        plt.show()

    def linePltDistanceSum(self):
        data=pd.read_csv('./wastes.csv')
        fig, ax = plt.subplots(figsize=(15,7))
        ax.set_xlabel('Date')
        ax.set_ylabel('Total distance travelled in the years')
        data.groupby(['timeStamp','sourceType']).sum()['distance'].unstack().plot(ax=ax)
        plt.show()

    def districtHistogram(self):
        data=pd.read_csv('./wastes.csv')
        fig, ax = plt.subplots(figsize=(15,7))
        ax.set_xlabel('Date')
        ax.set_ylabel('Total distance travelled in the years')
        data.groupby(['timeStamp','address']).sum()['amount'].plot(ax=ax)
        plt.show()





#start the programs
datamining=DataMining()
datamining.randomData()
datamining.piechart()#piechart

#lineplots
datamining.linePltAmountSum()
datamining.linePltDistanceSum()
datamining.linePltDurationSum()










