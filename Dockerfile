# this is a dockerfile to run the program in a container
FROM faucet/python3

# copy the project in the image
COPY . .

# install project binaries in the image FS
RUN pip3 install -r requirements.txt

