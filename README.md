# FFCS-Planner-Python
## Auto Slot Picker
An Algorithm that makes a VIT time table [ Auto Slot Picker](https://ffcs.vitrendz.com/)

### Problem Statement:
> Every College got it's own way of giving the courses to students but Vellore Institute of Technology - Vellore has a unique system for allotting courses to students called Fully Flexible credit system [FFCS](https://vit.ac.in/academics/ffcs "FFCS").
> The problem with this is there many subjects and a lot faculty members allotted to each subject and only limit slots available for selecting the subjects, students use to struggle a lot to select the courses without clashes of the subjects.

### Solution:
> The possible solution is that we make a 3D graph Data Structure where Slots, Subjects and faculty members are each dimension of the 3D graph:
![This is an image](https://miro.medium.com/max/1050/0*BEvnN1fOYyIotaw1.jpg)
> Now we just have to apply [DFS](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/) algorithm to travel to all the nodes and check whether there exists a path with given courses by the user and returing the all the possible paths with no clashes.
> As the Data Set is not that big we can filter all the required courses and apply the concept of permutations and combinations and get all the possible paths.

### End.
