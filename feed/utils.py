from django.conf import settings
from django.urls import reverse
from PIL import Image

from .modals import DeletePostModal


def pad_image(image_content, imagesize=settings.IMAGE_SIZE):
    image_content.open()
    with Image.open(image_content) as img:
        img_width, img_height = img.size
        img_ar = img_width / img_height
        if img_ar > 1:
            resized_img_width = imagesize
            resized_img_height = resized_img_width / img_ar
        elif img_ar == 1:
            resized_img_width, resized_img_height = imagesize, imagesize
        else:
            resized_img_height = imagesize
            resized_img_width = resized_img_height * img_ar
        resized_img = img.resize(
            (int(resized_img_width), int(resized_img_height)))
    with Image.new(
            'RGB',
            (imagesize, imagesize), (255, 255, 255, 255)) as background_img:
        offset = (int((imagesize - resized_img_width) // 2),
                  int((imagesize - resized_img_height) // 2))
        background_img.paste(resized_img, offset)
    image_content.close()
    return background_img


def get_delete_post_modal(pk, iscreator):
    delete_post_modal = DeletePostModal(iscreator)
    delete_link = reverse('instaclone-delete_post_view', kwargs={'pk': pk})
    delete_post_modal._creator_items[0]._link = delete_link
    return delete_post_modal
