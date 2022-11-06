# create s3 bucket
# aws s3 mb s3://muzi-test-sam
aws s3 mb s3://muzi-test-sam2

# package template
aws cloudformation package \
--s3-bucket muzi-test-sam2 \
--template-file template.yaml \
--output-template-file gen/generated-template.yaml

# deploy stack
aws cloudformation deploy \
--template-file gen/generated-template.yaml \
--stack-name hello-4rm-sam2 \
--capabilities CAPABILITY_IAM