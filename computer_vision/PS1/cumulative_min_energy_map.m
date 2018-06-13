function cumulativeEnergyMap = cumulative_min_energy_map(energyImg,seamDirection)
    I = energyImg;
    h = size(energyImg,1);
    w = size(energyImg,2);

    if  strcmp(seamDirection,'VERTICAL')
        for i=2:h
            for j = 1:w
                if j == 1
                    left = Inf;
                end
                if j > 1
                    left = I(i-1,j-1);     
                end
                if j == w
                    right = Inf;
                end
                if j < w
                    right = I(i-1, j+1);
                end
                middle = I(i-1, j);
                I(i,j) = I(i,j) + min([left, middle,right]);    
        
            end
        end
    
    elseif  strcmp(seamDirection,'HORIZONTAL')
         for j=2:w
            for i = 1:h
                if i == 1
                    top = Inf;
                end
                if i > 1
                    top = I(i-1,j-1);     
                end
                if i == h
                    bottom = Inf;
                end
                if i < h
                    bottom = I(i+1,j-1);
                end
                middle = I(i,j-1);
                I(i,j) = I(i,j) + min([top, middle,bottom]);
                
        
            end
         end
    end
 cumulativeEnergyMap = I;   
