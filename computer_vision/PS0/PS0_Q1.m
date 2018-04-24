function PS0_Q1
    clc
    load PS0_A.mat A
    B = sort(A(:), 'descend');
    figure(1)
    plot(B)
    
    figure(2);
    histogram(A,20)
    
    figure(3);
    C = A(length(A)/2 + 1: end, 1: length(A)/2);
    imagesc(C);
    
    figure(4);
     W = A - mean(A(:));
    imagesc(W);
     
     figure(5);
     mat = zeros(100,100,3);
     ind = A > mean(A(:));
     mat(ind(:,:,1)) = 255;
     imshow(mat);