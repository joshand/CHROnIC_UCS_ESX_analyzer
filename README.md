  703  docker stop dockerfile
  704  docker rm dockerfile
  705  docker ps -a
  706  docker images
  707  docker pull quay.io/hpreston/demo:latest
  708  docker pull python
  709  ls
  710  echo "# imapex_dockerbuild" >> README.md
  711  git init
  712  git add README.md
  713  git commit -m "first commit"
  714  git remote add origin https://github.com/chapeter/imapex_dockerbuild.git
  715  git push -u origin master
  716  git status
  717  git add .
  718  git status
  719  git commit -m "add Dockerfile and hello_world"
  720  git push
  721  ls
  722  vim README.md
  723  git add README.md
  724  git commit -m "updated README.md with program info"
  725  git push
  726  cd ~/projects/
  727  brew install node
  728  brew install ffmpeg --with-libass --with-fontconfig
  729  ssh admin@10.94.238.124
  730  export MARATHON_URL=https://control.green.browndogtech.com:8080/v2
  731  export MARATHON_USER=devops1
  732  export MARATHON_PASSWORD=DEVOPS1
  733  export MYUSERNAME=chapeter
  734  curl -k -X GET -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps     | python -m json.tool
  735  curl -k -X GET -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/data     | python -m json.tool
  736  curl -k -X GET -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/myhero     | python -m json.tool
  737  curl -k -X PUT -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/myhero     -d '{"instances": 3}'     | python -m json.tool
  738  curl -k -X PUT -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/myhero     -d '{"instances": 3}'     | python -m json.tool
  739  printenv | grep SPARK
  740  cd ima
  741  cd projects/imapex/
  742  ls
  743  mkdir cicdlab
  744  cd cicdlab/
  745  ls
  746  curl http://downloads.drone.io/drone-cli/drone_linux_amd64.tar.gz | tar zx
  747  ls
  748  rm -rf drone
  749  curl http://downloads.drone.io/drone-cli/drone_darwin_amd64.tar.gz | tar zx
  750  sudo cp drone /usr/local/bin
  751  printenv | grep SPARK_TO
  752  cd /tmp
  753  git clone http://github.com/chapeter/drone-spark
  754  history | grep build
  755  docker build -t chapeter/drone-spark:latest .
  756  cd drone-spark/
  757  docker build -t chapeter/drone-spark:latest .
  758  history | grep docker
  759  docker push chapeter/drone-spark:latest
  760  docker push chapeter/drone-spark:latest
  761  ls
  762  cd projects/
  763  ls
  764  cd imapex/cicdlab/
  765  ls
  766  ls
  767  git clone http://github.com/chapeter/cicd_demoapp
  768  cd cicd_demoapp/
  769  ls
  770  cat app_
  771  cat app_install.sh
  772  cat .git/config
  773  ls
  774  ls -a
  775  cat .gitignore
  776  ls -la
  777  cp drone_secrets_sample.yml drone-secrets.yml
  778  ls
  779  cat .gitignore
  780  mv drone-secrets.yml drone_secrets.yml
  781  vim drone_secrets.yml
  782  export DRONE_SERVER=http://drone.green.browndogtech.com
  783  vim ~/.bash_profile
  784  export DRONE_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXh0IjoiY2hhcGV0ZXIiLCJ0eXBlIjoidXNlciJ9.ahSQXEOd2WFL-zsVPJuKnRjHOA82LlMhiRxDmOqzpQo
  785  vim ~/.bash_profile
  786  drone repo ls
  787  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  788  ls
  789  cat .drone.sec
  790  ls
  791  ls -la
  792  cat .drone.yml
  793  git add .drone.sec
  794  git commit -m "Added .drone.sec file"
  795  git push
  796  ls
  797  cat .drone.yml
  798  vim .drone.yml
  799  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  800  git add .drone.*
  801  git status
  802  git commit -m "Updating build pipeline to include tests"
  803  git push
  804  vim .drone.yml
  805  history
  806  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  807  git add .drone.*
  808  git commit -m "Updated Publish Phase"
  809  git push
  810  ls
  811  cat .drone.yml
  812  ls
  813  ./app_install.sh
  814  ./app_install.sh
  815  ls
  816  vim .drone.yml
  817  history
  818  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  819  git add .drone*
  820  git commit -m "Updated Deploy Phase to Drone Config"
  821  git push
  822  vim .drone.yml
  823  history
  824  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  825  git add .drone.*
  826  git commit -m "Added Notify Phase to Drone Config"
  827  git push
  828  ls
  829  vim requirements.txt
  830  git add *
  831  git add .
  832  git status
  833  git commit -m "test"
  834  git push
  835  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  836  git add .drone *
  837  git add .drone.*
  838  git status
  839  git commit -m "updated drone.sec
  840  "
  841  git push
  842  ls
  843  cat .drone.yml
  844  ls
  845  cat drone_secrets.yml
  846  clear
  847    SPARK_TOKEN: NmQ1OGZmZDktYzI5ZS00ODFiLTk4OTYtZTJjMjcyOTA2N2VmNWE1OWQ1Y2ItZTgx
  848    SPARK_ROOM: Y2lzY29zcGFyazovL3VzL1JPT00vODExZmU2ZTAtODFjOS0xMWU2LWE4MTAtYjFhZDRlMjQ0MzU2
  849  printenv | grep SPARK
  850  vim drone_secrets.yml
  851  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  852  git add .drone.*
  853  git commit -m "Using a bot spark token doesnt work if they are not in this room /facepalm"
  854  git push
  855  vim ~/.bash_profile
  856  ls
  857  cat .drone.yml
  858  rm .drone.yml
  859  vim .drone.yml
  860  git add .drone.yml
  861  git commit -m "another test test test"
  862  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  863  git commit -m "another test test test"
  864  git add .drone.sec
  865  git commit -m "another test test test"
  866  git push
  867  cat .drone.yml
  868  vim demoapp.py
  869  git add demoapp.py
  870  git commit -m "Added hello/universe to the applicaiton"
  871  git push
  872  vim .drone.yml
  873  git add .drone.
  874  git add .drone.yml
  875  git commit -m "Testing notification colors"
  876  git push
  877  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  878  git add .drone.sec
  879  git status
  880  git commit -m "Testing notificaiton colors"
  881  git push
  882  vim .drone.yml
  883  ls
  884  cat .drone.
  885  cat .drone.yml
  886  vim .drone.yml
  887  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  888  git add .drone.*
  889  git commit -m "moving back to hanks notifier"
  890  git push
  891  ls
  892  ./app_uninstall.sh
  893  ./app_uninstall.sh
  894  cd projects/imapex/
  895  ls
  896  cd cicdlab/
  897  ls
  898  cd cicd_demoapp/
  899  ls
  900  ./app_install.sh
  901  ls
  902  cd .drone.yml
  903  vim .drone.yml
  904  cat .gitignore
  905  history | grep drone
  906  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  907  git add .drone.*
  908  git commit -m "testing inline html in markdown with spark"
  909  git push
  910  cat .drone.
  911  cat .drone.y
  912  cat .drone.yml
  913  docker pull chapeter/drone-spark
  914  ls
  915  vim Dockerfile
  916  touch test
  917  git add test
  918  git commit -m "another inline html test"
  919  git push
  920  vim .drone.yml
  921  hisotyr
  922  history
