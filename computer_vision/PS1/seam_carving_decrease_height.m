clear;
RGB = imread('inputSeamCarvingPrague.jpg');
energy_RGB = energy_img(RGB);
[reducedRGB, reducedenergy_RGB] = decrease_height(RGB, energy_RGB);
for i = 1:49
    [reducedRGB, reducedenergy_RGB] = decrease_height(reducedRGB, reducedenergy_RGB);
end
imwrite(uint8(reducedRGB),'outputReduceHeightPrague.png');

imshow(reducedRGB);
imshow(RGB);