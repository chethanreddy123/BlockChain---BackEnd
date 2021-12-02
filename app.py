from flask import Flask, app, request, jsonify
import json
from itertools import permutations
from itertools import combinations
import os

import flask
app = Flask(__name__)

@app.route('/index' , methods = ['GET' ,'POST'])
@cross_origin()
def index():

    value = request.json
    # value
    a = value["Slot"]

    Crc = list(value["CourseList"])

    


    MorE = a
    NoC = len(list((Crc)))
    LC = []
    LL = []

    

    for i in range(NoC):
        c = Crc[i]
        LC.append(c)

    with open("fall21data.json") as json_file:
        data = json.load(json_file)

    for i in data:
        if i['ctype'] == 'LO' and i['crcode'] in LC:
            LL.append(i['crcode'])
            LC.remove(i['crcode'])

    A1 , B1, C1, D1, E1, F1, G1 = [] , [] , [] , [] , [] , [] , []
    A2 , B2, C2, D2, E2, F2, G2 = [] , [] , [] , [] , [] , [] , []

    MS = ['A1' , 'B1', 'C1', 'D1', 'E1', 'F1', 'G1']
    ES = ['A2' , 'B2', 'C2', 'D2', 'E2', 'F2', 'G2']

    LabCourses = []
    LabCount = 0

    for Course in data :
        if MorE == "Morning":
            if Course['crcode'] in LC or Course['crcode'] in LL:
                if 'A1' in Course['slot'] : A1.append(Course)
                if 'B1' in Course['slot'] : B1.append(Course)
                if 'C1' in Course['slot'] : C1.append(Course)
                if 'D1' in Course['slot'] : D1.append(Course)
                if 'E1' in Course['slot'] : E1.append(Course)
                if 'F1' in Course['slot'] : F1.append(Course)
                if 'G1' in Course['slot'] : G1.append(Course)
                if 'L'  in Course['slot'] : 
                    val = Course['slot'][1:3]
                    if val.isdigit() :
                        if int(val) in list(range(31,61)): 
                            LabCourses.append(Course) 
                            LabCount += 1


        if MorE == "Evening":
            if Course['crcode'] in LC or Course['crcode'] in LL:
                if 'A2' in Course['slot'] : A2.append(Course)
                if 'B2' in Course['slot'] : B2.append(Course)
                if 'C2' in Course['slot'] : C2.append(Course)
                if 'D2' in Course['slot'] : D2.append(Course)
                if 'E2' in Course['slot'] : E2.append(Course)
                if 'F2' in Course['slot'] : F2.append(Course)
                if 'G2' in Course['slot'] : G2.append(Course)
                if 'L'  in Course['slot'] :
                    S1 = Course['slot'][1:3]
                    S2 = Course['slot'][1:2]
                    if S1.isdigit():
                        if int(S1) in list(range(1,31)): 
                            LabCourses.append(Course)
                            LabCount += 1     
                    elif S2.isdigit():
                        if int(S2) in list(range(1,31)): 
                            LabCourses.append(Course)
                            LabCount += 1

    LF = []
    LabCount = 0

    for i in LC :
        flage = False
        for j in data:
            if j['crcode'] == i and flage == False and 'L' in j['slot']:
                LabCount += 1
                LF.append(j['crcode'])
                flage = True

    LabCount += len(LL)
    LF = LF + LL

    Len1 = len(MS)
    Len2 = len(LC)

    for i in range(Len1-Len2):
        LC.append("NULL")

    AllCourseTracks = list(permutations(LC))

    NewAllCourseTracks = []


    n = len(AllCourseTracks)
    for i in AllCourseTracks:
        if i not in NewAllCourseTracks:
            NewAllCourseTracks.append(i)

    AllPossible = []

    if MorE == "Morning":
    
        for CourseTrack in NewAllCourseTracks:
            CheckList = [A1 , B1, C1, D1, E1, F1, G1]
            MyList = [False for i in CourseTrack]
            CurPath = []
            count = 0
        
            for i,j in zip(CourseTrack,CheckList):
                MakeList = [k['crcode'] for k in j]
                if i == "NULL":
                    MyList[count] = True
                    CurPath.append("NULL")
                else:
                    if i in MakeList:
                        val = None
                        for f in j:
                            if i == f['crcode'] and val == None:
                                val = f
                        MyList[count] = True
                        CurPath.append(val)
                count += 1
            
            
            if all(MyList):
                CurPath.remove('NULL')
                Temp = []
                for i in CurPath:
                    if i != "NULL":
                        Temp.append(i)
                AllPossible.append(Temp)

    if MorE == "Evening":
    
        for CourseTrack in NewAllCourseTracks:
            CheckList = [A2 , B2, C2, D2, E2, F2, G2]
            MyList = [False for i in CourseTrack]
            CurPath = []
            count = 0
        
            for i,j in zip(CourseTrack,CheckList):
                MakeList = [k['crcode'] for k in j]
            
                if i == "NULL":
                    MyList[count] = True
                    CurPath.append("NULL")
                else:
                    if i in MakeList:
                        val = None
                        for f in j:
                            if i == f['crcode'] and val == None:
                                val = f
                        MyList[count] = True
                        CurPath.append(val)         
                count += 1

            if all(MyList):
                CurPath.remove('NULL')
                Temp = []
                for i in CurPath:
                    if i != "NULL":
                        Temp.append(i)
                AllPossible.append(Temp)

    NewList = []
    
    AllLabSort = []
    
    for k in AllPossible:
        for i in k:
            for j in LabCourses:

                if i['ename'] == j['ename'] and i['crcode'] == j['crcode']:

                    NewList.append(j)
    
        for LabCourse in LabCourses:
            if LabCourse['slot'].count('L') > 4 :
                NewList.append(LabCourse)
            
        F = NewList.copy()
            
        AllLabSort.append(F)

    
        NewList.clear()

    count = 0

    def CheckAllVal(Mylist, LF):
        Flage = True
    
        for i in LF:
            if i not in [h['crcode'] for h in Mylist]:
                Flage = False
        if Flage == True:
            return True
        else :
            return False

    FinalLabList = []
    
    for i in AllLabSort:
        CurrLabList = list(combinations(i, len(LF)))
        for j in CurrLabList :
            if CheckAllVal(j , LF) == True :
                FinalLabList.append((j , count))
        count+=1
    
    

    def CheckList(List):
        for i in range(len(List)) :
            for j in range(len(List)):
                if i!=j and List[i]['slot'] in List[j]['slot']:
                    return False
        return True

    FFList = []
    val = 0
    
    AllPathsofLab = []  
    LabPaths = []
    
    for i in FinalLabList :
    
        if CheckList(i[0]) == True:
            FFList = i[0]
            AllPathsofLab.append(i[1])
            LabPaths.append(FFList)
        

        
    SuperFinalList = []

    count = 0

    for i in AllPathsofLab:
        if i >= len(AllPossible):
            break
        else:
            SuperFinalList.append(list(LabPaths[count])+list(AllPossible[i]))
        count += 1

    
    # print(SuperFinalList)

    FinalAnswer = flask.jsonify({"ListOfListOfCourses" : SuperFinalList})


    return FinalAnswer



if __name__ == '__main__':
    #app.run( debug = True )
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
