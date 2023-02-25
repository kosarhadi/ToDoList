import itertools
class Task:
    count=0
    id_obj=itertools.count()
    def __init__(self,title,status,date,userid):
        self.id=next(Task.id_obj)
        self.title=title
        self.status=status
        self.date=date
        self.userid=userid

        Task.count+=1
    
    def __del__(self):

        Task.count-=1

    def __str__(self) -> str:
        
        string=self.title +" "+self.status +" "+self.date
        return string

        

    