score=54
mypass=60
if score>mypass:
    gpoint=1+(score-mypass)/10
    print("学分绩点未",gpoint)
    print("通过考试")
else:
    print("学分绩点为0")
    print("未通过考试")