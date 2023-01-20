#Dictionary=->A collection which is ordered,mutable and access by key value.
myDict={"c":"Easy","java":"moderate","python":"okay_okay"};

print(myDict);#{'c': 'Easy', 'java': 'moderate', 'python': 'okay_okay'}

print(len(myDict));#3

print(myDict["java"]);#moderate

print(myDict["c"]);#Easy

print(myDict["python"]);#okay_okay

print(myDict.get("c"));#Easy

myDict["php"]="web";

print(myDict);#{'c': 'Easy', 'java': 'moderate', 'python': 'okay_okay', 'php': 'web'}

del(myDict["c"]);

print(myDict);#{'java': 'moderate', 'python': 'okay_okay', 'php': 'web'}

myDict["java"]="hello";

print(myDict.get("java"));#hello

myDict.pop("java");

print(myDict);#{'python': 'okay_okay', 'php': 'web'}

myDict.clear();

print(myDict);




