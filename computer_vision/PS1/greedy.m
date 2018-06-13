clear;
close all;

img = imread('japan.jpg');

subplot(3,2,1);
energy = energy_img(img);
seam =  find_horizontal_seam(energy);
view_seam(img,seam,'HORIZONTAL');
axis image;
title('Greedy Horizontal Seam');

subplot(3,2,2);
energy = energy_img(img);
energy = cumulative_min_energy_map(energy, 'HORIZONTAL'); 
seam =  find_horizontal_seam(energy);
view_seam(img,seam,'HORIZONTAL');
axis image;
title('Dynamic Programming Horizontal Seam');

subplot(3,2,3);
energy = energy_img(img);
seam =  find_vertical_seam(energy);
view_seam(img,seam,'VERTICAL');
axis image;
title('Greedy VERTICAL Seam');

subplot(3,2,4);
energy = energy_img(img);
energy = cumulative_min_energy_map(energy, 'VERTICAL'); 
seam =  find_vertical_seam(energy);
view_seam(img,seam,'VERTICAL');
axis image;
title('Dynamic Programming VERTICAL Seam');


subplot(3,2,5);
e = energy_img(img);
for i = 1:10
    fprintf('Iteration number %d\n',i);
    [img,e] = decrease_height(img,e);
end
imshow(img);
 axis image;
title('DP decrease height -10');

subplot(3,2,6);
e = energy_img(img);
 for i = 1:10
    fprintf('Iteration number %d\n',i);
    [img,e] = greedy_decrease_height(img,e);
end
imshow(img);
 axis image;
title('GD decrease height -10');
      
    
    
function [reducedColorImg,reducedEnergyImg] = greedy_decrease_height(im,energyImg)
    vt = find_horizontal_seam(energyImg);
    [h, r] = size(energyImg);
    remove = im(h-1,r,:); 
    
    for i = 1:r
        remove(1:vt(i)-1,i,:) = im(1:vt(i)-1, i,:);
        remove(vt(i) : h -1,i,:) = im(vt(i)+1:h,i,:);
       
    end
    reducedColorImg = remove;
    reducedEnergyImg = energy_img(reducedColorImg);

end

function [reducedColorImg,reducedEnergyImg] = greedy_decrease_width(im,energyImg)
    vt = find_vertical_seam(energyImg);
    [h, ~] = size(im);
    tmp_color = [];
    for i = 1:h
        remove = im(i,:,:); 
        remove(:,vt(i),:) = []; 
        tmp_color= [tmp_color; remove];
    
    end
    reducedColorImg = tmp_color;
    reducedEnergyImg = double(energy_img(reducedColorImg));  
end
    
