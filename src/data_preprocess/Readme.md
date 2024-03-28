# Pre-processing

This section encompasses three files:

1. **Skin_change_mask.ipynb**: This initial code refers to the augmentation process, involving rotation and slight changes in skin color for randomly selected images. However, utilizing a skin mask for color alteration significantly deteriorates image quality. Hence, it was decided to omit this step, as the original image dataset already includes photographs of individuals with diverse skin tones, including brown and black skin.
   
2. **Matrix_img.ipynb**: This code facilitates the creation of a matrix containing the paths of images from various directories. The columns represent different diseases and the names of these directories. Additionally, data augmentation processes are applied to the images within these directories.

3. **augmentation_dir.ipynb**: This Python notebook allows for the manipulation of image quantities within a specified directory. It can both reduce the number of images to a given amount and augment the dataset by adding images, potentially doubling the original count. Augmentation techniques such as rotation, scaling, and slight color changes are applied to the original images during this process.

## Conclusion

The pre-processing stage is critical in preparing image data for subsequent analysis and modeling. Despite the exclusion of the skin mask for color alteration due to its adverse effects on image quality, the implemented processes, as demonstrated in the provided notebooks, effectively handle tasks such as data augmentation and directory organization. These preparatory steps lay a solid foundation for further exploration and analysis in the field of image classification and disease detection.
