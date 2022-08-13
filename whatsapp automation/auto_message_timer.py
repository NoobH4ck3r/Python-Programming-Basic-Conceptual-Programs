import pywhatkit
from time import ctime, localtime


if __name__ == "__main__":
    groups_range = int(
        input("To how many groups or people you want to send the image and caption:\t"))
    group_id_no = []
    for i in range(groups_range):
        group_id_no.append(input(
            "Enter the group id which is present at the end of the invite link in about of group:\t"))
        continue
    image_path = input(
        "Enter the path of the image file which you want to send to the group:\t")
    message_caption = input(
        "Enter the caption you want to add int the message:\t")
    print("Messages will be sent at 12 pm. Please don't close the program")
    while True:
        if localtime().tm_hour == 11 and localtime().tm_min == 59 and localtime().tm_sec == 45:
            for items in group_id_no:
                pywhatkit.sendwhats_image(
                    receiver=items, img_path=image_path, caption=message_caption, tab_close=True, close_time=5)
                print(
                    f"Message sent successfully at {ctime()} on group id {items}")
                continue
            break
        else:
            continue
