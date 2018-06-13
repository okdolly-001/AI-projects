function [outputImg, meanHues] = quantize_HSV(origImg, k)
    HS = rgb2hsv(origImg);
    Hue = HS(:,:,1);
    [h,w] = size(Hue);
    numpixels = h* w;
    X = reshape(Hue, numpixels, 1);
    [cluster_indices, meanHues] = kmeans(double(X),k,'MaxIter',10000);

    labelled_pixels = reshape(cluster_indices, h, w);

    for i = 1:k
        [A, B] = find(labelled_pixels == i);
        for z = 1:size(A,1)
           Hue(A(z),B(z)) = meanHues(i,1);
        end
    end
    HS(:,:,1) = Hue;
   
outputImg = hsv2rgb(HS);

