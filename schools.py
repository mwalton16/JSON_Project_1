"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""

### Imports
import json
import csv
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

### Opening the JSON File
open_file_univ = open('univ.json','r')
univ_data = json.load(open_file_univ)

### Creating the Lists of Schools the Map will Use
university_list = []
for i in univ_data:
    conference_ID = i['NCAA']["NAIA conference number football (IC2020)"]
    if conference_ID == 102 or conference_ID == 107 or conference_ID == 108 or conference_ID == 127 or conference_ID == 130:
        university_list.append(i)

# check to see if list is complete
#for i in range(len(university_list)):
#    print(university_list[i]['instnm'])

### Map 1
size1, longitude1, latitude1,hovertext1 = [],[],[],[]
for i in university_list:
    if i["Graduation rate  women (DRVGR2020)"] > 50:
        school_name_1 =i['instnm']
        grad_rate_women_1 =i["Graduation rate  women (DRVGR2020)"]
        latitude1.append(i["Latitude location of institution (HD2020)"])
        longitude1.append(i["Longitude location of institution (HD2020)"])
        size_1 = 0.0005* i["Total  enrollment (DRVEF2020)"]
        size1.append(size_1)
        hovertext1.append(f"{school_name_1}, {grad_rate_women_1}%")

### Map 2
size2, longitude2, latitude2, hovertext2 = [],[],[],[]
for i in university_list:
    if i["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
        school_name_2 =i['instnm']
        enrollment_African_American =i["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        latitude2.append(i["Latitude location of institution (HD2020)"])
        longitude2.append(i["Longitude location of institution (HD2020)"])
        size_2 = 0.0005* i["Total  enrollment (DRVEF2020)"]
        size2.append(size_2)
        hovertext2.append(f"{school_name_2}, {enrollment_African_American}%")  

### Map 3
size3, longitude3, latitude3, hovertext3 = [],[],[],[]
for i in university_list:
    try:
        in_state_tuition = int(i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
    except TypeError:
        continue
    else:
        if in_state_tuition > 50000:
            school_name_3 =i['instnm']
            latitude3.append(i["Latitude location of institution (HD2020)"])
            longitude3.append(i["Longitude location of institution (HD2020)"])
            size_3 = 0.0005* i["Total  enrollment (DRVEF2020)"]
            size3.append(size_2)
            hovertext2.append(f"{school_name_3}, {in_state_tuition}%")

### Plotting the Data
figure_data_1 = [
    {
        'type': 'scattergeo','lat': latitude1,'lon': longitude1,'text': hovertext1,
        'marker' : {'size':  size1,'color': "blue",'colorscale': 'Viridis','reversescale': True,
        },
    }]

figure_layout_1 = Layout(title = 'Colleges and Universities with More than 50% of Female Students Graduating')

fig_1 = {'data':figure_data_1, 'layout': figure_layout_1} 

offline.plot(fig_1, filename= 'women_graduation_at_least_half.html')

figure_data_2 = [
    {
        'type': 'scattergeo','lat': latitude2,'lon': longitude2,'text': hovertext2,
        'marker' : {'size':  size2,'color': "blue",'colorscale': 'Viridis','reversescale': True,
        },
    }]

figure_layout_2 = Layout(title = 'Percent of Students Enrolled that are Black/African-American')

fig_2 = {'data': figure_data_2, 'layout': figure_layout_2} 

offline.plot(fig_2, filename= 'black_enrollment.html')

figure_data_3 = [
    {
        'type': 'scattergeo','lat': latitude3,'lon': longitude3,'text': hovertext3,
        'marker' : {'size':  size3,'color': "blue",'colorscale': 'Viridis','reversescale': True, 
        },
    }]

figure_layout_3 = Layout(title = 'Tuition Cost for In-State Students Off Campus If Above $50,000')

fig_3 = {'data': figure_data_3, 'layout': figure_layout_3}
offline.plot(fig_3, filename= 'tuition_cost_is_oc_50k.html')