CHAPETER-M-V072:cicd_demoapp chapeter$ !906
drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
CHAPETER-M-V072:cicd_demoapp chapeter$ git add .drone.*
CHAPETER-M-V072:cicd_demoapp chapeter$ git commit -m "."
[master 6abb7c0] .
 2 files changed, 2 insertions(+), 2 deletions(-)
 rewrite .drone.sec (100%)
CHAPETER-M-V072:cicd_demoapp chapeter$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

publish:
To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.12 KiB | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To http://github.com/chapeter/cicd_demoapp
   8a3beab..6abb7c0  master -> master
CHAPETER-M-V072:cicd_demoapp chapeter$ vim .drone.yml
CHAPETER-M-V072:cicd_demoapp chapeter$ history
  429  clear
  430  cat rooms.json
  431  cat rooms.json | grep id
  432  cat rooms.json | grep id | awk '{ print $2 } '
  433  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"//g
  434  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"//g"
  435  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"//g'
  436  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"//g' | sed 's/\,//g'
  437  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"/\'/g' | sed 's/\,//g'
  438  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"/\'/g'
  439  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"/'/g'
  440  cat rooms.json | grep id | awk '{ print $2 } ' | sed 's/\"/\\\'/g'
  441  cat rooms.json | grep id | awk '{ print $2 } ' | sed "s/\"/'/g"
  442  cat rooms.json | grep id | awk '{ print $2 } ' | sed "s/\"/'/g" | sed 's/\,//g'
  443  cat rooms.json | grep id | awk '{ print $2 } ' | sed "s/\"/'/g" | sed 's/\,//g'
  444  history
  445  grep id rooms.json
  446  grep "id" rooms.json
  447  cat rooms.json
  448  ls
  449  echo "id" > rooms.json
  450  grep "id" rooms.json
  451  vim exercise1.sh
  452  grep "id" rooms.json | awk { print $2 } ' | sed "s/\"/'/g" | sed 's/\,//g' > rooms_new.json
  453  ls
  454  grep "id" rooms.json | awk { print $2 } ' | sed "s/\"/'/g" | sed 's/\,//g' > rooms_new.json
  455  vim exercise1.sh
  456  clear
  457  virtualenv test2
  458  pip freeze
  459  source test2/bin/activate
  460  pip freeze
  461  exit
  462  ls
  463  cd kubernetes-the-hard-way/
  464  ls
  465  cd ..
  466  pwd
  467  exit
  468  python -i
  469  ls
  470  mv doubler doubler.py
  471  exit
  472  python -i
  473  vim doubler.py
  474  cd ..
  475  exit
  476  python -i
  477  exit
  478  python -i
  479  exit
  480  python
  481  python3
  482  which python3
  483  cd projects/imapex/
  484  ls
  485  cd python3/
  486  ls
  487  ls -l
  488  cd .virtualenv/
  489  ls
  490  cd ..
  491  source .virtualenv/bin/activate
  492  pip3 freeze
  493  pip freeze
  494  pip install --upgrade pip
  495  pip3 freeze
  496  pip3 install requests
  497  pip freeze
  498  pip3 freeze
  499  cat pip3 freeze | requirements.txt
  500  pip3 freeze | requirements.txt
  501  pip3 freeze > requirements.txt
  502  cat requirements.txt
  503  ls
  504  echo "Flask" >> requirements.txt
  505  ls
  506  cat requirements.txt
  507  pip3 install -r requirements.txt
  508  pip3 --version
  509  cat ~/scripts/nxapitools/nxsendcmd.py
  510  ls
  511  python3 weather.py
  512  which python3
  513  python get-pip.py
  514  curl -O https://bootstrap.pypa.io/get-pip.py
  515  ls
  516  source -h
  517  source -h-help
  518  source ---help
  519  which virtualenv
  520  which python
  521  docker login
  522  docker login -help
  523  docker login -e="." -u="chapeter" -p="95QXE53qeOzQBLqBzWPt283btAWlSa+NpDcZwhE8zvgsxFWzUoOgFPk7Li8LQWgl" quay.io
  524  docker login containers.cisco.com
  525  docker login -e="." -u="chapeter" -p="5q3WxqvyVkzaUXuCBomgqaHuF82CT4rOIanzgzhpGxL0ZdsA4oGAA2lajFsMQHhv+eehAcFSxHyVhlv5d/uY8/7tAGigs0DDN8gdiyR1RiQ=" containers.cisco.com
  526  docker -help
  527  docker info
  528  which virtualenv
  529  ls
  530  cd ..
  531  ls
  532  cd imapex101_testing_example/
  533  ls -l
  534  ls -a
  535  source .virtualenv/bin/activate
  536  mv ../python3/weather.py .
  537  rpy
  538  python3 -i
  539  python3 tests.py
  540  python3 tests.py
  541  clear
  542  python3 tests.py
  543  2to3
  544  python3 tests.py
  545  python3 tests.py
  546  python3 tests.py
  547  clear
  548  clear
  549  clear
  550  python3 tests.py
  551  clear
  552  python3 tests.py
  553  python3 -i doubler.py
  554  python3 tests.py
  555  python3 tests.py
  556  pip3 install flake3
  557  pip3 install flake8
  558  flake8 doubler.py
  559  flake8 doubler.py
  560  flake8 doubler.py
  561  flake8 doubler.py
  562  flake8 doubler.py
  563  flake8 doubler.py
  564  cat ~/.bash_profile
  565   brew install https://raw.githubusercontent.com/icholy/ttygif/master/ttygif.rb
  566   brew install https://raw.githubusercontent.com/icholy/ttygif/master/ttygif.rb
  567  ttyrec myrecording
  568  ls
  569  ttygif myrecording
  570  ls
  571  ttyrec -help
  572  man ttyrec
  573  ttyrec doubler
  574  cd imapex/
  575  ls
  576  cd imapex101_testing_example/
  577  ls
  578  mv doubler.py doubler2.py
  579  vim doubler2.py
  580  ttyrec doubler
  581  ttyrec doubler
  582  ls
  583  rm doubler
  584  rm doubler.py
  585  mv doubler2.py doubler.py
  586  vim doubler.py
  587  ls
  588  ttyrec doubler_gif
  589  ttygif -h
  590  ttygif --help
  591  man ttygif
  592  ttygif doubler_gif
  593  ttyrec doubler_gif
  594  ttygif doubler_gif
  595  cd ..
  596  ls
  597  git clone https://github.com/imapex-training/spark-room-viewer
  598  ls
  599  cd spark-room-viewer/
  600  ls
  601  git log
  602  virtualenv venv
  603  source venv/bin/activate
  604  pip install -r requirements.txt
  605  ls
  606  printenv | SPARK
  607  printenv | grep SPARK
  608  python app.py
  609  git log
  610  git checkout 059bea3d867118ed17851d1d7270437be37860a1
  611  git log
  612  git log
  613  git log
  614  git branch
  615  git master
  616  git checkout master
  617  git branch
  618  git log
  619  git tag
  620  git branch -m mynewfeature
  621  git log --pretty=oneline
  622  git fetch
  623  git branch
  624  cd ..
  625  cd ..
  626  ls
  627  cd spark-room-viewer/
  628  ls
  629  python app.py
  630  cd ..
  631  cd imapex/spark-room-viewer/
  632  ls
  633  git branch
  634  git checkout walkthrough
  635  git log
  636  cat .git/config
  637  ls
  638  ls
  639  cd .git/
  640  ls
  641  cd hooks/
  642  ls
  643  cat pre-commit.sample
  644  cd ..
  645  cd ..
  646  ls
  647  pwd
  648  cd ..
  649  deactivate
  650  git clone http://github.com/chapeter/101-github-lab
  651  cd 101-github-lab/
  652  ls
  653  git branch -m adding-email-addr
  654  git checkout adding-email-addr
  655  git remote add --track master upstream git://github.com/imapex/101-github-lab
  656  git fetch upstream
  657  git merge upstream/master
  658  git branch
  659  ls
  660  vim CONTRIBUTORS.txt
  661  git add CONTRIBUTORS.txt
  662  git commit -m "added email address - closes #2"
  663  git push -u origin adding-email-addr
  664  git branch
  665  git checkout master
  666  git branch
  667  git branch master
  668  git merge adding-email-addr
  669  git status
  670  cat CONTRIBUTORS.txt
  671  git push
  672  git add .
  673  git status
  674  git push origin/master
  675  git push -u origin master
  676  cd ..
  677  mkdir imapex101_dockerfile
  678  cd imapex101_
  679  cd imapex101_dockerfile/
  680  touch Dockerfile
  681  ls
  682  vim Dockerfile
  683  docker build -t chapeter/imapex101_dockerfile:latest
  684  docker build -t chapeter/imapex101_dockerfile:latest .
  685  docker images
  686  docker run -it chapeter/imapex101_dockerfile /bin/bash
  687  docker ps
  688  docker ps -a
  689  vim Dockerfile
  690  docker build -t chapeter/imapex101_dockerfile:latest .
  691  vim Dockerfile
  692  docker build -t chapeter/imapex101_dockerfile:latest .
  693  echo '#!/bin/bash' > hello_world.sh
  694  echo "while [ 0 -eq 0 ]; do" >> hello_world.sh
  695  echo "echo 'Hello World'" >> hello_world.sh
  696  echo "sleep 2" >> hello_world.sh
  697  echo "done" >> hello_world.sh
  698  bash hello_world.sh
  699  vim Dockerfile
  700  docker build -t chapeter/imapex101_dockerfile:latest .
  701  docker run -d --name dockerfile chapeter/imapex101_dockerfile:latest
  702  docker ps
  703  docker stop dockerfile
  704  docker rm dockerfile
  705  docker ps -a
  706  docker images
  707  docker pull quay.io/hpreston/demo:latest
  708  docker pull python
  709  ls
  710  echo "# imapex_dockerbuild" >> README.md
  711  git init
  712  git add README.md
  713  git commit -m "first commit"
  714  git remote add origin https://github.com/chapeter/imapex_dockerbuild.git
  715  git push -u origin master
  716  git status
  717  git add .
  718  git status
  719  git commit -m "add Dockerfile and hello_world"
  720  git push
  721  ls
  722  vim README.md
  723  git add README.md
  724  git commit -m "updated README.md with program info"
  725  git push
  726  cd ~/projects/
  727  brew install node
  728  brew install ffmpeg --with-libass --with-fontconfig
  729  ssh admin@10.94.238.124
  730  export MARATHON_URL=https://control.green.browndogtech.com:8080/v2
  731  export MARATHON_USER=devops1
  732  export MARATHON_PASSWORD=DEVOPS1
  733  export MYUSERNAME=chapeter
  734  curl -k -X GET -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps     | python -m json.tool
  735  curl -k -X GET -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/data     | python -m json.tool
  736  curl -k -X GET -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/myhero     | python -m json.tool
  737  curl -k -X PUT -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/myhero     -d '{"instances": 3}'     | python -m json.tool
  738  curl -k -X PUT -u $MARATHON_USER:$MARATHON_PASSWORD     -H "Content-type: application/json"     $MARATHON_URL/apps/$MYUSERNAME/myhero     -d '{"instances": 3}'     | python -m json.tool
  739  printenv | grep SPARK
  740  cd ima
  741  cd projects/imapex/
  742  ls
  743  mkdir cicdlab
  744  cd cicdlab/
  745  ls
  746  curl http://downloads.drone.io/drone-cli/drone_linux_amd64.tar.gz | tar zx
  747  ls
  748  rm -rf drone
  749  curl http://downloads.drone.io/drone-cli/drone_darwin_amd64.tar.gz | tar zx
  750  sudo cp drone /usr/local/bin
  751  printenv | grep SPARK_TO
  752  cd /tmp
  753  git clone http://github.com/chapeter/drone-spark
  754  history | grep build
  755  docker build -t chapeter/drone-spark:latest .
  756  cd drone-spark/
  757  docker build -t chapeter/drone-spark:latest .
  758  history | grep docker
  759  docker push chapeter/drone-spark:latest
  760  docker push chapeter/drone-spark:latest
  761  ls
  762  cd projects/
  763  ls
  764  cd imapex/cicdlab/
  765  ls
  766  ls
  767  git clone http://github.com/chapeter/cicd_demoapp
  768  cd cicd_demoapp/
  769  ls
  770  cat app_
  771  cat app_install.sh
  772  cat .git/config
  773  ls
  774  ls -a
  775  cat .gitignore
  776  ls -la
  777  cp drone_secrets_sample.yml drone-secrets.yml
  778  ls
  779  cat .gitignore
  780  mv drone-secrets.yml drone_secrets.yml
  781  vim drone_secrets.yml
  782  export DRONE_SERVER=http://drone.green.browndogtech.com
  783  vim ~/.bash_profile
  784  export DRONE_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXh0IjoiY2hhcGV0ZXIiLCJ0eXBlIjoidXNlciJ9.ahSQXEOd2WFL-zsVPJuKnRjHOA82LlMhiRxDmOqzpQo
  785  vim ~/.bash_profile
  786  drone repo ls
  787  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  788  ls
  789  cat .drone.sec
  790  ls
  791  ls -la
  792  cat .drone.yml
  793  git add .drone.sec
  794  git commit -m "Added .drone.sec file"
  795  git push
  796  ls
  797  cat .drone.yml
  798  vim .drone.yml
  799  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  800  git add .drone.*
  801  git status
  802  git commit -m "Updating build pipeline to include tests"
  803  git push
  804  vim .drone.yml
  805  history
  806  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  807  git add .drone.*
  808  git commit -m "Updated Publish Phase"
  809  git push
  810  ls
  811  cat .drone.yml
  812  ls
  813  ./app_install.sh
  814  ./app_install.sh
  815  ls
  816  vim .drone.yml
  817  history
  818  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  819  git add .drone*
  820  git commit -m "Updated Deploy Phase to Drone Config"
  821  git push
  822  vim .drone.yml
  823  history
  824  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  825  git add .drone.*
  826  git commit -m "Added Notify Phase to Drone Config"
  827  git push
  828  ls
  829  vim requirements.txt
  830  git add *
  831  git add .
  832  git status
  833  git commit -m "test"
  834  git push
  835  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  836  git add .drone *
  837  git add .drone.*
  838  git status
  839  git commit -m "updated drone.sec
  840  "
  841  git push
  842  ls
  843  cat .drone.yml
  844  ls
  845  cat drone_secrets.yml
  846  clear
  847    SPARK_TOKEN: NmQ1OGZmZDktYzI5ZS00ODFiLTk4OTYtZTJjMjcyOTA2N2VmNWE1OWQ1Y2ItZTgx
  848    SPARK_ROOM: Y2lzY29zcGFyazovL3VzL1JPT00vODExZmU2ZTAtODFjOS0xMWU2LWE4MTAtYjFhZDRlMjQ0MzU2
  849  printenv | grep SPARK
  850  vim drone_secrets.yml
  851  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  852  git add .drone.*
  853  git commit -m "Using a bot spark token doesnt work if they are not in this room /facepalm"
  854  git push
  855  vim ~/.bash_profile
  856  ls
  857  cat .drone.yml
  858  rm .drone.yml
  859  vim .drone.yml
  860  git add .drone.yml
  861  git commit -m "another test test test"
  862  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  863  git commit -m "another test test test"
  864  git add .drone.sec
  865  git commit -m "another test test test"
  866  git push
  867  cat .drone.yml
  868  vim demoapp.py
  869  git add demoapp.py
  870  git commit -m "Added hello/universe to the applicaiton"
  871  git push
  872  vim .drone.yml
  873  git add .drone.
  874  git add .drone.yml
  875  git commit -m "Testing notification colors"
  876  git push
  877  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  878  git add .drone.sec
  879  git status
  880  git commit -m "Testing notificaiton colors"
  881  git push
  882  vim .drone.yml
  883  ls
  884  cat .drone.
  885  cat .drone.yml
  886  vim .drone.yml
  887  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  888  git add .drone.*
  889  git commit -m "moving back to hanks notifier"
  890  git push
  891  ls
  892  ./app_uninstall.sh
  893  ./app_uninstall.sh
  894  cd projects/imapex/
  895  ls
  896  cd cicdlab/
  897  ls
  898  cd cicd_demoapp/
  899  ls
  900  ./app_install.sh
  901  ls
  902  cd .drone.yml
  903  vim .drone.yml
  904  cat .gitignore
  905  history | grep drone
  906  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  907  git add .drone.*
  908  git commit -m "testing inline html in markdown with spark"
  909  git push
  910  cat .drone.
  911  cat .drone.y
  912  cat .drone.yml
  913  docker pull chapeter/drone-spark
  914  ls
  915  vim Dockerfile
  916  touch test
  917  git add test
  918  git commit -m "another inline html test"
  919  git push
  920  vim .drone.yml
  921  hisotyr
  922  history
  923  drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
  924  git add .drone.*
  925  git commit -m "."
  926  git push
  927  vim .drone.yml
  928  history
