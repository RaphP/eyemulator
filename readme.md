


AU utilisés :
02 : lever les sourcils (seuil 3)
04 : froncer (seuil 1,2)
12 : sourire (seuil 0,6)

Leur ordre dans le vector face_analyser.GetCurrentAUsReg() :

4 6 7 10 12 14 1 2 5 0 15 17 20 23 25 26 45


1. Installer openFace
2. Modifier le fichier FaceLandmarkVid.cpp dans :
 /Users/yvon/Downloads/OpenFace-master/exe/FaceLandmarkVid

ajouter cout << face_model.detected_landmarks << endl;
Supprimer toutes les lignes faisant refference à 'visualizer' et ce qui en dépend (dont character press !)
On peut supprimer les ref a FPS tracker aussi


openFace : https://github.com/TadasBaltrusaitis/OpenFace

- Lancer le track sur la webcam en live :
    '/FaceLandmarkVid -device 0'


Controle du clavier : https://github.com/asweigart/pyautogui
