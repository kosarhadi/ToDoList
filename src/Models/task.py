class Task:
    count=0
    def __init__(self,title,status,date,userid,id=0):
        self.id=id
        self.title=title
        self.status=status
        self.date=date
        self.userid=userid

        Task.count+=1
    
    def __del__(self):

        Task.count-=1

    def __str__(self) -> str:
        
        string=str(self.id) +". "+self.title +" "+self.status +" "+self.date
        return string

        

    