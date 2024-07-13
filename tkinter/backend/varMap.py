class VarMap():
    '''UI에서 반환되는 변수와 DB의 변수 map 작성'''
    def __init__(self):
        self.DetailsTb = self.__createDetailsTb()
        self.UseraccountTb = self.__createUseraccountTb()
    
    def toDbVar(self, table, rawData):
        # UI 변수명을 DB 변수명으로 매핑 : 1. 매핑 테이블 지정
        if table == 'details':
            varMap = self.DetailsTb
        elif table == 'useraccount':
            varMap = self.UseraccountTb
        # UI 변수명을 DB 변수명으로 매핑 : rawData(dict)의 key를 varMap에서 찾아, varMap[key]의 value를 새로운 key로 하고, rawData[key]의 value를 새로운 value로 하는 dict 생성
        data = [[], []]
        for key in rawData:
            data[0].append(varMap[key])
            data[1].append(rawData[key])
        return data

    def __createUseraccountTb(self):
        '''useraccount Table에 대해, UI 변수명과 DB 변수명 매칭'''
        # 3page : phone_number or email_address
        Keys = ['phone_number', 'email_address', 'user_id']
        Vals = ['phone_num', 'email', 'ID']
        return self.__matchVarMap(Keys, Vals)

    def __createDetailsTb(self):
        '''details Table에 대해, UI 변수명과 DB 변수명 매칭'''
        # default keys
        Keys = ['user_id', 'ID']
        Vals = ['user_id', 'user_id']
        # 5page(7) : physical measurements
        Keys.extend(['나이', '성별', '키 (cm)', '체중 (kg)', '체지량지수 (BMI)', 
                     '체지방 (Kg)', '체지방률 (%)', '심장박동수 (bpm)', '허리둘레 (cm)', '골반과 허리둘레 (WHR)', 
                     '근육량 (kg)', '수축기 혈압 (SBP)', '이완기 혈압 (DBP)'])
        Vals.extend(['Age', 'Sex', 'Height', 'Weight', 'Bmi',
                     'Fat', 'Fat_percentage', 'Hr', 'Waist', 'Whr',
                     'Muscle', 'Sbp', 'Dbp'])
        # 5page(8) : blood tests
        Keys.extend(['저밀도콜레스테롤(LDL)', '고밀도콜레스테롤(HDL)', '중성지방(TG)', '알라닌아미노전이효소(ALT)', '헤모글로빈(Hb)', 
                     '갑상선자극호르몬(TSH)', '공복혈당(FG)', '식후2시간혈당(PPG)'])
        Vals.extend(['Ldl', 'Hdl', 'Tg', 'Alt', 'Hb',
                     'Tsh', 'Fg', 'Ppg'])
        return self.__matchVarMap(Keys, Vals)

    def __matchVarMap(self, Keys, Vals):
        # Match varMap
        _Matched = dict()
        for key, value in zip(Keys, Vals):
            _Matched[key] = value
        return _Matched