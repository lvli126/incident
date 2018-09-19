function X = GenerateEmission(Nimg, Nsize, Nobj)
%GENERATE Summary of this function goes here
shaper = vision.ShapeInserter('Fill',true);
shapee = vision.ShapeInserter('Shape','Circles','Fill',true);
X = zeros(Nsize*Nsize, Nimg);
for i = 1 : Nimg
    img0 = zeros(Nsize, Nsize);
    for j = 1 : Nobj
        EorR = rand();
        img = ones(Nsize);
        if(EorR > 0.5)
            %Rectangle
            scal = Nsize/15;
            scal2 = scal*(1+randn()*0.3);
            xc = randn()*Nsize/6+Nsize/2;
            yc = randn()*Nsize/6+Nsize/2;
            rect = int32([xc-scal/2, yc-scal2/2 scal scal2]');
            img = step(shaper, img, rect);
            img(img>0.9) = 1;
            img(img<=0.9) = 0;
            img = 1 - img;
            img = imrotate(img, randn()*10, 'crop');
            
            img0 = img0 + img;
        else
            scal = Nsize/15*(1+randn()*0.1);
            xc = randn()*Nsize/6+Nsize/2;
            yc = randn()*Nsize/6+Nsize/2;
            eps = int32([xc-scal/2, yc-scal/2 scal/2]');
            img = step(shapee, img, eps);
            img(img>0.9) = 1;
            img(img<=0.9) = 0;
            img = 1 - img;
            img = imrotate(img, randn()*10, 'crop');
            img0 = img0 + img;
        end
    end
    img0 = reshape(img0, Nsize*Nsize, 1);
    X(:, i) = img0*(1+randn()*0.2/6);
end
end

