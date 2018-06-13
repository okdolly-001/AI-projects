function verticalSeam = find_vertical_seam(cumulativeEnergyMap)
    [h,w] = size(cumulativeEnergyMap);
    v = [];
    for i = h:-1:1
        row = cumulativeEnergyMap(i,:);
        if i == h
            [~, index] = min(row);
            v = [v index];
        else
            if index == 1
                left = Inf;
            end
            if index > 1
                left = row(index-1);     
            end
            if index == w
                    right = Inf;
            end
            if index < w
                right = row(index+1);
            end
            middle = row(index);
            [~, tmp] = min([left,middle,right]);
            index = index + tmp -2;
            v = [ v index];
        end
    end
    verticalSeam = fliplr(v);
            
end
