for i in *.xml; do
    java -Xmx2584m -jar ~/microaccessibility/otp-analyst.jar $i
done