from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time

def web_scraping():
    def wait():
        wait = tk.Label(window, text="Lütfen Bekleyiniz...")
        wait.config(fg="red")
        wait.pack(pady=10)
    wait()

    product_name = product_name_entry.get()
    edge_driver_path = "msedgedriver.exe"
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)



    try:
        driver.set_window_position(-2000, 0) # arka planda işlem yapması için
        driver.get("https://www.akakce.com/")

        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        search.send_keys(product_name)
        search.send_keys(Keys.RETURN)

        product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'bt_v8')))
        product.click()

        product_cheapest_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'pn_v8')))
        product_cheapest_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'pt_v8')))
        product_cheapest_stock = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'stock_v8')))
        product_cheapest_company = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'v_v8')))

        name = ("Ürün adı:", product_cheapest_name.text)
        price = ("Ürün Fiyatı:", product_cheapest_price.text)
        stock = ("Ürün Stok Durumu:", product_cheapest_stock.text)
        company = ("Ürün Satıcısı:", product_cheapest_company.text)

        messagebox.showinfo(title="En Ucuz Ürün bulundu!", message=f"İşte {product_name}, hakkında bilgiler:\n\n {name}\n\n {price}\n\n {stock}\n\n {company}")
        driver.set_window_position(100, 0)
        time.sleep(10000)


     

    except Exception as e:
        print(f"Hata: {e}")

    finally:
        driver.quit()

window = tk.Tk()
window.title("Web Scraping Tools")
window.geometry("350x150+550+300")
window.resizable(False, False)

product_name_label = tk.Label(window, text="Webte en ucuz fiyatını bulmak istediğiniz ürün:")
product_name_label.pack(pady=10)

product_name_entry = tk.Entry(window, width=40)
product_name_entry.pack(pady=5)

search_btn = tk.Button(window, text="Ara", command=web_scraping)
search_btn.pack(pady=10)

window.mainloop()