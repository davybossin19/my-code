num_pages = 22

#Keeps track of pages clicked in stage 3
stage3_count = 1

#Loop through every page for Data base entry
for i in range (1,num_pages + 1):
    #On last page iteration we don't need to find index of next page button
    if i < num_pages:
        #First ten next page clicks
        if i <= 10:
            print('stage 1')
            print('page:', i)
            print('output:', i + 1 % 10,"\n")

        #Clicks for pages over (num_pages // 10) * 10
        elif (num_pages // 10 == i // 10) and i%10 != 0:
            #Flag is the number of the next page
            flag = 0
            for j in range(num_pages - 10, num_pages + 1):
                #This lets j reach the next page we need
                if j > (num_pages - (num_pages % 10)) + stage3_count:
                    flag = j
                    break
            print('flag:',flag)
            #Number of spaces between final page and next page
            diff = num_pages - flag
            #Final page index is 11, subtract difference to get index of next page
            k = 11 - diff
            #Increment count so next page moves forward
            stage3_count += 1

            print('stage 3')
            print('page:',i)
            print('output:',k,'\n')

        #All other next page clicks
        else:
            print('stage 2')
            print('page:', i)
            #Bounds output to cycle from 3 to 12
            print('output:', (i - 1) % 10 + 3,'\n')
