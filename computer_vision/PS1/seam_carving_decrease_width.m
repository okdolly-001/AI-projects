clear;
RGB = imread('inputSeamCarvingPrague.jpg');
energy_RGB = energy_img(RGB);
[reducedRGB, reducedenergy_RGB] = decrease_width(RGB, energy_RGB);
for i = 1:99
    [reducedRGB, reducedenergy_RGB] = decrease_width(reducedRGB, reducedenergy_RGB);
end
imwrite(uint8(reducedRGB),'outputReduceWidthPrague.png');
imshow(RGB);
 