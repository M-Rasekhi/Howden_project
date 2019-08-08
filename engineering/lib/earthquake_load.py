# To calculate the seismic response coefficient Cs based of ASCE 7-16 section Chapter 12.8




import numpy as np
import pandas as pd

class Quake():
    
    def __init__(self, site_class, res_mod_coeff, risk_cat, ss, s1, fund_period, long_period, height, structure_type, site_class_calculated ):
    #   res_mod_coeff = R
    #   risk_cat = Risk Category
    #   importance_factor=Ie
    #   fund_period = T
    #   long_period = TL
    
       self.site_class = site_class
       self.res_mod_coeff = res_mod_coeff
       self.risk_cat = risk_cat
       self.s1 = s1
       self.ss = ss
       self.fund_period = fund_period
       self.long_period = long_period
       self.height = height
       self.structure_type = structure_type
       self.site_class_calculated = site_class_calculated
       
# Importance factor section 11.5.1.and table 1.5-2
    def importance_factor(self):
        ie_dict = {'1': 1, '2': 1, '3': 1.25, '4': 1.5}
        ie = ie_dict[str(self.risk_cat)]
        
        return ie

# Short-period site coefficient Fa table 11.4-1
    def fa(self):
        
        array = [[0.8,0.8,0.8,0.8,0.8],
        [0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
        [1.3, 1.3, 1.2, 1.2, 1.2, 1.2],
        [1.6, 1.4, 1.2, 1.1, 1, 1]]

        df = pd.DataFrame(array, columns =[.25, .5, .75, 1, 1.25, 1.5], index= ['A', 'B', 'C', 'D'])
        faa = np.interp(self.ss, df.columns, df.loc[self.site_class])
    
        return faa   

# Long-Period site coefficient Fv
    def fv(self):
            
            array = [[0.8,0.8,0.8,0.8,0.8,0.8],
            [0.8,0.8,0.8,0.8,0.8,0.8],
            [1.5, 1.5, 1.5, 1.5,1.5, 1.4],
            [2.4, 2.2, 2, 1.9, 1.8, 1.7]]

            df = pd.DataFrame(array, columns =[.1, .2, .3, .4, .5, .6], index= ['A', 'B', 'C', 'D'])

            fvv = np.interp(self.s1, df.columns, df.loc[self.site_class])

            return fvv

# Warning message based on table 11.4-2 requirements for fv
    def fv_warning(self):
        Fv_w =""
        if self.site_class == "D" and self.s1 >= 0.2:
            Fv_w = '"Also see requirements for site-specific ground motions in section 11.4.8"'
        return Fv_w

    def sm_one(self):
        sm1 = self.fv()*self.s1
        return round(sm1, 3)

    def sm_s(self):
        sm_1 = self.fa()*self.ss
        return round(sm_1,3)
    
    def sd_one(self):
        sd_1 = self.sm_one() * 2 / 3
        return round(sd_1,3)

    def sd_s(self):
        sds = self.sm_s() * 2 / 3
        return round(sds,3)

    def seismic_design_cat(self):
        # Based on Sds
        sdc_list = ["A","B","C","D","E","F"]
        risk = self.risk_cat
        sds = self.sd_s()
        sd1 = self.sd_one()
        if risk < 4:
            if self.s1 >= 0.75:
                sdc1 = "E"
            elif sds < 0.167 :
                sdc1 = "A"
            elif sds >= 0.167 and sds < 0.33:
                sdc1 = "B"
            elif sds >= 0.33 and sds < 0.5:
                sdc1 = "C"
            else:
                sdc1 = "D"
        else:
            if self.s1 >= 0.75:
                sdc1 = "F"
            elif sds < 0.167 :
                sdc1 = "A"
            elif sds >= 0.167 and sds < 0.33:
                sdc1 = "C"
            elif sds >= 0.33 and sds < 0.5:
                sdc1 = "D"
            else:
                sdc1 = "D"

        # Based on Sd1
        if risk < 4:
            if self.s1 >= 0.75:
                sdc2 = "E"
            elif sd1 < 0.067 :
                sdc2 = "A"
            elif sd1 >= 0.067 and sd1 < 0.133:
                sdc2 = "B"
            elif sd1 >= 0.133 and sd1 < 0.2:
                sdc2 = "C"
            else:
                sdc2 = "D"
        else:
            if self.s1 >= 0.75:
                sdc2 = "F"
            elif sd1 < 0.067 :
                sdc2 = "A"
            elif sd1 >= 0.067 and sd1 < 0.133:
                sdc2 = "C"
            elif sd1 >= 0.133 and sd1 < 0.2:
                sdc2 = "D"
            else:
                sdc2 = "D"

        if sdc_list.index(sdc1) > sdc_list.index(sdc2):
            sdc =sdc1
        else:
            sdc =sdc2

        return sdc


    def cu(self):
            cu_list = [1.7, 1.6, 1.5, 1.4, 1.4]
            sd1_list = [0.1,0.15,0.2,0.3,0.4]
            c_u = np.interp(self.sd_one() , sd1_list, cu_list )

            # if self.sd_one() <= 0.1:
            #     c_u = cu_list[0]
            #     return c_u
            # elif self.s1>0.1 and self.s1<0.4:
               
            #     c_u = np.interp(float(self.sd_one()), sd1_list, cu_list)
            #     return c_u
            # else:
            #     c_u = cu_list[4]
            return c_u


    def ct(self):
        struct_type_for_ct = {"Steel moment-resisting frames":0.0724,"Concrete moment-resisting frames": 0.0466, "Steel eccentrically braced frames in accordance with Table 12.2-1 lines B1 or D1": 0.0731,"Steel buckling-restrained braced frames": 0.0731, "All other structural systems": 0.0488}
        c_t = struct_type_for_ct[self.structure_type]
        return c_t

    def x(self):
        struct_type_for_x = {"Steel moment-resisting frames":0.8,"Concrete moment-resisting frames":0.9, "Steel eccentrically braced frames in accordance with Table 12.2-1 lines B1 or D1": 0.75,"Steel buckling-restrained braced frames": 0.75, "All other structural systems": 0.75}
        xx = struct_type_for_x[self.structure_type]
        return xx

    def ta(self):
        t_a = self.ct()*self.height**self.x()
        return round(t_a,3)


    def cs(self):
        x = self.res_mod_coeff/self.importance_factor()
        c_s = self.sd_one()/x
        if self.sd_one() >= 0.6  and c_s < (0.5 * self.sd_one())/x:
            c_s = (0.5 * self.sd_one)/x
            
        elif self.fund_period <= self.long_period and c_s > self.sd_one()/(self.fund_period*x):
            c_s = self.sd_one()/(self.fund_period*x)
            
        elif self.fund_period > self.long_period and c_s > (self.sd_one() * self.long_period)/(self.fund_period**2 * x):
            c_s = (self.sd_one() * self.long_period)/(self.fund_period**2 * x)
            
        else:
            c_s = self.sd_one()/x
        return round(c_s,4)

z = Quake("C", 3, 2, 1.25, 0.5, 0.8, 12, 10 ,"All other structural systems", False)
print ("Ie= ", z.importance_factor())
print ("Fa= ", z.fa())
print ("Fv= ", z.fv(), z.fv_warning())
print ("Sm1= ", z.sm_one())
print ("Sms ", z.sm_s())
print ("Sd1= ", z.sd_one())
print ("Sds= ", z.sd_s())
print ("Cu= ", z.cu())
print ("Ct= ", z.ct())
print ("x= ", z.x())
print ("Ta= ", z.ta())
print ("Cs= ", z.cs())
print ("Seismic _design_cat= ", z.seismic_design_cat())
