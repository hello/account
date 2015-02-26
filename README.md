## INFO

staging url: [http://account-staging-zpbsmunavw.elasticbeanstalk.com/reset](http://account-staging-zpbsmunavw.elasticbeanstalk.com/reset)
prod beanstalk url: [http://account-prod-pdkvqqumsr.elasticbeanstalk.com/reset](http://account-prod-pdkvqqumsr.elasticbeanstalk.com/reset)
prod public url [https://account.hello.is/](https://account.hello.is/)


staging is only accessible via SSH/HTTP from: 199.87.82.114/32 (office IP)
prod is only accessible via SSH from: 199.87.82.114/32 (office IP)


## HOW TO

1. git clone this repo.
2. replace `OptionSettingFile=/Users/tim/codebin/envs/passwordreset/.elasticbeanstalk/optionsettings.account-prod` in `.elasticbeanstalk/config` with your own path.
3. git checkout staging
4. Do work
5. git commit -m"blah"
6. git aws.push to push to staging

To push to prod, same as above but from master.


## TODO

- [ ] Find a better way to commit the config without personal environment path