CHAPETER-M-V072:cicd_demoapp chapeter$ !923
drone secure --repo chapeter/cicd_demoapp --in drone_secrets.yml
CHAPETER-M-V072:cicd_demoapp chapeter$ git add .drone.*
CHAPETER-M-V072:cicd_demoapp chapeter$ git commit -m "..."
[master 4551851] ...
 2 files changed, 2 insertions(+), 2 deletions(-)
 rewrite .drone.sec (100%)
CHAPETER-M-V072:cicd_demoapp chapeter$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.11 KiB | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To http://github.com/chapeter/cicd_demoapp
   6abb7c0..4551851  master -> master
CHAPETER-M-V072:cicd_demoapp chapeter$ ls
Dockerfile               app_uninstall.sh         drone_secrets.yml        sample-demoapp.json
README.md                chapeter-demoapp.json    drone_secrets_sample.yml test
app_install.sh           demoapp.py               requirements.txt         testing.py
CHAPETER-M-V072:cicd_demoapp chapeter$ rm test
CHAPETER-M-V072:cicd_demoapp chapeter$ git add .
CHAPETER-M-V072:cicd_demoapp chapeter$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    test

CHAPETER-M-V072:cicd_demoapp chapeter$ git commit -m "testing more inline color"
[master 2d85d02] testing more inline color
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 test
CHAPETER-M-V072:cicd_demoapp chapeter$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 2, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 229 bytes | 0 bytes/s, done.
Total 2 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To http://github.com/chapeter/cicd_demoapp
   4551851..2d85d02  master -> master
