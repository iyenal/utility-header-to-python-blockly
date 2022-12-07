float timeSinceFrameMs();
bool isButtonRight();
bool isButtonLeft();
bool isButtonDown();
bool isButtonUp();
bool isButtonY();
bool isButtonX();
bool isButtonB();
bool isButtonA();
void enableObject(char *name);
void disableObject(char *name);
void createLog(char *text);
void cleanLog();
void createText(int xpos,int ypos,int r,int g,int b,float fontsize,char *text);
void updateSprite(char *name,char *asset);
void moveSprite(char *name,float x,float y,int layer);
void setSprite(char *name,float x,float y,float sizeX,float sizeY,int layer);
void deleteObject(char *name);
void deleteSpritefontText(char *name);
void createSpritefontText(char *name,int xpos,int ypos,int fontsize,float condens,int lines,int columns,char *text,char *fontface,char *spritefont);
void createSpriteWithCoords(char *name,char *asset,float x,float y,float sizeX,float sizeY,float t0,float t1,float t2,float t3,int layer);
void createSpriteWithColor(char *name,char *asset,float x,float y,float sizeX,float sizeY,int r,int g,int b,int layer);
void createSprite(char *name,char *asset,float x,float y,float sizeX,float sizeY,int layer);
float getObjectSZ(char *name);
float getObjectSY(char *name);
float getObjectSX(char *name);
float getObjectRZ(char *name);
float getObjectRY(char *name);
float getObjectRX(char *name);
float getObjectPZ(char *name);
float getObjectPY(char *name);
float getObjectPX(char *name);
void setObjectwithRotationScale(char *name,float x,float y,float z,float rotX,float rotY,float rotZ,float scX,float scY,float scZ);
void moveObjectwithRotationScale(char *name,float x,float y,float z,float rotX,float rotY,float rotZ,float scX,float scY,float scZ);
void setObject(char *name,float x,float y,float z);
void createObjectwithRotationScale(char *name,char *asset,float x,float y,float z,float rotX,float rotY,float rotZ,float scX,float scY,float scZ);
void createObjectwithScale(char *name,char *asset,float x,float y,float z,float scX,float scY,float scZ);
void createObjectwithRotation(char *name,char *asset,float x,float y,float z,float rotX,float rotY,float rotZ);
void createObject(char *name,char *asset,float x,float y,float z);
void writeFile(char *filename,char *text);
char *openFile(char *filename);
int timeSinceStartup();
char *getPlatform();
void enableRenderWireframe();
void enableRenderSolid();
void enableRenderTexture();
void enableRenderShaded();
void moveCamera(float x,float y,float z,float rx,float ry,float rz);
void setCamera(float x,float y,float z,float rx,float ry,float rz);
void createAssetSkybox(char *s1,char *s2,char *s3,char *s4,char *s5,char *s6);
void createAssetPlane(char *name);
void createAssetTeapot(char *name);
void createAssetCone(char *name);
void createAssetTorus(char *name);
void createAssetSphere(char *name);
void createAssetCube(char *name);
void createAssetModel(char *name,char *filename);
void createAssetParticle(char *name,char *filename,int ParticleCount,int FrameCount,float scaleParticle);
void createAssetTexture(char *name,char *filename);
