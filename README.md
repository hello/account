## INFO

staging url: [http://account-staging-zpbsmunavw.elasticbeanstalk.com/reset](http://account-staging-zpbsmunavw.elasticbeanstalk.com/reset)

prod beanstalk url: [http://account-prod-pdkvqqumsr.elasticbeanstalk.com/reset](http://account-prod-pdkvqqumsr.elasticbeanstalk.com/reset)

prod public url [https://account.hello.is/](https://account.hello.is/)


* staging is only accessible via SSH/HTTP from: 199.87.82.114/32 (office IP)
* prod is only accessible via SSH from: 199.87.82.114/32 (office IP)

## GOOD TO KNOW

Things usually work better in virtualenv, so please make sure you use one.

## PREP
- put all your AWS credentials in the right place, usually in `~/.elasticbeanstalk/aws\_credential\_file` with
```
AWSAccessKeyId=<your access key id>
AWSSecretKey=<your secret>
```

- download the [EB tool](http://aws.amazon.com/code/6752709412171743) from AWS
- unzipping the download, you need to set the path to the `eb` command.
```
export PATH=$PATH:<path to unzipped EB CLI package>/eb/macosx/python2.7
```

## HOW TO


1. git clone this repo.
2. create `config` in `.elasticbeanstalk` (get template from Tim)
3. replace `OptionSettingFile=/Users/tim/codebin/envs/passwordreset/.elasticbeanstalk/optionsettings.account-prod` in `.elasticbeanstalk/config` with your own path.
4. git checkout staging
5. Do work
6. git commit -m"blah"
7. git aws.push to push to staging

To push to prod, same as above but from master.


## TODO

- [ ] Find a better way to commit the config without personal environment path
