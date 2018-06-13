function [histEqual, histClustered] = get_hue_hists(im, k)
        [quantized, ~] = quantize_HSV(im, k);
        Hue = rgb2hsv(quantized);
        Hue = Hue(:,:,1);
        [h,w] = size(Hue);
        numpixels = h* w;
        
        Hue = reshape(Hue,numpixels,1);
        [cluster_indices, ~] = kmeans(double(Hue),k);
        histEqual = hist(Hue, k);
        histClustered = hist(cluster_indices, k);

        figure
        subplot(1, 2, 1);
        hist(Hue, k);
        title('histEqual'); 

        subplot(1, 2, 2);
        hist(cluster_indices, k);
        title('histClustered');
        
end

