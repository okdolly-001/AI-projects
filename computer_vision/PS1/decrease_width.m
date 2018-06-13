function [reducedColorImg,reducedEnergyImg] = decrease_width(im,energyImg)
    min_cumu = cumulative_min_energy_map(energyImg,'VERTICAL');
    vt = find_vertical_seam(min_cumu);
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
    




