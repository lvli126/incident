sz_phantom = 256;
n_theta = 256;
n_theta_small = 64;

% ct = phantom(sz_phantom);
ct = GenerateSheppLogans(1, sz_phantom, 0.1);
ct = squeeze(ct);
theta = linspace(0, 180, n_theta);


sino_l = radon(ct, theta);
n_s = size(sino_l,1);
sino_m = imresize(sino_l, [n_s, n_theta_small]);
sino_s = imresize(sino_m, [n_s, n_theta]);

ct_r_l = iradon(sino_l, theta,'linear','Shepp-Logan');
ct_r_s = iradon(sino_s, theta,'linear','Shepp-Logan');

subplot(131), imshow(ct, [0.9, 1.1]);
subplot(132), imshow(ct_r_l, [0.9, 1.1]);
subplot(133), imshow(ct_r_s, [0.9, 1.1]);
