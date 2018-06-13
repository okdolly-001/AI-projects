function [ centers ] = detect_circles(im, radius, useGradient)
orig = im;
im = rgb2gray(im);
im = double(im);
[row, col] = size(im);
edges = edge(im, 'canny');
edge_indices = find(edges);
accumulator = zeros(row, col);
centers = [];
radi = [];
if useGradient == 0
    for i = 1: size(edge_indices,1)
        [x, y] = ind2sub([row, col], edge_indices(i));
        for angle=1:360
            a = abs(ceil( x - radius*cos(angle)));
            b = abs(ceil(y + radius*sin(angle)));
            if(a > 0 && a < row && b < col && b > 0)
                accumulator(a,b) = accumulator(a,b) + 1;
             end
        end
    end
end
if useGradient == 1
    for i = 1: size(edge_indices,1)
        [x, y] = ind2sub([row, col], edge_indices(i));
    %    [dx, dy] = imgradientxy(edges);
        [dy,dx] = gradient(im);
        gradientDirections = atan2(-dy,dx);
        for angle =  (-gradientDirections-45):  (-gradientDirections+45)
%          angle = gradientDirections(x, y);
            a = abs(ceil( x - radius*cos(angle)));
            b = abs(ceil(y + radius*sin(angle)));
            if(a > 0 && a < row && b < col && b > 0)
                accumulator(a,b) = accumulator(a,b) + 1;
            end
        end
  
    end
end


accumulator = accumulator/max(accumulator(:));

accumulator_inds = find(accumulator >0.85);


for i = 1: size(accumulator_inds,1)
    [ax, ay] = ind2sub([row, col], accumulator_inds(i));
    centers = [centers; [ay,ax]];
    radi = [radi ; radius];
end

% 
% % % 
% imshow(orig);
% hold on;
% viscircles(centers, radi,'LineStyle','--');
% title('Threshold = 85%, Radius = 60 ,useGradient = 0 ');


