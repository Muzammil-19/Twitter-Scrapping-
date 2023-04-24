import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chr_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chr_driver.get("https://twitter.com/sachin_rt")

# window to stay open
# driver_path = "path/to/chromedriver"
# chr_options = Options()
# chr_options.add_experimental_option("detach", True)
# chr_driver = webdriver.Chrome(driver_path, options=chr_options)
# chr_driver.get("https://twitter.com/sachin_rt")
# # print(chr_driver.title)



def get_details():

    biography = chr_driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span')
    bio_text=biography.text
    print("biography:", bio_text)

    followers_count = chr_driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span')
    followers_count_text = followers_count.text
    print("followers_count:", followers_count_text)

    following_count = chr_driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span')
    following_count_text = following_count.text
    print("following_count:", following_count_text)


    # likes_count = chr_driver.find_element(By.XPATH,'//*[@id="id__bzkrxy203yr"]/div[3]/div/div/div[2]/span/span/span')
    # likes_count_text = likes_count.text
    # print("likes_count:", likes_count_text)

    
    user_id = chr_driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span')
    user_id_text = user_id.text
    print("user_id:", user_id_text)

    # chr_driver.quit()


get_details()


