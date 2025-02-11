FROM gcc:6 as buildstage
WORKDIR /app
copy first.c first.c
RUN gcc first.c -o myexe
#RUN gcc lw.c -static -nostartfiles -o myexe


#FROM gcc:6 as finalimage			v1
#FROM gcr.io/distroless/cc as finalimage	v2
#FROM alpine as finalimage			v3
#FROM scratch as finalimage			v4

COPY --from=buildstage /app/myexe /myexe
CMD ["./myexe"]



