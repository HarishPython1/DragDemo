import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://phptravels.com/")
time.sleep(10)#Hard wait
driver.find_element_by_xpath("//span[text()='Login']").click()

print("current window ",driver.current_window_handle)
c_w = driver.current_window_handle#1
#current active window id is captured

w_h = driver.window_handles#[1,2]
#return type is list

for i in w_h:#[1,2]
    if i!=c_w:
        driver.switch_to.window(i)

driver.find_element_by_id("inputEmail").send_keys("TestWindow")
#driver.close()#closes currently active window
driver.quit()#closes currently active browser session






# driver.get("https://jqueryui.com/droppable/")
# print("entered url")
#
# driver.implicitly_wait(30)
# frame_val = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
# driver.switch_to.frame(frame_val)
# print("switched to iframe")
#
# src_drag = driver.find_element_by_id("draggable")
# print("captured src val")
# dest_drop = driver.find_element_by_id("droppable")
# print("captured dest val")
#
# a = ActionChains(driver)
# a.drag_and_drop(src_drag,dest_drop).perform()
# print("dragged and dropped succ")


