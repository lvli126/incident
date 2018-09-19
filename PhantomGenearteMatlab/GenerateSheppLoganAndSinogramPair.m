function [X, S] = GenerateSheppLoganAndSinogramPair(Nimg, Nsize, Ntheta, sigma)
    X = GenerateSheppLogans(Nimg, Nsize, sigma);
    theta = linspace(0, 180, Ntheta);
    sino_0 = radon(X(:,:,1), theta);
    n_s = size(sino_0, 1);
    S = zeros(n_s, Ntheta, Nimg);
    for i = 1 : Nimg
        sino = radon(X(:, :, i), theta);
        S(:,:,i) = sino;
    end
end