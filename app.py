import itertools
from flask import Flask, app, request, jsonify
import json
from itertools import permutations
from itertools import combinations
import os
from flask_cors import CORS, cross_origin

# Importing Modules

import flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/index', methods=['GET', 'POST'])
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

    with open("WinterSem22Updated1.json") as json_file:
        data = json.load(json_file)

    for i in data:
        if i['slot'].count('L') > 3 and i['crcode'] in LC:
            LL.append(i['crcode'])
            LC.remove(i['crcode'])

    A1, B1, C1, D1, E1, F1, G1 = [], [], [], [], [], [], []
    A2, B2, C2, D2, E2, F2, G2 = [], [], [], [], [], [], []

    MS = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1']
    ES = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2']

    LabCourses = []
    LabCount = 0
    LabOnlyCourses = []

    for Course in data:
        if MorE == "Morning":
            if Course['crcode'] in LC or Course['crcode'] in LL:
                if 'A1' in Course['slot']:
                    A1.append(Course)
                if 'B1' in Course['slot']:
                    B1.append(Course)
                if 'C1' in Course['slot']:
                    C1.append(Course)
                if 'D1' in Course['slot']:
                    D1.append(Course)
                if 'E1' in Course['slot']:
                    E1.append(Course)
                if 'F1' in Course['slot']:
                    F1.append(Course)
                if 'G1' in Course['slot']:
                    G1.append(Course)
                if 'L' in Course['slot']:
                    val = Course['slot'][1:3]
                    if val.isdigit():
                        if int(val) in list(range(31, 61)):
                            LabCourses.append(Course)
                            if Course['slot'].count('L') > 3:
                                LabOnlyCourses.append(Course)
                                LabCount += 1

        if MorE == "Evening":
            if Course['crcode'] in LC or Course['crcode'] in LL:
                if 'A2' in Course['slot']:
                    A2.append(Course)
                if 'B2' in Course['slot']:
                    B2.append(Course)
                if 'C2' in Course['slot']:
                    C2.append(Course)
                if 'D2' in Course['slot']:
                    D2.append(Course)
                if 'E2' in Course['slot']:
                    E2.append(Course)
                if 'F2' in Course['slot']:
                    F2.append(Course)
                if 'G2' in Course['slot']:
                    G2.append(Course)
                if 'L' in Course['slot']:
                    S1 = Course['slot'][1:3]
                    S2 = Course['slot'][1:2]
                    if S1.isdigit():
                        if int(S1) in list(range(1, 31)):
                            LabCourses.append(Course)
                            LabCount += 1
                            if Course['slot'].count('L') > 3:
                                LabOnlyCourses.append(Course)
                                LabCount += 1
                    elif S2.isdigit():
                        if int(S2) in list(range(1, 31)):
                            LabCourses.append(Course)
                            LabCount += 1
                            if Course['slot'].count('L') > 3:
                                LabOnlyCourses.append(Course)
                                LabCount += 1

    LF = []

    LabCount = 0
    for i in LC:
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

    AllCourseTracks = list(permutations(LC))  # ALL PATHS

    NewAllCourseTracks = []  # Final All paths

    n = len(AllCourseTracks)
    for i in AllCourseTracks:
        if i not in NewAllCourseTracks:
            NewAllCourseTracks.append(i)

    AllPossible = []

    if MorE == "Morning":

        for CourseTrack in NewAllCourseTracks:
            CheckList = [A1, B1, C1, D1, E1, F1, G1]
            MyList = [False for i in CourseTrack]
            CurPath = []
            count = 0

            for i, j in zip(CourseTrack, CheckList):
                if i == "NULL":
                    MyList[count] = True
                    CurPath.append("NULL")
                else:
                    if i in [m['crcode'] for m in j]:
                        val = []
                        for f in j:
                            if i == f['crcode']:
                                val.append(f)
                        MyList[count] = True
                        CurPath.append(val)
                        # print(CurPath)
                count += 1
            # print(MyList)

            if all(MyList):

                # CurPath.remove('NULL')
                Temp = []
                for i in CurPath:
                    if i != "NULL":
                        Temp.append(i)
                AllPossible.append(Temp)

    if MorE == "Evening":

        for CourseTrack in NewAllCourseTracks:
            CheckList = [A2, B2, C2, D2, E2, F2, G2]
            MyList = [False for i in CourseTrack]
            CurPath = []
            count = 0

            for i, j in zip(CourseTrack, CheckList):
                Fal = False
                if i == "NULL":
                    MyList[count] = True
                    CurPath.append("NULL")
                else:
                    if i in [m['crcode'] for m in j]:
                        val = []
                        for f in j:
                            if i == f['crcode']:
                                if i == f['crcode']:
                                    val.append(f)

                        MyList[count] = True
                        CurPath.append(val)
                count += 1

            if all(MyList):
                # CurPath.remove('NULL')
                Temp = []
                for i in CurPath:
                    if i != "NULL":
                        Temp.append(i)
                AllPossible.append(Temp)

    AllPaths = []

    for i in AllPossible:
        EachPossible = list(itertools.product(*i))
        for j in EachPossible:
            AllPaths.append(j)

    count = 0

    SuperFinalList = []

    for i in AllPaths:
        TempList = []
        for j in i:
            for k in LabCourses:
                if k['crcode'] == j['crcode'] and k['ename'] == j['ename']:
                    TempList.append(k)

        # print(TempList)

        LabCombo = list(combinations(LabOnlyCourses, len(LL)))
        for b in LabCombo:
            flage = True
            hen = []
            hen = TempList.copy()
            hen = hen + list(b)
            for l in range(len(hen)):
                for m in range(len(hen)):
                    if l != m and hen[l]['slot'] in hen[m]['slot']:
                        flage = False
            if flage == True:
                if count < 100:
                    SuperFinalList.append(list(i) + hen)
                    count += 1
                else:
                    break


# print(SuperFinalList)

    FinalAnswer = flask.jsonify({"ListOfListOfCourses": SuperFinalList})

    return FinalAnswer


if __name__ == '__main__':
    #app.run( debug = True )
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
