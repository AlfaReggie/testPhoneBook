class Contact:

    def __init__(self, name, fam_name, phone):
        self.name = name
        self.fam_name = fam_name
        self.phone = phone

    def change_cont_info(self, contact: list, flag: str, new_info):
        if flag in 'name':
            contact[0] = new_info
        elif flag in 'famname':
            contact[1] = new_info
        elif flag in 'phone':
            contact[2] = new_info

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Family name: {self.fam_name}\n" \
               f"Phone: {self.phone}"
