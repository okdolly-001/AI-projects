function energyImg = energy_img(im)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    I = double(rgb2gray(im));
    [dx, dy] = imgradientxy(I);
    energyImg = double(sqrt(dx.^2+dy.^2));
    
end

