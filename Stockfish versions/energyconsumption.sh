for n in `seq 1 30`
do
  for version in `seq 1 14`
  do
    if [ $version -ne 3 ]; then
      perf stat -o tempenergy.data -e power/energy-cores/ ./reprosearch.sh $version
      echo "Version $version, round $n\n" >> energy.data
      cat tempenergy.data >> energy.data
    fi
  # probably sleep
  sleep 10
  done
done

rm tempenergy.data
