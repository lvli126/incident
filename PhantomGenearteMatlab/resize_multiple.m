function imgs_new = resize_multiple(imgs, nx0, ny0, nx1, ny1)
    n_img = size(imgs, 2);
    imgs_new = zeros(nx1*ny1, n_img);
    for i = 1 : n_img
        tmp = imgs(:, i);
        tmp = reshape(tmp, nx0, ny0);
        tmp2 = imresize(tmp, [nx1 ny1]);
        tmp2 = reshape(tmp2, nx1 * ny1, 1);
        imgs_new(:, i) = tmp2;
    end
end