import time
from os import wait

import pytest



from selenium.webdriver.common.by import By




class TestLogin:
    def test_login(self,setup):
        self.driver = setup
        self.driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=1800&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fevents%2Fgreatsummersale%2F%3F_encoding%3DUTF8%26amp%3Bref_%3Dmay25_H1_main_event%26amp%3Bpd_rd_w%3DIHKIe%26amp%3Bcontent-id%3Damzn1.sym.ca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_p%3Dca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_r%3DGRCBY62VYWNXQAG324KV%26amp%3Bpd_rd_wg%3DFpyxz%26amp%3Bpd_rd_r%3D982b7619-cce4-4b11-9735-d4948b55c835&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_p13n_profilepicker_authportal_in&openid.mode=checkid_setup&marketPlaceId=A21TJRUUN4KGV&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        time.sleep(20)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys("7860752096")
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_password"]').send_keys("Pnb@123#")
        self.driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
        time.sleep(10)

    def test_mycart(self,setup):
        self.driver = setup
        self.driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=1800&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fevents%2Fgreatsummersale%2F%3F_encoding%3DUTF8%26amp%3Bref_%3Dmay25_H1_main_event%26amp%3Bpd_rd_w%3DIHKIe%26amp%3Bcontent-id%3Damzn1.sym.ca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_p%3Dca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_r%3DGRCBY62VYWNXQAG324KV%26amp%3Bpd_rd_wg%3DFpyxz%26amp%3Bpd_rd_r%3D982b7619-cce4-4b11-9735-d4948b55c835&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_p13n_profilepicker_authportal_in&openid.mode=checkid_setup&marketPlaceId=A21TJRUUN4KGV&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        time.sleep(20)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys("7860752096")
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_password"]').send_keys("Pnb@123#")
        self.driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="nav_prefetch_yourorders"]/span').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="a-page"]/section/div[1]/div[3]/ul/li[1]').click()
        self.driver.find_element(By.XPATH,'//*[@id="a-autoid-2-announce"]/div[2]').click()
        self.status = self.driver.find_element(By.XPATH,'//*[@id="title"]/h1')
        if self.status == "Your Orders":
            self.driver.find_element(By.XPATH,'//*[@id="title-B01DEWVZ2C-grid"]/span/span/span[2]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,'//*[@id="a-autoid-1"]/span/input').click()
            value_cart = self.driver.find_element(By.XPATH,'//*[@id="atc-container-B01DEWVZ2C"]/div/form/div[2]/div[2]/div[2]/span[2]')
            print(value_cart)
    def test_checkout(self,setup):
        self.driver = setup
        self.driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=1800&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fevents%2Fgreatsummersale%2F%3F_encoding%3DUTF8%26amp%3Bref_%3Dmay25_H1_main_event%26amp%3Bpd_rd_w%3DIHKIe%26amp%3Bcontent-id%3Damzn1.sym.ca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_p%3Dca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_r%3DGRCBY62VYWNXQAG324KV%26amp%3Bpd_rd_wg%3DFpyxz%26amp%3Bpd_rd_r%3D982b7619-cce4-4b11-9735-d4948b55c835&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_p13n_profilepicker_authportal_in&openid.mode=checkid_setup&marketPlaceId=A21TJRUUN4KGV&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        time.sleep(20)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys("7860752096")
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_password"]').send_keys("Pnb@123#")
        self.driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,'//*[@id="nav-cart"]').click()
        self.status = self.driver.find_element(By.XPATH,'//*[@id="sc-active-items-header"]').is_displayed()

        if self.status == True:
            #procede to check out
            self.driver.find_element(By.XPATH,'//*[@id="sc-buy-box-ptc-button"]/span/input').click()
            self.status1 = self.driver.find_element(By.XPATH,'//*[@id="nav-checkout-title-header-text"]').is_displayed()
            if self.status1 == True :
                print("you have checked out enetr the payment mode")

    def test_serch_product(self,setup):
        self.driver = setup
        self.driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=1800&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fevents%2Fgreatsummersale%2F%3F_encoding%3DUTF8%26amp%3Bref_%3Dmay25_H1_main_event%26amp%3Bpd_rd_w%3DIHKIe%26amp%3Bcontent-id%3Damzn1.sym.ca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_p%3Dca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_r%3DGRCBY62VYWNXQAG324KV%26amp%3Bpd_rd_wg%3DFpyxz%26amp%3Bpd_rd_r%3D982b7619-cce4-4b11-9735-d4948b55c835&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_p13n_profilepicker_authportal_in&openid.mode=checkid_setup&marketPlaceId=A21TJRUUN4KGV&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        time.sleep(20)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys("7860752096")
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_password"]').send_keys("Pnb@123#")
        self.driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
        time.sleep(10)
        serch = self.driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')

        serch.clear()
        serch.send_keys("Samsung S24")
        self.driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
        time.sleep(10)
    def test_add_serch_item_intocart(self,setup):
        self.driver = setup
        self.driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=1800&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fevents%2Fgreatsummersale%2F%3F_encoding%3DUTF8%26amp%3Bref_%3Dmay25_H1_main_event%26amp%3Bpd_rd_w%3DIHKIe%26amp%3Bcontent-id%3Damzn1.sym.ca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_p%3Dca41c68d-d184-4861-9f50-2308856b1e21%26amp%3Bpf_rd_r%3DGRCBY62VYWNXQAG324KV%26amp%3Bpd_rd_wg%3DFpyxz%26amp%3Bpd_rd_r%3D982b7619-cce4-4b11-9735-d4948b55c835&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_p13n_profilepicker_authportal_in&openid.mode=checkid_setup&marketPlaceId=A21TJRUUN4KGV&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        time.sleep(20)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys("7860752096")
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@id="ap_password"]').send_keys("Pnb@123#")
        self.driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
        time.sleep(10)
        serch = self.driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')

        serch.clear()
        serch.send_keys("Samsung S24")
        self.driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
        time.sleep(10)

        # results = self.driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
        #
        # print(f"Total products found: {len(results)}")
        #
        # for index, result in enumerate(results, start=1):
        #     try:
        #         title = result.find_element(By.XPATH, './/h2/a/span').text
        #         link = result.find_element(By.XPATH, './/h2/a').get_attribute("href")
        #         print(f"{index}. {title}\n   Link: {link}\n")
        #     except Exception as e:
        #         print(f"Could not extract info for result {index}: {e}")

















