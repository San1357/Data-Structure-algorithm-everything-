Array - simple data structure that are used to storing similar elements .
      
      - Collection of items ( items = integer , strings , DVD's,  games, book etc basically anything but the store same type of anything). 

      - can hold upto N items( but same type ).
      
      - Now we gonna create an Array to hold up to 15 DVD's. (In Java)
      
      1) NOw question is why 15 DVD only?
      - It is because agr tmhare pass gr pe sirf 15 cassete h to pura almari nhi na book kr loge sirf 15 cassete k liye . Tm utna hi bda cassette box(ya container )
         loge jitna cassette tmhe rkhna h . ab maan lo tm pura alamari  book kr lye aur tmhe sirf 15 cassette hi rkhna h to pheli baat tmhari mummy chappale chaapal 
         maarengi aur dusri baat ye ki agr tm 15 k size ka cassette box lye rhte to tm bche hue baki space me kuch aur rkh skte the  . SMJHE ? :)
         
         ha to chlo ab code likhte h :
         
         // The actual code for creating an Array to hold DVD's.
          
           DVD[] dvdCollection = new DVD[15];

           // A simple definition for a DVD.
           public class DVD {
                 public String name;
                 public int releaseYear;
                 public String director;

                 public DVD(String name, String releaseYear, String director) {
                       this.name = name;
                       this.releaseYear = releaseYear;
                       this.director = director;
                 }

                 public String toString() {
                       System.out.println(
                              this.name + ", directed by " + this.director + ", released in " + this.releaseYear));
                 }
            }
 
