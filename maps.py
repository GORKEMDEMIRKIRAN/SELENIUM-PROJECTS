



# DOSYA İÇİNE "CHROME,EDGE,MOZILLA" DRIVER EKLEDİM.


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException,WebDriverException,NoSuchElementException

from selenium.webdriver.edge.service import Service as sv_edge
from selenium.webdriver.chrome.service import Service as sv_chrome
from selenium.webdriver.firefox.service import Service as sv_firefox

import time


# 3 FARKLI TARAYICIDA GOOGLE MAPS GİRİŞ YAPTIK.

# Tarayıcılar;   MICROSOFT EDGE, CHROME, FIREFOX

servic_edge=sv_edge(".\\msedgedriver.exe")
driver_edge=webdriver.Edge(service=servic_edge)
driver_edge.get("https://www.google.com/maps")

# servic_chrome=sv_chrome(".\\chromedriver.exe")
# driver_chrome=webdriver.Chrome(service=servic_chrome)
# driver_chrome.get("https://www.google.com/maps")

# servic_firefox=sv_firefox(".\\geckodriver.exe")
# driver_firefox=webdriver.Firefox(service=servic_firefox)
# driver_firefox.get("https://www.google.com/maps")




# Bu fonksiyon maps  mevcut olan yol tarifi butonuna tıklamaktadır.
def button_click():
    # Bu kısımda haritalardaki yol tarifi butununa tıklıyor.
    way_button=driver_edge.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/div[2]/button")
    #way_button = WebDriverWait(driver_edge, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[2]/button")))
    #way_button=driver_edge.find_element(By.ID,"hArJGc")
    way_button.click()

# Verilen iki nokta arasındaki süre ve km bilgisini oluşturur.
def two_point_enter(first_point,second_point):
    # BU VERİLEN İKİ NOKTA ATASINDAKİ MESAFENİN SAAT VE KM CİNSİNDEN DEĞERİNİ VERİR.
    # girilen 2 nokta ismini "string" olarak çeviriyor.
    first_point=str(first_point)
    second_point=str(second_point)
  
    # ilk nokta ve ikinci nokta olarak girilen kutuların "xpath" bağlantılarını buluyor.
    first_length = WebDriverWait(driver_edge, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")))
    second_length=driver_edge.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/input")
    # ilk noktayı giriyor ve aratıyor.
    # ikinci noktayıda giriyor ve aratıyor.
    
    first_length.send_keys(first_point)
    second_length.send_keys(second_point)
    second_length.send_keys(Keys.ENTER)
    
    
    #  Bulunamayan değerler için saat ve mesafe bilgilerine 0 değerini atadık.
    try:
        error_message = WebDriverWait(driver_edge, 1).until(
            expected_conditions.visibility_of_element_located((
            By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[4]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/a")))
            
        print(f"Hata: {first_point} ve {second_point} arasında sonuç bulunamadı.")
        return f"Hata mesajı: {first_point} ve {second_point} arasında sonuç bulunamadı."
    except TimeoutException:
        pass

    # Saat ve mesafe bilgisini birlikte alıyor.
    try:
        # Saati bilgisinin hmtl uzantısı
        hours = WebDriverWait(driver_edge, 10).until(
                expected_conditions.visibility_of_element_located((    
                By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[1]")))
        
        hours_info = hours.text
    except TimeoutException:
        print(f"Saat bilgisi bulunamadı: {first_point} ve {second_point}")
        hours_info = 0

    try:
        # Km bilgisinin html uzantısı
        distance = WebDriverWait(driver_edge, 10).until(
                expected_conditions.visibility_of_element_located((
                By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]")))
        
        distance_info = distance.text
    except TimeoutException:
        print(f"Mesafe bilgisi bulunamadı: {first_point} ve {second_point}")
        distance_info = 0
        
    
    # ilk nokta - ikinci nokta - saat bilgisi - mesafe bilgisi
    total = [first_point, second_point, hours_info, distance_info]
    # ilk ve ikinci hücreyi temizler.
    first_length.clear()
    second_length.clear()

    return total


# Liste içinde verilen bütün 2 noktalı konumları dk ve km cinsinden değerlerini maps çekicektir.
# verilen bilgi =[1.konum,2.konum]
# alınan bilgi = [1.konum,2.konum,süre(dk_cinsinden),mesafe(km cinsinden)]
# çıktıyı liste halinde vericektir.

def dowload_maps(area):
    # sadece iki nokta mesafe ve saat bilgisini vericek.
    update_list=list()
    button_click()
    for inside in area:
        i=inside[0]
        j=inside[1]
        data=two_point_enter(i,j)
        update_list.append(data)
    return update_list




driver_edge.quit()
