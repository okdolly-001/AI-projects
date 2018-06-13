function [reducedColorImg,reducedEnergyImg] = decrease_height(im,energyImg)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    min_cumu = cumulative_min_energy_map(energyImg,'HORIZONTAL');
    vt = find_horizontal_seam(min_cumu);
    [h, r] = size(energyImg);
    remove = im(h-1,r,:); 
    
   
    for i = 1:r
        remove(1:vt(i)-1,i,:) = im(1:vt(i)-1, i,:);
        remove(vt(i) : h -1,i,:) = im(vt(i)+1:h,i,:);
       
    end
    reducedColorImg = remove;
    reducedEnergyImg = energy_img(reducedColorImg);

end

% function [reducedColorImg,reducedEnergyImg]= decrease_height(im,energyImg)
% 
% cmem = cumulative_min_energy_map(energyImg, 'HORIZONTAL');
% hs = find_horizontal_seam(cmem);
% 
% [rows,columns] = size(energyImg);
% 
% reducedColorImg = zeros(rows-1, columns, 3);
% 
% for i = 1:columns
%     reducedColorImg(1:hs(i)-1,i,:) = im(1:hs(i)-1,i,:);
%     reducedColorImg(hs(i):rows-1,i,:) = im(hs(i)+1:rows,i,:);  
% end
%  reducedColorImg = uint8(reducedColorImg);
%  
%  reducedEnergyImg = energy_img(reducedColorImg);
% 
% end