CHAPETER-M-V072:cicd_demoapp chapeter$ touch test
CHAPETER-M-V072:cicd_demoapp chapeter$ git add test
CHAPETER-M-V072:cicd_demoapp chapeter$ git commit -m "spark doesn't like html"
[master c26f1e1] spark doesn't like html
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test
CHAPETER-M-V072:cicd_demoapp chapeter$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 263 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 1 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To http://github.com/chapeter/cicd_demoapp
   2d85d02..c26f1e1  master -> master
CHAPETER-M-V072:cicd_demoapp chapeter$ cd ~/projects/
CHAPETER-M-V072:projects chapeter$ ls
acifloorplan            eman-tools              spark-mqtt-bot          tests
devnet-hunt             imapex                  spark-python            tty.gif
django-test             kubernetes-the-hard-way spark-room-viewer       untitled
doubler                 myrecording             sparkdaily              zeus-testing
dynamodb                sdtest                  testing
CHAPETER-M-V072:projects chapeter$ cd imapex/
CHAPETER-M-V072:imapex chapeter$ ls

101-github-lab            imapex101_dockerfile      mod_general_development   spark-room-viewer

cicdlab                   imapex101_testing_example python3
CHAPETER-M-V072:imapex chapeter$ mkdir CROnIC
CHAPETER-M-V072:imapex chapeter$ cd CROnIC/
CHAPETER-M-V072:CROnIC chapeter$
CHAPETER-M-V072:CROnIC chapeter$ ls
CHAPETER-M-V072:CROnIC chapeter$ git clone https://github.com/chapeter/CROnIC-UCS-ESX-Matrix
Cloning into 'CROnIC-UCS-ESX-Matrix'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
CHAPETER-M-V072:CROnIC chapeter$ rm -rf CROnIC-UCS-ESX-Matrix/
CHAPETER-M-V072:CROnIC chapeter$ git clone https://github.com/chapeter/CROnIC-UCS-ESX-Matrix
Cloning into 'CROnIC-UCS-ESX-Matrix'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
CHAPETER-M-V072:CROnIC chapeter$ ls
CROnIC-UCS-ESX-Matrix
CHAPETER-M-V072:CROnIC chapeter$ cd CE
-bash: cd: CE: No such file or directory
CHAPETER-M-V072:CROnIC chapeter$ cd CROnIC-UCS-ESX-Matrix/
CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$ ls
CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$ touch requirements.txt
CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$ touch Dockerfile
CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$ vim .gitignore
CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$ vim Readme.md
CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$ cat Readme.md
# boilerplate - Hello World

