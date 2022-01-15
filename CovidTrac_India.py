
from tkinter import*
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
z=r.recognize_google(audio)
s=z.split(" ")
try:
   
    print("" + r.recognize_google(audio))
#except sr.UnknownValueError:
   # print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

   #for searching

    
from googlesearch import *
import webbrowser
#to search, will ask search query at the time of execution
query = r.recognize_google(audio)


chrome_path = r'x %s'
if r.recognize_google(audio)!="coronavirus":
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)
y=(s[0])



"""for windows"""
'''import win32com.client as wincl
if y=="open":
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("ok searching on google and opening")
if y=="open":
   x=(s[1])
   import os
   os.system(x+'.exe')'''
   
   
   
   
if r.recognize_google(audio)=="coronavirus":
    from tkinter import*
    import os
    import sys
    def command(otp): 
        print(otp)
       
    
    it=[]
    co= Tk()
    co.geometry=("1920*1080")
    co.config(bg="cyan")
    co.title("Covid-19")
    #Q1
    '''w= Text(m,height="12",width="100",bg="yellow",font=("Algerian",20),fg="black") 
    w.insert(INSERT,  "Take Self assessment")
    w.pack(side="top")'''
    
    
    #Buttons
    op0="Take self assessment"
    op1="No. of Covid Cases"
    op2="state wise cases"
    asses=Button(co,text="TAKE SELF ASSESSMENT",font=("Monotype Corsiva",20),activeforeground="red",command=lambda h=op0:[openm(),command(h)])
    cases=Button(co,text="NO. OF COVID CASES",font=("Monotype Corsiva",20),activeforeground="green",command=lambda i=op1:[command(i),runz()])
    state=Button(co,text="STATE WISE CASES",font=("Monotype Corsiva",20),activeforeground="green",command=lambda i=op2:[command(i),runst()])
    
    asses.pack(pady=20)
    cases.pack(pady=30)
    state.pack(pady=35)
    all=asses,cases,state
    it.extend(all) 
    
    #Take Self Assessment
    #window(2)
    
    def openNewWindow():
        output0="yes"
        output1="no"
        newWindow= Tk()
        newWindow.geometry=("1920*1080")
        newWindow.config(bg="yellow")
        newWindow.title("Coronavirus Self Test")
    #questions
        r= Text(newWindow,height="13",width="130",bg="yellow",font=("ALGERIAN",18),fg="black")
        r.insert(INSERT, "Are you experiencing any of the following symptoms (or a combination of these symptoms)?\n\nfever\n\nnew cough\n\ndifficulty breathing (for example, struggling for each breath, cannot hold breath for more than 10 seconds)\n")
        r.pack(side="top")
    #button
        b1=Button(newWindow,text="YES",font=("Monotype Corsiva",20),activeforeground="green",command=lambda lm=output0:[opens(),command(lm)] )
        b2=Button(newWindow,text="NO",font=("Monotype Corsiva",20),activeforeground="red",command=lambda mp=output1:[opens(),command(mp)] )
        b1.pack(side="left")
        b2.pack(side="right")
     
    #3 window
    def opens():
        output0="yes"
        output1="no"
        s= Tk()
        s.geometry=("1920*1080")
        s.config(bg="yellow")
        s.title("Coronavirus Self Test")
    #question
        z= Text(s,height="13",width="130",bg="yellow",font=("ALGERIAN",18),fg="black")
        z.insert(INSERT, "In the last 14 days, have you been in close physical contact with someone who tested positive for COVID-19?\n\nClose physical contact means:\n\nbeing less than 2 metres away in the same room, workspace, or area for over 15 minutes living in the same home")
        z.pack(side="top")
        b3=Button(s,text="YES",activeforeground="red",font=("Monotype Corsiva",20),command=lambda ln=output0:[openj(),command(ln)] )
        b4=Button(s,text="NO",activeforeground="green",font=("Monotype Corsiva",20),command=lambda ld=output1:[openj(),command(ld)] )
        b3.pack(side="left")
        b4.pack(side="right")
    #4 window  
    def openj():
        output0="yes"
        output1="no"
        j= Tk()
        j.geometry=("1920*1080")
        j.config(bg="yellow")
        j.title("Coronavirus Self Test")
    
        jz= Text(j,height="13",width="130",bg="yellow",font=("ALGERIAN",20),fg="black")
        jz.insert(INSERT, "Have you travelled or came from an outside country?,\n(like USA,Italy,Russia,China)")
        jz.pack(side="top")
        b5=Button(j,text="YES",font=("Monotype Corsiva",20),activeforeground="green",command=openy )
        b6=Button(j,text="NO",font=("Monotype Corsiva",20),activeforeground="red",command=openx)
        b5.pack(side="left")
        b6.pack(side="right")
        
    # 1st window
    #command output
    def command(d): 
        print(d)
        
    def openx():
        
        x= Toplevel(co)
        x.geometry=("1920*1080")
        x.config(bg="red")
        x.title("Coronavirus Self Test")
        canvas = Canvas(x,width = 1500, height = 1080, bg = 'white')
        id = canvas.create_text(300, 80,font=("Algerian",80),fill="GREEN", text=("lOW RISK"))
        id2 = canvas.create_text(580, 280,font=("Algerian",40),fill="Blue", text=("STAY HOME.SAVE LIVES."))
        id3 = canvas.create_text(595, 310,font=("Algerian",16), text=("Help stop coronavirus"))
        id4 = canvas.create_text(200, 400,font=("Algerian",30), text=("1.  STAYhome"))
        id5 = canvas.create_text(320, 500,font=("Algerian",30), text=("2.   Keep a safe distance"))
        id6 = canvas.create_text(290, 600,font=("Algerian",30), text=("3.   Wash hands often"))
        id7 = canvas.create_text(290, 700,font=("Algerian",30), text=("4.   Cover your cough"))
        id8 = canvas.create_text(340, 800,font=("Algerian",30), text=("5.   SICK?Call the helpline"))
                
                
        canvas.pack(expand = YES)
        gif1 = PhotoImage(file = 'rim.gif')
        gif2 = PhotoImage(file = 'yep.gif')
        gif3 = PhotoImage(file = 'asv.gif')
        gif4 = PhotoImage(file = 'ca.gif')
        gif5 = PhotoImage(file = 'ea.gif')
        gif6 = PhotoImage(file = 'sa.gif')
        gif7 = PhotoImage(file = 're.gif')
                
        canvas.create_image(700, 10, image = gif1, anchor = NW)
        canvas.create_image(500, 110, image = gif2, anchor = NW)
        canvas.create_image(800, 300, image = gif3, anchor = NW)
        canvas.create_image(810, 600, image = gif4, anchor = NW)
        canvas.create_image(1200, 300, image = gif5, anchor = NW)
        canvas.create_image(1200, 600, image = gif6, anchor = NW)
        canvas.create_image(1100, 110, image = gif7, anchor = NW)
    
        x.mainloop()
    
    def openy():
    
        y= Toplevel(co)
        y.geometry=("1920*1080")
        y.config(bg="red")
        y.title("Coronavirus Self Test")
        canvas = Canvas(y,width = 1500, height = 1080, bg = 'white')
        id = canvas.create_text(300, 80,font=("Algerian",80),fill="red", text=("HIGH RISK"))
        id2 = canvas.create_text(580, 280,font=("Algerian",40),fill="Blue", text=("STAY HOME.SAVE LIVES."))
        id3 = canvas.create_text(595, 310,font=("Algerian",16), text=("Help stop coronavirus"))
        id4 = canvas.create_text(200, 400,font=("Algerian",30), text=("1.  STAYhome"))
        id5 = canvas.create_text(320, 500,font=("Algerian",30), text=("2.   Keep a safe distance"))
        id6 = canvas.create_text(290, 600,font=("Algerian",30), text=("3.   Wash hands often"))
        id7 = canvas.create_text(290, 700,font=("Algerian",30), text=("4.   Cover your cough"))
        id8 = canvas.create_text(340, 800,font=("Algerian",30), text=("5.   SICK?Call the helpline"))
        
        
        canvas.pack(expand = YES, fill = BOTH)
        gif1 = PhotoImage(file = 'job.gif')
        gif2 = PhotoImage(file = 'yep.gif')
        gif3 = PhotoImage(file = 'asv.gif')
        gif4 = PhotoImage(file = 'ca.gif')
        gif5 = PhotoImage(file = 'ea.gif')
        gif6 = PhotoImage(file = 'sa.gif')
        gif7 = PhotoImage(file = 're.gif')
        
        canvas.create_image(700, 10, image = gif1, anchor = NW)
        canvas.create_image(500, 110, image = gif2, anchor = NW)
        canvas.create_image(800, 300, image = gif3, anchor = NW)
        canvas.create_image(810, 600, image = gif4, anchor = NW)
        canvas.create_image(1200, 300, image = gif5, anchor = NW)
        canvas.create_image(1200, 600, image = gif6, anchor = NW)
        canvas.create_image(1100, 110, image = gif7, anchor = NW)
        y.mainloop()
             
    
    ti=[]
    def openm():
        m= Tk()
        m.geometry=("1920*1080")
        m.config(bg="yellow")
        m.title("Coronavirus Self Test")
        #Q1
        w= Text(m,height="12",width="100",bg="yellow",font=("Algerian",20),fg="black") 
        w.insert(INSERT,  "Are you experiencing any of the following symptoms?\n\nsevere difficulty breathing (for example, struggling for each breath, speaking in single words)\n\nsevere chest pain\n\nhaving a very hard time waking up\n\nfeeling confused\n\nlost consciousness\n")
        w.pack(side="top")
        
    
        #Buttons
        output0="yes"
        output1="no"
        b=Button(m,text="YES",font=("Monotype Corsiva",20),activeforeground="red",command=lambda h=output0:[openNewWindow(),command(h)])
        bb=Button(m,text="NO",font=("Monotype Corsiva",20),activeforeground="green",command=lambda i=output1:[openNewWindow(),command(i)])
        b.pack(side="left")
        bb.pack(side="right")
    
        ti.append(b) 
    
    
    def runz():
        import bs4
        import requests
        
        from bs4 import BeautifulSoup as soup
        
        my_url = 'https://www.worldometers.info/coronavirus/country/india/'
        res = requests.get(my_url)
        page_html = res.text
        page_soup = soup(page_html, 'html.parser')
        
        ze=page_soup.find('span',style="color:#aaa")   
        cases=(ze.getText())
    
        death= page_soup.findAll('span')[5]
        deaths =(death.getText())
    
        recovered = page_soup.findAll('span')[6]
        recover = recovered.getText()
    
        print("No of cases in india :" , cases)
        print("No of death in india :" , deaths)
        print("No of recovered cases in india :" , recover)
    
        
    def runst():
            
        import bs4
        import requests
        
        from prettytable import PrettyTable
        x = PrettyTable()
        
        
        
        from bs4 import BeautifulSoup as soup
        
        my_url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/India_medical_cases_by_state_and_union_territory'
        res = requests.get(my_url)
        page_html = res.text
        page_soup = soup(page_html, 'html.parser')
        
        ze=page_soup.findAll('table', class_='wikitable' )[0]
        
        AN = ze.find_all('td')[0].getText()
        AN_D = ze.find_all('td')[1].getText()
        AN_R = ze.find_all('td')[2].getText()
        AN_A = ze.find_all('td')[3].getText()
        
        AP = ze.find_all('td')[4].getText()
        AP_D = ze.find_all('td')[5].getText()
        AP_R = ze.find_all('td')[6].getText()
        AP_A = ze.find_all('td')[7].getText()
        
        AR_P = ze.find_all('td')[8].getText()
        AR_P_D = ze.find_all('td')[9].getText()
        AR_P_R = ze.find_all('td')[10].getText()
        AR_P_A = ze.find_all('td')[11].getText()
        
        Assam = ze.find_all('td')[12].getText()
        Assam_D = ze.find_all('td')[13].getText()
        Assam_R = ze.find_all('td')[14].getText()
        Assam_A = ze.find_all('td')[15].getText()
        
        
        Bihar = ze.find_all('td')[16].getText()
        Bihar_D = ze.find_all('td')[17].getText()
        Bihar_R = ze.find_all('td')[18].getText()
        Bihar_A = ze.find_all('td')[19].getText()
        
        Chandigarh = ze.find_all('td')[20].getText()
        Chandigarh_D = ze.find_all('td')[21].getText()
        Chandigarh_R= ze.find_all('td')[22].getText()
        Chandigarh_A = ze.find_all('td')[23].getText()
        
        
        Chhattisgarh = ze.find_all('td')[24].getText()
        Chhattisgarh_D = ze.find_all('td')[25].getText()
        Chhattisgarh_R = ze.find_all('td')[26].getText()
        Chhattisgarh_A = ze.find_all('td')[27].getText()
        
        ddi= ze.find_all('td')[28].getText()
        ddi_D = ze.find_all('td')[29].getText()
        ddi_R = ze.find_all('td')[30].getText()
        ddi_A = ze.find_all('td')[31].getText()
        
        Delhi = ze.find_all('td')[32].getText()
        Delhi_D = ze.find_all('td')[33].getText()
        Delhi_R = ze.find_all('td')[34].getText()
        Delhi_A = ze.find_all('td')[35].getText()
        
        
        Goa = ze.find_all('td')[36].getText()
        Goa_D = ze.find_all('td')[37].getText()
        Goa_R = ze.find_all('td')[38].getText()
        Goa_A = ze.find_all('td')[39].getText()
        
        Gujrat = ze.find_all('td')[40].getText()
        Gujrat_D = ze.find_all('td')[41].getText()
        Gujrat_R = ze.find_all('td')[42].getText()
        Gujrat_A = ze.find_all('td')[43].getText()
        
        haryana = ze.find_all('td')[44].getText()
        haryana_D = ze.find_all('td')[45].getText()
        haryana_R = ze.find_all('td')[46].getText()
        haryana_A = ze.find_all('td')[47].getText()
        
        
        HP = ze.find_all('td')[48].getText()
        HP_D = ze.find_all('td')[49].getText()
        HP_R = ze.find_all('td')[50].getText()
        HP_A = ze.find_all('td')[51].getText()
        
        
        JK = ze.find_all('td')[52].getText()
        JK_D = ze.find_all('td')[53].getText()
        JK_R = ze.find_all('td')[54].getText()
        JK_A = ze.find_all('td')[55].getText()
        
        Jharkhand = ze.find_all('td')[56].getText()
        Jharkhand_D = ze.find_all('td')[57].getText()
        Jharkhand_R = ze.find_all('td')[58].getText()
        Jharkhand_A = ze.find_all('td')[59].getText()
        
        Karnataka = ze.find_all('td')[60].getText()
        Karnataka_D = ze.find_all('td')[61].getText()
        Karnataka_R = ze.find_all('td')[62].getText()
        Karnataka_A = ze.find_all('td')[63].getText()
        
        Kerala = ze.find_all('td')[64].getText()
        Kerala_D = ze.find_all('td')[65].getText()
        Kerala_R = ze.find_all('td')[66].getText()
        Kerala_A = ze.find_all('td')[67].getText()
        
        
        Ladakh = ze.find_all('td')[68].getText()
        Ladakh = ze.find_all('td')[68].getText()
        Ladakh_D = ze.find_all('td')[69].getText()
        Ladakh_R = ze.find_all('td')[70].getText()
        Ladakh_A = ze.find_all('td')[71].getText()
        
        ld = ze.find_all('td')[72].getText()
        ld_D = ze.find_all('td')[73].getText()
        ld_R = ze.find_all('td')[74].getText()
        ld_A = ze.find_all('td')[75].getText()
        
        MP = ze.find_all('td')[76].getText()
        MP_D = ze.find_all('td')[77].getText()
        MP_R = ze.find_all('td')[78].getText()
        MP_A = ze.find_all('td')[79].getText()
        
        
        Maharashtra = ze.find_all('td')[80].getText()
        Maharashtra_D = ze.find_all('td')[81].getText()
        Maharashtra_R = ze.find_all('td')[82].getText()
        Maharashtra_A = ze.find_all('td')[83].getText()
        
        Manipur = ze.find_all('td')[84].getText()
        Manipur_D = ze.find_all('td')[85].getText()
        Manipur_R = ze.find_all('td')[86].getText()
        Manipur_A = ze.find_all('td')[87].getText()
        
        Meghalaya = ze.find_all('td')[88].getText()
        Meghalaya_D = ze.find_all('td')[89].getText()
        Meghalaya_R = ze.find_all('td')[90].getText()
        Meghalaya_A = ze.find_all('td')[91].getText()
        
        Mizoram = ze.find_all('td')[92].getText()
        Mizoram_D = ze.find_all('td')[93].getText()
        Mizoram_R = ze.find_all('td')[94].getText()
        Mizoram_A = ze.find_all('td')[95].getText()
        
        Nagaland = ze.find_all('td')[96].getText()
        Nagaland_D = ze.find_all('td')[97].getText()
        Nagaland_R = ze.find_all('td')[98].getText()
        Nagaland_A = ze.find_all('td')[99].getText()
        
        Odisha = ze.find_all('td')[100].getText()
        Odisha_D = ze.find_all('td')[101].getText()
        Odisha_R = ze.find_all('td')[102].getText()
        Odisha_A = ze.find_all('td')[103].getText()
        
        Puducherry= ze.find_all('td')[104].getText()
        Puducherry_D = ze.find_all('td')[105].getText()
        Puducherry_R = ze.find_all('td')[106].getText()
        Puducherry_A = ze.find_all('td')[107].getText()
        
        Punjab = ze.find_all('td')[108].getText()
        Punjab_D = ze.find_all('td')[109].getText()
        Punjab_R = ze.find_all('td')[110].getText()
        Punjab_A = ze.find_all('td')[111].getText()
        
        Rajasthan= ze.find_all('td')[112].getText()
        Rajasthan_D = ze.find_all('td')[113].getText()
        Rajasthan_R = ze.find_all('td')[114].getText()
        Rajasthan_A = ze.find_all('td')[115].getText()
        
        Sikkim= ze.find_all('td')[116].getText()
        Sikkim_D = ze.find_all('td')[117].getText()
        Sikkim_R = ze.find_all('td')[118].getText()
        Sikkim_A = ze.find_all('td')[119].getText()
        
        Tamil_Nadu = ze.find_all('td')[120].getText()
        TN_D = ze.find_all('td')[121].getText()
        TN_R = ze.find_all('td')[122].getText()
        TN_A = ze.find_all('td')[123].getText()
        
        Telangana = ze.find_all('td')[124].getText()
        Telangana_D = ze.find_all('td')[125].getText()
        Telangana_R = ze.find_all('td')[126].getText()
        Telangana_A = ze.find_all('td')[127].getText()
        
        Tripura = ze.find_all('td')[128].getText()
        Tripura_D = ze.find_all('td')[129].getText()
        Tripura_R = ze.find_all('td')[130].getText()
        Tripura_A = ze.find_all('td')[131].getText()
        
        
        
        UK = ze.find_all('td')[132].getText()
        UK_D = ze.find_all('td')[133].getText()
        UK_R = ze.find_all('td')[134].getText()
        UK_A = ze.find_all('td')[135].getText()
        
        UP = ze.find_all('td')[136].getText()
        UP_D = ze.find_all('td')[137].getText()
        UP_R = ze.find_all('td')[138].getText()
        UP_A = ze.find_all('td')[139].getText()
        
        WB = ze.find_all('td')[140].getText()
        WB_D = ze.find_all('td')[141].getText()
        WB_R = ze.find_all('td')[142].getText()
        WB_A = ze.find_all('td')[143].getText()
        
        
        x.field_names = ["S.No", "States/union teritory", "Total cases", "death","recovered","Active cases"]
        x.add_row([1,"Andaman and nicobar inslands", AN, AN_D, AN_R,AN_A])
        x.add_row([2,"Andra Pradesh", AP, AP_D, AP_R,AP_A])
        x.add_row([3,"Arunachal Pradesh", AR_P, AR_P_D, AR_P_R,AR_P_A])
        x.add_row([4,"Assam", Assam, Assam_D, Assam_R,Assam_A])
        x.add_row([5,"Bihar", Bihar, Bihar_D, Bihar_R,Bihar_A])
        x.add_row([6,"Chandigarh", Chandigarh, Chandigarh_D, Chandigarh_R,Chandigarh_A])
        x.add_row([7,"Chhattisgarh", Chhattisgarh, Chhattisgarh_D, Chhattisgarh_R,Chhattisgarh_A])
        x.add_row([8,"Dadra and Nagar Haveli and Daman and Diu", ddi, ddi_D, ddi_R,ddi_A])
        x.add_row([9,"Delhi", Delhi, Delhi_D, Delhi_R,Delhi_A])
        x.add_row([10,"Goa", Goa, Goa_D, Goa_R,Goa_A])
        x.add_row([11,"Gujarat", Gujrat, Gujrat_D, Gujrat_R,Gujrat_A])
        x.add_row([12,"Haryana", haryana, haryana_D, haryana_R,haryana_A])
        x.add_row([13,"Himachal Pradesh", HP, HP_D, HP_R,HP_A])
        x.add_row([14,"Jammu and Kashmir", JK, JK_D, JK_R,JK_A])
        x.add_row([15,"Jharkhand", Jharkhand, Jharkhand_D, Jharkhand_R,Jharkhand_A])
        x.add_row([16,"Karnataka", Karnataka, Karnataka_D, Karnataka_R,Karnataka_A])
        x.add_row([17,"Kerala", Kerala, Kerala_D, Kerala_R,Kerala_A])
        
        x.add_row([18,"Ladakh", Ladakh, Ladakh_D, Ladakh_R,Ladakh_A])
        x.add_row([19,"Lakshadweep", ld, ld_D, ld_R,ld_A])
        x.add_row([20,"Madhya Pradesh", MP, MP_D, MP_R,MP_A])
        x.add_row([21,"Maharashtra", Maharashtra, Maharashtra_D, Maharashtra_R,Maharashtra_A])
        x.add_row([22,"Manipur", Manipur, Manipur_D, Manipur_R,Manipur_A])
        x.add_row([22,"Meghalaya", Meghalaya, Meghalaya_D, Meghalaya_R,Meghalaya_A])
        x.add_row([24,"Mizoram", Mizoram, Mizoram_D, Mizoram_R,Mizoram_A])
        x.add_row([25,"Nagaland", Nagaland, Nagaland_D, Nagaland_R,Nagaland_A])
        
        x.add_row([25,"Odisha", Odisha, Odisha_D, Odisha_R,Odisha_A])
        x.add_row([26,"Puducherry", Puducherry, Puducherry_D, Puducherry_R,Puducherry_A])
        x.add_row([27,"Punjab", Punjab, Punjab_D, Punjab_R,Punjab_A])
        x.add_row([28,"Rajasthan", Rajasthan, Rajasthan_D, Rajasthan_R,Rajasthan_A])
        x.add_row([29,"Andaman and nicobar inslands", AN, AN_D, AN_R,AN_A])
        x.add_row([30,"Sikkim",Sikkim, Sikkim_D, Sikkim_R,Sikkim_A])
        x.add_row([31,"Tamil Nadu", Tamil_Nadu, TN_D, TN_R,TN_A])
        x.add_row([32,"Telangana", Telangana, Telangana_D, Telangana_R,Telangana_A])
        x.add_row([33,"Tripura", Tripura, Tripura_D, Tripura_R,Tripura_A])
        x.add_row([34,"Uttarakhand", UK, UK_D, UK_R,UK_A])
        x.add_row([35,"UTTER PRADESH", UP, UP_D, UP_R,UP_A])
        x.add_row([36,"West Bengal", WB, WB_D, WB_R,WB_A])
        print(x)
        
    
    
    
    
    mainloop()









#for opening program

"""
    m = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = m.listen(source)
try:
  
    print("" +m.recognize_google(audio) )
#except sr.UnknownValueError:
   # print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

w=m.recognize_google(audio)

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("okay opening ")


add=m.recognize_google(audio)
"""
