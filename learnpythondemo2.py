class changer:
    def change(self,item,listpara=None):
        if not listpara:
            listpara=[]
        for i in listpara:
            print(i)
        listpara.append(item)
        return self
if __name__=="__main__":
      changer().change(1,[2,3]).change(2).change(3)