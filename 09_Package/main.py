import tools.str_utils as str_utils
import tools.file_utils as file_utils

if __name__ == "__main__":
    str = str_utils.str_reverse("1234")
    
    file_utils.append_to_file("./09_Package/FileTest.txt",str)
    file_utils.print_file_info("./09_Package/FileTest.txt")
    
    