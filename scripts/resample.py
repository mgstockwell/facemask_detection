import boto3
# Delete files from test and train
# Copy new set of random files

bucket_name = '511004593648-msds436'
train_size = 100
test_size = 20

def delete_s3_files(tgt_obj):
    '''Deletes all files in target'''
    session = boto3.Session()
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)
    delete_source = {
        'Bucket': bucket_name,
        'Key': tgt_obj
    }
    bucket.delete(delete_source)

def copy_s3_file(src_obj, tgt_obj):
    '''Copies a source file to target location'''
    session = boto3.Session()
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)
    copy_source = {
        'Bucket': bucket_name,
        'Key': src_obj
    }
    bucket.copy(copy_source, tgt_obj)

dirs = ['../test/mask',
   '../test/no_mask',
   '../train/mask',
   '../train/no_mask',]
for dir in dirs:
    #delete all files
    delete_s3_files(dir)


# move S3 files
train_range = random.sample(range(10000),train_size)
test_range = random.sample(range(10000),test_size)
for n in train_range:
  file_name = "seed" + str(n).zfill(4) + ".png"
  f_with = "new_with_mask/with-mask-default-mask-" + file_name
  f_without = "new_without_mask/" + file_name
  copy_s3_file(f_without, f'train/{file_name}')
  copy_s3_file(f_with, f'train/{file_name}')
for n in test_range:
  file_name = "seed" + str(n).zfill(4) + ".png"
  f_with = "new_with_mask/with-mask-default-mask-" + file_name
  f_without = "new_without_mask/" + file_name
  copy_s3_file(f_without, f'test/{file_name}')
  copy_s3_file(f_with, f'test/{file_name}')