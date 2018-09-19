function MultiFilePhantom(fnprefix, nfile, perfile, imgsize, sigma)    
    for ifile = 1 : nfile
        filename = [fnprefix,int2str(ifile),'.mat'];
        X = GenerateSheppLogans(perfile, imgsize, sigma);
        save(filename, 'X');        
        disp(['file ',num2str(ifile),' of ',num2str(nfile), ' finished']);
    end
end