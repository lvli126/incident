function [X, Xg] = GenerateEmissionWithGaussian(Nimg, Nsize, Nobj, hker, sigmah, sigmaker)
    X = GenerateEmission(Nimg, Nsize, Nobj);
    Xg = zeros(size(X));
    for i = 1 : Nimg
        img = X(:,i);
        img = reshape(img, Nsize, Nsize);
        img = ScatteringGaussian(img, ceil(max(3,hker*(1+rand()*sigmah))), sigmaker);
        img = reshape(img, Nsize*Nsize, 1);
        Xg(:,i) = img;
    end
end