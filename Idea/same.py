class keep:
    ptr = []
    point = []
    KeyCount = []
    flag = []
    check_flag = []

    def get_ptr(self):
        return self.ptr

    def get_point(self):
        return self.point

    def get_KeyCount(self):
        return self.KeyCount

    def get_flag(self):
        return self.flag

    def get_check_flag(self):
        return self.check_flag

    def add_ptr(self,words:str):
        self.ptr += words
        return self.ptr
    
    def point_append(self,num:int):
        self.point.append(num)
        return self.point

    def KeyCount_append(self,words:str):
        self.KeyCount.append(words)
        return self.KeyCount

    def flag_changer(self):
        self.flag.append(0)

    def check_flag_up(self):
        self.check_flag.append(0)
    
    def check_flag_reset(self):
        self.check_flag.clear()

    def flag_reset(self):
        self.flag.clear()

    def allclear(self):
        self.ptr.clear()
        self.point.clear()
        self.KeyCount.clear()