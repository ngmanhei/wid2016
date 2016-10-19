function res = racv2016_eval(path, comp_id, test_set, output_dir)

RACV2016opts = get_racv2016_opts(path);
RACV2016opts.testset = test_set;

for i = 1:length(RACV2016opts.classes)
  cls = RACV2016opts.classes{i};
  res(i) = racv2016_eval_cls(cls, RACV2016opts, comp_id, output_dir);
end

fprintf('\n~~~~~~~~~~~~~~~~~~~~\n');
fprintf('Results:\n');
aps = [res(:).ap]';
fprintf('%.1f\n', aps * 100);
fprintf('%.1f\n', mean(aps) * 100);
fprintf('~~~~~~~~~~~~~~~~~~~~\n');

function res = racv2016_eval_cls(cls, RACV2016opts, comp_id, output_dir)

test_set = RACV2016opts.testset;
year = RACV2016opts.dataset(4:end);

addpath(fullfile(RACV2016opts.datadir, 'RACV2016code'));

res_fn = sprintf(RACV2016opts.detrespath, comp_id, cls);

recall = [];
prec = [];
ap = 0;
ap_auc = 0;

do_eval = (str2num(year) <= 2007) | ~strcmp(test_set, 'test');
if do_eval
  % Bug in RACV2016evaldet requires that tic has been called first
  tic;
  [recall, prec, ap] = RACV2016evaldet(RACV2016opts, comp_id, cls, true);
  ap_auc = xRACV2016ap(recall, prec);

  % force plot limits
  ylim([0 1]);
  xlim([0 1]);

  print(gcf, '-djpeg', '-r0', ...
        [output_dir '/' cls '_pr.jpg']);
end
fprintf('!!! %s : %.4f %.4f\n', cls, ap, ap_auc);

res.recall = recall;
res.prec = prec;
res.ap = ap;
res.ap_auc = ap_auc;

save([output_dir '/' cls '_pr.mat'], ...
     'res', 'recall', 'prec', 'ap', 'ap_auc');

rmpath(fullfile(RACV2016opts.datadir, 'RACV2016code'));
