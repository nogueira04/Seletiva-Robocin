# Seletiva-Robocin

Este repositório contém as pastas clonadas e modificadas dos dois algorítmos utilizados na seletiva, stella_vslam e VINS-Fusion, além de outras pastas necessárias para a execução dos algoritmos, como datasets e arquivos de configuração. Utilizei docker e ROS para executar os algoritmos.

Para executar o VINS-Fusion utilizando o EuroC dataset, siga os seguintes passos:

```
source ~/catkin_ws/devel/setup.bash
roslaunch vins vins_rviz.launch
rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_mono_imu_config.yaml 
rosbag play /rosbags/MH_01_easy.bag
```

Para executar o stella no dataset, siga os seguintes passos:

1. Execute a imagem docker:
```
docker run -it --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix:ro \
    --volume /datasets:/dataset:ro \
    stella_vslam-desktop
```

2. Dentro da imagem, rode o algoritmo:

```
./run_euroc_slam \
    -v /dataset/orb_vocab.fEbow \
    -d /dataset/MH_01_easy/mav0/ \
    -c ../example/euroc/EuRoC_mono.yaml
```

Para executar o stella em tempo real, siga os seguintes passos:

1. Execute a imagem do servidor do Socket Viewer:
```
sudo docker run --rm -it --name stella_vslam-ros-server --net=host stella_vslam-ros-server
```

2. Execute a imagem do docker
```
sudo docker run --rm -it --name stella_vslam-ros-socket --device /dev/video0 --net=host --volume /home/gabriel/stella_vslam_ros/teste/:/teste stella_vslam-ros-socket
```

3. Execute o script do node ros da câmera, o qual publica as imagens da webcam no tópico utilizado pelo algoritmo:
```
python3 ../teste/nodeCamera.py &
```

4. Execute o algoritmo
```
ros2 run stella_vslam_ros run_slam -v ../teste/orb_vocab.fbow -c ../teste/EuRoC_mono.yaml 
```
Repositorios clonados e colocados no projeto foram utilizados com motivações acadêmicas.
