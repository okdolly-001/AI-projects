function [outputImg, meanColors] = quantize_RGB(origImg, k)
    outputImg = origImg;
    [h,w, ~] = size(origImg);
    numpixels = h* w;
    X = reshape(origImg, numpixels, 3);
    [cluster_indices, meanColors] = kmeans(double(X),k,'MaxIter',10000);
    %cluster_indices:each row indicates the cluster assignment 
    %of the corresponding observation (numpixels*1)
    %meanColors
    labelled_pixels = reshape(cluster_indices, h, w);
    %meanColors returns k cluster centroid locations (k x 3)
    %where row j is the centroid of cluster j
    for i = 1:k
        for j = 1:3
            [A, B] = find(labelled_pixels == i);
            for z = 1:size(A,1)
             outputImg(A(z),B(z),j) = meanColors(i,j);
            end
        end
    end
    outputImg = uint8(outputImg);