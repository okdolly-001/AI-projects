function PS0_Q2
   clear
   RGB = imread('bluesky.jpg');
   
   figure;
   subplot(3, 2,1);
   I = rgb2gray(RGB);
   imshow(I);
   title('a) gray scale');
   
   subplot(3,2,2);
    b = uint8(I);
    b = imcomplement(b);
    imshow(b);
    title('b) negative image');
    
    subplot(3,2,3);
    c =  flipdim(RGB ,2);    
    imshow(c);
    title('c) mirror image');
    
    subplot(3,2,4);
    d(:,:,1) = RGB(:,:,3);
    d(:,:,3) = RGB(:,:,1);
    d(:,:,2) = RGB(:,:,2);
    imshow(d);
    title("d) swap red blue");
    
    subplot(3,2,5);
    e = double(RGB) + double(c) / 2;
    imshow(uint8(e));
    title("e) average two image");
    
    subplot(3,2,6);
    [height, width, dim] = size(I);
    dummy = randi([-255,255], [height,width]);
    f = double(I) + dummy;
    f(f<0) = 0; 
    f(f>255) = 255;
    f = uint8(f);
    imshow(f);
    title("f) random noise and thresholding")
    
