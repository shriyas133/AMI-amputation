function [EMGdata, Filename] = EMG_readAllFolder(F, DataType)

fileID = fopen(F.name);
delimiter = ',';
startRow = 2;

if DataType == 0
formatSpec = '%*s%*s%f%f%f%f%f%f%f%f%f%[^\n\r]'; %% data set that has affected / unaffected limb
else
formatSpec = '%*s%*s%f%f%f%f%f%[^\n\r]'; %% data set that has only affected limb
end

dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'TextType', 'string', 'EmptyValue', NaN, 'HeaderLines' , startRow-1, 'ReturnOnError', false, 'EndOfLine', '\r\n');
fclose(fileID);
EMGdata = [dataArray{1:end-1}];
Filename = F.name;    
end