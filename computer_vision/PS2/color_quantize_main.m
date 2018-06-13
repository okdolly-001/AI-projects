clear;
close all;

origImg = imread('fish.jpg');
subplot(2,2,1);
[img1, ~] = quantize_HSV(origImg, 5);
imshow(img1);
title('HSV image with k = 5');

subplot(2,2,2);
[img2, ~] = quantize_HSV(origImg, 25);
imshow(img2);
title({'HSV image with k = 25'});

subplot(2,2,3);
[img3, ~] = quantize_RGB(origImg, 5);
imshow(img3);
title('RGB image with k = 5');

subplot(2,2,4);
[img4, ~] = quantize_RGB(origImg, 25);
imshow(img4);
title('RGB image with k = 25');



[histEqual, histClustered] = get_hue_hists(origImg, 5);


subplot(2,2,1);
bar(histEqual);
title({'Equal histogram', 'for HSV image with k = 5'});

subplot(2,2,2);
bar(histClustered);
title({'Clustered histogram', 'for HSV image with k = 5'});


[histEqual2, histClustered2] = get_hue_hists(origImg, 25);


subplot(2,2,3);
bar(histEqual2);
title({'Equal histogram', 'for HSV image with k = 25'});


subplot(2,2,4);
bar(histClustered2);
title({'Clustered histogram', 'for HSV image with k = 25'});


e1 = compute_quantization_error(origImg,img1);
e2 = compute_quantization_error(origImg,img2);
e3 = compute_quantization_error(origImg,img3);
e4 = compute_quantization_error(origImg,img4);

fprintf("The error of HSV image with k = 5 is %d \n",e1);
fprintf("The error of HSV image with k = 25 is %d \n",e2);
fprintf("The error of RGB image with k = 5 is %d \n",e3);
fprintf("The error of RGB image with k = 25 is %d \n",e4);


