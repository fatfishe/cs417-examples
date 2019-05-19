FROM python:3.7

COPY . /cs417-examples
WORKDIR /cs417-examples

#CMD ["python", "estimatePrecision.py", "10000", "16"]
CMD ["/bin/bash"]

