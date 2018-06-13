function view_seam(im,seam,seamDirection)
    [h,w,~] = size(im);
    imshow(im)
    hold on
    if strcmp(seamDirection, 'VERTICAL')
        for i = 1:h
            if 1<i  &&  i< w            
                im(i,seam(i),:)= [255,0,0];
                im(i,seam(i)+1,:)= [255,0,0];
            else
                im(i,seam(i),:)= [255,0,0];
               
            end
        end
        imagesc(im);
    end
     if strcmp(seamDirection, 'HORIZONTAL')
        for j = 1:w
           if 1<j  &&  j <h    
            im(seam(j)-1,j,:) = [255,0,0];   
            im(seam(j),j,:) = [255,0,0];     
            im(seam(j)+1,j,:) = [255,0,0];
           else
               im(seam(j),j,:) = [255,0,0]; 
           end 
        end
     end
    imagesc(im);
    
end

