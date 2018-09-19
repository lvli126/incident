function clshow(x, window)
sz = sqrt(size(x,1));
if isempty(window)
imshow(reshape(x, sz, sz), []);
else
imshow(reshape(x, sz, sz), window);    
end
end

