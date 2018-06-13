function [error] = compute_quantization_error(origImg,quantizedImg)
     diff = double(origImg) - double(quantizedImg);
     error = sum(diff(:).^2);

end