Any applicable badges (build/documentation/collaboration/licenses should go here

# Description

Boilerplate is a starting point application for the IMAPEX team @ Cisco.


# Installation

## Environment

Prerequisites

* Python 2.7+
* [setuptools package](https://pypi.python.org/pypi/setuptools)

## Downloading

Provide instructions for how to obtain the software from this repository, if there are multiple options - please include
as many as possible

Option A:

If you have git installed, clone the repository

    git clone https://github.com/imapex/boilerplate

Option B:

If you don't have git, [download a zip copy of the repository](https://github.com/imapex/boilerplate/archive/master.zip)
and extract.

Option C:

The latest build of this project is also available as a Docker image from Docker Hub

    docker pull username/image:tag

## Installing

Provide instructions on how to install / use the application

# Usage

Provide any relevant code samples / CLI's to leverage the code

    python app.py


# Development

Provide any notes for other contributors.  This includes how to run tests / etc


## Linting

We use flake 8 to lint our code. Please keep the repository clean by running:

    flake8

## Testing

The IMAPEX team should attempt to have unittests with  100% code coverage. An example test suite is contained
within the tests.py file for the boilerplate application

The tests are can be run in the following ways::

    python tests.py


When adding additional code or making changes to the project, please ensure that unit tests are added to cover the
new functionality and that the entire test suite is run against the project before submitting the code.
Minimal code coverage can be verified using tools such as coverage.py.

For instance, after installing coverage.py, the toolkit can be run with the command::

    coverage run tests.py

and an HTML report of the code coverage can be generated with the command::

    coverage html


# License

Include any applicable licenses here as well as LICENSE.TXT in the root of the repository

CHAPETER-M-V072:CROnIC-UCS-ESX-Matrix chapeter$
