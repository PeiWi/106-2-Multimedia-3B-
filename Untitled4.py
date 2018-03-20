
# coding: utf-8

# In[13]:


from skimage import io

img1=io.imread('C:/Users/PeiW/Picture/01.jpg', as_grey=True)

print(type(img1))
print(img1.shape)

io.imshow(img1)
io.show()

