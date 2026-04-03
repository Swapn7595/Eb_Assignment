from selenium.webdriver.common.by import By



class PracticePageLocators:
    # Add locators for the DropDown here
    DROPDPOWN_EXAMPLE = (By.XPATH, "//select[@id='dropdown-class-example']")
    DROPDOWN_OPTION = (By.XPATH, "//select[@id='dropdown-class-example']/option[normalize-space()='{visible_text}']")
    
    
    # Radio Buttons locators
    RADIO_BUTTONS = (By.XPATH, "//input[@name='radioButton']")
    RADIO_BUTTON_OPTION = (By.XPATH, "//input[@name='radioButton' and @value='{value}']")
    
    
