from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium import webdriver


driver = webdriver.Chrome()

print_options = PrintOptions()

# driver.get("https://helion.pl")



print_options.page_ranges = [1,2,3]

driver.get("wydruk1.html")

base64code = driver.print_page(print_options)
