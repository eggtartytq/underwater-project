from corruptions import *


target_file = 'train_val\images'
current_file=os.path.dirname(os.path.abspath(__file__))
train_file= os.path.join(current_file, target_file)

Gaussian_Noise = os.path.join(current_file, 'train_val\modified\Gaussian_Noise')
Shot_Noise = os.path.join(current_file, 'train_val\modified\Shot_Noise')
Impulse_Noise = os.path.join(current_file, 'train_val\modified\Impulse_Noise')
Defocus_Blur = os.path.join(current_file, 'train_val\modified\Defocus_Blur')
Frosted_Glass_Blur = os.path.join(current_file, 'train_val\modified\Frosted_Glass_Blur')
Motion_Blur = os.path.join(current_file, 'train_val\modified\Motion_Blur')
Zoom_Blur = os.path.join(current_file, 'train_val\modified\Zoom_Blur')
Brightness = os.path.join(current_file, 'train_val\modified\Brightness')
Contrast = os.path.join(current_file, 'train_val\modified\Contrast')
Elastic = os.path.join(current_file, 'train_val\modified\Elastic')
Pixelate = os.path.join(current_file, 'train_val\modified\Pixelate')
jpeg_comp = os.path.join(current_file, 'train_val\modified\jpeg_comp')

def modify():
    os.chdir(train_file)

    for image_name in os.listdir(os.getcwd()):
        curr_im = os.path.join(train_file, image_name)
        im = Image.open(curr_im)

        test_gaussian = gaussian_noise(im)
        trans_gaussian = Image.fromarray(np.uint8(test_gaussian))
        trans_gaussian.save(os.path.join(Gaussian_Noise, image_name))

        test_shot = shot_noise(im)
        trans_shot = Image.fromarray(np.uint8(test_shot))
        trans_shot.save(os.path.join(Shot_Noise, image_name))

        test_impulse = impulse_noise(im)
        trans_impulse = Image.fromarray(np.uint8(test_impulse))
        trans_impulse.save(os.path.join(Impulse_Noise, image_name))

        test_defocus = defocus_blur(im)
        trans_defocus = Image.fromarray(np.uint8(test_defocus))
        trans_defocus.save(os.path.join(Defocus_Blur, image_name))

        test_motion = motion_blur(im)
        trans_motion = Image.fromarray(np.uint8(test_motion))
        trans_motion.save(os.path.join(Motion_Blur, image_name))

        test_zoom = zoom_blur(im)
        trans_zoom = Image.fromarray(np.uint8(test_zoom))
        trans_zoom.save(os.path.join(Zoom_Blur, image_name))

        test_brightness = brightness(im)
        trans_brightness = Image.fromarray(np.uint8(test_brightness))
        trans_brightness.save(os.path.join(Brightness, image_name))

        test_contrast = contrast(im)
        trans_contrast = Image.fromarray(np.uint8(test_contrast))
        trans_contrast.save(os.path.join(Contrast, image_name))

        test_elastic = elastic_transform(im)
        trans_elastic = Image.fromarray(np.uint8(test_elastic))
        trans_elastic.save(os.path.join(Elastic, image_name))

        test_pixelate = pixelate(im)
        trans_pixelate = Image.fromarray(np.uint8(test_pixelate))
        trans_pixelate.save(os.path.join(Pixelate, image_name))

        test_jpeg_compression = jpeg_compression(im)
        trans_jpeg_compression = Image.fromarray(np.uint8(test_jpeg_compression))
        trans_jpeg_compression.save(os.path.join(jpeg_comp, image_name))

def modify_frost():
    os.chdir(train_file)
    for image_name in os.listdir(os.getcwd()):
        curr_im = os.path.join(train_file, image_name)
        im = Image.open(curr_im)

        test_frost = frost(im)
        trans_frost = Image.fromarray(np.uint8(test_frost))
        trans_frost.save(os.path.join(Frosted_Glass_Blur, image_name))

#modify()
modify_frost()