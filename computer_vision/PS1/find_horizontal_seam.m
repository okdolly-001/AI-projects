function horizontalSeam = find_horizontal_seam(cumulativeEnergyMap)
[h,w] = size(cumulativeEnergyMap);
    v = [];
    for i = w:-1:1
        col = cumulativeEnergyMap(:,i);
        if i == w
            [~, index] = min(col);
            v = [v index];
        else
            if index == 1
                top = Inf;
            end
            if index > 1
                top = col(index-1);     
            end
            if index == h
                bottom = Inf;
            end
            if index < h
                bottom = col(index+1);
            end
            middle = col(index);
            [~, tmp] = min([top,middle,bottom]);
            index = index + tmp -2;
            v = [ v index];
        end
    end
horizontalSeam = fliplr(v);
